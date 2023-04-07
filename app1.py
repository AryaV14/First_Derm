from flask import Flask, render_template, request ,send_from_directory,url_for
from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asldfkjlj'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
	photo = FileField(
		validators=[
			FileAllowed(photos, 'Only images are allowed'),
			FileRequired('File field should not be empty')
		]
	)
submit = SubmitField('Upload')

#  def predict_label(img_path):
# 	i = image.load_img(img_path, target_size=(100,100))
# 	i = image.img_to_array(i)/255.0
# 	i = i.reshape(1, 100,100,3)
# 	p = model.predict_classes(i)
# 	return dic[p[0]]


@app.route('/uploads/<filename>')
def get_file(filename):
	return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

# routes
@app.route("/", methods=['GET', 'POST'])
def upload_image():
	form = UploadForm()
	if form.validate_on_submit():
		filename = photos.save(form.photo.data)
		file_url = url_for('get_file', filename=filename)
	else:
		file_url = None
	return render_template("index.html", form=form,file_url=file_url)



# @app.route("/submit", methods = ['GET', 'POST'])
# def get_output():
# 	if request.method == 'POST':
# 		img = request.files['my_image']

# 		img_path =  img.filename	
# 		img.save(img_path)

# 		p = predict_label(img_path)

# 	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)