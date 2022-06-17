from pydoc import describe
from django.db import models


''' Models for Login Details '''
class Login(models.Model):
    userName = models.CharField(max_length=100, primary_key = True)
    password = models.CharField(max_length=1000)
    salt = models.CharField(max_length=1000, default= '')
    position_teacher = models.CharField(max_length=1000, default='False')
    position_student = models.CharField(max_length=1000, default='False')
    class Meta:
        db_table = "login";

 
''' Models for Teachers Details '''
class TeachersDetails(models.Model):
    teachers_userName = models.ForeignKey(Login, primary_key=True, default='unknown', on_delete=models.SET_DEFAULT)
    teachers_name = models.CharField(max_length=100)
    teachers_email = models.CharField(max_length=100)
    teachers_mobileNumber = models.CharField(max_length=1000)
    teachers_image=models.CharField(max_length=20000, null=True, blank=True)

    class Meta:
        db_table = "teachers"

''' Models for Classroom Details '''
class ClassroomDetails(models.Model):
    classroom_code = models.CharField(max_length=100, primary_key = True) 
    teacher_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    subject_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_of_creation = models.CharField(max_length=100)

    class Meta:
        db_table = "classroomDetails"

''' Models for Student Details '''
class StudentDetails(models.Model):
    student_userName = models.ForeignKey(Login, primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    student_name = models.CharField(max_length=100) 
    student_gender = models.CharField(max_length=100) 
    student_email = models.CharField(max_length=100) 
    student_mobileNumber = models.CharField(max_length=1000)
    student_image=models.CharField(max_length=100000, null=True)

    class Meta:
        db_table = "studentDetails"

''' Models for Class Access '''
class ClassAccess(models.Model):
    student_userName = models.ForeignKey(StudentDetails, default='unknown',on_delete=models.SET_DEFAULT)
    classroom_code = models.ForeignKey(ClassroomDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    date = models.CharField(max_length=1000)

    class Meta:
        db_table = "classAccess"


''' Models for Notes '''
class Notes(models.Model):
    classroom_code = models.ForeignKey(ClassroomDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    teachers_userName = models.ForeignKey(TeachersDetails, default='unknown', on_delete=models.SET_DEFAULT)
    file = models.CharField(max_length=10000)

    class Meta:
        db_table = "notes" 


''' Models for Attendence '''
class Attendence(models.Model):
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    classroom_code = models.ForeignKey(ClassroomDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    date = models.CharField(max_length=1000, default='1') 
    students_names = models.CharField(max_length=100000) 
    status = models.CharField(max_length=100000) 

    class Meta:
        db_table = "attendence"


''' Models for Quiz Details '''
class QuizDetails(models.Model):
    quiz_id = models.CharField(max_length=1000, primary_key=True)
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    classroom_code = models.ForeignKey(ClassroomDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    date = models.CharField(max_length=1000)
    totalMarks = models.CharField(max_length=10000)
    quiz_topic = models.CharField(max_length=1000)
    question1 = models.CharField(max_length=1000)
    answer1_option1 = models.CharField(max_length=1000)
    answer1_option2 = models.CharField(max_length=1000)
    answer1_option3 = models.CharField(max_length=1000)
    answer1_option4 = models.CharField(max_length=1000)
    correct1_answer_option = models.CharField(max_length=1000) 
    marks1 = models.CharField(max_length=1000) 
    question2 = models.CharField(max_length=1000)
    answer2_option1 = models.CharField(max_length=1000)
    answer2_option2 = models.CharField(max_length=1000)
    answer2_option3 = models.CharField(max_length=1000)
    answer2_option4 = models.CharField(max_length=1000)
    correct2_answer_option = models.CharField(max_length=1000) 
    marks2 = models.CharField(max_length=1000) 
    question3 = models.CharField(max_length=1000)
    answer3_option1 = models.CharField(max_length=1000)
    answer3_option2 = models.CharField(max_length=1000)
    answer3_option3 = models.CharField(max_length=1000)
    answer3_option4 = models.CharField(max_length=1000)
    correct3_answer_option = models.CharField(max_length=1000) 
    marks3 = models.CharField(max_length=1000) 
    question4 = models.CharField(max_length=1000)
    answer4_option1 = models.CharField(max_length=1000)
    answer4_option2 = models.CharField(max_length=1000)
    answer4_option3 = models.CharField(max_length=1000)
    answer4_option4 = models.CharField(max_length=1000)
    correct4_answer_option = models.CharField(max_length=1000) 
    marks4 = models.CharField(max_length=1000) 
    question5 = models.CharField(max_length=1000)
    answer5_option1 = models.CharField(max_length=1000)
    answer5_option2 = models.CharField(max_length=1000)
    answer5_option3 = models.CharField(max_length=1000)
    answer5_option4 = models.CharField(max_length=1000)
    correct5_answer_option = models.CharField(max_length=1000) 
    marks5 = models.CharField(max_length=1000) 
    question6 = models.CharField(max_length=1000)
    answer6_option1 = models.CharField(max_length=1000)
    answer6_option2 = models.CharField(max_length=1000)
    answer6_option3 = models.CharField(max_length=1000)
    answer6_option4 = models.CharField(max_length=1000)
    correct6_answer_option = models.CharField(max_length=1000) 
    marks6 = models.CharField(max_length=1000) 
    question7 = models.CharField(max_length=1000)
    answer7_option1 = models.CharField(max_length=1000)
    answer7_option2 = models.CharField(max_length=1000)
    answer7_option3 = models.CharField(max_length=1000)
    answer7_option4 = models.CharField(max_length=1000)
    correct7_answer_option = models.CharField(max_length=1000) 
    marks7 = models.CharField(max_length=1000) 
    question8 = models.CharField(max_length=1000)
    answer8_option1 = models.CharField(max_length=1000)
    answer8_option2 = models.CharField(max_length=1000)
    answer8_option3 = models.CharField(max_length=1000)
    answer8_option4 = models.CharField(max_length=1000)
    correct8_answer_option = models.CharField(max_length=1000) 
    marks8 = models.CharField(max_length=1000) 
    question9 = models.CharField(max_length=1000)
    answer9_option1 = models.CharField(max_length=1000)
    answer9_option2 = models.CharField(max_length=1000)
    answer9_option3 = models.CharField(max_length=1000)
    answer9_option4 = models.CharField(max_length=1000)
    correct9_answer_option = models.CharField(max_length=1000) 
    marks9 = models.CharField(max_length=1000) 
    question10 = models.CharField(max_length=1000)
    answer10_option1 = models.CharField(max_length=1000)
    answer10_option2 = models.CharField(max_length=1000)
    answer10_option3 = models.CharField(max_length=1000)
    answer10_option4 = models.CharField(max_length=1000)
    correct10_answer_option = models.CharField(max_length=1000) 
    marks10 = models.CharField(max_length=1000)

    class Meta:
        db_table = "quizDetails"


''' Models for Quiz Result '''
class QuizResult(models.Model):
    quiz_id = models.ForeignKey(QuizDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    student_userName = models.ForeignKey(StudentDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    classroom_code = models.ForeignKey(ClassroomDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    total_marks = models.CharField(max_length=10000)
    obtained_marks = models.CharField(max_length=10000)

    class Meta:
        db_table = "quizResult"

''' Models for Quiz Result '''
class QuizAccess(models.Model):
    id = models.CharField(max_length=10000, primary_key=True) 
    status = models.CharField(max_length=10000)

    class Meta:
        db_table = "quizAccess"  

''' Models for Notes '''
class Notes(models.Model):
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    classroom_code = models.ForeignKey(ClassroomDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    notes = models.CharField(max_length=10000)
    title_of_notes  = models.CharField(max_length=10000)
    decpriction_of_notes  = models.CharField(max_length=10000)
    type = models.CharField(max_length=100)
    class Meta:
        db_table = "notes"