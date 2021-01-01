import urllib.request
from bs4 import BeautifulSoup

fout=open("data.out","w")

baseLink="https://www.top500.org/lists/top500/"



for year in range(1994,2021):

    link=baseLink+str(year)+"/11/"

    #print(link)
    f=urllib.request.urlopen(link)

    content=f.read()

    soup=BeautifulSoup(content,'html.parser')

    textContent=soup.get_text()

    l=textContent.split(sep="\n")


    #print(textContent,file=fout)

    for i,line in enumerate(l):
        if line=="1":
            startingPos=i
            #print("For year {}: YES {}".format(year,i))

    l=l[startingPos:] #We get rid of everything but the top

    for i,el in enumerate(l):
        if len(el)>0 and el[0].isalpha():
            print("In {}, the best computer was: {} which had {} cores and achieved a maximum performance of Rmax={}".format(year,el,l[i+6],l[i+7]))
            bestPos=i
            break

  #  print(l[bestPos+7]) #The number of cores


    #for line in l:
     #   print(line,file=fout)

    #print(l)






