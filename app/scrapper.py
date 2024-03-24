# 유저는 python, javascript, java 등과 같은 용어를 검색할 수 있어야 합니다.
# 스크래퍼는 berlinstartupjobs.com, weworkremotely.com 및 web3.career의 결과를 표시해야 합니다.
# 우리는 이미 berlinstartupjobs.com 스크래퍼에 대한 코드가 있으므로 weworkremotely.com 및 web3.career를 스크래핑하는 코드를 작성해야 합니다.
# 검색 URL은 다음과 같습니다:
import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# url = "https://berlinstartupjobs.com/engineering/"
skills = [
    "python",
    "typescript",
    "javascript",
    "rust"
]

def scrape_jobs(keyword):
    base_url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    print(f"Scraping jobs related to {keyword}...")
    print(base_url)
    response = requests.get(base_url, headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs_list = soup.find("ul", class_="jobs-list-items")
    if jobs_list is not None:
        jobs = jobs_list.find_all("li")
        all_jobs = []

        for job in jobs:
            title = job.find("h4", class_="bjs-jlid__h").text
            company = job.find("a", class_="bjs-jlid__b").text
            position = job.find("h4", class_="bjs-jlid__h").text
            jd = job.find("div", class_="bjs-jlid__description").text.strip()
            url = job.find("a", class_="bjs-jlid__b").attrs["href"].strip()
            job_data = {
                "title": title,
                "company": company,
                "job_description": jd,
                "url": url
            }

            all_jobs.append(job_data)
        return  all_jobs
    else:
        print("No jobs found on the provided URL.")
        return []



def get_jobs(word):
    base_url = f"https://berlinstartupjobs.com/skill-areas/{word}/"
    jobs = scrape_jobs(word)
    return jobs


