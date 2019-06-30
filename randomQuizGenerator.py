import random

   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.

#list of 4









    
        

        
        
        
        
    

    

for quizNum in range(5):
    stringQuiz = "States Quiz\n\n"
    stringKey = ""
    
    keys =  list(capitals.keys())
    random.shuffle(keys)

    answers = []
    

    for i in range(0,len(capitals)):
        
        answerKey  = {}
        
        stringQuestion = str(i+1) + ". What is the capital of " + keys[i] + "?\n"
        
        stringQuiz += stringQuestion
        
        answers = []

        answers.append(keys[i])

        for j in range(0,3):
        
            x = random.randint(0,49)
            while(x == i):
                x = random.randint(0,49)
            
            answers.append(keys[x])

        random.shuffle(answers)
        stringLetter = " " 
        for k in range(0,4):
            if k == 0:
                stringLetter = "A " 
                
            if k == 1:
                stringLetter = "B "
                
            if k == 2:
                stringLetter = "C "
         
            if k == 3:
                stringLetter = "D "
       
                        
            stringAnswer = stringLetter + capitals.get(answers[k]) + "\n"
            
            answerKey[capitals.get(answers[k])] = stringLetter
            if capitals.get(keys[i]) == capitals.get(answers[k]):
                stringKey += str(i+1) + ". " + answerKey.get(capitals.get(answers[k])) + " \n"
                
            
            stringQuiz += stringAnswer
            
        stringQuiz += "\n"
        

    quizTitle = 'quiz' + str(quizNum+1) + '.txt'
        
    quizFile = open(quizTitle, 'w')
    quizFile.close()
    quizFile = open(quizTitle, 'a')
    quizFile.write(stringQuiz)
    quizFile.close()
    
    answerTitle = 'answer' + str(quizNum+1) + '.txt'
        
    answerFile = open(answerTitle, 'w')
    answerFile.close()
    answerFile = open(answerTitle, 'a')
    answerFile.write(stringKey)
    answerFile.close()
       # TODO: Create the quiz and answer key files.

       # TODO: Write out the header for the quiz.

       # TODO: Shuffle the order of the states.

       # TODO: Loop through all 50 states, making a question for each.