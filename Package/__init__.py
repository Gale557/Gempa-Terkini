from bs4 import BeautifulSoup
import requests
def function():
    try:
        content = requests.get("https://www.bmk g.go.id/")
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text)
        print(soup)
    else:
        print("Error")
