
from random import gammavariate
from flask import Flask
from flask import jsonify
from flask import request

class Calculation :

    def triggerSayHello(self,name) :
        if(name.isalpha()):
            return "Hello " + name
        else:
            return "Name must contains only letters"


    def calculateSum(self,a,b) :

        return a + " + " + b + " = " + str(int(a) + int(b)) 


    def calculateExamGrade(self,grade) :
     gradeToInt = int(grade)

     if(gradeToInt >=0 and gradeToInt  <=49) :
        return self.decorateTheSuccesMesage('Your grade is 5')

     elif(gradeToInt >=50 and gradeToInt <=59) :
        return self.decorateTheSuccesMesage('Your grade is 6')

     elif(gradeToInt >=60 and gradeToInt <=69) :
        return self.decorateTheSuccesMesage('Your grade is 7')
    
     elif(gradeToInt >=70 and gradeToInt <=79) :
        return self.decorateTheSuccesMesage('Your grade is 8')

     elif(gradeToInt >=80 and gradeToInt <=89) :
        return self.decorateTheSuccesMesage('Your grade is 9')
    
     elif(gradeToInt >=90 and  gradeToInt <=100) :
        return self.decorateTheSuccesMesage('Your grade is 10')
     else :
         
        return self.decorateTheErrorMessage('The exam points are out of range')


    def decorateTheSuccesMesage(self,messagge) :
        return jsonify({"message " : messagge})

    def decorateTheErrorMessage(self,message):
        return jsonify({"error" : message})
      
  
    def minMaxResponse(self,list) :

        
        if(len(list) > 1):
            results = self.findMaxAndMin(list)
            return self.decorateTheSuccesMesage ("Minimum value: " + str(results[1]) + "," + "Maximumum value: " + str(results[0]))

        elif(len(list) == 1):
            return self.decorateTheErrorMessage("Minimum and maximum value is: " + str(list[0])  + ", " + str(list[0]) + " is the single number in the list")
        
        else:
            return self.decorateTheErrorMessage("There are no numbers in the list")



    def findMaxAndMin(self,list) : 
        
        maxValue = max([int(x) for x in list])
        minValue = min([int(x) for x in list])
        return [maxValue,minValue]