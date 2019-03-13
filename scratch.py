from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

#Lynda Flemming (Assingments)(Social Studies)
html = urllib.request.urlopen('https://www.catawbaschools.net/Page/10769').read()
print(text_from_html(html), file=open("socialstudiesassingments.txt", "a"))

#Lynda Flemming (Home Work Due Dates)(Social Studies)
html = urllib.request.urlopen('https://www.catawbaschools.net/Page/11185').read()
print(text_from_html(html), file=open("socialstudieshomeworkduedate.txt", "a"))

#Google Drive Link to Math Homework
print('<a href="https://drive.google.com/drive/folders/1-P6qa803WY2amw2vEWnjPP_8cPEMxlTp">mathhomework</a>', file=open("mathhomework.html", "a"))
#Google Drive Link to Science Homework
print('<a href="https://drive.google.com/drive/folders/1YsZjXzp6DBlmoHiYzPicmAuZDa5M0bXT">sciencehomework</a>', file=open("sciencehomework.html", "a"))