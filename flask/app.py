from flask import Flask , render_template

app = Flask(__name__)

# @ -- is Dictator
@app.route('/') # Home page
def home():
    #return "Hello ,world ! This is my first Flask App"
    return render_template("template.htmlindex.html")    # load the HTML file

@app.route('/about')
def about():
    return render_template("template.html/about.html")
if __name__=='__main__':
    app.run(debug=True)

