from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

#now let us create the juicy paths 

urlpatterns=[
    url(r'^$',views.index, name='index'),
    #url(r'explore',views.explore,name ='explore'),
    url(r'notification',views.notification,name ='notification'),
    url(r'profile',views.profile,name ='profile'),
    url(r'login',views.login,name ='login'),
    url(r'logout',views.index,{'next_page': 'accounts:login'}, name='logout'),
    url(r'upload',views.upload,name ='upload'),
    
]

if settings.DEBUG:
    urlpatterns= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
