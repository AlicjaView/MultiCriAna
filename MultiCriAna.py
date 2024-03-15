def weighted_sum_decision(criteria_weights, alternatives_scores):
    """
    Function performing multi-criteria decision analysis using the weighted sum method.
    
    :param criteria_weights: Criteria weights (list or tuple)
    :param alternatives_scores: Scores of alternatives for each criterion (nested list)
    :return: List of final scores for each alternative
    """
    num_criteria = len(criteria_weights)
    num_alternatives = len(alternatives_scores)
    
    if num_criteria == 0 or num_alternatives == 0:
        return None
    
    # Check if the number of scores for each alternative matches the number of criteria
    for scores in alternatives_scores:
        if len(scores) != num_criteria:
            return None
    
    # Normalize weights
    total_weight = sum(criteria_weights)
    criteria_weights = [weight / total_weight for weight in criteria_weights]
    
    final_scores = []
    for i in range(num_alternatives):
        score = sum(criteria_weights[j] * alternatives_scores[i][j] for j in range(num_criteria))
        final_scores.append(score)
    
    return final_scores

def get_user_input():
    num_alternatives = int(input("Enter the number of alternatives: "))
    alternatives_names = []
    alternatives_scores = []

    # Get names and scores for alternatives
    print("Enter names and scores for each alternative:")
    for i in range(num_alternatives):
        name = input(f"Name of alternative {i+1}: ")
        alternatives_names.append(name)

    num_criteria = int(input("Enter the number of criteria: "))
    criteria_names = []
    criteria_weights = []

    # Get names and weights for criteria
    print("Enter names and weights for each criterion (weights should be in the range of 1-10):")
    for i in range(num_criteria):
        name = input(f"Name of criterion {i+1}: ")
        weight = float(input(f"Weight of criterion {name}: "))
        criteria_names.append(name)
        criteria_weights.append(weight)

    # Get scores for alternatives
    print("Enter scores for each alternative:")
    for i in range(num_alternatives):
        scores = []
        for j in range(num_criteria):
            score = float(input(f"Score (on a scale of 1-10) for criterion {criteria_names[j]} for alternative {alternatives_names[i]}: "))
            scores.append(score)
        alternatives_scores.append(scores)

    return criteria_weights, criteria_names, alternatives_names, alternatives_scores

def main():
    criteria_weights, criteria_names, alternatives_names, alternatives_scores = get_user_input()
    
    final_scores = weighted_sum_decision(criteria_weights, alternatives_scores)
    
    if final_scores:
        # Combine alternative names, their scores, and criteria weights
        combined_results = zip(alternatives_names, final_scores)
        
        # Sort the results from least important to most important
        sorted_results = sorted(combined_results, key=lambda x: x[1])
        
        # Find the alternative with the highest score
        max_score = max(final_scores)
        
        # Display the sorted results, highlighting the highest score
        for name, score in sorted_results:
            if score == max_score:
                print(f"***Score for alternative {name}: {score}***")
            else:
                print(f"Score for alternative {name}: {score}")

if __name__ == "__main__":
    main()
