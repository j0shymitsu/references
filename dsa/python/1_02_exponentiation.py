# BASIC EXPONENTIATION
def get_estimated_spread(audience_followers):
    if len(audience_followers) == 0:
        return 0
    else:
        avg = sum(audience_followers) / len(audience_followers)
        est_spread = avg * (len(audience_followers)**1.2)
    
    return est_spread

# GEOMETRIC SEQUENCE/GEOMETRIC PROGRESSION
## Where each term is found by multiplying the previous term by a constant
def get_follower_prediction(follower_count, influencer_type, num_months):
    match influencer_type:
        case "fitness":
            return follower_count * (4**num_months)
        case "cosmetic":
            return follower_count * (3**num_months)
        case _ :
            return follower_count * (2**num_months)
        
# EXPONENTIAL DECAY
def decayed_followers(initial_followers, fraction_lost_daily, days):
    remainder = initial_followers * ((1 - fraction_lost_daily)**days)
    return remainder