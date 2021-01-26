#B1901264
#TAN SHI QI 
class Assignment :
    'field: name, assignmentMark,daysLate'
    #class variable
    def __init__(self,name,assignmentMark,daysLate):
        self.name = name
        self.assignmentMark = assignmentMark
        self.daysLate = daysLate       
    #getter methods
    def getName(self):
        return self.name
    def getAssignmentMark(self):
        return self.assignmentMark
    
    def getDaysLate(self):
        return self.daysLate
    
    def getPenaltyMark(self):
        penalty_mark=0
        if(self.daysLate!=0):
            penalty_mark =5*self.getDaysLate()
        return penalty_mark
    
    def getFinalMark(self):
        finalMark=self.getAssignmentMark()-self.getPenaltyMark()
        return finalMark
    #setter methods       
    def setName(self,name):
        self.name =name
            
    def setAssignmentMark(self,assignmentMark):
        self.assignmentMark =(assignmentMark)
            
    def setDaysLate(self,daysLate):
         if(self.daysLate>0):
             self.daysLate =(daysLate)
          
    def __str__(self):
        if(self.daysLate!=0):
            return '{}:{} (Adjusted by {} marks of original {})'.format(self.getName(),self.getFinalMark(),self.getPenaltyMark(),self.getAssignmentMark())
        else:
            return '{}: {}'.format(self.getName(),self.getFinalMark())

    def __lt__(self,other):
        return self.getFinalMark() < other.getFinalMark()
    def __le__(self,other):
        return self.getFinalMark() <=other.getFinalMark()
  
class AssignmentList:
    
    def __init__(self,subjectname):
        self.subjectname = str(subjectname)
        self.assignmentList = []
    #getter methods
    def getSubjectName(self):
        return self.subjctname
    
    def getassignmentList(self):
        return self.assignmentList
    #setter methods 
    def setSubjectName(self,subjectname):
        self.subjectname=name
        
    def setassignmentList(self):
        self.assignmentList = []
        
    # add another assignments    
    def addAssignment(self,object):
        self.assignmentList.append(object)
    #get the total number of assignment    
    def getnoOfAssignment(self):
        return len(self.assignmentList)
    
    #display all assignment
    def allAssignment(self):
        result=''
        no=1
        for object in self.assignmentList:
                result+=str(no)+'.'+str(object)+'\n'
                no+=1
        return result
    # get the average mark
    def averageMark(self):
        totalMark=0
        for object in self.assignmentList:
            totalMark+=object.getFinalMark()
            averageMark=totalMark/(len(self.assignmentList))
        return averageMark
    #find the lowest mark
    def lowestMarkAssignment(self):
        lowestMarkAssignment=self.assignmentList[0]
        for i in range(1,len(self.assignmentList)):
            if self.assignmentList[i].getFinalMark()<lowestMarkAssignment.getFinalMark():
                lowestMarkAssignment=self.assignmentList[i]
        return lowestMarkAssignment
    #find the highest mark
    def highestMarkAssignment(self):
        highestMarkAssignment=self.assignmentList[0]
        for i in range(1,len(self.assignmentList)):
            if self.assignmentList[i].getFinalMark()>highestMarkAssignment.getFinalMark():
                highestMarkAssignment=self.assignmentList[i]
        return highestMarkAssignment
    #find the total number of late assignment
    def noOfLateSubmissions(self):
        totalLate=0
        noOfLateSubmissions=self.assignmentList[0]
        for i in range(len(self.assignmentList)):
             L=0
             if self.assignmentList[i].getDaysLate()>L:
                totalLate+=1
        return totalLate  
    #get the assignment with the mark between        
    def getAssignmentsWithMarkBetween(self):
        Markbetween=''
        inputMark=self.assignmentList[0]
        mark1=int(input('Enter integer mark 1:'))
        if (mark1<0):#if the input is invalid need to enter again
            print('Invalid value! Please enter again')
            mark1=int(input('Enter integer mark 1:'))
        mark2=int(input('Enter integer mark 2(>mark1):'))
        if (mark2< mark1 or mark2<0):#if the input is invalid need to enter again
            print('Invalid value! Please enter again')
            mark2=int(input('Enter integer mark 2(>mark1):'))     
        for i in range(len(self.assignmentList)):
            if(mark1<=self.assignmentList[i].getFinalMark()<=mark2):
                Markbetween+=str(self.assignmentList[i])+'\n'
            #elif(mark1>=self.assignmentList[i].getFinalMark()>=mark2):
                #Markbetween+=str(self.assignmentList[i])+'\n'
        print('Assignment(s):\n',Markbetween)
        if (Markbetween==''):# if the input no between in the list will show the message
            print('No assignments with marks between{} and {}!'.format(mark1,mark2))
        return Markbetween
    #sort the assignment by name or mark
    def sortsAssignments(self):
        sortListResult=''
        searchCategory='name' and 'mark'
        searchCategory=input('Sort according to <name> or <mark>?')
        if (searchCategory.lower() == 'mark'):
            sortList=sorted(self.assignmentList, key=lambda self:self.getFinalMark())
            for object in sortList:
                sortListResult+=str(object)+'\n'
                
        elif (searchCategory.lower() == 'name'):
            sortList=sorted(self.assignmentList, key=lambda self:self.getName())
            for object in sortList:
                sortListResult+=str(object)+'\n'
        print('Assignments sorted according to {}\n{}'.format(searchCategory,sortListResult))
            
        
        return sortListResult
    #save the file
    def saveToFile(self):
        fileName=str(input('File name?'))
        lop=[]
        fileSave=open(str(fileName),'w')
        for object in self.assignmentList:
            lop.append(object)
            fileSave.write('{},{},{}\n'.format(object.getName(),object.getAssignmentMark(),object.getDaysLate()))
        fileSave.close()
        print('Data successfully saved...')
        return len(lop)

    #load the file
    def loadFromFile(self):
        fileLoadName=str(input('File name?'))
        fileLoad=open(str(fileLoadName),'r')
        for line in fileLoad:
            line=line.rstrip('\n')
            data=line.split(',')
            name=data[0]
            assignmentMark=int(data[1])
            daysLate=int(data[2])
            newAssignment=Assignment(name,assignmentMark,daysLate)
            self.assignmentList.append(newAssignment)
        fileLoad.close()
        print('Data has been successfully loaded...')
        
        



    
