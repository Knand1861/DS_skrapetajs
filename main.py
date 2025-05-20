import requests
from bs4 import BeautifulSoup
import os
from openpyxl import load_workbook, Workbook
ITEM = "rtx+3070"
def main():
    #RD
    URL = "https://www.rdveikals.lv/search/lv/word/"+ITEM+"/page/1/"
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    item_containers = soup.find_all("li", class_="product")
    print("Item count:",len(item_containers))
    items = []
    for i in item_containers:
        price = i.find("p", class_="price").get_text()
        name = i.find("div", class_="product__info__part").find("a").get_text()
        name = ' '.join(name.split())
        items.append([name,price,"RD"])
    save_to_excel(items)

def save_to_excel(items):
    file_path = "data.xlsx"

    if os.path.exists(file_path):
        workbook = load_workbook(file_path)
    else:
        workbook = Workbook()
    
    sheet = workbook.active
    bias = 2
    for i in range(0,len(items)):
        sheet[f"A{i+bias}"] = items[i][0]
        sheet[f"B{i+bias}"] = items[i][1]
        sheet[f"C{i+bias}"] = items[i][2]
    workbook.save(file_path)

if __name__ == "__main__":
    main()