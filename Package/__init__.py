from bs4 import BeautifulSoup
import requests
def function():
    content = requests.get("https://www.bmkg.go.id/")

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        find = soup.find("title")
        title = find.string
        print(title)
