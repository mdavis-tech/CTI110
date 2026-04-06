# Misti Davis
# 04/06/2026
# P4HW1 - Score List and Grade Calculator
# This program collects a user-defined number of scores, validates input,
# removes the lowest score, calculates the average, and assigns a letter grade.


"""
PSEUDOCODE:

1. Ask the user how many scores they want to enter
2. Create an empty list to store scores

3. Loop for the number of scores:
    a. Ask user to enter a score
    b. While the score is NOT between 0 and 100:
        - Display error message
        - Ask again for a valid score
    c. Add valid score to the list

4. Find the lowest score in the list
5. Remove the lowest score from the list

6. Calculate the average of the remaining scores

7. Determine letter grade based on average:
    A = 90-100
    B = 80-89
    C = 70-79
    D = 60-69
    F = below 60

8. Display:
    - Lowest score
    - Modified score list
    - Average
    - Letter grade
"""


# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Create empty list
score_list = []

# Loop to collect scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    # Validate score
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    # Add valid score to list
    score_list.append(score)

# Find and remove lowest score
lowest_score = min(score_list)
score_list.remove(lowest_score)

# Calculate average
average = sum(score_list) / len(score_list)

# Determine letter grade
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {letter_grade}")
print("--------------------------------")