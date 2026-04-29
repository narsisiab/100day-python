# for loops , range and code blocks

# fruits=["apple", "peach","banana"]
# for fruit in fruits:
#     print(fruit)
# ---------------------------------------------------

students_score = [12, 13, 56, 25]
# score_sum = sum(students_score)
# print(score_sum)
# -----------------
# sum_score = 0
# for score in students_score:
#     sum_score += score
# print(sum_score)
# ----------------------
print(max(students_score))
max_score = 0
for score in students_score:
    if score > max_score:
        max_score = score
print(max_score)
