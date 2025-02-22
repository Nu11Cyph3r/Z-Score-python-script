# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58,
               42, 25, 97, 49, 33, 75, 53, 14, 53,
               45, 87, 75, 66, 62, 55, 57, 44, 44,
               94, 19, 96, 12, 59, 86, 88, 61, 68,
               37, 64, 19, 46, 68, 98, 19, 54, 65,
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11,
               -18, -13, -24, -21, 14, 19, 20, 13, 16,
               8, 4, 3, 18, 22, 17, 7, -12, -3,
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575,
               25, 225, 150, 425, 75, 175, 650,
               600, 625, 675, 250, 100, 0, 375,
               500, 400, 450, 300, 525, 50, 200]


#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set) / len(data_set)


def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set]) / len(data_set)
    # return the square root of the variance calculation
    return variance ** .5


def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)


def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)


#########################################
# Complete the following function. #
# You may call the functions above, #
# but do not define any others. #
# You will need to add parameters. #
# You may also use arithmetic operators, #
# i.e. +, -, *, **, / #
#########################################

def z_score(score, data_set, avg):
    """
    Calculates and return z-score of the score.
    """
    zScore = (score - mean(data_set)) / stdev(data_set, mean(data_set))
    return zScore


# Call z_score() with necessary arguments to get the z-score for:
# 1. the mean of the population list,
mean_z_score = z_score(mean(population1), (population2), population3)
# 2. the greatest value in the population list,
greatest_z_score = z_score(greatest(population1), (population2), population3)
# 3. the least value in the population list.
least_z_score = z_score(least(population1), (population2), population3)

# Print the results upto 2 decimal places.
print("The z-score for the mean is: {:.2f}".format(mean_z_score))
print("The z-score for the greatest value is: {:.2f}".format(greatest_z_score))
print("The z-score for the least value is: {:.2f}".format(least_z_score))

###################################
#   Group members:                #
#   Dexter Francis                #
#   Nathaniel Schwarz             #
###################################
