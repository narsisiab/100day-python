# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks
# we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# Example Input
# 56
# Example Output
# You have 1768 weeks left
# ---------------------------------------------------------------------------------------------------
# def life_in_weeks(age):
#     age=int(input("how old are you? "))
#     year_remain=90 - age
#     week_remain=year_remain *52
#     print(f"You have {week_remain} weeks left")
# life_in_weeks(0)
# ----------------------------------------------------------------------
def life_in_weeks(age):
    year_remain = 90 - age
    week_remain = year_remain * 52
    print(f"You have {week_remain} weeks left")


life_in_weeks(21)
