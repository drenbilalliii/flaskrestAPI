# flaskrestAPI

# Simple Flask API

Purpose: Evaluate the process and effort on learning new things and applying personal problem solving skills

Task Description:  Create a simple REST API using Flask as a web application (server) and implement some api routes (methods) as described below, also use MongoDB as a database service

Tasks:

1. Say Hello - Implement a method (api route) that says hello to you
	1. Create a flask route '/hello' that returns "Hello <name>", the name should be passed as a query string parameter
	2. name must contains only letters
2. Sum two numbers - Implement a method (api route) which takes two numbers and return their sum
	1. Implement a route '/sum' which takes as query string parameters two numbers, and returns their sum in the format: "<number1> + <number2> = <number1+number2>"
3. Calculate exam grade - Implement a method (api route) that takes exam points and returns the grade
	1. Implement a route '/calculate_exam_grade'  that takes as an input exam points and returns the exam grade in the format: "Your grade is: <grade>"
		- The exam points must be within this range 0 <= exam points <= 100
		- If exam points are negative or more than 100, you should return a message telling that the exam points are out of range
		- Grade conversion ranges:
			1. 5, if 0 <= exam points <= 49
			2. 6, if 50 <= exam points <= 59
			3. 7, if 60 <= exam points <= 69
			4. 8, if 70 <= exam points <= 79
			5. 9, if 80 <= exam points <= 85
			6. 10, if 86 <= exam points <= 100
4. MinMax -  Implement a method (api route) which finds the minimum and the maximum value from a list
	1. Implement a route '/minmax' that takes as an JSON Object data a list of numbers, and finds the minimum and maximum numbers. The return must be in the format: "Minimum value: <minimum>, maximum value: <maximum>"
		- If the list is empty you should return a message indicating that the input list is empty
		- If the list contains only one number, you should return: "Minimum and maximum value is: <number>", <number> is the single number in list
5. Insert - Implement a method (api route) which insert a product into mongoDB 
	1. Create a route '/insert_product', which takes as an input JSON format data and inserts it in the product collection
		- Product Collection Structure: 
			{
				"productID" : "abcdef123456",
				"name : "Adidas Rivalry Low",
				"category" : "shoes",
				"price" : 71.29,
				"basePrice" : 89.95
			} 
		- Attribute productID must be generated on the server side and it is a unique ID of length 12 containing only numbers and letters (the server should accept on request data only name, category, price and base price of a product)
      6.    Find - Implement a method (api route) that will find some documents (records) from mongoDB
	1. Create a route '/find_products', that will find all products from category "shirts". The category should be passed as a query string parameter and the response should be a JSON Object

Notes: 
1. *** Methods for tasks 2,3,4 must be implemented on a single class named "Calculations", and this class must be instantiated in the flask server, then on each respective route you should call the respective methods from "Calculations" object. This class must be written in a different python script and not in the same place with the flask server.
2. MongoDB database name must be behamics and collection should be named products
3. MongoClient from pymongo library must be used as a database connection interface
4. You should provide a python script inside the application to test all api endpoints (routes) using requests library (Bonus if you can test endpoints using an API client tool such as Postman or Insomnia)
