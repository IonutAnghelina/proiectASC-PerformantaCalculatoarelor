import matplotlib.pyplot as plt

fin=open("maxperf3.txt","r")

l=fin.read().split(sep="\n")

#print(l[0])
performance=[]
years=list(range(1994,2021))
length=len(l)
#print(l[-1])

for i in range(0,length-1,3):
    print("{} {} {}".format(l[i],l[i+1],l[i+2]))
    x1=float(l[i].split()[-1])
    x2=float(l[i+1].split()[-1])
    x3=float(l[i+2].split()[-1])

    #print((x1+x2+x3)/3)
    performance.append((x1+x2+x3)/3)
plt.plot(years,performance)

plt.xlabel("Year")
plt.ylabel("Performance(TFlop/s)")

plt.show()

growth=[]

for i in range(1,len(performance)):
    progress=(performance[i]-performance[i-1])/performance[i-1]
    growth.append(100*progress)


plt.plot(years[1:],growth)

plt.xlabel("Year")
plt.ylabel("Progress percentage")

plt.show()

print("Progresul mediu inregistrat este {}%".format(sum(growth)/len(growth)))



