from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

def index(request):
    students = Student.objects.all().order_by('rank')
    total_studs = Student.objects.all().order_by('-total')
    rnk = 1
    for s in total_studs:
        s.rank = rnk
        s.save()
        rnk += 1
    return render(request, 'student.html', {'students':students})  
         

@csrf_exempt
def StudentCreate(request):
    if request.method == 'POST' and request.is_ajax():
        if Student.objects.filter(name=request.POST['name']).exists():
            return JsonResponse({'msg':'Student Name already Exists'})

        total = int(request.POST['mark_one']) + int(request.POST['mark_two']) + int(request.POST['mark_three'])
        Studentdata = Student(name=request.POST['name'],mark_one=request.POST['mark_one'],mark_two=request.POST['mark_two'],mark_three=request.POST['mark_three'],total=total) 
        Studentdata.save()
        new_id = Studentdata.id
        student_data = Student.objects.filter(id=new_id).values()
             
        return JsonResponse({'student_data':list(student_data)})
    else:
        return JsonResponse({'data':'failure'})     


@csrf_exempt
def StudentDelete(request):
    if request.method == 'POST' and request.is_ajax():
        id = request.POST['deleteId']
        student = Student.objects.get(id=id).delete()
        return JsonResponse({'data':'success'})
    else:
        return JsonResponse({'data':'failure'})     


@csrf_exempt
def StudentShow(request):
    if request.method == 'POST' and request.is_ajax():
        edidId = request.POST['editId']
        StudentData = Student.objects.filter(pk=edidId).values()
        return JsonResponse({'StudentData':list(StudentData),'data':'success'})
    else:
        return JsonResponse({'data':'failure'})    


@csrf_exempt  
def StudentUpdate(request):
    if request.method == 'POST' and request.is_ajax():
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['name']
        mark_one = body['mark_one']
        mark_two = body['mark_two']
        mark_three = body['mark_three']
        total = int(mark_one) + int(mark_two) + int(mark_three)

        updateId = body['updateId']
        Student.objects.filter(pk=updateId).update(name=name,mark_one=mark_one,mark_two=mark_two,mark_three=mark_three,total=total)     
        return JsonResponse({'data':'Success'})
    else:
        return JsonResponse({'data':'failure'})   

