from flask import Flask
from flask import request
from flask import render_template
import os
from subprocess import call
import uuid 

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/getToken',methods=['POST','GET'])
def getToken():
    default_name = '0'
    data = request.form.get('name', default_name)
    result="You have not given your name"
    if data == '0':
        return render_template('getToken.html',data=result)
    else:
        result=data+"_"+str(uuid.uuid4())
        print(result)
        return render_template('getToken.html',data=result)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
