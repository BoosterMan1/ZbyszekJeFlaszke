from flask import Flask, render_template, request
import string
import random


app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def pasgenerate():

    password = None

    if request.method=='POST':
        try:
            length = int(request.form.get('numbers', 8))
        except:
            length = 0
        charles= ""

        if request.form.get('big'):
            charles += string.ascii_uppercase
        if request.form.get('smol'):
            charles += string.ascii_lowercase
        if request.form.get('special'):
            charles += "!@#$%^&*()-_=+{[}]|:;"'<,>.?/'
        if request.form.get('leters'):
            charles += string.ascii_letters

        if charles:
            password = ''.join(random.choices(charles, k=length))
        else:
            password = "Wybierz coś, nie wstydź się (:"



    return render_template('index.html', password=password)

app.run()

