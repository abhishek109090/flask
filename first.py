from flask import Flask,render_template,url_for,redirect,request
import psycopg2
app = Flask(__name__)


def connection():
    conn=psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Abhi@2001"


    )
    return conn



@app.route('/')
def myfun():
    return "form submitted"

@app.route('/Home')
def Home():
   
    return "form submitted"
@app.route('/temp/<int:core>')
def temp(core):
    return render_template('hi.html',name=core)

@app.route('/url/<var>')
def url(var):
    if var=='name':
        return redirect(url_for('myfun'))
    else:
        return redirect(url_for('temp'))



@app.route('/register',methods=['GET','POST'])
def user():
    if request.method=='POST':
        phone=request.form['phone']
        email=request.form['email']
        password=request.form['password']
        id=request.form['id']
        conn=connection()
        cur=conn.cursor()
        cur.execute("update users set phone=%s,email=%s,password=%s where id=%s",(phone,email,password,id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('fetchuser'))
    return render_template('user.html')

@app.route('/users')
def fetchuser():
    conn=connection()
    cur=conn.cursor()
    cur.execute('select * from users')
    rows=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('fetch.html',rows=rows)

@app.route('/deleteuser/<int:id>',methods=["GET",'PUT','POST','DELETE'])
def deleteuser(id):
    conn=connection()
    cur=conn.cursor()
    cur.execute("delete from users where id=%s",(id,))
    conn.commit()
    cur.close()
    conn.close()
    return render_template('fetch.html')




if __name__=="__main__":
    app.run()

