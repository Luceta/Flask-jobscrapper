import requests
from bs4 import BeautifulSoup


def extract_jobs(url):
    print("web3 page Scrapping")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs_list = soup.select("tbody.tbody tr:not(.border-paid-table)")
    job_info_list = []

    for job in jobs_list:
        company: str | None = (
            job.select_one("div.d-flex.align-middle span.company").text.strip()
            if job.select_one("div.d-flex.align-middle span.company")
            else None
        )
        location = job.select_one("td.job-location-mobile").text.strip()

        try:
            salary = job.select_one("td p.text-salary").text.strip()
        except AttributeError:
            salary = None
        job_title = job.select_one("h2.fs-6.fs-md-5.fw-bold.my-primary").text.strip()
        job_link = job.select_one("a").get("href") if job.select_one("a") else None
        job_data = {
            "company": company,
            "location": location,
            "salary": salary,
            "job_title": job_title,
            "job_link": job_link,
        }

        job_info_list.append(job_data)

    return job_info_list


def get_jobs(keyword):
    base_url = f"https://web3.career/{keyword}-jobs"
    jobs = extract_jobs(base_url)
    return jobs
