import httplib
import urllib
import base64
import os
import json
from flask import Flask, request, jsonify
import urllib
import requests
from urlparse import urlparse
from translate import Translator
app = Flask(__name__)
def xulyanh(eurl):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'nhap key cua ban',
    }
    
    params = urllib.urlencode({
        'visualFeatures': 'Description',
        'language': 'en',
    })
    dataurl = {'url':eurl}
    jsondata=json.dumps(dataurl)
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, jsondata, headers)
    response = conn.getresponse()
    data = response.read()
    print data
    print "#################################"
    b = json.loads(data)
    a = b['description']['captions'][0]['text']
    print a
    translator= Translator(to_lang="vi")
    translation = translator.translate(a)
    conn.close()
    return translation
@app.route('/')
def hello():
    return 'test web'
@app.route('/api', methods=['GET', 'POST'])
def add_message():
  imageurl = request.args.get('message')
  eurl= urllib.unquote(imageurl).decode('utf8')
  ketqua = xulyanh(eurl)
  result = {"messages": [{"text": ketqua}]}
  return jsonify(result)
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
