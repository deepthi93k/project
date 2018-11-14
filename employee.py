from flask import Flask, render_template

from data import Employee

app=Flask(__name__)
getEmployee = Employee()

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home') 
def home():
    return render_template("home.html")                                                                                                                                                                                                                                  
    

@app.route('/Employee')
def Employee():
    return render_template('employee1.html',myEmployeelist=getEmployee)                                                                                                                                                                                                                                     
    
if(__name__=='__main__'):
    

    app.run(debug=True)        

