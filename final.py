# impoting required modules
import requests
from bs4 import BeautifulSoup
import spacy
from spacy import displacy
import check



# importing wiki articles in paragraphs
def find_para(i):
    b = i[:len(i)-1]
    # url = f"https://en.wikipedia.org/wiki/{b}"
    url = f"https://en.wikipedia.org/wiki/History_of_India"
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    body = soup.find('div', {'id': 'mw-content-text'})
    return body.find_all('p')


# finding all places indicators
def find_places(i):
    nlp = spacy.load('xx_ent_wiki_sm')
    # Text with nlp
    doc = nlp(i)
    # Display Entities
    a= displacy.render(doc, style="ent")
    soup = BeautifulSoup(a, 'html.parser')
    coor = soup.find_all('mark')
    newList = []
    for j in coor:
        if j.find('span').text == 'LOC':
            c=(j.text.split('    ')[1])
            newList.append(c[0:len(c)-1])
    return newList        

# finding all time indicators
def findTime(k):
    timeList1 = ['BCE', 'CE', 'centuries', 'century', 'Centuries', 'Century', 'AD', 'millennium']
    flist=[]
    lis = k.split(' ')
    flist = []
    for j in range(1,len(lis)):
        for i in timeList1:
            o = 0
            for q in timeList1:
                if lis[j-1].startswith(q):
                    o = 1
                    break
            if o == 0:
                if j != len(lis)-1:
                    if lis[j].startswith(i):
                        l=0
                        n = 'asjghxas'
                        for m in timeList1:
                            if lis[j+1].startswith(m):
                                l = 1
                                n = m
                                break
                        if l == 0:
                            flist.append(lis[j-1]+' '+i)
                        else:
                            flist.append(lis[j-1]+' '+i+' '+n)   
                    else:
                        if lis[j].startswith(i):
                            flist.append(lis[j-1]+' '+i)
    for j in range(1,len(lis)-1):
        if lis[j]=='years' and lis[j+1]=='ago':
            flist.append(lis[j-1]+' years ago')
    # print(flist)
    return flist

f = open("project.txt", "r")
titles = f.readlines()

# for i in titles:
#     lis=list(find_links(i))


paraList=list(find_para(titles[0]))   
for para in paraList[0:4]:
    sentPara = str(para).split('.')
    for i in range(0, len(sentPara)):   
        # print(sentPara[i]) 
        sentPara[i] = BeautifulSoup(sentPara[i], 'html.parser')
    paraPlaces = find_places(str(para.text))
    paraTime = findTime(str(para.text))
    # print(paraTime)
    
    for i in sentPara:
        sentLinks = i.find_all('a')
        sentPlaces = find_places(str(i.text))
        sentTime = findTime(str(i.text))
        # print(find_places(str(i.text)))
       
        for k in sentLinks:
            if k.get('href').startswith('''#cite_note'''):
                continue
            a = sentPlaces
            if len(sentPlaces) == 0:
                a = paraPlaces
            a = paraPlaces if len(sentPlaces) == 0 else sentPlaces    
            b = paraTime if len(sentTime) == 0 else sentTime    
            tup = (k.get('href'), a, b, check.allplaces(k.get('href')))
            print(f"{tup} \n")
            # print(sentTime)

    print("***********************************************************************")
f.close()