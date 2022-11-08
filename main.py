from bs4 import BeautifulSoup
import requests
import mailler as mailler
import time

email_list = []
songs = []
al = []
 
def get_content():
    url="https://www.naijaloaded.com.ng/" 
    page=requests.get(url)
    soup=BeautifulSoup (page.content, 'html.parser')
    for div in soup.find_all('div', class_= "recommended-wrap"):
        for uref in div.find_all('a'):
           for h3 in div.find_all('h3'):
               songs.append(h3.get_text() +" --- " + uref['href']+"\n")
        return songs


def get_emails():
    with open("list.txt", "r") as list:
        obj = list.read()
        emails = obj.split('\n')
        for email in emails:
            email_list.append(email.split('-')[1])
 
               
def run():
    get_emails()
    for mail in email_list:
        print(mail)
        content_list = get_content()
        subject = "Bulk Music List"
        content_list[0] = subject
        for cl in content_list:
            cl = cl+'\n'
            al.append(cl)
        content = ''.join(al)
        send = mailler.Report_to_mail(mail,subject,content)
        send.run()
        print(f"[+] sending message to {mail}")
        time.sleep(2)
 
run()
