import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    # Generate a random problem using the OPERATORS and the OPERANDS
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)  # randomly select an operator from a list

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)  # eval function to evaluate the expression
    return expr, answer

wrong = 0
input("Press Enter to start")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #{i+1}: {expr} = ")
        if guess == str(answer):
            break
        else:
            print("Incorrect. Please try again.")
            wrong += 1

end_time = time.time()
total_time = end_time - start_time
print(f"Nice work, you finished in {total_time:.2f} seconds with {wrong} incorrect attempts!")
