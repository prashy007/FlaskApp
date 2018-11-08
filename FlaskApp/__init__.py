from flask import Flask, render_template, request, url_for, redirect, flash
import sys
import wtforms

import mysql.connector


from wtforms import Form
from wtforms import TextField,validators,PasswordField
from wtforms.validators import Required

app = Flask(__name__)

app.secret_key = b'_5#y2L"wdDFE\n\xec]/'


@app.route('/')
def homepage():
    return render_template('main.html')



@app.route('/dashboard/')
def dashboard():
    flash("Welcome to my app")
    return render_template("dashboard.html")


@app.errorhandler(405)
def page_not_found(e):
    return render_template("405.html")


@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)
        username  = form.username.data
        userID = form.userID.data
        message= form.message.data

        if request.method == "POST" and form.validate():
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="user")
                mycursor = mydb.cursor()
                sqlFormula = "INSERT INTO user1 (name, ID) VALUES (%s, %s)"
                new_user= (username, userID)
                mycursor.execute(sqlFormula, new_user)
                sqlFormula = "INSERT INTO msg (ID, message) VALUES (%s, %s)"
                new_msg= (userID, message)
                mycursor.execute(sqlFormula, new_msg)
                #flash(message)
                sql= "SELECT message,no FROM msg WHERE ID = %s AND message = %s"
                no= (userID, message)
                mycursor.execute(sql, no)
                result = mycursor.fetchall()

                #for res in result:
                    #flash("Your msg id is:")
                    #flash(res[0])
                    #flash("Please remember for future use")
                mydb.commit()

                #return result
                return render_template("register-result.html", result=result)
                mycursor.close()
                mydb.close()
                #mydb.commit()
                #flash("Thanks for registering!")
                #mycursor.close()
                #mydb.close()


            except Exception as e:
                return(str(e))
                #return("userID is already taken, please choose another")

        return render_template("register.html", form=form)

    except Exception as e:
        return(str(e))

@app.route('/posting/', methods=["GET","POST"])
def post_page():
    try:
        form = PostingForm(request.form)
        userID = form.userID.data
        message= form.message.data

        if request.method == "POST" and form.validate():
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="user")
                mycursor = mydb.cursor()
                sqlFormula = "INSERT INTO msg (ID, message) VALUES (%s, %s)"
                new_msg= (userID, message)
                mycursor.execute(sqlFormula, new_msg)
                #flash(message)
                sql= "SELECT message,no FROM msg WHERE ID = %s AND message = %s"
                no= (userID, message)
                mycursor.execute(sql, no)
                result = mycursor.fetchall()
                mydb.commit()
                return render_template("post-result.html", result=result)
                mycursor.close()
                mydb.close()

            except Exception as e:
                return("userID didn't match, please try again")


        return render_template("posting.html", form=form)

    except Exception as e:
        return(str(e))

@app.route('/all/', methods=["GET","POST"])
def all_page():
    try:
        form = AllForm(request.form)
        userID = form.userID.data

        if request.method == "POST" and form.validate():
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="user")
                mycursor = mydb.cursor()
                sql= "SELECT ID FROM msg WHERE ID = %s"
                userID=(userID,)
                mycursor.execute(sql, userID)
                result = mycursor.fetchall()
                result=result[0]
                for res in result:
                    if (res == userID[0]):
                        sqlFormula1 = "SELECT message,no FROM msg WHERE ID = %s "
                        #userID=(userID,)
                        mycursor.execute(sqlFormula1, userID)
                        result = mycursor.fetchall()
                        result = tuple(result)
                        #for res in result:
                            #flash(res)

                        mydb.commit()

                        #return result
                        return render_template("all-result.html", result=result)
                        mycursor.close()
                        mydb.close()
                    else:
                        flash("UserID didn't match")

            except Exception as e:
                return("userID didn't match, please try again")


        return render_template("all.html", form=form)

    except Exception as e:
        return(str(e))

@app.route('/specific/', methods=["GET","POST"])
def specific_page():
    try:
        form = SpecificForm(request.form)
        userID = form.userID.data
        msgID= form.msgID.data

        if request.method == "POST" and form.validate():
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="user")
                mycursor = mydb.cursor()
                sql= "SELECT ID FROM msg WHERE ID = %s"
                userID=(userID,)
                mycursor.execute(sql, userID)
                result = mycursor.fetchall()
                result=result[0]
                for res in result:
                    if (res == userID[0]):
                        sqlFormula1 = "SELECT message FROM msg WHERE ID = %s AND no = %s"
                        msgID=(msgID,)
                        s_msg=(userID[0],msgID[0])
                        mycursor.execute(sqlFormula1, s_msg)
                        result = mycursor.fetchone()
                        for res in result:
                            #flash(res)
                            def isPalindrome(res):
                                rev = ''.join(reversed(res))
                                if (res == rev):
                                    return True
                                return False
                            ans = isPalindrome(res)
                            if (ans):
                                result=("This is palindrome")
                                return render_template("specific-result.html", res=res, result=result)
                            else:
                                result=("No it's not palindrome" + res)
                                return render_template("specific-result.html", res=res, result=result)
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                    else:
                        flash("UserID didn't match")

            except Exception as e:
                return("Something didn't match, please try again")


        return render_template("specific.html", form=form)

    except Exception as e:
        return(str(e))

@app.route('/delete/', methods=["GET","POST"])
def delete_page():
    try:
        form = DeleteForm(request.form)
        userID = form.userID.data
        msgID= form.msgID.data

        if request.method == "POST" and form.validate():
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="user")
                mycursor = mydb.cursor()
                sql= "SELECT ID FROM msg WHERE ID = %s"
                userID=(userID,)
                mycursor.execute(sql, userID)
                result = mycursor.fetchall()
                result=result[0]
                for res in result:
                    if (res == userID[0]):
                        sqlFormula1 = "DELETE FROM msg WHERE ID = %s AND no = %s"
                        msgID=(msgID,)
                        s_msg=(userID[0],msgID[0])
                        mycursor.execute(sqlFormula1, s_msg)
                        flash("Deleted")
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                    else:
                        flash("UserID didn't match")
            except Exception as e:
                flash("UserID didn't match")

        return render_template("delete.html", form=form)

    except Exception as e:
        return(str(e))

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    userID = PasswordField('New userID', [
        validators.Required(),
        validators.EqualTo('confirm', message='userID must match')])
    confirm = PasswordField('Repeat userID')
    message = TextField('message')

class PostingForm(Form):
    userID = PasswordField('userID')
    message = TextField('message')

class AllForm(Form):
    userID = PasswordField('userID')


class SpecificForm(Form):
    userID = PasswordField('userID')
    msgID = PasswordField('msgID')

class DeleteForm(Form):
    userID = PasswordField('userID')
    msgID = PasswordField('msgID')


if __name__ == "__main__":

    app.run()
