import matplotlib.pyplot as plt

fin=open("maxPerf.txt")

performance=[]

def parseNumber(x):
    y="".join(x.split(","))
    return y

for line in fin.readlines():
    l=line.split()
    l[-1]=parseNumber(l[-1])
    print(l[-1])
    performance.append(float(l[-1]))


years=list(range(1994,2021))

#print(years)


plt.plot(years,performance)
plt.show()


growth=[]

for i in range(1,len(performance)):
    progress=(performance[i]-performance[i-1])/performance[i-1]
    growth.append(100*progress)

plt.plot(years[1:],growth)
plt.show()
