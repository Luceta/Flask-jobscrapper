from flask import Flask, render_template, request, redirect, send_file
from .scrapper import get_jobs as berlin_jobs
from .wework import get_jobs as wwr_jobs
from .web3 import get_jobs as web3_jobs
from .exporter import save_to_file

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
            berlin = berlin_jobs(keyword)
            web3 = web3_jobs(keyword)
            wwr = wwr_jobs(keyword)
            jobs = berlin + wwr + web3
            db[keyword] = jobs
    else:
        return redirect("/")
    return render_template(
        "search.html", keyword=keyword, jobs=jobs, jobCount=len(jobs)
    )


@app.route("/export")
def export():
    try:
        word = request.args.get("keyword")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv", as_attachment=True)
    except:
        return redirect("/")
