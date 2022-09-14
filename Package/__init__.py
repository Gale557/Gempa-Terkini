from bs4 import BeautifulSoup
import requests
def Data_extraction():
    content = requests.get("https://www.bmkg.go.id/")

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        title = soup.find('title')
        result = soup.find('div', {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren("li")
        print(title.text)
        for res in result:
            print(res.text)

