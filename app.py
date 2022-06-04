from flask import Flask, render_template, url_for
import func

app = Flask(__name__)

date = func.load_candidates_from_json()


@app.route('/')
def all_candidates():
    return render_template("all_cand.html", lst=date)


@app.route('/candidate/<int:x>')
def one_candidate(x):
    cand = func.get_candidate(x, date)
    return render_template("one_cand.html", cand=cand)


@app.route('/search/<candidate_name>')
def search_name(candidate_name):
    candidate_name_list = func.get_candidates_by_name(candidate_name, date)
    return render_template("search_name.html",
                           lst=candidate_name_list,
                           x=len(candidate_name_list))


@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    candidate_skill_list = func.get_candidates_by_skill(skill_name, date)
    return render_template("search_name.html",
                           lst=candidate_skill_list,
                           x=len(candidate_skill_list))


if __name__ == "__main__":
    app.run(debug=False)
