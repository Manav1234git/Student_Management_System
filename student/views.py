from django.shortcuts import render,redirect

from .models import Student
def student_home(request):

    student_data=Student.objects.all()

    data={"student_data":student_data}
    return render(request,"student/student_home.html",data)

def add_student(request):
    if request.method == "POST":
        student_name=request.POST.get("input_name")
        student_email=request.POST.get("input_email")
        student_phone_no=request.POST.get("input_phone_no")
        
        Student.objects.create(name=student_name,email=student_email,phone_no=student_phone_no)
        return redirect("student_home")
    

    return render(request,"student/add_student.html")

def delete_student(request,id):
    my_student=Student.objects.get(id=id)
    my_student.delete()
    print("done")
    return redirect("student_home")

def update_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        student.name=request.POST.get("input_name")
        student.email=request.POST.get("input_email")
        student.phone_no=request.POST.get("input_phone_no")
        student.save()
        return redirect("student_home")
    parameters={"student":student}
    return render(request,"student/update_student.html",parameters)