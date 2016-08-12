from flask import Flask, render_template, json, redirect, request
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from flask import session

mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'I am the best'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'my_cart'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')
	
@app.route('/Login')
def Login():
	return render_template('login.html')
	
@app.route('/Signup')
def Signup():
	return render_template('signupme.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('_createUser',(_name,_email,_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return redirect('/welcomehome')
				#return json.dumps({'message':'User created successfully !'})
				#return render_template('Welcome.html')
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()
		
@app.route('/welcomehome')
def welcomehome():
    return render_template('Welcome.html')
		
		
		
@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('_validloginId',(_username,))
        data = cursor.fetchall()
        if len(data) > 0:
            #if check_password_hash(str(data[0][3]),_password):
            if (str(data[0][3])==_password):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Sorry you are not registered')
 
    except Exception as e:
        return render_template('error.html',error = '-_- Something went wrong')
    finally:
        cursor.close()
        con.close()

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('myhomepage.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')

		
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')
		

@app.route('/Wishlist')
def Wishlist():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')
		


	
@app.route('/addWish1',methods=['POST'])
def addWish1():
    try:
        if session.get('user'):
            _user = session.get('user')
			#mysql code
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('_addWish',(_user,'I-Phone','64.99'))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'An error occurred!')
 
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()

@app.route('/addWish2',methods=['POST'])
def addWish2():
    try:
        if session.get('user'):
            _user = session.get('user')
			#mysql code
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('_addWish',(_user,'Laptop','250.99'))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'An error occurred!')
 
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()		
		
@app.route('/addWish3',methods=['POST'])
def addWish3():
    try:
        if session.get('user'):
            _user = session.get('user')
			#mysql code
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('_addWish',(_user,'Keyboard','40.99'))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'An error occurred!')
 
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()

@app.route('/addWish4',methods=['POST'])
def addWish4():
    try:
        if session.get('user'):
            _user = session.get('user')
			#mysql code
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('_addWish',(_user,'Mouse','10.99'))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'An error occurred!')
 
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()
		

@app.route('/addWish5',methods=['POST'])
def addWish5():
    try:
        if session.get('user'):
            _user = session.get('user')
			#mysql code
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('_addWish',(_user,'Smart Watch','239.99'))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'An error occurred!')
 
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()

@app.route('/addWish6',methods=['POST'])
def addWish6():
    try:
        if session.get('user'):
            _user = session.get('user')
			#mysql code
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('_addWish',(_user,'Apple Desktop','949.99'))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'An error occurred!')
 
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()
		
		
@app.route('/getWish')
def getWish():
    try:
        if session.get('user'):
            _user = session.get('user')
 
            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('sp_GetWishByUser',(_user,))
            wishes = cursor.fetchall()
 
            wishes_dict = []
            for wish in wishes:
                wish_dict = {
                        'Id': wish[0],
                        'UserId': wish[1],
                        'Name': wish[2],
                        'Price': wish[3],
                        'Date': wish[4]}
                wishes_dict.append(wish_dict)
 
            return json.dumps(wishes_dict)
        else:
            return render_template('error.html', error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error = 'Still not getting the error')
    finally:
        cursor.close()
        con.close()


@app.route('/store')
def Store():
	return render_template('myhomepage.html')
	
		
if __name__ == "__main__":
    app.run(port=5002)