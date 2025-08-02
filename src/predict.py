import os
import pickle
import pandas as pd

# Dynamically load pickled files from the artifacts directory
def load_pickle(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, "..", "artifacts", file_name)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File {file_name} not found at {full_path}")
    with open(full_path, "rb") as f:
        return pickle.load(f)

def predict(round_input, category_input, cutoff_rank_input):
    # Load models and encoders
    model_college = load_pickle("model_college.pkl")
    model_branch = load_pickle("model_branch.pkl")
    encoder_round = load_pickle("encoder_round.pkl")
    encoder_category = load_pickle("encoder_category.pkl")

    # Validate and encode inputs
    try:
        encoded_round = encoder_round.transform([round_input])[0]
        encoded_category = encoder_category.transform([category_input])[0]
    except ValueError as e:
        raise ValueError("Invalid Round or Category. Please enter a value from the training data.") from e

    # Prepare input for prediction
    X_input = pd.DataFrame([{
        "Round": encoded_round,
        "Category": encoded_category,
        "CutoffRank": cutoff_rank_input
    }])

    # Make predictions
    pred_college = model_college.predict(X_input)[0]
    pred_branch = model_branch.predict(X_input)[0]

    return pred_college, pred_branch
