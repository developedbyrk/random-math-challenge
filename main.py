import random
import time

OPERATORS = ['+', '-', '*']
MIN_VALUE = 5
MAX_VALUE = 10
MAX_PROBLEMS = 10

def generateProblems():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    operant = random.choice(OPERATORS)

    problem = f"{left} {operant} {right}"
    currectAns = eval(problem)

    return problem, currectAns


input("Press Enter when you're ready to begin...")

start_time = time.time()

wrong = 0

for i in range(MAX_PROBLEMS):
    problem, currectAns = generateProblems()

    while True:
        userAns = input(f"#Problem {i + 1} is {problem}: ")

        if str(currectAns) == userAns:
            break
        
        wrong += 1

end_time = time.time()
time_taken = end_time - start_time

print(f"Wrong Attemts : {wrong}")
print(f"You completed the quiz in {round(time_taken, 2)} seconds.")