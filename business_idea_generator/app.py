from flask import Flask, render_template, request
from database import init_db, save_idea, get_all_ideas
import random

app = Flask(__name__)
init_db()

startup_names = [
"EcoSpark", "FitTrack", "StudyFlow", "AgriTech Pro",
"HealthMate", "FoodEase", "QuickLearn", "SmartCart"
]

problems = [
"Students struggle to manage study schedules.",
"Small businesses lack affordable marketing tools.",
"People find it hard to maintain fitness routines.",
"Farmers need better crop monitoring solutions."
]

solutions = [
"A mobile platform with smart planning features.",
"A web dashboard with automation and analytics.",
"A personalized tracking and reminder system.",
"A data-driven monitoring and recommendation tool."
]

target_audiences = [
"College Students",
"Small Business Owners",
"Fitness Enthusiasts",
"Farmers",
"Teachers",
"Working Professionals"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["GET", "POST"])
def generate():

 if request.method == "POST":

    industry = request.form.get("industry", "").strip()
    budget = request.form.get("budget", "").strip()
    market = request.form.get("market", "").strip()

    # Validation
    if budget == "" or market == "":
        return render_template(
            "generate.html",
            error="Please fill all fields."
        )

    budget_value = budget.replace("₹", "").replace(",", "")

    if not budget_value.isdigit():
        return render_template(
            "generate.html",
            error="Budget must contain numbers only."
        )

    idea = {
        "startup_name": random.choice(startup_names),
        "industry": industry,
        "problem": random.choice(problems),
        "solution": random.choice(solutions),
        "target_audience": random.choice(target_audiences),
        "revenue_model": random.choice([
            "Subscription",
            "Freemium",
            "Advertising",
            "Commission Based"
        ]),
        "market_score": random.randint(60, 95)
    }

    save_idea(
        idea["startup_name"],
        industry,
        idea["problem"],
        idea["solution"],
        idea["target_audience"],
        idea["revenue_model"],
        idea["market_score"]
    )

    return render_template("result.html", idea=idea)

 return render_template("generate.html")

@app.route("/dashboard")
def dashboard():

    ideas = get_all_ideas()

    total_ideas = len(ideas)

    avg_score = 0

    if total_ideas > 0:
        avg_score = round(
            sum([idea[7] for idea in ideas]) / total_ideas,
            2
        )

    return render_template(
        "dashboard.html",
        ideas=ideas,
        total_ideas=total_ideas,
        avg_score=avg_score
    )


if __name__ == "__main__":
    app.run(debug=True)