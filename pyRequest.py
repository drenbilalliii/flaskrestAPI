from flask.json import jsonify
import requests
import unittest
import json
from random import randint


class RequestObserver(unittest.TestCase) :


    CONST_URL = "http://192.168.100.37:5000/"

    #OK
    def test_successful_grade(self) :

 
        piket = [54,56,65,23,53,87,52,8,78,1000,67,99]
        
        ranNum = piket[randint(0,len(piket)-1)]
        r = requests.post(self.CONST_URL +"calculate_exam_grade",data= {'grade' : ranNum})
        
        self.assertEqual(200,r.status_code)

        print("---------TASK-3----------")
        print("---------Calculate exam grade ----------")
        print('Post request parameter that is sent ' + str(ranNum))
        print("----------RESPONSE--------")
        print(r.text)

    #OK
    def test_succesful_min_max(self):
        numbers = {'numbers': [1,4,5,6]}

        list_to_json_array = json.dumps(numbers)
    
        headers = {'Content-Type': 'application/json'}


        r = requests.post(self.CONST_URL+"minmax",data=list_to_json_array,headers=headers)

        self.assertEqual(200,r.status_code)
 
        print("--------------TASK-4-----------------") 
        print("--------------MinMax -----------------")
        print("Response that is being sent")
        print("--------------RESPONSE-----------------")
        print(r.text)
    
    #OK
    def test_succesful_sayHello(self) :

        name = "Dren"
          
        r = requests.get(self.CONST_URL + "sayHello/?name=" + name)

          
        self.assertEqual(200,r.status_code)

        print("---------TASK-1----------")
        print("---------Say Hello----------")
        print('Post request parameter that is sent ' + name)
        print("----------RESPONSE--------")
        print(r.text)

    
    #OK
    def test_calculate_sum(self) :

        a = randint(0,10)
        b = randint(0,10)
        r = requests.get(self.CONST_URL + "calculatesum/?firstNumber="+str(a)+"&secondNumber="+str(b))

        print("---------TASK-2----------")
        print("---------Sum two numbers----------")
        print('GET request parameter that is sent ' + str(a)  + " with " + str(b))
        print("----------RESPONSE--------")
        print(r.text)

    #OK
    def test_find_by_category(self) :

        category = "shoes"
        r = requests.get(self.CONST_URL + "find_products/?category="+category)
        self.assertEqual(200,r.status_code)
        print("---------TASK-6----------")
        print("---------Find----------")
        print('Get request parameter that is sent ' + category)
        print("----------RESPONSE--------")
        print(r.text)

    #OK
    def test_insert_product(self):


        data = {"name" : "Adidas Rivarly Low",
                "category" : "shoes",
                "price" : 23.5,
                "basePrice" : 30.00}

        list_to_json_array = json.dumps(data)
    
        headers = {'Content-Type': 'application/json'}

        r = requests.post(self.CONST_URL + 'insert_product',data=list_to_json_array,headers=headers)
        self.assertEqual(200,r.status_code)
        print("---------TASK-5----------")
        print("---------Insert----------")
        print("----------RESPONSE--------")
        print(r.text)


     


object = RequestObserver()

object.test_succesful_sayHello()
object.test_calculate_sum()
object.test_successful_grade()
object.test_succesful_min_max()
object.test_insert_product()
object.test_find_by_category()