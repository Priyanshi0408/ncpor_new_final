from django.contrib import admin
from nsidc_app.models import about

# from nsidc_app.models import research_drop

from nsidc_app.models import informationResearch
from nsidc_app.models import researchScientist
from nsidc_app.models import researchGrant, myclass,gemclass,procurementclass,panelmentclass
from nsidc_app.models import enquiryclass,corigendumclass
from nsidc_app.models import careerclass
from nsidc_app.models import scientificPublication
from nsidc_app.models import scientificExpedition
from nsidc_app.models import polarenvironments,polaroceans,polarscience,mineralresources,geosciences,atmosphere
from nsidc_app.models import  antarctic,arctic,southern_ocean,himalaya,newsclass,eventclass
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css={
            "all":("css/main.css",)
        }

        js=("js/blog.js",)

admin.site.register(about, BlogAdmin)


# admin.site.register(research_drop,BlogAdmin)(drop-dowm-->dropdowm through cms / made by priyanshi)

admin.site.register(informationResearch, BlogAdmin)
admin.site.register(researchScientist, BlogAdmin)
admin.site.register(researchGrant, BlogAdmin)
admin.site.register(scientificPublication, BlogAdmin)
admin.site.register(scientificExpedition, BlogAdmin)
admin.site.register(antarctic,BlogAdmin)
admin.site.register(arctic,BlogAdmin)
admin.site.register(southern_ocean,BlogAdmin)
admin.site.register(himalaya,BlogAdmin)
admin.site.register(myclass)
admin.site.register(corigendumclass)
admin.site.register(panelmentclass)
admin.site.register(procurementclass)
admin.site.register(gemclass)
admin.site.register(enquiryclass)
admin.site.register(careerclass)
admin.site.register(polarenvironments,BlogAdmin)
admin.site.register(polaroceans,BlogAdmin)
admin.site.register(polarscience,BlogAdmin)
admin.site.register(geosciences,BlogAdmin)
admin.site.register(atmosphere,BlogAdmin)
admin.site.register(mineralresources,BlogAdmin)
admin.site.register(newsclass,BlogAdmin)
admin.site.register(eventclass,BlogAdmin)

# admin.site.register(research_drop,BlogAdmin)(drop-dowm-->dropdowm through cms / made by priyanshi)
