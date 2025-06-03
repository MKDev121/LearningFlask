#Import  the Flask Class  from the flask module
from flask import Flask, request

#Create a Flask application instance
app=Flask(__name__)

#Define a route to root URL ("/")
@app.route("/")
def hello_world():
    # This function will be executed when the user visits the root URL
    return "<p>Hello, World!</p>"

@app.route("/profile")
def view_profile():
    return "<p>This is profile section</p>"

@app.route("/profile/<username>")
def view_user_profile(username):
    return f"User: {username}"

@app.route("/profile/<int:userID>")
def view_userID(userID):
    return f"User ID: {userID}"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        return "Logged in"
    else:
        return  "Login form"


#Run the application in the debug mode if the script is executed directly
if __name__=="__main__":
    app.run(debug=True)

