# Exercise 1: Shopping List Calculator

# Step 1: Get input for 3 items and their prices
item1_name = input("Enter the name of the first item: ")
item1_price = float(input("Enter the price of the first item: "))
item2_name = input("Enter the name of the second item: ")
item2_price = float(input("Enter the price of the second item: "))
item3_name = input("Enter the name of the third item: ")
item3_price = float(input("Enter the price of the third item: "))

# Step 2: Store the items in a list of sublists
shopping_list = [[item1_name, item1_price], [item2_name, item2_price], [item3_name, item3_price]]

# Step 3: Calculate the total cost using indexing
total = shopping_list[0][1] + shopping_list[1][1] + shopping_list[2][1]

# Step 4: Print each item and price, and the total
print("Shopping List:")
print("Item:", shopping_list[0][0], "- Price: $", shopping_list[0][1])
print("Item:", shopping_list[1][0], "- Price: $", shopping_list[1][1])
print("Item:", shopping_list[2][0], "- Price: $", shopping_list[2][1])
print("Total cost: $", total)

# Bonus: Add tax calculation
tax_rate = float(input("Enter the tax rate (e.gsome text Tax Rate (%): "))
tax_amount = total * (tax_rate / 100)
total_with_tax = total + tax_amount
print("Total with tax: $", total_with_tax)

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 2: Student Grade Manager

# Step 1: Create a list with 3 predefined scores
grades = [85.5, 90.0, 78.5]

# Step 2: Get one more score from user and append it
new_score = float(input("Enter a new score: "))
grades.append(new_score)

# Step 3: Print first and last scores using indexing
print("First score:", grades[0])
print("Last score:", grades[-1])

# Step 4: Calculate average of all 4 scores
average = (grades[0] + grades[1] + grades[2] + grades[3]) / 4
print("Average score:", average)

# Step 5: Sort the list and print it
grades.sort()
print("Sorted grades:", grades)

# Bonus: Insert a bonus score of 5.0 at the start
grades.insert(0, 5.0)
print("Grades with bonus:", grades)

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 3: Word Slicer

# Step 1: Get a sentence from the user
sentence = input("Enter a sentence with at least 4 words: ")

# Step 2: Convert to a list of words
words = sentence.split()

# Step 3: Use slicing and indexing to print specific words
print("First 2 words:", words[0:2])
print("Last 2 words:", words[-2:])
print("Third word:", words[2])

# Step 4: Print total number of words and datatype
print("Total words:", len(words))
print("Datatype:", type(words))

# Bonus: Concatenate first and last words
new_string = words[0] + " " + words[-1]
print("First and last word combined:", new_string)

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 4: Budget Tracker

# Step 1: Initialize list with 3 expenses
expenses = [25.5, 10.0, 15.75]

# Step 2: Get one more expense from user and append it
new_expense = float(input("Enter a new expense: "))
expenses.append(new_expense)

# Step 3: Calculate total and average of 4 expenses
total = expenses[0] + expenses[1] + expenses[2] + expenses[3]
average = total / 4
print("Total expenses:", total)
print("Average expense:", average)

# Step 4: Insert $5.00 at the start
expenses.insert(0, 5.0)

# Step 5: Print updated list
print("Updated expenses:", expenses)

# Bonus: Print and sum the last 3 expenses
last_three = expenses[-3:]
last_three_sum = last_three[0] + last_three[1] + last_three[2]
print("Last 3 expenses:", last_three)
print("Sum of last 3 expenses:", last_three_sum)

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 5: Name Analyzer

# Step 1: Get full name from user
full_name = input("Enter your full name (3 parts, e.g., John Adam Smith): ")

# Step 2: Split into a list
names = full_name.split()

# Step 3: Print first, last, and middle names
print("First name:", names[0])
print("Last name:", names[-1])
print("Middle name:", names[1:2])

# Step 4: Create list of lengths and print it
lengths = [len(names[0]), len(names[1]), len(names[2])]
print("Lengths of each name:", lengths)

# Step 5: Calculate and print total characters
total_chars = lengths[0] + lengths[1] + lengths[2]
print("Total characters:", total_chars)

# Bonus: Remove middle name and print updated list
names.pop(1)
print("List after removing middle name:", names)

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 6: Number Guessing Game

# Main task
secret_number = 42
attempts = 0

# Get initial guess
guess = int(input("Guess the number (1-100): "))
attempts = attempts + 1

# Keep asking until correct
while guess != secret_number:
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess the number (1-100): "))
    attempts = attempts + 1

# Print result
print("Congratulations! You guessed the number:", secret_number)
print("It took you", attempts, "attempts.")

# Bonus: With max attempts
secret_number = 42
attempts = 0
max_attempts = 5

# Get initial guess
guess = int(input("Guess the number (1-100, 5 attempts max): "))
attempts = attempts + 1

# Keep asking until correct or max attempts reached
while guess != secret_number and attempts < max_attempts:
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess the number (1-100): "))
    attempts = attempts + 1

# Check if they won or lost
if guess == secret_number:
    print("Congratulations! You guessed the number:", secret_number)
    print("It took you", attempts, "attempts.")
else:
    print("Game Over! The number was", secret_number)


# ----------------------------------------------------------------------------------------------------------------------------
    
# Exercise 7: Sum Until Stop
    
# Main task
total = 0.0

# Get first number
number = float(input("Enter a number (negative to stop): "))

# Keep adding until a negative number
while number >= 0:
    total = total + number
    number = float(input("Enter a number (negative to stop): "))

# Print result
print("Total sum:", total)

# Bonus: Include count
total = 0.0
count = 0

# Get first number
number = float(input("Enter a number (negative to stop): "))

# Keep adding and counting until a negative number
while number >= 0:
    total = total + number
    count = count + 1
    number = float(input("Enter a number (negative to stop): "))

# Print results
print("Total sum:", total)
print("Number of values entered:", count)

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 8: List Builder

# Main task
items = []

# Get first item
item = input("Enter an item (type 'done' to stop): ")

# Keep adding until 'done'
while item != "done":
    items.append(item)
    item = input("Enter an item (type 'done' to stop): ")

# Print results
print("Final list:", items)
print("Number of items:", len(items))

# Bonus: Print first half
items = []

# Get first item
item = input("Enter an item (type 'done' to stop): ")

# Keep adding until 'done'
while item != "done":
    items.append(item)
    item = input("Enter an item (type 'done' to stop): ")

# Print results
print("Final list:", items)
print("Number of items:", len(items))

# Print first half using slicing
half_index = len(items) // 2
print("First half of list:", items[0:half_index])

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 9: Reverse Number Printer

# Main task
number = 10

# Print numbers down to 1
while number > 0:
    print(number)
    number = number - 1

# Print done
print("Done!")

# Bonus: Print only even numbers
number = 10

# Print even numbers down to 2
while number > 0:
    if number % 2 == 0:
        print(number)
    number = number - 1

# Print done
print("Done!")

# ----------------------------------------------------------------------------------------------------------------------------

# Exercise 10: Word Length Collector

# Main task
word_lengths = []

# Get first word
word = input("Enter a word (press Enter to stop): ")

# Keep adding lengths until empty string
while word != "":
    word_lengths.append(len(word))
    word = input("Enter a word (press Enter to stop): ")

# Calculate total characters
total_chars = word_lengths[0] + word_lengths[1] + word_lengths[2] if len(word_lengths) >= 3 else 0

# Print results
print("Word lengths:", word_lengths)
print("Total characters:", total_chars)

# Bonus: Include first and last word lengths
word_lengths = []

# Get first word
word = input("Enter a word (press Enter to stop): ")

# Keep adding lengths until empty string
while word != "":
    word_lengths.append(len(word))
    word = input("Enter a word (press Enter to stop): ")

# Calculate total characters
total_chars = word_lengths[0] + word_lengths[1] + word_lengths[2] if len(word_lengths) >= 3 else 0

# Print results
print("Word lengths:", word_lengths)
print("Total characters:", total_chars)
print("First word length:", word_lengths[0])
print("Last word length:", word_lengths[-1])