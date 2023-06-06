from random import randint

monday= "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
tuesday = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE"
wednesday = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE"
thursday = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
friday = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"

# converting to list
monday= monday.split(", ")
tuesday= tuesday.split(", ")
wednesday= wednesday.split(", ")
thursday= thursday.split(", ")
friday= friday.split(", ")

days=[tuesday,wednesday,thursday,friday]

# extending all the colors into one list
for i in days:
    monday.extend(i)

newWeek = set(monday)
ColorCount = {}

# how many times a color occurs
for i in newWeek:
    ColorCount[i] = monday.count(i)

print(len(monday))
# The mean is Blue because it occurs the most
print(ColorCount)

# 2)
# The Staff wear Blue most times of the week


# 3)
print("-------3--------")
median = sorted(monday)
print(len(median)/2)

# median
print(median[48])
# median is GREEN


# 6)
print("-------6--------")
# Count the occurrences of the color red
redCount = monday.count("RED")

# Calculate the total number of colors
totalColors = len(monday)

# Calculate the probability of choosing red
probability_red = redCount / totalColors
print(f"probability of choosing the color red at random is {probability_red}")


# 9)
print("-------9--------")
ConcatNum=""
for i in range(4):
    ab = randint(0, 1)
    ConcatNum += str(ab)

# 4 digits 0s and 1s
print(ConcatNum)

# converted to base 10
print(int(ConcatNum,2))
