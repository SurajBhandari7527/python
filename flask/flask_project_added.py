from flask import Flask,render_template
app=Flask(__name__) # app is the instance(object) of class Flask. __name__ evaluates the name of the current module to find where packages are located

@app.route('/') #route is a URL pattern and / is the root URL of the web application. it is the default page user see when they visit the URL
def home(): #creating a function named home
    return render_template('login.html') # this will print the String "hello world " in the default web page 

@app.route('/about')
def about_page():
    return "About Page"

if __name__=="__main__": #if no external module is imported __name__= __main__ , __name__=module name if imported
    app.run(debug=True) #app.run() starts the Flask development server which will listen for incoming HTTP req and route them to appropriate functions.
    # dubug=True enables flask debug mode the server will show the changes while reloading if changes are made to the code. NO need to rerun the code

