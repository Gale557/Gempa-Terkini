from bs4 import BeautifulSoup
import requests
def data_extraction():
    global scale, center, bt, lu, depth, magnitudo
    content = requests.get("https://www.bmkg.go.id/")

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        title = soup.find('title')
        result = soup.find('div', {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren("li")
        print(title.text)
        i = 0
        for result in result:
            if i == 1:
                magnitudo = result.text
            elif i == 2:
                depth = result.text
            elif i == 3:
                location = result.text.split(" - ")
                lu = location[0]
                bt = location[1]
            elif i == 4:
                center = result.text
            elif i == 5:
                scale = result.text
            i +=1
    print("LIVE GEMPA")
    print(f"Magnitude : {magnitudo} Magnitude")
    print(f"Depth : {depth}")
    print(f"LU : {lu}")
    print(f"BT: {bt}")
    print(f"Center : {center}")
    print(f"scale: {scale}")
