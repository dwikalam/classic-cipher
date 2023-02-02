from cipher import standardVigenere, autoKeyVigenere, extendedVigenere, affine, playfair, hill, enigma
from flask import *
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/vigenere', methods=["GET", "POST"])
def vigenere_page():
    if request.method == "POST":
        if request.form["vigenereType"] == "standard":
            return redirect("/vigenere/standard")
        elif request.form["vigenereType"] == "autokey":
            return redirect("/vigenere/autokey")
        elif request.form["vigenereType"] == "extended":
            return redirect("/vigenere/extended")
    return render_template("vigenere.html")

@app.route('/vigenere/standard', methods=["GET", "POST"])
def standard_vigenere_page():
    if request.method == "POST":
        if request.form["enc_dec_mode"] == "Encrypt":
            plainteks = request.form["plainteks"]
            key = request.form["key"]
            result = standardVigenere.encrypt(plainteks, key)

            return render_template("standardVigenere.html", data=result, encrypt=True, fileContent="")
        elif request.form["enc_dec_mode"] == "Decrypt":
            cipherteks = request.form["cipherteks"]
            key = request.form["key"]
            result = standardVigenere.decrypt(cipherteks, key)

            return render_template("standardVigenere.html", data=result, encrypt=False, fileContent="")
    
    fileContent = ""
    if 'fileContent' in session:
        fileContent = session['fileContent']
    return render_template("standardVigenere.html", data="", fileContent=fileContent)

@app.route('/vigenere/autokey', methods=["GET", "POST"])
def autokey_vigenere_page():
    if request.method == "POST":
        if request.form["enc_dec_mode"] == "Encrypt":
            plainteks = request.form["plainteks"]
            key = request.form["key"]
            result = autoKeyVigenere.encrypt(plainteks, key)

            return render_template("autokeyVigenere.html", data=result, encrypt=True, fileContent="")
        elif request.form["enc_dec_mode"] == "Decrypt":
            cipherteks = request.form["cipherteks"]
            key = request.form["key"]
            result = autoKeyVigenere.decrypt(cipherteks, key)

            return render_template("autokeyVigenere.html", data=result, encrypt=False, fileContent="")
    
    fileContent = ""
    if 'fileContent' in session:
        fileContent = session['fileContent']
    return render_template("autokeyVigenere.html", data="", fileContent=fileContent)

@app.route('/vigenere/extended', methods=["GET", "POST"])
def extended_vigenere_page():
    if request.method == "POST":
        if request.form["enc_dec_mode"] == "Encrypt":
            filePath = session["filePathVigenereExtended"]
            key = request.form["key"]
            outputFilePath = "../data/output/extended-vigenere/" + request.form["outputFileName"]
            result = extendedVigenere.encrypt(filePath, key, outputFilePath)
            return render_template("extendedVigenere.html", data=result, encrypt=True)

        elif request.form["enc_dec_mode"] == "Decrypt":
            filePath = session["filePathVigenereExtended"]
            key = request.form["key"]
            outputFilePath = "../data/output/extended-vigenere/" + request.form["outputFileName"]
            result = extendedVigenere.decrypt(filePath, key, outputFilePath)
            return render_template("extendedVigenere.html", data=result, encrypt=False)

    if "modeVigenereExtended" in session:
        filePath = {"filePath": session["filePathVigenereExtended"]}
        if session["modeVigenereExtended"] == "radioEncrypt":
            return render_template("extendedVigenere.html", data=filePath, encrypt=True)
        elif session["modeVigenereExtended"] == "radioDecrypt":
            return render_template("extendedVigenere.html", data=filePath, encrypt=False)
    
    return render_template("extendedVigenere.html", data="", encrypt=True)

@app.route('/affine')
def affine_page():
    return render_template("affine.html")

@app.route('/affine/encrypt')
def affine_encrypt():
    plainText = request.args.get("plainText")
    keyM = int(request.args.get("keyM"))
    keyB = int(request.args.get("keyB"))
    return affine.encrypt(plainText, keyM, keyB)

@app.route('/affine/decrypt')
def affine_decrypt():
    cipherText = request.args.get("cipherText")
    keyM = int(request.args.get("keyM"))
    keyB = int(request.args.get("keyB"))
    return affine.decrypt(cipherText, keyM, keyB)

@app.route('/playfair')
def playfair_page():
    return render_template("playfair.html")

@app.route('/playfair/encrypt')
def playfair_encrypt():
    plainText = request.args.get("plainText")
    plainKey = request.args.get("plainKey")
    return playfair.encrypt(plainText, plainKey)

@app.route('/playfair/decrypt')
def playfair_decrypt():
    cipherText = request.args.get("cipherText")
    plainKey = request.args.get("plainKey")
    return playfair.decrypt(cipherText, plainKey)

@app.route('/hill')
def hill_page():
    return render_template("hill.html")

@app.route("/hill/keycheck", methods = ["POST"])
def hill_check():
    key = request.form.get("key")
    key = json.loads(key)
    size = int(request.form.get("size"))
    keyMatrix = [[int(key[i*size+j]) for j in range(size)] for i in range(size)]
    if hill.keycheck(keyMatrix) :
        return "ok"
    return "Not ok"

@app.route("/hill/encrypt", methods=["POST"])
def hill_encrypt():
    plainText = request.form.get("plainText")
    size = int(request.form.get("size"))
    key = request.form.get("key")
    keyMatrix = hill.generateKeyMatrix(key, size)

    return hill.encrypt(plainText, keyMatrix)

@app.route("/hill/decrypt", methods=["POST"])
def hill_decrypt():
    cipherText = request.form.get("cipherText")
    size = int(request.form.get("size"))
    key = request.form.get("key")
    keyMatrix = hill.generateKeyMatrix(key, size)

    return hill.decrypt(cipherText, keyMatrix)

@app.route('/enigma')
def enigma_page():
    return render_template("enigma.html")

@app.route('/enigma/encrypt')
def enigma_encrypt():
    plainText = request.args.get("plainText")
    key1 = request.args.get("key1")
    key2 = request.args.get("key2")
    key3 = request.args.get("key3")
    return enigma.encrypt(plainText, key1, key2, key3)

@app.route('/enigma/decrypt')
def enigma_decrypt():
    cipherText = request.args.get("cipherText")
    key1 = request.args.get("key1")
    key2 = request.args.get("key2")
    key3 = request.args.get("key3")
    return enigma.decrypt(cipherText, key1, key2, key3)

@app.route('/upload-vigenere/<vtype>', methods = ['GET', 'POST'])
def upload_file_vigenere(vtype):
    if request.method == 'POST':
        if vtype == "extended":
            f = request.files['file']
            filename = f.filename
            f.save(f"../data/input/{filename}")
            filePath = f"../data/input/{filename}"
            
            session['filePathVigenereExtended'] = filePath
            session['modeVigenereExtended'] = request.form["enc_dec_mode"]
            return redirect(url_for('extended_vigenere_page'))
        
        f = request.files['file']
        f.save(f"../data/input/{vtype}-vigenere-input.txt")
        f = open(f"../data/input/{vtype}-vigenere-input.txt")
        if vtype == "standard":
            fileContent = f.read()
            session['fileContent'] = fileContent
            return redirect(url_for('standard_vigenere_page', fileContent=fileContent))
        if vtype == "autokey":
            fileContent = f.read()
            session['fileContent'] = fileContent
            return redirect(url_for('autokey_vigenere_page', fileContent=fileContent))

    return redirect('/')

@app.route('/upload/<cipher>', methods = ['GET', 'POST'])
def upload_file(cipher):
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f"{cipher}-cipher.txt")
        f.save(f'../data/input/{filename}')
        f = open(f"../data/input/{filename}")
        return render_template(f"{cipher}.html", fileContent=f.read())
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=3000)