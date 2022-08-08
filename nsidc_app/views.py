from datetime import datetime
from http.client import HTTPResponse
from django.forms import DateField
from django.http import HttpResponse
from django.shortcuts import render
from nsidc_app.models import about
from django.utils import timezone

from nsidc_app.models import informationResearch
from nsidc_app.models import researchScientist
from nsidc_app.models import researchGrant, myclass,gemclass,procurementclass,panelmentclass
from nsidc_app.models import enquiryclass,corigendumclass
from nsidc_app.models import careerclass
from nsidc_app.models import scientificPublication, antarctic,arctic,southern_ocean,himalaya
from nsidc_app.models import scientificExpedition
from nsidc_app.models import polarenvironments,polaroceans,polarscience,mineralresources,geosciences,atmosphere,newsclass,eventclass

# Create your views here.

def home(request):
    abouts = about.objects.all()
    research_example_down_resgr = antarctic.objects.all()
    research_example_down_sps = arctic.objects.all()
    # researchs_drops = research_drop.objects.all()
    informationResearchs = informationResearch.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    scientificPublications = scientificPublication.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    research_example_down_scientist = southern_ocean.objects.all()
    research_example_down = himalaya.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    new = newsclass.objects.all()
    c = new.exclude(closingdate__lte=datetime.today())
    eve = eventclass.objects.all()
    d = eve.exclude(closingdate__lte=datetime.today())
    context = {'abouts': abouts, 'informationResearchs': informationResearchs, 'researchScientists': researchScientists, 'researchGrants': researchGrants, 'scientificPublications': scientificPublications,
               'scientificExpeditions': scientificExpeditions, 'redsc': research_example_down_scientist, 'redrg': research_example_down_resgr, "down_publ": research_example_down_sps, 'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,'him':research_example_down,'nw':c,'event':d}
    return render(request, 'home.html', context)
# def about_jobs(request):
#     return HttpResponse("this is home page")
# def about_ncpor(request):
#     return HttpResponse("this is home page")
# def about_sponsors(request):
#     return HttpResponse("this is home page")
# def about_highlights(request):
#     return HttpResponse("this is home page")
# def about_copyright(request):
#     return HttpResponse("this is home page")
# def about_contact(request):
#     return HttpResponse("this is home page")
# def about_greendata(request):
#     return HttpResponse("this is home page")
# def about_home(request):
#     abouts = about.objects.all()
#     context = {'abouts':abouts}
#     return render(request,'about.html',context)


def about_example(request, slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    About = about.objects.filter(slug=slug).first()
    researchGrants = researchGrant.objects.all()
    scientificPublications = scientificPublication.objects.all()
    informationResearchs = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'about': About,
               'ab': abouts,
               'rs': researchScientists,
               'rsg': researchGrants,
               'sfpb': scientificPublications,
               'ifrsc': informationResearchs,
               'expd': scientificExpeditions
               }
    return render(request, 'about_example.html', context)


# Research
def research_scientists(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/r_scientists.html', context)


def research_grants(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/research_grants.html', context)


def research_publications(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/scientific_publications.html', context)


def research_information(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/InformationResearch.html', context)


def scientific_expeditions(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/ScientificExpeditions.html', context)


# def research_example(request,slug):
#     Researchs = research.objects.filter(slug=slug).first()
#     context = {'research':Researchs}
#     return render(request,'research_example.html',context)
def research_scientists_example(request, slug):
    abouts = about.objects.all()
    Researchs = researchScientist.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_scientist_example.html', context)


def research_grants_example(request, slug):
    abouts = about.objects.all()
    Researchs = researchGrant.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_grant_example.html', context)


def research_publications_example(request, slug):
    abouts = about.objects.all()
    Researchs = scientificPublication.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_publications_example.html', context)


def research_information_example(request, slug):
    abouts = about.objects.all()
    Researchs = informationResearch.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_IR_example.html', context)


def scientific_expeditions_example(request, slug):
    abouts = about.objects.all()
    Researchs = scientificExpedition.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_scientific_example.html', context)


# image Dropdown
def Antarctic(request, slug):
    rsres = antarctic.objects.filter(slug=slug).first()
    context = {'resrchesg': rsres}
    return render(request, 'research/research_example.html', context)


def Arctic(request, slug):
    rsres = arctic.objects.filter(slug=slug).first()
    context = {'resrchesg': rsres}
    return render(request, 'research/research_example.html', context)


def Southern_ocean(request, slug):
    resgr = southern_ocean.objects.filter(slug=slug).first()
    context = {'resrchesg': resgr}
    return render(request, 'research/research_example.html', context)


def Himalaya(request, slug):
    publica = himalaya.objects.filter(slug=slug).first()
    context = {'resrchesg': publica}
    return render(request, 'research/research_example.html', context)
    # return render(request,'research/research_scientific_example.html',context)
    # return HttpResponse("fbjfns")

# def research_drop_example(request,slug,slug_drop):
#     Researchs_Drops = research_drop.objects.filter(slug=slug,slug_drop=slug_drop).first()
#     context = {'research_drop':Researchs_Drops}
#     return render(request,'research_drop.html',context)(drop-dowm-->dropdowm through cms / made by priyanshi)

def tender(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'tender.html', context)
    # return HttpResponse("hello")


def tenderTable(request):
    c=myclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/tenderTable.html", context)

def CorrigendumTable(request):
    c=corigendumclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/CorrigendumTable.html", context)
    # return HttpResponse("fnfjn")
def ProcurementTable(request):
    c=procurementclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/ProcurementTable.html", context)
def PanelmentTable(request):
    c=panelmentclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/PanelmentTable.html", context)
def EnquiryTable(request):
    c=enquiryclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/EnquiryTable.html", context)
def GeMTable(request):
    c=gemclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/GeMTable.html", context)

def tenderArchive(request):
    c1=myclass.objects.filter(closingdate__lte=datetime.today())
    c2=corigendumclass.objects.filter(closingdate__lte=datetime.today())
    c3=panelmentclass.objects.filter(closingdate__lte=datetime.today())
    c4=procurementclass.objects.filter(closingdate__lte=datetime.today())
    c5=gemclass.objects.filter(closingdate__lte=datetime.today())
    c6 = enquiryclass.objects.filter(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co1':c1,
        'co2':c2,
        'co3':c3,
        'co4':c4,
        'co5':c5,
        'co6':c6,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/tenderArchive.html", context)


# career
def careers(request):
    c=careerclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "career.html", context)

def careerArchive(request):
    c = careerclass.objects.filter(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':c,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "careerArchive.html", context)

# Webmail
def webMail(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "webMail.html", context)
def news(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "news.html", context)


# our research drop down

def polar_science(request,slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    polar_res = polarscience.objects.filter(slug=slug).first()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
        'po': polar_res,
    }
    return render(request, 'our_research/polarscience.html', context)

def polar_oceans(request,slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    polar_res = polaroceans.objects.filter(slug=slug).first()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
        'po': polar_res,
    }
    return render(request, 'our_research/polaroceans.html', context)

def polar_env(request,slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    polar_res = polarenvironments.objects.filter(slug=slug).first()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
        'po': polar_res,
    }
    return render(request, 'our_research/polarenv.html', context)

def mineral_resources(request,slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    polar_res = mineralresources.objects.filter(slug=slug).first()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
        'po': polar_res,
    }
    return render(request, 'our_research/mineralresources.html', context)

def atmos(request,slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    polar_res = atmosphere.objects.filter(slug=slug).first()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
        'po': polar_res,
    }
    return render(request, 'our_research/atmos.html', context)

def geoscience(request,slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    polar_res = geosciences.objects.filter(slug=slug).first()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
        'po': polar_res,
    }
    return render(request, 'our_research/geoscience.html', context)

def dataCenter(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'DataCenter.html', context)

# news and event

def news_archive(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()

    c = newsclass.objects.filter(closingdate__lte=datetime.today())
    context = {
        'co' : c,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
    }
    return render(request, 'news_archive.html',context)

def event_archive(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()

    c = eventclass.objects.filter(closingdate__lte=datetime.today())
    context = {
        'co' : c,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions,
    }
    return render(request, 'events_archive.html',context)