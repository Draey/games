from flask import Flask

app = Flask(__main__) #create instance of flask web app

@app.route("/home/parallels/Desktop/flask") #define how to access this specific page --> 
def home():
    return "Hello! this is the main page <h1>Hello Planet Earth<h1>"

if __name__ == "__main__":
    app.run()