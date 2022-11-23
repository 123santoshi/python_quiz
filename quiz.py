class questions:
    correct_count=0
    wrong_count=0
    total_score=0
    def __init__(self,question,option1,option2,option3,option4,answer,score,question_no):
        self.question=question
        self.option1=option1
        self.option2=option2
        self.option3=option3
        self.option4=option4
        self.answer=answer
        self.score=score
        self.question_no=question_no
    def setvalues(self):
        print("Question {0} : {1}".format(self.question_no,self.question),"\n")
        print("option 1 : ",self.option1,"\n")
        print("option 2 : ",self.option2,"\n")
        print("option 3 : ",self.option3,"\n")
        print("option 4 : ",self.option4,"\n")
        self.user_ans=int(input("Enter yout option  :  "))
        if(self.user_ans==self.answer):
            print("\nYOUR ANSWER IS CORRECT\n")
            questions.correct_count+=1
            questions.total_score+=self.score
            print("YOUR SCORE FOR THIS QUESTION IS  :",self.score,"OUT OF",self.score,"\n")
            print("*********************  &&&&&&&&&&&&&&&&&&&&&   *********************\n")
        else:
            print("\nYOR ANSWER IS WRONG\n")
            questions.wrong_count+=1
            print("YOUR SCORE FOR THIS QUESTION IS  :",0,"OUT OF ",self.score,"\n")
            print("THE CORRECT ANS IS :",self.answer,"\n")
            print("*********************   &&&&&&&&&&&&&&&&&&&&&   *********************\n")
    def display(self):
        print("*************************************** QUIZ REPORT  ***************************************\n")
        print("   DEAR ",name.upper(),"\n")
        print("   YOU ANSWERED TOTALLY {0} CORRECT ANSWERS AND {1} WRONG ANSWERS\n".format(questions.correct_count,questions.wrong_count))
        print("   YOUR TOTAL SCORE IN THE QUIZ IS :",questions.total_score,"\n")
        if(questions.total_score>=70):
            print("   YOU HAVE PASSED THE EXAM\n")
            print("   CONGRATULATIONS\n")
        else:
            print("   YOU ARE NOT CLEARED THE EXAM\n")
            print("   BETTER LUCK NEXT TIME\n")
        print("*************************************** END  ***************************************")
    
print("\n")
print("************** WELCOME TO THE QUIZ **************\n")
print("************** please enter details for quiz ****\n")
name=input("Enter Your Name   :  ")
age=int(input("\nEnter Your Age    :  "))
option=input("\n ***** ARE YOU READY TO PLAY THE QUIZ (PRESS Y/YES/yes/y for play)***** :  ")
if(option=="yes" or option=="YES" or option=="Y" or option=="y"):
    print("\n****** %%%% ****** All THE BEST FOR THE QUIZ ****** %%%% ****** \n")
else:
    print("OK BYE")
    exit(0)
obj1=questions("Which of the following statements are used in Exception Handling in Python?","try","catch","finally","All of the above",4,20,1)
obj2=questions(" Python is developed by whom",
                "James gosling",
                "Dennis Ritchie",
                    "Guido van rossum",
                    "B.jarne stronstup",
                    3,
                    20,2)
obj3=questions("What is the maximum length of a Python identifier?",
                "32","No-fixed Length is specified","16","128",2,20,3)
obj4=questions("Which of the following concepts is not a part of Python?",
                "Pointers","Dynamic Typing ","Loops","None Of the Above",1,20,4)
obj5=questions("How is a code block indicated in Python",
                "Brackets","Semicolon","Indentation","Key",3,20,5)
obj1.setvalues()
obj2.setvalues()
obj3.setvalues()
obj4.setvalues()
obj5.setvalues()
obj1.display()

