from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/list_of_largest_companies_in_the_United_States_by_revenue"
page=requests.get(url)
soup=BeautifulSoup(page.text, 'html.parser')
table=soup.find_all('table')[1] #extracting the table from the wikipedia page
world_titles=table.find_all('th') #th is what represented each header of the tables
world_table_titles=[title.text.strip() for title in world_titles] #making the headers into a list

#the th and tr and td are all gotten from the website so look at the website code

import pandas  as pd
df=pd.DataFrame(columns= world_table_titles) #putting into dataframe
column_data= table.find_all('tr')
for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]#taking the  row data into lists

    length=len(df)
    df.loc[length]=individual_row_data #putting each row data into the data frame
print(df)

df.to_csv(r'C:\textbooks\python files\companies.csv', index=False)# exported into a csv file which is an excel spreadsheet
