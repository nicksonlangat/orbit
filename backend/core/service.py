import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.db import transaction

from .models import Organization


def scrape_data(tag):
    questions = []

    url = f"https://stackoverflow.com/questions/tagged/{tag}" 

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="questions")

    posts = results.find_all("div", class_="s-post-summary")

    for post in posts:
        title = post.find("h3", class_="s-post-summary--content-title")
        link = post.find("h3", class_="s-post-summary--content-title").a["href"]
        description = post.find("div", class_="s-post-summary--content-excerpt")
        stats = post.find("div", class_="s-post-summary--stats js-post-summary-stats")
        stats_list = stats.find_all("div", class_="s-post-summary--stats-item")
        all_stats = []
        for stat in stats_list:
            number = stat.find("span", class_="s-post-summary--stats-item-number")
            unit = stat.find("span", class_="s-post-summary--stats-item-unit")
            all_stats.append({
                "number": number.text,
                "unit": unit.text
            })
        meta = post.find("div", class_="s-post-summary--meta")
        tags = meta.find("div", class_="s-post-summary--meta-tags")
        tag_list = tags.find("ul", class_="js-post-tag-list-wrapper")
        all_tags = tag_list.find_all("li", class_="js-post-tag-list-item")
        post_tags = [
            {"name": tag.text,
             "link": f"https://stackoverflow.com{tag.a['href']}" } for tag in all_tags]
        user = meta.find("div", class_="s-user-card s-user-card__minimal")
        avatar = user.find("div", class_="gravatar-wrapper-16").img["src"]
        user_info = user.find("div", class_="s-user-card--info")
        name = user_info.find("div", class_="s-user-card--link").a.text
        name_link = user_info.find("div", class_="s-user-card--link").a["href"]
        time = user.find("time", class_="s-user-card--time").span.text
        all_stats[0], all_stats[1] = all_stats[1], all_stats[0]

        questions.append({
            "title": title.text,
            "description": description.text,
            "stats": all_stats,
            "tags": post_tags,
            "avatar": avatar,
            "time": time,
            "name": name,
            "user_link": name_link,
            "link": f"https://stackoverflow.com{link}"
        })

    return questions

def get_github_issues(url):

    url = url.strip().split('/')
    owner = url[3]
    repo = url[4]
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/issues", 
        headers={"Authorization": f"Bearer {settings.GITHUB_ACCESS_TOKEN}"}
        )
    
    return response.json()

@transaction.atomic
def organization_create(data, *args, **kwargs) -> Organization:

    obj = Organization(
        url=data["url"]
    )

    obj.full_clean()
    obj.save()

    return obj
