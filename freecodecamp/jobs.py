import time
import requests
from bs4 import BeautifulSoup


def main():
    search = input("Enter a search term: ").replace(" ", "+")
    excl = exclusions()
    time_ = input("Repeat the program with interval of how many minutes? ")
    print(f"The program will search for job listing once every {time_} minutes...\n")
    try:
        while True:
            get_jobs(search, excl)
            time.sleep(int(time_) * 60)
    except KeyboardInterrupt:
        print("\nGoodbye!")


def exclusions() -> list:
    exclude = []
    print("Unfamiliar skills: ")
    try:
        while True:
            excl = input("> ")
            exclude.append(excl)
    except KeyboardInterrupt:
        print("> > > > > > > > > > > > > > > > >\n")
        return exclude


def get_jobs(search: str, exclude: list) -> None:
    webpage = requests.get(f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={search}&txtLocation=")
    soup = BeautifulSoup(webpage.text, "lxml")

    latest_jobs = soup.find_all("li", {"class":"clearfix job-bx wht-shd-bx"})
    for job in latest_jobs:
        date = job.find("span", {"class":"sim-posted"}).span.text.strip()
        if "few" not in date:
            continue
        skills = job.find("span", {"class":"srp-skills"}).text.split(",")
        skills = list(map(str.strip, skills))
        if bool(set(exclude).intersection(skills)):
            continue
        company = job.find("h3", {"class":"joblist-comp-name"}).text.strip()
        info = job.header.h2.a["href"]
        print(f"Company: {company}")
        print(f"Required Skills: {', '.join(x.capitalize() for x in skills)}")
        print(f"Apply here: {info}\n")
    print("=============================================================================")


if __name__ == "__main__":
    main()