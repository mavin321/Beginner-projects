import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/List_of_best-selling_video_games"
page=requests.get(url)
soup=BeautifulSoup(page.text, "html.parser")
table=soup.find_all('table')[1]
world_titles=table.find_all("th")
world_table_titles=[title.text.strip() for title in world_titles]
table_columns=world_table_titles[:8]

import pandas as pd


column_data=table.find_all('tr')
row_data_list = []
for row in column_data[1:]:
    cells= row.find_all(["td", "th"])
    row_data=[]

    for cell in cells:
        cell_text= cell.get_text(strip=True)
        rowspan = int(cell.get("rowspan", 1))
        colspan = int(cell.get("colspan", 1))

        row_data.extend([cell_text] * colspan)

    row_data_list.append(row_data)

max_columns = len(table_columns)
normalized_rows = [row + [""] * (max_columns - len(row)) for row in row_data_list]

    # Create a pandas DataFrame
df = pd.DataFrame(normalized_rows, columns=table_columns)

print(df)
df.to_csv(r'C:\textbooks\python files\videogames.csv', index=False)