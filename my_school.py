'''
################################# DOCUMENTATION #################################

Author:
Prateek Kumar Singh

Limitations of the code:
The first field in the data, the top left corner of scores file must be changed accordingly with the addition of more students and courses. And must not exceed 99.
The courses and students in the scores file must be present in the courses and student files respectively for prorper code execution.
The student and course IDs must strictly start with 'S' and 'C' respectively.

'''

# Importing Essential Libraries.
import sys
from datetime import datetime

# Empty Lists as global variables to store Objects.
courses, students = [], []

class Students:
    '''
    This class contains student information, it has three attributes namely:
    student_id- Uniquely identifies every student
    student_name- Gives the name of a student
    study_mode- Indicates the type to study the student is enrolled in i.e.(Full time or Part time)
    '''

    # Default values for the threshold of FT & PT students.
    thresholdFT=50
    thresholdPT=30

    # Defining a Constructor.
    def __init__(self, student_id, student_name=None, study_mode=None):
        self.__student_id = student_id
        self.__student_name = student_name
        self.study_mode = study_mode

    # A getter method to access student_id.
    @property
    def student_id(self):
        return self.__student_id
    
    # A getter method to access student_name.
    @property
    def student_name(self):
        return self.__student_name

    # A setter method to set threshold value for FT students.
    @staticmethod
    def set_thresholdFT(value):
        Students.thresholdFT=value
    
    # A setter method to set threshold value for PT students.
    @staticmethod
    def set_thresholdPT(value):
        Students.thresholdPT=value

    # Using the Staticmethod decorator to create a Static Method student_report.
    @staticmethod
    def student_report():
        # Executes only when the scores file is not blank or empty.
        if scores_EXIST==True: 

            New_data = Old_data = ""

            # Checking if student_report.txt already exists and then storing its data.
            try:
                with open('student_report.txt') as reading: 
                    Old_data = reading.read()
            except:
                pass
            else:
                reading.close()

            student_summary = open('student_report.txt', 'w')
        
            Enl,GPA,compulsory_courses=[],[],[]

            # This chunk is used to obtain the number of compulsory courses undertaken by every student.
            for j in range(len(data)):
                course_count=0
                for i in range(len(courses)):
                    if courses[i].course_type[0]=='C' and isinstance(data[j][i], int):
                        course_count+=1
                compulsory_courses.append(course_count)

            # This chunk finds the GPA and the total number of credits for every Student.
            for i in range(len(data)):
                Credit_sum,TotalCredit=0,0
                for j in range(len(data[i])):
                    if isinstance(data[i][j],int):
                        if data[i][j] >= 80:
                            Credit_sum+=4*int(courses[j].course_credit)
                        elif data[i][j] >= 70 and data[i][j] < 80:
                            Credit_sum+=3*int(courses[j].course_credit)
                        elif data[i][j] >= 60 and data[i][j] < 70:
                            Credit_sum+=2*int(courses[j].course_credit)
                        elif data[i][j] >= 50 and data[i][j] < 60:
                            Credit_sum+=1*int(courses[j].course_credit)
                        elif data[i][j] < 50:
                            Credit_sum+=0
                        TotalCredit+=int(courses[j].course_credit)
                Enl.append(TotalCredit)

                if TotalCredit!=0:
                    GPA.append(round(Credit_sum/TotalCredit,2))
                else:
                    GPA.append('--')

            # Gives the data & time of when the report was generated.
            GenerationTime=datetime.now()
            GenerationTimeFormat = datetime.strftime(GenerationTime, "%d/%m/%Y %H:%M")
            print('Report Generated on: '+str(GenerationTimeFormat), file = student_summary) # writing to text file.

            embed= "{:<12}{:<15}{:<7}{:<7}{:<6}"
            print(embed.format("SID","Name","Mode","CrPt","GPA"))
            print(embed.format("SID","Name","Mode","CrPt","GPA"), file = student_summary) # writing to text file.
            
            print("-"*46)
            print("-"*46, file = student_summary) # writing to text file.
            embed2= "{:<12}{:<16}{:<7}{:<3}{:<3}{:<6}"

            valid_GPA, invalid_GPA=[], []
            for grade in GPA:
                if isinstance(grade,float):
                    valid_GPA.append(grade)
                else:
                    invalid_GPA.append('--')

            # to Arrange the GPAs in descending order.
            valid_GPA.sort(reverse=True) 
            valid_GPA+=invalid_GPA
            for j in range(len(valid_GPA)):
                i=GPA.index(valid_GPA[j]) # Index of highest GPA in the GPA list.
                if students[i].study_mode[0]=='F' and (compulsory_courses[i]<3 or Enl[i]<Students.thresholdFT):
                    sign='!'
                else:
                    sign=''   
                if students[i].study_mode[0]=='P' and (compulsory_courses[i]<2 or Enl[i]<Students.thresholdPT):
                    sign='!'
                    
                print(embed2.format(students[i].student_id,students[i].student_name,students[i].study_mode,Enl[i],sign,GPA[i]))
                print(embed2.format(students[i].student_id,students[i].student_name,students[i].study_mode,Enl[i],sign,GPA[i]), file = student_summary) # writing to text file.

                # Replacing GPA with -1, so that index of second student with same marks can be determined.
                GPA[i]=-1 

            print('\n', file=student_summary) # writing to text file.
            student_summary.close()
            
            print("student_report.txt generated!")

            # Reading the new output.
            with open('student_report.txt') as new: 
                New_data = new.read()
            new.close()
            
            New_data += Old_data
            
            # Appending the latest report with the old data.
            with open ('student_report.txt', 'w') as append:
                append.write(New_data)
            append.close()

        else:
            print('Scores file is EMPTY!..')


class Courses:
    '''
    This class contains the details about the courses, it has four attributes namely:
    course_id- Uniquely identifies every course
    course_title- Gives the name of the course
    course_type- Identifies the type of course i.e (compulsory or elective)
    course_credit- Gives the credit value of the course
    '''

    # Defining a Constructor.
    def __init__(self, course_id, course_title=None, course_type=None, course_credit=None):
        self.__course_id = course_id
        self.__course_title = course_title
        self.course_type = course_type
        self.course_credit = course_credit
    
    # A getter method to access course_id.
    @property
    def course_id(self):
        return self.__course_id
    
    # A getter method to access course_title.
    @property
    def course_title(self):
        return self.__course_title

    # A setter method to set course title for a paticular course.
    @course_title.setter
    def setTitle(self,value):
        self.course_title = value
    
    # A setter method to change the type of compulsory courses.
    def setType(self,value):
        if self.course_type[0]=='C' and value[0]=='C':
            self.course_type = value
        else:
            return None

    # A setter method to set credit value for a paticular course.
    def setCredit(self,value):
        self.course_credit = value

    @staticmethod
    def AverageCourse():
        global enrollments
        course_average,enrollments=[],[]
        for score in range(len(data[0])):
            value,enrollment,enrld_StdNo=0,0,0
            for std in range(len(data)):
                if isinstance(data[std][score], int):
                    value+=data[std][score]
                    enrollment+=1
                elif data[std][score]=='--': # in case of pending results.
                    enrld_StdNo+=1
                    enrollment+=1 # increment takes place since pending result does not mean student is not enrolled.
            enrollments.append(enrollment)

            if enrollment !=0 and enrollment!=enrld_StdNo:
                course_avg=round(value/(enrollment-enrld_StdNo),2)
                course_average.append(course_avg)
            else:
                if value==0:
                    course_average.append("--")
                else: 
                    course_avg=round(value/(enrollment-enrld_StdNo),2)
                    course_average.append(course_avg)
        return course_average
        
    @staticmethod
    def show_report():
        # Executes only when the scores file is not blank or empty.
        if scores_EXIST==True:
            
            New_data = Old_data = ""
            
            # Checking if course_report.txt already exists and then storing its data.
            try:
                with open('course_report.txt') as reading: 
                    Old_data = reading.read()
            except:
                pass
            else:
                reading.close()

            course_summary = open('course_report.txt', 'w')

            # Returns a list with average scores of courses.
            x=Courses.AverageCourse() 

            # Gives the data & time of when the report was generated.
            GenerationTime=datetime.now()
            GenerationTimeFormat = datetime.strftime(GenerationTime, "%d/%m/%Y %H:%M")
            print('Report Generated on: '+str(GenerationTimeFormat), file = course_summary) # writing to text file.

            embed= "{:<15}{:<21}{:<5}{:<6}{:<6}"
            print(embed.format("CID","Name","Pt.","Enl.","Avg."))
            print(embed.format("CID","Name","Pt.","Enl.","Avg."), file = course_summary) # writing to text file.
            
            print("-"*53)
            print("-"*53, file = course_summary) # writing to text file.

            embed2= "{:<12}{:<3}{:<21}{:<5}{:<6}{:<6}"
            for i in range(len(courses)):
                if courses[i].course_type[0]=="C": 
                    sign='*' # for compulsory courses.
                else:
                    sign='-' # for elective courses.
                    if courses[i].course_credit==None:
                        courses[i].course_credit=6

                if x[i]=='':
                    x[i]="--"

                print(embed2.format(courses[i].course_id,sign,courses[i].course_title,courses[i].course_credit,enrollments[i],x[i]))
                print(embed2.format(courses[i].course_id,sign,courses[i].course_title,courses[i].course_credit,enrollments[i],x[i]), file = course_summary) # writing to text file.
            print("-"*53)
            print("-"*53, file = course_summary) # writing to text file.

            # Creating a list containing only float elements so that min() function can be used to determine worse performing subject.
            y= list(i for i in x if isinstance(i, float))

            print("The worse performing course is "+str(courses[x.index(min(y))].course_id)+" with an average of "+str(min(y)))
            print("The worse performing course is "+str(courses[x.index(min(y))].course_id)+" with an average of "+str(min(y)), file = course_summary) # writing to text file.

            print('\n', file=course_summary) # writing to text file.
            course_summary.close()

            print("courses_report.txt generated!\n")

            # Reading the new output.
            with open('course_report.txt') as new: 
                New_data = new.read()
            new.close()
            
            New_data += Old_data
            
            # Appending the latest report with the old data.
            with open ('course_report.txt', 'w') as append:
                append.write(New_data)
            append.close()

        else:
            print('Scores file is EMPTY!..')

class School:
    '''
    The School Class is the Central Data Repository.
	It contains the details about Students and courses.
    '''

    # Defining a Constructor.
    def __init__(self):
        self.student = Students
        self.course = Courses
    
    def read_scores(self):
        global scores_EXIST
        scores_EXIST=False
        student_count=0
        scores_file = open(sys.argv[1],"r")
        line_from_file = scores_file.readline()
        while(line_from_file!=""):
            scores_EXIST=True # Declaring that the scores file is not Empty.
            fields_from_line = line_from_file.strip("\n").split(" ")

            if fields_from_line[0][0] != 'S':
                global data
                # 2-D array to store the scores of courses for respective students.
                data = [["" for i in range(int(fields_from_line[0][1]))] for j in range(int(fields_from_line[0][0]))] 
                
                for i in range(1,len(fields_from_line)):
                    c = self.course(fields_from_line[i])
                    courses.append(c)
            else:
                s = self.student(fields_from_line[0])
                students.append(s)
                for k in range(1,len(fields_from_line)):
                    if fields_from_line[k] == '-1':
                        data[student_count][k-1] = ""
                    if fields_from_line[k] == '888' or fields_from_line[k] == 'TBA' :
                        data[student_count][k-1] = "--"
                    
                    try:
                        if float(fields_from_line[k])>=0 and float(fields_from_line[k])<=100:
                            data[student_count][k-1] = int(float(fields_from_line[k]))
                    except:
                        pass
                student_count+=1
                
            line_from_file = scores_file.readline()		
        scores_file.close()

    @staticmethod
    def show_scores():
        # Executes when the scores file is not Empty.
        if scores_EXIST==True: 
            s,c,avg=[],[],[]

            for std in range(len(data)):
                value=0
                for score in range(len(data[std])):
                    if isinstance(data[std][score], int):
                        value+=data[std][score]
                number = len(list(i for i in data[std] if isinstance(i, int)))
                if number!=0:
                    average = value/number
                    avg.append(round(average,2))
                else:
                    avg.append('--')
            
            # Creating a list containing only float elements so that max() function can be used to determine the top student.
            max_avg=list(i for i in avg if isinstance(i, float))

            for i in range(len(students)):
                s.append(students[i].student_id)
            for j in range(len(courses)):
                c.append(courses[j].course_id)

            embed ="{:^12}"+"|{:^12}"*len(c) 
            print(embed.format(" ", *c))
            print("-"*16*len(c))
            for student, score in zip(s, data):
                print(embed.format(student, *score))
            print("-"*16*len(c))
            
            print(str(len(students))+" students, "+str(len(courses))+" courses, the top student is "+str(students[avg.index(max(max_avg))].student_id)+", average "+str(max(max_avg))+'\n')
        else: 
            print('Scores file is EMPTY!..')

    def read_courses(self):

        course_file = open(sys.argv[2],"r")
        line_from_file = course_file.readline()
        while(line_from_file!=""):
            fields_from_line = line_from_file.strip("\n").split(" ")

            for i in range(len(courses)):
                if courses[i].course_id == fields_from_line[0]:
                    try:
                        courses[i] = self.course(fields_from_line[0],fields_from_line[1],fields_from_line[2],fields_from_line[3])
                    except:
                        courses[i] = self.course(fields_from_line[0],fields_from_line[1],fields_from_line[2])
                    break
                
            line_from_file = course_file.readline()		
        course_file.close()
    
    def read_students(self):
        student_file = open(sys.argv[3],"r")
        line_from_file = student_file.readline()
        while(line_from_file!=""):
            fields_from_line = line_from_file.strip("\n").split(" ")

            for i in range(len(students)):
                if students[i].student_id == fields_from_line[0]:
                    students[i] = self.student(fields_from_line[0],fields_from_line[1],fields_from_line[2])
                    break
            else:
                s = self.student(fields_from_line[0],fields_from_line[1],fields_from_line[2])
                students.append(s)
                
            line_from_file = student_file.readline()		
        student_file.close()


def main():
    '''
	This is the main function of the program.
	It executes automatically whenever the program is run.
	'''
    # creating a school object.
    schoolOBJ= School()

    try: 
        schoolOBJ.read_scores()    
    except : # this will execute when scores.txt file is not entered in the command line.
        print("[Usage:] Python "+ sys.argv[0] +" <scores file>")
    else:
        schoolOBJ.show_scores()
    
    try:
        schoolOBJ.read_courses()
    except: # this will execute when courses.txt file is not entered in the command line.
        print("[Usage:] Python "+ sys.argv[0] +" <scores file> <course file>")
    else:
        Courses.show_report()

    try:
        schoolOBJ.read_students()
    except: # this will execute when students.txt file is not entered in the command line.
        print("[Usage:] Python "+ sys.argv[0] +" <scores file> <course file> <student file>")
    else:
        Students.student_report()

if __name__=="__main__":
	main()