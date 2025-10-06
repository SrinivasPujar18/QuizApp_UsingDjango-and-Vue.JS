from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)           #Class Category

class AnswerAdmin(admin.StackedInline): #(2) data showing in inline
    model = Answer                      #(2)

class QuestionAdmin(admin.ModelAdmin):  #(2) 
    inlines = [AnswerAdmin]             #(2) data showing in inline

admin.site.register(Question, QuestionAdmin) #Class Question
admin.site.register(Answer)             #Class Answer