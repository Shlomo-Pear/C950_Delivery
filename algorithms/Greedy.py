"""
Greedy algorithm

Unused and unaltered
"""

# Greedy Algorithm: Min Expenses => Max Profits
# Ref: WGU Webinar: Python Modules; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a6e33b6d-9753-4ba4-a1b6-ac8000f5d250

# todo adapt to package weight for truck loadup
def greedyAlgorithmMinExpenses(budget):
    total = budget
    c25dollar = 0
    c10dollar = 0
    c5dollar = 0
    c1dollar = 0
    while (budget >= 25):
        if c25dollar > 3:  # Why 3? 0, 1, 2, 3 will not break so 4 times.
            break
        c25dollar += 1
        budget -= 25
    while (budget >= 10):
        c10dollar += 1
        budget -= 10
    while (budget >= 5):
        c5dollar += 1
        budget -= 5
    while (budget > 0):
        if c1dollar > 3:
            break
        c1dollar += 1
        budget -= 1

        cDVDs = c25dollar + c10dollar + c5dollar + c1dollar

        print(f"${total:.2f}-Total Dollar Budget: {cDVDs}-DVDs =>")
        print(f" {c25dollar} x 25 dollar movie = ${c25dollar*25.00:.2f}")
        print(f" {c10dollar} x 10 dollar movie = ${c10dollar*10.00:.2f}")
        print(f" {c5dollar} x 5 dollar movie = ${c5dollar * 5.00:.2f}")
        print(f" {c1dollar} x 1 dollar movie = ${c1dollar * 1.00:.2f}")
