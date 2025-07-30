import requests

Api="384cfd98ee6343baa50c742972497ba2"
# query=int(input("Enter which type of news you want to view: "))
query="AI"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-04-26&sortBy=publishedAt&apiKey={Api}"
print(url)
r=requests.get(url)

data=r.json()
articles=data["articles"]
i=0
for i in range(1,10):
    for index,article in enumerate (articles):
        news=index,article["title"], article["description"], article["url"]
        print(news)
        print("\n--------------------------------------------------------\n")
        i=i+1
        if i>=10:
            break
    if i>=10:
        break
    


