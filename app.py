from flask import Flask
from Housing.logger import logging
from Housing.exception  import HousingException
import sys

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():

    return "Logging and Debug completed"

if __name__=="__main__":
    
    app.run(debug=True)
