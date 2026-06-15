import time

def countdown_challenge(n):
    if n < 0:
        return

    print(f"Counting down: {n}")  
    time.sleep(0.5) 
    countdown_challenge(n - 1)
    print(f"{n}") 

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

start_val = 5

print(f"--- Starting Countdown from {start_val} ---")
countdown_challenge(start_val)

print("\n--- Factorial Calculation ---")
result = calculate_factorial(start_val)
print(f"The factorial of {start_val} is: {result}")