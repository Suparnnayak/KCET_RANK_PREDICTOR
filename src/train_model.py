import os
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def train():
    try:
        # Load data
        data_path = os.path.join("data", "kcet_cutoff_data.csv")
        df = pd.read_csv(data_path)
        print("📄 Data loaded:", data_path)

        # Select features and targets
        X = df[["Round", "Category", "CutoffRank"]].copy()
        y_college = df["College"]
        y_branch = df["Branch"]

        # Encode categorical features
        encoder_round = LabelEncoder()
        encoder_category = LabelEncoder()

        X["Round"] = encoder_round.fit_transform(X["Round"].astype(str))
        X["Category"] = encoder_category.fit_transform(X["Category"].astype(str))

        # Handle invalid CutoffRank values
        X["CutoffRank"] = pd.to_numeric(X["CutoffRank"], errors="coerce")
        X = X[(X["CutoffRank"] > 0) & (X["CutoffRank"] < 300000)]

        # Remove any infinities or NaNs
        X.replace([np.inf, -np.inf], np.nan, inplace=True)
        X.dropna(inplace=True)

        # Align targets with cleaned X
        y_college = y_college.loc[X.index]
        y_branch = y_branch.loc[X.index]

        print("\n✅ Cleaned Data Info:")
        print(X.info())
        print("✅ Max CutoffRank:", X["CutoffRank"].max())

        # Train models
        print("\n🚀 Training college model...")
        model_college = RandomForestClassifier(n_estimators=50, max_depth=25, random_state=42)
        model_college.fit(X, y_college)

        print("🎓 College model trained!")

        print("\n🚀 Training branch model...")
        
        model_branch = RandomForestClassifier(n_estimators=50, max_depth=25, random_state=42)
        model_branch.fit(X, y_branch)

        print("🎓 Branch model trained!")

        # Save models and encoders
        os.makedirs("artifacts", exist_ok=True)
        with open("artifacts/model_college.pkl", "wb") as f:
            pickle.dump(model_college, f)
        with open("artifacts/model_branch.pkl", "wb") as f:
            pickle.dump(model_branch, f)
        with open("artifacts/encoder_round.pkl", "wb") as f:
            pickle.dump(encoder_round, f)
        with open("artifacts/encoder_category.pkl", "wb") as f:
            pickle.dump(encoder_category, f)

        print("\n✅ All models and encoders saved in 'artifacts/'")

    except MemoryError:
        print("❌ MemoryError: Try reducing n_estimators or max_depth in RandomForestClassifier.")
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")

if __name__ == "__main__":
    train()
