# LOGARITHMS
## A Logarithm is the inverse of an exponent.

import math

# BASIC LOGARITHM
def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * (math.log(num_followers, 2))

# MIN DOUBLINGS TO REACH A TARGET
def min_doublings_to_reach(start, target):
    count = 0
    while(start < target):
        start *= 2
        count += 1
    return count

# LOGARITHMIC SCALE
def log_scale(data, base):
    logs = []
    for num in data:
        logs.append(math.log(num, base))
    return logs

