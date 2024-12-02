# import requests
# from bs4 import BeautifulSoup
#
# url = "https://catalog.data.gov/dataset/electric-vehicle-population-data"
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     html_content = response.text
#     print("Page fetched successfully!")
#     print(html_content)
#
#     with open("page.html", "w", encoding="utf-8") as file:
#         file.write(html_content)
#         print("HTML content saved to 'page.html'.")
# else:
#     print(f"Failed to fetch page. Status code: {response.status_code}")
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Fetch và parse HTML
url = "https://www.scrapingcourse.com/ecommerce/"
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Trích xuất dữ liệu
    titles = [h2.text for h2 in soup.find_all("h2")]
    link = [a['href'] for a in soup.find_all("a", href=True)]
    links = []

    print(titles)
    print(len(titles))
    x = 16
    for i in range(16,32):
        links.append(link[x])
        x = x + 2
    print(links)
    print(len(links))

else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
