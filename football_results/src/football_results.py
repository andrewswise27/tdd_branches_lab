def get_result(final_score):
    if final_score["Home"] > final_score["Away"]:
        return "Home Win"
    elif final_score["Away"] > final_score["Home"]:
        return "Away Win"
    else:
        return "Draw"
    

def get_results(final_scores):
    return list(final_scores.keys())
    
    # (You could try and use a list comprehension for this)