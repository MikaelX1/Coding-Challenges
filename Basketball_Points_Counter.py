#You are counting points for a basketball game, given the amount of 2-pointers scored and
# 3-pointers scored, find the final points for the team and return that value.
# Example : points(1, 1) ➞ 5


def points(x,y):
    final_pt = 2*x + 3*y
    return final_pt

Two_pt = int(input("Enter the number of 2-pt made:"))
Three_pt = int(input("Enter the number of 3-pt made:"))

print("The final points is:", points(Two_pt,Three_pt))
