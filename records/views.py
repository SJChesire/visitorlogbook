from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .models import Visitor, Organization, Visitee
from django.http import HttpResponse, HttpResponseRedirect, request

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
    return render(request, "records/visitor.html", context)


def retrieve_visitor(request):
    visitor = Visitor.objects.all()
    return render(request, 'records/visitor.html', {'visitor': visitor})


class Visitors:
    objects = None


def retrieve_visitors(request):
    visitors = Visitors.objects.all()
    return render(request, 'records/visitor.html', {'visitors': visitors})


def update_visitor(request,pk):
    visitor = Visitor.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('/records')

    context = {
        'visitor': visitor,
    }

    return render(request, 'visitor.html', context)


def delete_visitor(request,pk):
    visitor = Visitor.objects.get(id=pk)

    if request.method == 'POST':
        visitor.delete()
        return redirect('/records')

    context = {
        'visitor': visitor,
    }

    return render(request, 'visitor.html', context)


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
    organization = Organization.objects.all()
    return render(request, 'records/organization.html', {'organization': organization})


class Organizations:
    objects = None


def retrieve_organizations():
    organizations = Organizations.objects.all()
    return render(request, 'records/organization.html', {'organizations': organizations})


def update_organization(request,pk):
    organization = Organization.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('/records')

    context = {
        'organization': organization,
    }

    return render(request, 'organization.html', context)


def delete_organization(request,pk):
    organization = Organization.objects.get(id=pk)

    if request.method == 'POST':
        organization.delete()
        return redirect('/records')

    context = {
        'organization': organization,
    }

    return render(request, 'organization.html', context)


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


def retrieve_visitee():
    visitee = Visitee.objects.all()
    return render(request, 'records/visitee.html', {'visitee': visitee})


class Visitees:
    objects = None


def retrieve_visitees():
    visitees = Visitees.objects.all()
    return render(request, 'records/visitee.html', {'visitees': visitees})


def update_visitee(request,pk):
    visitee = Visitee.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('/records')

    context = {
        'visitee': visitee,
    }

    return render(request, 'visitee.html', context)


def delete_visitee(request,pk):
    visitee = Visitee.objects.get(id=pk)

    if request.method == 'POST':
        visitee.delete()
        return redirect('/records')

    context = {
        'visitee': visitee,
    }

    return render(request, 'visitee.html', context)


