import random

def test():
    print("Welcome to the Capitals Quiz")
    correct = 0
    incorrect = 0
    answer = 0
    states=[
        {
            "name": "Alabama",
            "capital": "Montgomery"
        }, {
            "name": "Alaska",
            "capital": "Juneau"
        }, {
            "name": "Arizona",
            "capital": "Phoenix"
        }
            ]
    random.shuffle(states)

    for state in states: 
       
        print(f'What is the capital of this state: {state["name"]}?')
        userInput = input().lower()
        if(userInput == state["capital"].lower()):
            answer +=1
            correct += 1
            total_correct += correct
            print("Correct!")
            print(f'Correct Answer {correct} Incorrect Answer {incorrect} You have answer {answer} times')

        else: 
            answer +=1
            incorrect +=1
            print("Incorrect!")
            print(f"Correct Answer {correct} Incorrect Answer {incorrect} You have answer {answer} times")

        if(answer == 3):
            print("Do you have to play capital games again? Y/N")
            userInput = input().lower()
            if(userInput == 'y'):
                test()
            else:
                print("Total Correct Answers:", total_correct)
                return

test()
