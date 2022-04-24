from flask import Flask, render_template, request
import aspose.words as aw

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "C:/Users/Downloads"
@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_hanler():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      savepath = request.form['loc']
      ftype = request.form['name']
      if ftype == 'pdf':
         doc=aw.Document(f.filename)
         doc.save(savepath+"output.pdf")
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
      
      return render_template('output.html')
		
def main():
   app.run(debug = True)

