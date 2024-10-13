from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Person, Question
from django.template import loader
from django.shortcuts import render
from django.db.models import F
from django.views import generic

# Using Custom Views

"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
"""

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# Using Generic Views

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def TestView1(request):
    istekler = Question.objects.all()
    return render(request, 'polls/test_view_1.html', locals())


import django_tables2 as tables
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

class PersonTable(tables.Table):
    class Meta:
        model = Person
        #template_name = "django_tables2/bootstrap.html"
        #template_name = "django_tables2/semantic.html"
        template_name = "django_tables2/bootstrap5-responsive.html"
        # https://django-tables2.readthedocs.io/en/latest/pages/custom-rendering.html#available-templates

class PersonListView(tables.SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'polls/test_view_1.html'

from django_filters import FilterSet

class PersonFilter(FilterSet):
    class Meta:
        model = Person
        #fields = {"name": ["exact", "contains"], "country": ["exact"]}
        fields = {"name": ["exact", "contains"], "email": ["exact", "contains"]}

class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    template_name = "polls/filter_view.html"

    filterset_class = PersonFilter