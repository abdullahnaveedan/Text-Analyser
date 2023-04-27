from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #Home Page
    path('', views.home ,name="Home"),
    path('textmodify', views.textmodify ,name="textmodify"),
    path('contact',views.contact, name="contact")
    # path('capitalFirst', views.capfirst ,name="capfirst"),
    # path('newLineRemove', views.newlinerem ,name="newlinerem"),
    # path('spaceRemove', views.spacerem ,name="spacerem"),
    # path('charCount', views.charcnt ,name="charcnt")
]
