import requests
from bs4 import BeautifulSoup
try:
    enter = int(input("enter the page number :"))
    res = requests.get(f"https://news.ycombinator.com/?p={enter}")
    # print(res.text)
    data = BeautifulSoup(res.text, "html.parser")
    links = data.select(".titleline > a")
    print(links[0])
    subtext = data.select(".subtext")
    print(subtext[0])


    def create_api(links, subtext):
        api=[]
        for index, item in enumerate(links):
            title = item.getText()
            href = item.get("href", None)
            vote = subtext[index].select(".score")
            # print(vote)
            if len(vote):
                point = int(vote[0].getText().replace(" points", ""))
                # print(point)


        if point > 99:
              api.append({"title": title, "link": href, "votes": point})
            # api.append({"title": title, "link":href})
        return api
    print(create_api(links, subtext))
except ValueError:
    print("only integers are allowed")



