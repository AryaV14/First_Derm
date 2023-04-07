from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = 'uploads'


def predict_label(img_path):
	i = image.load_img(img_path, target_size=(100,100))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 100,100,3)
	p = model.predict_classes(i)
	return dic[p[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']
        filename = secure_filename(img.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
	# 	img_path = "static/" + img.filename	
		img.save(os.path.join(basedir,app.config['IMAGE_UPLOADS'],filename))
        return render_template("index.html")
	# 	p = predict_label(img_path)

	# return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)