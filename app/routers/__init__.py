"""defining our routes"""

from app import routes, gcrypter
from flask import render_template, request, jsonify, redirect, url_for


@routes.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@routes.route("/encrypt/", methods=['GET', 'POST'])
def encrypt():
    if request.query_string:
        text = request.query_string.decode().split('=')[1]
        return jsonify(encrypted=gcrypter.encrypt(t=text))
    elif request.method == 'POST':
        text = request.form.to_dict()['text']
        return jsonify(encrypted=gcrypter.encrypt(t=text))
    return redirect(url_for('routes.index'))


@routes.route("/decrypt/", methods=['GET', 'POST'])
def decrypt():
    if request.query_string:
        values = request.query_string.decode().split('&')
        value1 = int(values[0].split('=')[1])
        value2 = int(values[1].split('=')[1])
        return jsonify(decrypted=gcrypter.decrypt(v1=value1, v2=value2))
    elif request.method == 'POST':
        values = request.form.to_dict()
        value1 = int(values['value1'])
        value2 = int(values['value2'])
        return jsonify(decrypted=gcrypter.decrypt(v1=value1, v2=value2))
    return redirect(url_for('routes.index'))
