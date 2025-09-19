from flask import Flask ,render_template ,request
import pymysql


app= Flask(__name__)

# mysql connextion confiig
db=pymysql.connect(
    host="localhost",
    user="root",
    password="root",    
    database="backend_db"   # DB name

)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name= request.form ['name'],
    email= request.form ['email']

    cursor=db.cursor()
    sql="INSERT INTO users (name,email) VALUES (%s,%s)"
    cursor.execute(sql,(name,email))
    db.commit()

    return f'<h3> Thanks ,{name} ! Your data is Saved .</h3>'

if __name__ ==  "__main__":
    app.run(debug=True)
