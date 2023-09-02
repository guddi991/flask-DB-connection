from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        
        # Omit the 'user_id' column from the INSERT statement
        cursor.execute('''INSERT INTO users (name, email, age) VALUES (%s, %s, %s)''', (name, email, age))
        
        mysql.connection.commit()
        cursor.close()
        return "Done!!"

@app.route('/allusers',methods=[''])

 
app.run(host='localhost', port=5000)