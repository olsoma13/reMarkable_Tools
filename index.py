from flask import Flask
from flask import request
import pdfkit

# reminder when running for dev:
# export FLASK_APP=index.py
# export FLASK_ENV=development

app = Flask(__name__)

def gen_url(anURL):
    if anURL is not None:
        pdfkit.from_url(anURL, '.tmp/anURLpdf.pdf')
        return True
    else:
        return False
    
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/transform_url', methods=['POST'])
def transform_url():
    myURL = request.form['url']
    gen_url(myURL)
    app.logger.debug('form data url = %s', myURL )
    return 'OK'
