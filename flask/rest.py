
    
##############################
from flask import Flask, Response
from flask import request
from flask import render_template
import os


app = Flask(__name__)
app.config["DEBUG"] = True
        
@app.route('/ready',methods=['GET','POST'])
def ready():
    status_code = Response(status=200)
    return status_code
   
@app.route('/live',methods=['GET','POST'])
def live():
    status_code = Response(status=200)
    return status_code         

 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
     
    
