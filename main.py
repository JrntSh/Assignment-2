"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
AVARAGE_BOOK_COST = 20


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return (annual_cost / CLASS_DAYS_PER_SEMESTER) / 2


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return (annual_cost / credits) / 2


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (((annual_cost / CS1430_MEETINGS_PER_SEMESTER) / 2) / credits) * CS1430_CREDITS

def worth_it(annual_cost):
    """Give back how many books can be bought if the same amount was spent on books as was spent on tuition."""
    return annual_cost / AVARAGE_BOOK_COST


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits this semester: "))

    while True:
        # Show your menu here.

        print("Menu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per CS1430 class")
        print("6. Worth it?")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Cost per semester: ${(annual_cost) / SEMESTERS_PER_YEAR:.2f}")
        if choice == "2":
            print(f"Cost per month: ${(annual_cost) / MONTHS_PER_YEAR:.2f}")
        if choice == "3":
            print(f"Cost per day: ${((annual_cost) / CLASS_DAYS_PER_SEMESTER) / 2:.2f}")
        if choice == "4":
            print(f"Cost per credit: ${((annual_cost) / credits) / 2:.2f}")
        if choice == "5":
            print(f"Cost per CS1430 class: ${((((annual_cost) / CS1430_MEETINGS_PER_SEMESTER) / 2) / credits) * CS1430_CREDITS:.2f}")
        if choice == "6":
            print(f"Number of books that could be bought: {annual_cost / AVARAGE_BOOK_COST:.0f}") 
        if choice == "Q":
            break

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
