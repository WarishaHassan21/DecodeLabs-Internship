from flask import Flask, render_template, request
from recommender import recommend_movies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        user_preferences = request.form.getlist("genre")
        recommendations = recommend_movies(user_preferences)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)