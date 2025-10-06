from django.db import models
import uuid                                     #(1)
import random                                   #(3)                                         
# Create your models here.
class BaseModel(models.Model):                       #(1)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  #uuid helps to make uniqueID (ex: UUID('38156268-e6da-461b-b18f-79e75c754b71') and UUID('502eb032-bd3f-4c07-a146-8f72dc38616b'))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:               # Using NestedClass, because we don't want BaseModel as Table in database.
        abstract = True

class Category(BaseModel):  #Inheritance        #Table of category of questions, based on subjects.
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:           #(2) it helps to show the data NAME in string.
        return self.category_name       #(2)

class Question(BaseModel):              #Table of questions
    category = models.ForeignKey(Category, related_name='catagory', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:           #(2) it helps to show the data NAME in string.
        return self.question            #(2)
    
    def get_answers(self):                  #(3) It returns the answers
        answer_objs = list(Answer.objects.filter(question = self) )
        random.shuffle(answer_objs)
        data =[]
        for answer_obj in answer_objs:
            data.append({
                'answer' : answer_obj.answer,
                'is_correct' : answer_obj.is_correct
            })
        return data

class Answer(BaseModel):                    #Table of answers
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:           #(2) it helps to show the data NAME in string.
        return self.answer            #(2)