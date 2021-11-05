import json #So JSON will work

#List declarations
answerKey = ['A', 'C', 'D', 'C', 'A', 'B', 'A', 'C', 'A', 'D', 
             'B', 'A', 'C', 'A', 'A', 'C', 'D', 'C', 'A', 'D',
             'C', 'A', 'A', 'C', 'D', 'C', 'A', 'B', 'A', 'D']

#Function to read json file into a dictionary
def readJson(key1): 
    #Opens JSON file
    f = open('app.json')
    #Reads file into list
    studentAnswers = json.load(f)
    f.close()
    #Calls function to pass lists
    grade(studentAnswers, key1)

#This function grades the student answers list 
def grade(stuAnswers, key2):
    #Creates lists to store correct and incorrect answers
    correct_list = []
    wrong_list = []
    
    #Uses the 'enumerate' function to return the index.
    for index, (ai, bi) in enumerate(zip(key2, stuAnswers)):
        #Since problems start with 1, not 0
        problem_number = index + 1 
        #If items in list are the same that item is moved to new list
        if ai == bi:
            correct_list.append(problem_number)
        #Else if they are not the same the item is appended into this list
        else:
            wrong_list.append(problem_number)

    #Print the length of the list, not the list itself.
    print(len(correct_list), 'questions were answered correctly.')
    print(len(wrong_list), 'questions were answered incorrectly.')

    if len(correct_list) >= 15:
        print('Congrats, you have passed')
    else: 
        print('Sorry, you have failed. Please study and try again.')
    
    #Pass list to letter grade
    letter_grade(correct_list)
    #Passes lists to results function 
    results(correct_list, wrong_list)

#Prints what the grade percentage and letter grade is  
def letter_grade(correct):
    grade = (len(correct)/30) * 100
    print(f"Your score is: {grade:.2f}%")
    if grade > 89:
        print("You passes with an A.")
    elif grade > 79:
        print("You passed with a B.")
    elif grade > 69:
        print("You passed with a C.")
    elif grade > 59:
        print("You passed with a D.")
    else:
        print("You failed with an F.")
    
#This function changes the items in the lists and merges them into one list  
def results(correct, incorrect):
    #Sends the currect state of the correct list to JSON file to be used later in display function
    with open('out.json', 'w') as f:
        json.dump(correct, f)
    f.close()
    #Sends the currect state of the incorrect list to JSON file to be used later in display function
    with open('out1.json', 'w') as f:
        json.dump(incorrect, f)
    f.close()
    #Change all items in list to Y
    for index, item in enumerate(correct):
        if item < 50:
            correct[index] = 'Y' 
    #Change all items in list to N
    for index, item in enumerate(incorrect):
        if item < 50:
            incorrect[index] = 'N'
    #Merge lists into single list
    result = correct + incorrect
    #Reads result list to function
    with open('result.json', 'w') as f:
        json.dump(result, f)
    f.close()
    
    #Passes lists to function 
    display(correct, incorrect)
    
def display(correct, incorrect):
    #Opens JSON file
    f = open('out.json')
    #Reads file into list
    correct1 = json.load(f)
    f.close()
    #Opens JSON file
    f = open('out1.json')
    #Reads file into list
    incorrect1 = json.load(f)
    f.close()
    #Print
    print("Total results for correct and incorrectly answered questions(Y = correct, N = incorrect): ")
    #Displays correct question numbers alongside correct symbol
    for num1, num2 in zip(correct1, correct):
        print(str(num1), '  ', str(num2))
    #Does same as above but for incorrect
    for num1, num2 in zip(incorrect1, incorrect):
        print(str(num1), '  ', str(num2))
            
#Main  
#Function call
readJson(answerKey)