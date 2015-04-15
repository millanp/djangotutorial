from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from pollolol.models import Question, Choice
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'pollolol/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollolol/detail.html', {'question':question})
def results(request, question_id):
    return HttpResponse("Lookn rsults of q %s"%question_id)
def vote(request, question_id):
    p = Question.objects.get(pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'pollolol/detail.html', {
            'question':p,
            'error_message':"You didn't select a choice!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('pollolol:results', args=(p.id)))