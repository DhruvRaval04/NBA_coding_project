class WebScraper(): 
  
    def create_csv(url):
        import requests
        from bs4 import BeautifulSoup
        import csv
        import re
        page = requests.get(url)

        year_number = re.findall(r'\d+', url)

        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table',id ="per_game_stats")

        # find all rows
        rows = table.findAll('tr')

        # strip the header from rows
        headers = rows[0]
        header_text = []

        # add the table header text to array
        for th in headers.findAll('th'):
            header_text.append(th.text)

        # init row text array
        row_text_array = []

        # loop through rows and add row text to array
        for row in rows[1:]:
            row_text = []
        # loop through the elements
            for row_element in row.findAll(['th', 'td']):
        # append the array with the elements inner text
                row_text.append(row_element.text.replace('\n', '').strip())
         # append the text array to the row text array
            row_text_array.append(row_text)

        with open((str(year_number) + ".csv"), "w",  encoding="utf-8") as f:
            wr = csv.writer(f)
            wr.writerow(header_text)
            for row_text_single in row_text_array:
                wr.writerow(row_text_single) 


    def mvp(url):
        import requests
        from bs4 import BeautifulSoup
        import csv
        import re

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        tempinfo = soup.find("div", id = "meta")
        listofaccolades = tempinfo.find_all('a')
        mvp = ''
        num = 0
        for i in listofaccolades: 
            if num == 5:
                mvp = i.text
            num = num+1
        return str(mvp)
        #print(mvp)

    #mvp("https://www.basketball-reference.com/leagues/NBA_1988.html")

    def teamrecord(url):
        import requests
        from bs4 import BeautifulSoup as bs
        import csv
        import re
        import pandas as pd 

        r = requests.get(url)
        soup = bs(r.content, 'lxml')
        table = pd.read_html(str(soup.select_one('table:has(th:-soup-contains("Rk"))')))[0]
        columns = ['Player','Tm']
        table = table.loc[:, columns].iloc[:, :2]
        table.columns = columns
        w, h = 3, len(table)
        masterlist = [[0 for x in range(w)] for y in range(h)] 

        for i in range(len(table)):
            for j in range(2):
                masterlist[i][j] = table.iloc[i][j]
        
     
