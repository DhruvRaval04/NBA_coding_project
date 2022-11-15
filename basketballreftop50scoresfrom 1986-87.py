from import_requests import WebScraper
import requests
from bs4 import BeautifulSoup
import csv
import re

yeargap = 50
year = 1960
w, h = 2, 50
mvplist = [[0 for x in range(w)] for y in range(h)] 
while (year!=2010):
    i = 0
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html#per_game_stats::pts_per_g"
    #WebScraper.create_csv(url)

    mvpurl = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + ".html"
    mvp = WebScraper.mvp(mvpurl) 
    mvplist[i][0] = year
    mvplist[i][1] = mvp

    year = year + 1
    i = i+1

print(mvplist)
headings = ["Year", "MVP"]

with open(("mvp.csv"), "w",  encoding="utf-8") as f:
    wr = csv.writer(f,delimiter=',')
    wr.writerow(headings)
    wr.writerows(mvplist)