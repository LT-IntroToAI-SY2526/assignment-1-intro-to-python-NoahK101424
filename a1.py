# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
> "I'm learning Python basics in a high school programming class. I have some experience with java. Can you create 5-7 practice problems that cover: 
> - Variables and basic data types 
> - Conditionals (if/elif/else) 
> - Loops (for and while) 
> - Functions 
> - Basic list operations 
> > Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Temperature Converter (Variables, Basic Data Types, Conditionals)]
[Create a program that converts temperatures between Celsius and Fahrenheit. The program should:

 - Ask the user for a temperature value and the unit (C or F)
 - Convert the temperature to the other unit
 - Display the result with appropriate messaging

Formulas:

Celsius to Fahrenheit: F = (C * 9/5) + 32
Fahrenheit to Celsius: C = (F - 32) * 5/9]

Examples: 

Enter temperature: 25
Enter unit (C for Celsius, F for Fahrenheit): C
25°C is equal to 77.0°F

Enter temperature: 68
Enter unit (C for Celsius, F for Fahrenheit): F
68°F is equal to 20.0°C
"""
def temperature_converter(temp, unit):
    """Interactive temperature converter"""

    #calculations to change convert the temperatures depending on whether the user inputs "C" or "F"
    if unit.upper() == 'C':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {fahrenheit}°F")
    elif unit.upper() == 'F':
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {celsius:.1f}°C")
    else:
        print("Invalid unit. Please enter C or F.")

"""
Problem 2: [Grade Calculator (Conditionals, Functions)]
Write a function called calculate_grade() that takes a numerical score (0-100) and returns the letter grade based on this scale:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60

The program should also indicate if the score is invalid (outside 0-100 range).
Example Input/Output:
calculate_grade(85) → "B"
calculate_grade(92) → "A"
calculate_grade(58) → "F"
calculate_grade(105) → "Invalid score"
"""

def calculate_grade(score):
    """Calculate letter grade from numerical score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

"""
Problem 3: [Number Guessing Game (Loops, Conditionals)]

Create a number guessing game where:

The computer generates a random number between 1 and 100
The user has 7 attempts to guess the number
After each guess, provide feedback: "Too high", "Too low", or "Correct!"
Keep track of the number of attempts used
If the user runs out of attempts, reveal the answer

Example Input/Output:
I'm thinking of a number between 1 and 100. You have 7 guesses.
Enter your guess: 50
Too high! 6 guesses remaining.
Enter your guess: 25
Too low! 5 guesses remaining.
Enter your guess: 37
Too high! 4 guesses remaining.
Enter your guess: 31
Correct! You won in 4 attempts!
"""

def number_guessing_game():
    """Number guessing game with 7 attempts"""
    secret_number = random.randint(1, 100)
    attempts_left = 7
    
    print("I'm thinking of a number between 1 and 100. You have 7 guesses.")
    
    while attempts_left > 0:
        try: #allows you to wrap a block of code that might potentially raise an error (an "exception") during its execution.
            guess = int(input("Enter your guess: "))
            attempts_left -= 1
            
            if guess == secret_number:
                print(f"Correct! You won in {7 - attempts_left} attempts!") #f-string, The f prefix allows you to directly insert Python expressions and variables into a string by enclosing them within curly braces {}
                return
            elif guess > secret_number:
                if attempts_left > 0:
                    print(f"Too high! {attempts_left} guesses remaining.")
                else:
                    print("Too high!")
            else:
                if attempts_left > 0:
                    print(f"Too low! {attempts_left} guesses remaining.")
                else:
                    print("Too low!")
                    
        except ValueError: #except keyword is used within a try-except block to handle exceptions (errors) that occur during the execution of code.
            print("Please enter a valid number.")
            attempts_left += 1  # Don't penalize for invalid input
    
    print(f"Game over! The number was {secret_number}.")

    """
Problem 4: [Word Counter (Functions, Loops, Basic List Operations)]

    Write a function called analyze_text() that takes a string of text and returns a dictionary containing:

Total number of words
Total number of characters (excluding spaces)
Most frequent word (case-insensitive)
List of words longer than 5 characters

Example Input/Output:
pythontext = "Python programming is fun and Python is powerful"
result = analyze_text(text)
# Should return:
{
    'total_words': 8,
    'total_characters': 37,
    'most_frequent': 'python',
    'long_words': ['python', 'programming', 'powerful']
}
    """
def analyze_text(text):
    """Analyze text and return statistics"""
    # Convert to lowercase and split into words (by spaces)
    words = text.lower().split()
    
    # Remove punctuation and get clean words
    clean_words = []
    for word in words:
        clean_word = ''.join(char for char in word if char.isalpha())
        if clean_word:  # Only add non-empty words
            clean_words.append(clean_word)
    
    # Count characters (excluding spaces)
    char_count = sum(1 for char in text if char != ' ')
    
    # Find most frequent word
    if clean_words:
        word_counts = Counter(clean_words)
        most_frequent = word_counts.most_common(1)[0][0] #most_common is a method of the Counter Class that returns a list of the most common to least common elemets
    else:
        most_frequent = None
    
    # Find long words (longer than 5 characters)
    long_words = [word for word in clean_words if len(word) > 5]
    
    return {
        'total_words': len(clean_words),
        'total_characters': char_count,
        'most_frequent': most_frequent,
        'long_words': list(set(long_words))  # Remove duplicates
    }

"""
problem 5: [Shopping Cart Calculator (Lists, Functions, Loops)]

Create a shopping cart system with the following functions:

add_item(cart, item_name, price, quantity) - adds items to cart
remove_item(cart, item_name) - removes an item from cart
calculate_total(cart) - calculates total price
apply_discount(total, discount_percent) - applies percentage discount
display_cart(cart) - shows all items in a formatted way

Each cart item should be stored as a dictionary with keys: 'name', 'price', 'quantity'
Example Usage:
pythoncart = []
add_item(cart, "Apple", 0.99, 5)
add_item(cart, "Banana", 0.59, 3)
add_item(cart, "Orange", 1.29, 2)

display_cart(cart)
# Output:
# Apple: $0.99 x 5 = $4.95
# Banana: $0.59 x 3 = $1.77
# Orange: $1.29 x 2 = $2.58
# Total: $9.30

total = calculate_total(cart)
discounted_total = apply_discount(total, 10)
# Final total after 10% discount: $8.37
"""
#like a constructor in java
def add_item(cart, item_name, price, quantity):
    """Add item to shopping cart"""
    item = { #Curly braces are used to create dictionaries, which are unordered collections of key-value pairs OR define sets
        'name': item_name,
        'price': price,
        'quantity': quantity
    }
    cart.append(item) #.append() method is used to add a single element to the end of a list.

def remove_item(cart, item_name):
    """Remove item from shopping cart"""
    for i, item in enumerate(cart): #enumerate() gives you BOTH the position AND the value when looping
        if item['name'].lower() == item_name.lower(): #checks if the input through "item_name" matches with an item in the cart
            cart.pop(i)
            return True
    return False #if the inputed item doesn't exist, retruns false

def calculate_total(cart):
    """Calculate total price of items in cart"""
    total = 0
    for item in cart:
        total += item['price'] * item['quantity'] #each item OBJECT has a name, price, and quantity (through the constructor), which is then used with the quantity here to get the price of the items in the cart
    return total

def apply_discount(total, discount_percent):
    """Apply percentage discount to total"""
    discount_amount = total * (discount_percent / 100)
    return total - discount_amount

def display_cart(cart):
    """Display all items in cart with formatting"""
    if not cart:
        print("Cart is empty")
        return
    
    for item in cart:
        subtotal = item['price'] * item['quantity']
        print(f"{item['name']}: ${item['price']:.2f} x {item['quantity']} = ${subtotal:.2f}")
    
    total = calculate_total(cart)
    print(f"Total: ${total:.2f}")



# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here
#assert temperature_converter(0, "C") == 32, "temperature_converter failed"

print("\nTesting Problem 2:")
assert calculate_grade(95) == "A", "calculatre_grade(95) failed"

print("\nTesting Problem 3:")
# Add your tests here
assert 

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


