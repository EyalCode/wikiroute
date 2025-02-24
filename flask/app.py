from flask import render_template, request
from config import app, db
from bfs import breadth_first_search


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        routes = breadth_first_search(request.form["source"], request.form["target"])
    else:
        routes = []

    return render_template("index.html", routes=routes)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
