from flask import Flask, redirect, url_for, render_template 
#url for and redirect allow return a redirect from a specific function, 
#render grabs an html file and renders as web page

app = Flask(__name__) #create instance of flask web app

@app.route("/<name>") #define how to access this specific page --> 
def home(name):
    return render_template("index.html", content=name, r=2) #this will display the index.html page - index.html will be rendered, then varibale content of name will be replaced in the content.html file




""""
@app.route("/<name>") #this basically allows us to display the info below based on what we write afer the /
def user(name):
    return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!")) #When you go /admin it will reutrn url for user, and pass the arg admin
"""




if __name__ == "__main__":
    app.run()

    #redirect different pages from our code