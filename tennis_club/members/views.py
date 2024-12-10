from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.

# ALL MEMBERS PAGE
def members(request):
    mymembers = Member.objects.all()
    # mymembers = Member.objects.all().order_by("last_name")
    # mymembers = Member.objects.filter(Q(first_name="Ay") | Q(last_name="Abegunde")).values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers": mymembers
    }
    return HttpResponse(template.render(context, request))

# MEMBER DETAILS PAGE


def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        "member": member,
    }

    return HttpResponse(template.render(context, request))

# HOMEPAGE


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
