from django.conf.urls import url
from users import views

urlpatterns = [
   # url(r'^users/(?P<first_name>.+)/$', views.BloggersSearchList.as_view()),
    url(r'^users/search/$', views.BloggersSearchList.as_view()),
    url(r'^users/$', views.BloggersList.as_view()),

]