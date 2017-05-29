from django.conf.urls import url
from . import views
urlpatterns = [
    #url(r'^', views.index, name="ثبت خرج"),
    url(r'^submit/expense', views.Submit_Expense, name="ثبت خرج"),
    url(r'^submit/income', views.Submit_Income, name="incoem"),
    url(r'^event/eventtype', views.Event_Type, name="Event Type"),
]
