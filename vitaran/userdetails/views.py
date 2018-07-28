from django.shortcuts import render
from userdetails.forms import UserDetailForm

# Create your views here.

def userdetail(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = UserDetailForm()
    return render(request, 'userdetail/userdetail.html', {'form': form})

def adddetails(request, user):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))