from django.conf.urls import include, url
from . import views

app_name = 'CrmAPI'
urlpatterns = [
    # Examples:
    # url(r'^$', 'APIs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', views.index, name='index'),
    url(r'^sign_in/', views.sign_in, name='sign_in'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^index/', views.index, name='index'),
]
