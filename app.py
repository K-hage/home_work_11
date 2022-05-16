from flask import Flask, request, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates_list = load_candidates_from_json()

    candidates = {x["id"]: x["name"] for x in candidates_list}
    return render_template("list.html",
                           candidates=candidates
                           )


@app.route("/candidate/<int:pk>")
def candidate_card(pk):
    candidates_list = get_candidate(pk)

    return render_template("card.html",
                           name=candidates_list["name"],
                           position=candidates_list["position"],
                           image=candidates_list["picture"],
                           skills=candidates_list["skills"]
                           )


@app.route("/search/")
@app.route("/search/<candidate_name>")
def candidate_search(candidate_name=""):
    candidates_list = get_candidates_by_name(candidate_name)

    candidates = {x["id"]: x["name"] for x in candidates_list}
    return render_template("search.html",
                           total_candidates=len(candidates_list),
                           candidates=candidates,
                           name=candidate_name
                           )


@app.route("/skills/")
@app.route("/skills/<skill>")
def candidates_skill(skill=""):
    candidates_list = get_candidates_by_skill(skill)

    candidates = {x["id"]: x["name"] for x in candidates_list}
    return render_template("skills.html",
                           total_candidates=len(candidates_list),
                           candidates=candidates,
                           skill=skill
                           )


if __name__ == "__main__":
    app.run(debug=True)
