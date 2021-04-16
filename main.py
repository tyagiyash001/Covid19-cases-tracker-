import requests
from bs4 import BeautifulSoup

import tkinter as tk

def get_html_data(url):
    data=requests.get(url)
    return data.text

def get_covid_data():
    url="https://www.worldometers.info/coronavirus/"
    html_data=get_html_data(url)
    soup = BeautifulSoup(html_data, 'html.parser')
    info_div=soup.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")

    all_data=""

    for block in info_div:
        text=block.find("h1",class_=None).get_text()
        count=block.find("span",class_=None).get_text()
        all_data=all_data+text+" "+count+"\n"
    return all_data

def get_country_data():
    name=textfield.get()
    url="https://www.worldometers.info/coronavirus/country/"+name

    html_data = get_html_data(url)
    soup = BeautifulSoup(html_data, 'html.parser')

    info_div = soup.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")

    all_data = ""

    for block in info_div:
        text=block.find("h1",class_=None).get_text()
        count=block.find("span",class_=None).get_text()
        all_data=all_data+text+" "+count+"\n"
    mainlabel['text']=all_data

root=tk.Tk()
f=("poppins",25,"bold")
root.geometry("900x700")
root.title("Covid Tracker")

banner=tk.PhotoImage(file="covid.png")
bannerlabel=tk.Label(root,image=banner)

bannerlabel.pack()

textfield=tk.Entry(root,width=50)
textfield.pack()

intro=tk.Label(root,text="World Stats for covid 19 are given below.. For specific country's stats type name in above box",font=f)
intro.pack()

mainlabel=tk.Label(root,text=get_covid_data(),font=f)
mainlabel.pack()


gbtn=tk.Button(root,text="Get Data",font=f,relief='solid',command=get_country_data)
gbtn.pack()


root.mainloop()
