from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^contest/(?P<contest_id>\d+)/begin/$', views.begin_contest, name='begin_contest'),
    url(r'^contest/end/$', views.show_contest_endpage, name='end_contest'),
    url(r'^contest/(?P<contest_id>\d+)/walkthrough/$', views.walkthrough_contest, name='handle_walkthrough'),
    url(r'^contest/walkthrough/1/$', views.walkthrough_contest1, name='walkthrough_contest1'),
    url(r'^contest/test_wheel/$', views.test_wheel, name='test_wheel'),

    #To show the first question of the contest
    url(r'^contest/(?P<contest_id>\d+)/(?P<question_id>\d+)/welcome/$', views.show_contest_welcomepage, name='welcome_contest'),
    url(r'^contest/(?P<contest_id>\d+)/question/(?P<question_id>\d+)/$', views.show_question, name='show_question'),


    url(r'^timer/$', views.timer, name='timer'),
    # url('hackathon/form/$', TemplateView.as_view(template_name='science_olympiad/hackathon_form.html'), name='hackathon_form'),
    # url('gallery/form/$', TemplateView.as_view(template_name='science_olympiad/gallery_form.html'), name='gallery_form'),
]



