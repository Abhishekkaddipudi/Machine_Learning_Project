from flask import Flask
from Housing.logger import logging
from Housing.exception  import HousingException
import sys

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("hello")
    except Exception as e:
        houisng=HousingException(e,sys).error_message
        logging.info(houisng)

    return "HellWorld"

if __name__=="__main__":
    
    app.run(debug=True)
