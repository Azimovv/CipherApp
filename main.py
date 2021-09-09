from flask import Flask, request, redirect, url_for, render_template
from caesar import crypter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', content=['caesar', 'affine'])


@app.route('/caesar', methods=['POST', 'GET'])
def caesar():
    if request.method == 'POST':
        text = request.form['nm']
        if request.form['submit_button'] == 'Encrypt':
            return render_template('caesar.html')\
                   + 'Encrypted Message:' + crypter(text, 0, 1)
        elif request.form['submit_button'] == 'Decrypt':
            return render_template('caesar.html') \
                    + 'Decrypted Message:' + crypter(text, 0, 3)
    else:
        return render_template('caesar.html')


@app.route('/affine', methods=['POST', 'GET'])
def affine():
    return render_template('affine.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
