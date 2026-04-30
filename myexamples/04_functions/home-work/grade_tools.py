def is_passing(score):
    return score >= 50


# Score label
# 90 - 100 A
# 80 - 90  B
# 70 - 80  C
# 60 - 70  D
# <50      F
def grade_label(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 50 and score < 70:
        return "D"
    else:
        return "F"
    return None

print("Is passed:",is_passing(51))
print("Is passed:",is_passing(49))
print("Grade:",grade_label(91))
print("Grade:",grade_label(81))
print("Grade:",grade_label(71))
print("Grade:",grade_label(51))
print("Grade:",grade_label(61))
print("Grade:",grade_label(41))