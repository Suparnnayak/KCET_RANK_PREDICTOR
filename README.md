# 🎓 KCET Admission Predictor

A machine learning-based web app that predicts the most likely **college** and **branch** based on a student's **KCET rank**, **category**, and **counselling round**.

## 📌 Features

- Predicts **college** and **branch** from real historical KCET data
- Built with `RandomForestClassifier`
- Clean web interface using **Flask**
- Input form with dropdowns for Round and Category
- Lightweight, efficient predictions (only one year of data used)

## 🚀 How it Works

1. User selects:
   - Round (e.g., *Mock*, *Round 1*)
   - Category (e.g., *GM*, *2AR*, *SCG*)
   - KCET Rank (e.g., *12345*)

2. The model uses trained encoders and classifiers to predict:
   - Most probable **college**
   - Most probable **branch**

## 🗂️ Project Structure

```
KCET_RANK_DETECTOR/
│
├── app.py                  # Flask app entry point
├── data/
│   └── kcet_cutoff_data.csv      # Cleaned CSV data
├── artifacts/             
│   ├── model_college.pkl         # College prediction model
│   ├── model_branch.pkl          # Branch prediction model
│   ├── encoder_round.pkl         # LabelEncoder for Round
│   └── encoder_category.pkl      # LabelEncoder for Category
├── src/
│   ├── train_model.py            # Model training script
│   └── predict.py                # Prediction logic
├── static/
│   ├── image.jpg                 # Background image
│   ├── temp.jpg                  # Form container background
│   └── style.css                 # CSS styling
├── templates/
│   └── index.html                # Webpage template
└── README.md
```

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Target 1**: College
- **Target 2**: Branch
- **Features**: Round, Category, Cutoff Rank
- **Libraries**: pandas, scikit-learn, flask, pickle

## ✅ Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/kcet-admission-predictor.git
   cd kcet-admission-predictor
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Train the model (if not already trained):
   ```bash
   python src/train_model.py
   ```

5. Run the app:
   ```bash
   python app.py
   ```

6. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

## 📝 Notes

- Make sure `kcet_cutoff_data.csv` only contains **one year of data** to keep model size small
- `model_college.pkl` and `model_branch.pkl` are saved using **pickle**
- Drop-downs are used in the form to avoid invalid inputs

## 📸 UI Snapshot

> ![Sample UI](static/sample_ui.png) *(Add this if you have a screenshot)*

## 🧑‍💻 Author

**Suparn Nayak**  
B.E. CSE, Sir M Visvesvaraya Institute of Technology, Bengaluru  
Developed with guidance from Manohar Patkar sir

## 📬 Feedback / Contact

- Raise an issue or feature request on this repo
- Reach out via LinkedIn or Email for collaboration

## 🏁 License

This project is open-source and free to use for educational purposes.