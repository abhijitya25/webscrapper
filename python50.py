import json
import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd


def trail(cruc_link):

    link = requests.get(cruc_link).text
    soup = BeautifulSoup(link, 'lxml')

    right_table = soup.find_all("a", class_="morelink")
    middle_table = soup.find_all("td", class_="ralign")
    left_table = soup.find_all("a", class_="resultquery ahint")

    definition = [word.get_text() for word in right_table]
    length = [word.get_text() for word in middle_table]
    solution = [word.get_text() for word in left_table]
    no_of_res = len(length)

    today = date.today()
    today_date = today.strftime("%d/%m/%Y")
    dictionary = []
    for i in range(0, len(definition)):
        temp = {}
        temp["Id"] = i + 1
        temp["Definition"] = definition[i]
        temp["Length"] = length[i]
        temp["Solution"] = solution[i]
        print(temp)
        dictionary.append(temp)

    output = {"URL_text": cruc_link,
              "Scrape_date": today_date,
              "Number_of_Results": no_of_res,
              "Dictionary": dictionary}

    for item in output:
        print(item, output[item])

    with open('output_js.json', 'a') as json_file:
        json.dump(output, json_file)


data = pd.read_csv("C:/Users/hp/Downloads/url.csv", encoding="ISO-8859-1")
df = pd.DataFrame(data, columns=['URL_list'])

links_to_str = df.astype(str).values.flatten().tolist()


for i in range(len(links_to_str)):
    trail(links_to_str[i])

