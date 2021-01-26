#B1901264
#TAN SHI QI 
from uniAssign import Assignment,AssignmentList
student=AssignmentList('')
def main():
    subjectName=str(input('Enter subject name:'))
    print('{} Assignment Organiser'.format(subjectName))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    choice=menu()
    while choice!=0:
        #precessing
        if choice ==1:
            addNewAssignment()
            
        elif choice==2:
            if student.assignmentList==[]:
                print('No assignment has been added yet!')
            else:
                displayAllAssignments()
                
        elif choice==3:
            displaySummary()
            
        elif choice==4:
            displayMark_betweenvalue()
            
        elif choice==5:
           student.sortsAssignments()
        elif choice==6:
            if student.assignmentList==[]:
                print('No assignment has been added yet!')
            else:
                SaveAssignment()
        elif choice==7:
            LoadAssignment()
            

        else:
            print('Invalid choice! Try again.')
  
        print()
        print('{} Assignment Organiser'.format(subjectName))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        choice=menu()

    print('Department is closed...')

def menu():
    print('1. Add an assignment')
    print('2. Display All assignments')
    print('3. Display Summary information for all assignments')
    print('4. Display assignments with marks between values entered by user')
    print('5. Sort and display assignments by name or marks')
    print('6. Saving assignment to file')
    print('7. Loading assignment from file')
    print()
    print('0. Exit')
    print()
    response=int(input('Your choice:'))
    return response

#allow user to add new assignment
def addNewAssignment():
    print('Adding assignment:')
    name=str(input('Student name?'))
    if (name==''):
        print('Name cannot empty! Please enter again')
        name=str(input('Student name?'))
        
    assignmentMark=int(input('Integer mark?'))
    if assignmentMark<0:
         print('Invalid value! Please enter again')
         assignmentMark=int(input('Integer mark?'))
         
    daysLate=int(input('Days late?'))
    if daysLate<0:
        print('Invalid value! Please enter again')
        daysLate=int(input('Days late?'))
    newAssignment=Assignment(name,assignmentMark,daysLate)
    student.addAssignment(newAssignment)
    print('Addition success...')
    return name,assignmentMark,daysLate   
    
#will display all assignment
def displayAllAssignments():
        print('Your assignments are\n')
        print(student.allAssignment())
#will display the assignment summary
def displaySummary():
    print('Number of assignment submitted: ' ,(student.getnoOfAssignment()))
    print('Average mark for all assignment(s):',(student.averageMark()))
    print('Highest mark assignment:\n * ',str(student.highestMarkAssignment()))
    print('Lowest mark assignment:\n * ',str(student.lowestMarkAssignment()))
    if(student.noOfLateSubmissions()==0):
        print('There is no late submission assignment.')
    else:
        print('The number of late submitted assignments:',student.noOfLateSubmissions())
#display the assignment between the value
def displayMark_betweenvalue():
    student.getAssignmentsWithMarkBetween()
# sort the assignment
def SortAssignment():
    student.sortsAssignments()
#save the assignment
def SaveAssignment():
    student.saveToFile()
#load the assignment    
def LoadAssignment():
    newdata='Y'and 'N';
    if student.assignmentList!=[]:
        newdata=input('Do you want to save current assignments? (Y/N)')
        if(newdata.upper()=='Y'):
            student.saveToFile()
        elif(newdata.upper()=='N'):
            print('You are not save the file')
    else:
        student.loadFromFile()

    
main()
    
