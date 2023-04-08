from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello(name=None):
    return render_template('index.html')


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)