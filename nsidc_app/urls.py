from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name= 'home'),

    # path("about/", views.about_home , name= 'about'),
    # path("about/jobs", views.about_jobs , name= 'about'),
    # path("about/contact", views.about_contact , name= 'about'),
    # path("about/copyright", views.about_copyright , name= 'about'),
    # path("about/greendata", views.about_greendata , name= 'about'),
    # path("about/highlights", views.about_highlights , name= 'about'),
    # path("about/ncpor", views.about_ncpor , name= 'about'),
    # path("about/sponsors", views.about_sponsors , name= 'about'),
    path("about_example/<str:slug>",views.about_example,name = 'example'),

    
    path("research/information", views.research_information , name= 'research'),
    path("research/publications", views.research_publications , name= 'research'),
    path("research/research", views.research_grants , name= 'research'),
    path("research/scientists", views.research_scientists , name= 'research'),
    path("research/scientific", views.scientific_expeditions , name= 'research'),
    # path("research_example/<str:slug>",views.research_scientist_example,name = 'research_example'),
    path("research_information_example/<str:slug>",views.research_information_example,name = 'research_example'),
    path("research_publications_example/<str:slug>",views.research_publications_example,name = 'research_example'),
    path("research_grants_example/<str:slug>",views.research_grants_example,name = 'research_example'),
    path("research_scientists_example/<str:slug>",views.research_scientists_example,name = 'research_example'),
    path("scientific_expeditions_example/<str:slug>",views.scientific_expeditions_example,name = 'research_example'),

    # path("research_example",views.research_example,name = 'research_example'),
    # path("research_example/research_scientists",views.res_exam_rese_sct,name="research"),
    path("research/research_example/<str:slug>",views.Antarctic,name = 'research_example'),
    path("research/research_grants/<str:slug>",views.Arctic,name = 'research_example'),
    path("research/research_down_publi/<str:slug>",views.Southern_ocean,name = 'research_example'),
    path("research/research_down_publi/<str:slug>",views.Himalaya,name = 'research_example'),
    path("tender/", views.tender, name="tender"),
    path("careers", views.careers, name="career"),
    path("careerArchive", views.careerArchive, name="career"),
    path("tender/tender", views.tenderTable, name="tender"),
    path("tender/corrigendum", views.CorrigendumTable, name="Tender"),
    path("tender/procurement", views.ProcurementTable, name="Tender"),
    path("tender/empanelment", views.PanelmentTable, name="Tender"),
    path("tender/enquiry", views.EnquiryTable, name="Tender"),
    path("tender/GeM", views.GeMTable, name="Tender"),
    path("tender/archive", views.tenderArchive, name="Tender"),
    path("webMail", views.webMail, name="webMail"),
    path("news", views.news, name="news"),
    

    path("polarscience/<str:slug>",views.polar_science,name= 'our_research'),
    path("atmosphere/<str:slug>",views.polar_science,name= 'our_research'),
    path("geoscience/<str:slug>",views.polar_science,name= 'our_research'),
    path("polaroceans/<str:slug>",views.polar_science,name= 'our_research'),
    path("polarenv/<str:slug>",views.polar_science,name= 'our_research'),
    path("mineral/<str:slug>",views.polar_science,name= 'our_research'),
    
    path("dataCenter",views.dataCenter,name= 'dataCenter'),
    path("newsarchive",views.news_archive,name='news'),
    path("eventsarchive",views.event_archive,name='news')
]