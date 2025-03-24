student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
# total_exam_score=sum(student_scores)
# print(total_exam_score)
# sum=0
# for score in student_scores:
#     sum+=score
# print(sum)
# print(max(student_scores))

# ----------------------------------------------************************************----------------------------------------------------------
largest=0
for score in student_scores:
    if largest<score:
        largest=score
print(f"The Largest number is: {largest}")