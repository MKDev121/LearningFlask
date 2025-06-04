from flask import Flask , request

app = Flask(__name__)

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        name= request.form['name']
        email=request.form['email']
        
        return f'''Name: {name}
            Email: {email}'''
    else:
        return '''
            <form method="post">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name"><br><br>
                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email"><br><br>
                <input type="submit" value="Submit">
            </form>
        '''





if __name__=="__main__":
    app.run(debug=True)
