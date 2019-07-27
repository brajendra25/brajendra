import numpy
import collections
import matplotlib.pyplot as plt

#print(numpy.__version__)
fileDict = {}
duplicateList =[]
lines = []
splitLines =[]

width = 1/2.2
column1=[]
column2 =[]

def ReadData(file):
    fileName = file
    fileData = open(fileName,'r')
    lines = fileData.readlines()
    for line in lines:
        splitLines=line.split(',')
        if splitLines[4] not in fileDict:
            fileDict[splitLines[4]] = [(splitLines[2],splitLines[3])]
            duplicateList.append(splitLines[4]) 
            
        else:
            newValue = splitLines[2],splitLines[3]
            fileDict[splitLines[4]].append(newValue)
            duplicateList.append(splitLines[4])
       

    '''This will have count of RO Ven wise'''
    counter=collections.Counter(duplicateList)
    
    
    
    
    #print("Visit of VIN:")
    #print(counter)
    fileOpen = open("E:\Brajendra\\countVisit.txt",'w')
    fileOpen.writelines("VInNo" + "," +"Count" + "\n")
    count = 0
    for key in counter:
         if count > 0:
             column1.append(key)
             column2.append(counter[key])
             fileOpen.writelines(str(key).replace('\n',''))
             fileOpen.writelines(",")
             fileOpen.writelines(''+ str(counter[key]))
             fileOpen.writelines("\n")
         count = count  + 1
    
     
    #print("VIn with RO and Work Type:")
    #print(fileDict)

    
    #print("Duplicate List :", duplicateList)
    #print(counter)
    fileData.close()

''''testList = ('RO_NO', 'WORK_TYPE')
print("Test Length :",len(testList))'''
    
ReadData("E:\Brajendra\Python-Data\data.txt")
print("Start")
#plt.plot(column2,column1,color="red")
plt.xticks(rotation=90)
plt.bar(column1, column2, width, color="blue")
plt.show()
print("End")
