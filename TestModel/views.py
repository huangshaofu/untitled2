from django.shortcuts import render

# Create your views here.
def index(question,question_id):
    context          = {}
    context['hello'] = 'test---url'
    return render(question, 'TestModel/hello.html', context)