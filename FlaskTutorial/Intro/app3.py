from flask import Flask,make_response

app= Flask(__name__)

@app.route("/custom_response")
def custom_response():
    response=make_response("<h1>Custom Response</h1>")
    response.headers['Content-Type']='text/html'
    response.status_code=200
    return response

@app.route("/tuple_response")
def tuple_response():
    return "<h1>Tuple response</h1>",201,{'Content-Type':'text/html'}

if __name__=="__main__":
    app.run(debug=True)
