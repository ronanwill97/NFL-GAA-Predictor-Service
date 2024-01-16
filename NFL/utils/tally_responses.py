import pandas as pd
import json


# Function to score a single prediction
def score_prediction(prediction, actual_winner):
    if prediction == actual_winner:
        return 8 if actual_winner == "Draw" else 5
    return 0


def load_updated_results(path):
    with open(path, 'r') as file:
        return json.load(file)


def extract_actual_results(updated_results):
    actual_results = {}
    for round_name, divisions in updated_results.items():
        for division, matches in divisions.items():
            for match in matches:
                match_name = f"{match[0]} vs {match[1]}"
                winner = match[2]
                actual_results[match_name] = winner
    return actual_results


def calculate_scores(fixtures_path, actual_results):
    fixtures = pd.read_csv(fixtures_path)
    match_names = fixtures.columns[3:]
    scores = {}
    for index, row in fixtures.iterrows():
        user_name = row['Name']
        user_score = sum(score_prediction(row[match], actual_results.get(match, None)) for match in match_names)
        scores[user_name] = user_score
    return scores



def main():
    results = load_updated_results("../../../GAAScores/tests/testfiles/all_results_predicted.json")
    extracted_results = extract_actual_results(results)
    scores = calculate_scores("../../../GAAScores/tests/responses/Fixtures - Round 6.csv", extracted_results)

    print("User - Score")
    print("------------")
    for user, score in scores.items():
        print(f"{user} - {score}")

if __name__ == "__main__":
    main()