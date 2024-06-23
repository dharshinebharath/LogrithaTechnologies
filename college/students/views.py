from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.template.context_processors import csrf
from .models import Students

def home(request):
    #return HttpResponse("Home Page")
    homepage=loader.get_template('home.html')
    return HttpResponse(homepage.render())

def students(request):
    #return HttpResponse("Students Page")
    # studentspage=loader.get_template('students.html')
    # return HttpResponse(studentspage.render())
    students=Students.objects.all()
    data={
        "students":students
    }
    return render(request,'students.html',data)
    

def registration(request):
    #return HttpResponse("Students Page")
    registrationpage=loader.get_template('form.html')
    return HttpResponse(registrationpage.render())

def add_user(request):
    # form_data_page=loader.get_template('form_data.html')
    # return HttpResponse(form_data_page.render())
    if request.method=="GET":
        name=request.GET.get("name")
        email=request.GET.get("email")
        department=request.GET.get("department")
        if (name is not None) and (email is not None) and (department is not None):
            Students.objects.create(name=name,email=email,department=department)
            data={
                "name":name,"email":email,"department":department,"message":"Data Inserted Successfully"
            }
            return render(request,'form_data.html',data)

        else:
            data={
                "error_message":"Invalid Access",
            }
            return render(request,'form_data.html',data)



def update_form(request,id):
    #return HttpResponse("Students Page")
    print(id)
    student=get_object_or_404(Students,id=id)
    # update_form=loader.get_template('update_form.html')
    # return HttpResponse(update_form.render())
    data={
        'student':student
    }
    return render(request,'update_form.html',data)

def update_user(request,id):
    # form_data_page=loader.get_template('form_data.html')
    # return HttpResponse(form_data_page.render())
    print(id)
    student=get_object_or_404(Students,id=id)
    if request.method=="GET":
        name=request.GET.get("name")
        email=request.GET.get("email")
        department=request.GET.get("department")
        if (name is not None) and (email is not None) and (department is not None):
            student.name=name
            student.email=email
            student.department=department
            student.save()
            # Students.objects.create(name=name,email=email,department=department)
            data={
                "name":name,"email":email,"department":department,"message":"Data Updated Successfully"
            }
            return render(request,'update_form_data.html',data)

        else:
            data={
                "error_message":"Invalid Access",
            }
            return render(request,'update_form_data.html',data)

def delete_user(request,id):
    
    print(id)
    student=get_object_or_404(Students,id=id)
    student.delete()
    data={
        'message':"User Deleted Successfully"
    }
    return render(request,'delete.html',data)


