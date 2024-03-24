import requests
from bs4 import BeautifulSoup


def extract_jobs(url):
    print("weworkremote page Scrapping")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    job_section = soup.find_all("section", class_="jobs")
    remote_jobs_a_tags = [
        a
        for section in job_section
        for a in section.find_all(
            "a", href=lambda href: href and href.startswith("/remote-jobs")
        )
    ]

    job_info_list = []
    for job in remote_jobs_a_tags:
        company = (
            job.find("span", class_="company").text.strip()
            if job.find("span", class_="company")
            else None
        )
        job_title = (
            job.find("span", class_="title").text.strip()
            if job.find("span", class_="title")
            else None
        )
        location = (
            job.find("span", class_="region").text.strip()
            if job.find("span", class_="region")
            else None
        )
        job_link = "https://weworkremotely.com" + job["href"]

        job_data = {
            "company": company,
            "title": job_title,
            "location": location,
            "job_link": job_link,
        }

        job_info_list.append(job_data)

    return job_info_list


def get_jobs(keyword):
    base_url = (
        f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    )
    jobs = extract_jobs(base_url)
    return jobs
