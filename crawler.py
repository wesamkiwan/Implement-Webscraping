from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

##########################################

url="https://en.wikipedia.org/wiki/List_of_largest_banks"
html_data=requests.get(url).text
soup=BeautifulSoup(html_data,"html.parser")


data= pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
for row in soup.find_all('tbody')[4].find_all('tr')[1:]:        #[1:] used to delete the first list as it is empty list (must be checked again)
    cells=row.find_all('td')
    bank_name=cells[1].text.strip()
    market_cap=cells[2].text.strip()
    data=data.append({"Name":bank_name,"Market Cap (US$ Billion)":market_cap}, ignore_index=True)
    
print(data)

final_data=data.to_json()
print(final_data)