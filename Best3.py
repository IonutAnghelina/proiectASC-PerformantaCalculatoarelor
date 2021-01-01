import urllib.request
from bs4 import BeautifulSoup

fout=open("data.out","w")
maxPerf=open("maxPerf3.txt","w")

baseLink="https://www.top500.org/lists/top500/"

def parseNumber(x):
    y="".join(x.split(","))
    return y



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
            l[i+7]=parseNumber(l[i+7])
            if year<=2004:
                performanceIndex=float(l[i+7])/1000
            else:
                performanceIndex=float(l[i+7])

            print("In {}, the best computer was: {} which had {} cores and achieved a maximum performance of Rmax={} TFlop/s".format(year,el,l[i+6],performanceIndex))
            bestPos=i
            print("First {}: {}".format(year,performanceIndex),file=maxPerf)
            break

    l=l[bestPos+1:]

    for i,line in enumerate(l):
        if line=="2":
            startingPos=i
            #print("For year {}: YES {}".format(year,i))

    l=l[startingPos:] #We get rid of everything but the top

    for i,el in enumerate(l):
     if len(el)>0 and el[0].isalpha():
        l[i+7]=parseNumber(l[i+7])
        if year<=2004:
            performanceIndex=float(l[i+7])/1000
        else:
            performanceIndex=float(l[i+7])

        print("In {}, the second best computer was: {} which had {} cores and achieved a maximum performance of Rmax={} TFlop/s".format(year,el,l[i+6],performanceIndex))
        bestPos=i
        print("Second {}: {}".format(year,performanceIndex),file=maxPerf)
        break


    l=l[bestPos+1:]

    for i,line in enumerate(l):
        if line=="2":
            startingPos=i
            #print("For year {}: YES {}".format(year,i))

    l=l[startingPos:] #We get rid of everything but the top

    for i,el in enumerate(l):
     if len(el)>0 and el[0].isalpha():
        l[i+7]=parseNumber(l[i+7])
        if year<=2004:
            performanceIndex=float(l[i+7])/1000
        else:
            performanceIndex=float(l[i+7])

        print("In {}, the third best computer was: {} which had {} cores and achieved a maximum performance of Rmax={} TFlop/s".format(year,el,l[i+6],performanceIndex))
        bestPos=i
        print("Third {}: {}".format(year,performanceIndex),file=maxPerf)
        break

    #for line in l:
     #   print(line,file=fout)

    #print(l)






