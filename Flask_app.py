## Create a simple result calculation form for cs branch in 3 subjects  

from flask import Flask,render_template,request

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        computernetwork = float(request.form['computer network'])
        operatingsystem = float(request.form['operating system'])
        DBMS = float(request.form['DBMS'])

        average_marks=(computernetwork + operatingsystem + DBMS)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        


        return render_template('result.html',results=average_marks)






if __name__=='__main__':
    app.run(debug=True)
    
    
    
    