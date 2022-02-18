from django.urls import path, include, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^form/$', views.view_form, name="view_form"),
    re_path(r'^(?P<section>\w+)/$', views.view_section, name="view_section"),
    re_path(r'^inventors/register/$', views.add_inventor2, name='add_inventor'),
    

    # url(r'^contest/(?P<contest_id>\d+)/begin/$', views.begin_contest, name='begin_contest'),
    #
    re_path(r'^contest/end/$', views.show_contest_endpage, name='end_contest'),
    re_path(r'^contest/(?P<contest_id>\d+)/walkthrough/$', views.walkthrough_contest, name='handle_walkthrough'),
    re_path(r'^contest/walkthrough/1/$', views.walkthrough_contest1, name='walkthrough_contest1'),
    re_path(r'^contest/test_wheel/$', views.test_wheel, name='test_wheel'),

    #To show the first question of the contest
    re_path(r'^contest/(?P<contest_id>\d+)/(?P<question_id>\d+)/welcome/$', views.show_contest_welcomepage, name='welcome_contest'),
    re_path(r'^contest/(?P<contest_id>\d+)/question/(?P<question_id>\d+)/$', views.show_question, name='show_question'),



    re_path(r'^timer/$', views.timer, name='timer'),
    # url('hackathon/form/$', TemplateView.as_view(template_name='science_olympiad/hackathon_form.html'), name='hackathon_form'),
    # url('gallery/form/$', TemplateView.as_view(template_name='science_olympiad/gallery_form.html'), name='gallery_form'),
]

