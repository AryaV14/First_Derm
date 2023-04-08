from flask import Flask, render_template,request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello(name=None):
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
    #add processing code




    
        text = "Prediction : "

        return text

if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)