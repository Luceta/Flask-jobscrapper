from flask import Flask, render_template,request, redirect
from .scrapper  import scrape_jobs,get_jobs
from .wework import get_jobs as wejobs

app = Flask(__name__)


db = {}

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword:
        keyword = keyword.lower()
        from_db = db.get(keyword)

        if from_db:
            jobs = from_db
        else:
            # jobs = get_jobs(keyword)
            we_jobs = wejobs(keyword)


            db[keyword] = we_jobs
    else:
        return redirect("/")
    return render_template("search.html",keyword=keyword,jobs=we_jobs )
