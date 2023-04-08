# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")