from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .models import Visitor, Organization
from django.http import HttpResponse, HttpResponseRedirect

from .organization_entry_form import OrganizationForm
from .visitee_entry_form import VisiteeForm
from .visitor_entry_form import VisitorsForm


# def index(request):
#     return HttpResponse("Hello and Welcome to Spin Mobile Limited")


def create_visitor(request):
    """
    request:-
        - visitor_name
        - phone_number
        - id_or_passport
        - organization - FK (pk)
        - visitee - FK (pk)
        - time in
        -time out
    :return httpresponse succeed(data) or error(error message)
    """
    context = {}

    # add the dictionary during initialization
    form = VisitorsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "./records/visitor.html", context)


def retrieve_visitor():
    pass


def update_visitor():
    pass


def delete_visitor():
    pass


def create_organization(request):
    """
       request:-
           - organization_name
           - mobile_number

       :return httpresponse succeed(data) or error(error message)
       """
    context = {}

    # add the dictionary during initialization
    form = OrganizationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "records/organization.html", context)


def retrieve_organization():
  pass


def update_organization():
    pass


def delete_organization():
    pass


def create_visitee(request):
    """
          request:-
              - visitee_name
              - visitee_status
              - visitor_name


          :return httpresponse succeed(data) or error(error message)
          """
    context = {}

    # add the dictionary during initialization
    form = VisiteeForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "records/visitee.html", context)
