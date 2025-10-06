from django.http import JsonResponse                    #(2) import JsonResponse
from django.shortcuts import  render, HttpResponse, redirect        #(1) (6)
from .models import *                                               #(2)
import random                                                       #(2)
# Create your views here.
def home(request):                                                          #(1)
    #return HttpResponse("Hello world!")                                     #(1) render in server
    context = {'categories' : Category.objects.all()} #(5) For choosing the list of category in frontend

    if request.GET.get('category'): #(6) For rendering the web page to connect
        return redirect(f"/quiz?category={request.GET.get('category')}")
    
    return render(request, 'home.html', context) #(4) (5)

def quiz(request):
    context = {'category' : request.GET.get('category')} #(8)
    return render(request, 'quiz.html', context)

# {
#     'status' : True
#     'data' : [
#         {},
#     ]
# }

def get_quiz(request):                                                      #(2)
    try:
        #question_objs = list(Question.objects.all())
        question_objs = Question.objects.all() #(7)
        if request.GET.get('category'): #(7)
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        
        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)             #shuffling the question randomly

        print(question_objs)

        for question_obj in question_objs:                                  #(2)
            data.append({
                "uid" : question_obj.uid,
                "category" : question_obj.category.category_name,
                "question" :question_obj.question,
                "marks" : question_obj.marks,
                "answer" : question_obj.get_answers()               #(3) from editing in models.py

            })
        
        payload = {'status' : True , 'data' : data}
        return JsonResponse(payload)
    
    except Exception as e:                                                  #(2)
        print(e)
        return HttpResponse("Something went wrong!")