
from flask import Flask
from flask import request,jsonify
from werkzeug.utils import redirect
app = Flask(__name__)
import Calculations
import uuid
import pymongo
import helper
from pymongo import *


calculation = Calculations.Calculation()


@app.route('/sayHello/')
def sayHelloRoute():

    name = request.args['name']
    if(name):
        return calculation.triggerSayHello(name)


@app.route('/calculatesum/')
def calculateSumRoute() :

    a = request.args['firstNumber']
    b = request.args['secondNumber']

    if(a and b) :
        return calculation.calculateSum(a,b)

@app.route('/calculate_exam_grade',methods=['POST'])
def calculateExamGrade() :
     grade =  request.form.get('grade')

     if(grade) :
      return calculation.calculateExamGrade(grade)

@app.route('/minmax',methods=['POST'])
def returnMaxAndMin() :

    responseJson = request.json

    listOfNumbers = responseJson['numbers']
    
    return calculation.minMaxResponse(listOfNumbers)


#--------------------------------------------------------
#TASK 5



client =  pymongo.MongoClient('localhost',27017)

db = client["behamics"]
col = db["products"]  



@app.route('/insert_product',methods=['POST'])
def saveProduct() :
        try:

            responseJson = request.json

            db.products.insert_one({"product_id" : helper.generateUniqueID(),
                "name" : str(responseJson["name"]),
                                    "category" : str(responseJson["category"]),
                                    "price" : responseJson["price"],
                                    "basePrice" : responseJson["basePrice"]})
            
            return jsonify({"message " : "Produkti u insertua",
                            "status" : 201})

        except:
        
            return jsonify({"error" : "Ndodhi nje gabim gjate insertimit",
                        "status" : 500})



#TASK 6
@app.route('/find_products/')
def findByCategory():

    category = request.args['category']
    if(category):
        try:
            products = db.products.find({"category" : category})
            return jsonify({"data" : str(list(products)),
            "status" : 200 })
        except:
            return jsonify({"error " : "Not found with this category",
            "status" : 404})
    else:
            return ""

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)