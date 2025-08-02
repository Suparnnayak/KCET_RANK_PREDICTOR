from flask import Flask, render_template, request
from src.predict import predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        round_input = request.form.get("round_input").strip()
        category_input = request.form.get("category_input").strip()
        try:
            cutoff_rank = float(request.form.get("cutoff_rank"))

            college, branch = predict(round_input, category_input, cutoff_rank)
            prediction = {
                "college": college,
                "branch": branch
            }

        except ValueError as e:
            error = f"Prediction failed: {str(e)}"

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
