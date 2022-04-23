from xml.dom.minidom import Document
from flask import Flask, render_template, request
import aspose.words as aw

import os

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_hanler():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      ftype = request.form['name']
      if ftype == 'pdf':
         doc=aw.Document(f.filename)
         doc.save("Output.pdf")
      elif ftype== 'docx':
         doc=aw.Document(f.filename)
         doc.save("Output.docx")
      elif ftype =='txt':
         doc=aw.Document(f.filename)
         doc.save("Output.txt")
      elif ftype =='doc':
         doc=aw.Document(f.filename)
         doc.save("Output.doc")
      elif ftype =='xml':
         doc=aw.Document(f.filename)
         doc.save("Output.xml")
      elif ftype =='html':
         doc=aw.Document(f.filename)
         doc.save("Output.html")
      
      return '<h1>file uploaded successfully<h1>'
		
def main():
   app.run(debug = True)
