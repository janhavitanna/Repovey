"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
#from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns =[
    url(r'^admin/', admin.site.urls),


    #url(r'^showIP/$', 'survey.cxq_views.showIP'),
    #url(r'^result/$', 'survey.cxq_views.result'),
    url(r'^add_component/$', 'surveyapp.cxq_views.add_component'),
    url(r'^add_component/(?P<surveyID>\d+)/$', 'surveyapp.cxq_views.add_component'),
    url(r'^delete_survey_cxq/$','surveyapp.cxq_views.delete_survey'),
    # url(r'^cxqtestmutiajax/$','survey.cxq_views.multiajax'),

    url(r'^(\d+)/cxq_save_survey/$','surveyapp.cxq_views.save_survey'),
    url(r'^create_survey_cxq/$','surveyapp.cxq_views.create_survey'),
    url(r'^create_response/$','surveyapp.views.create_response'),
    url(r'^view_survey/(?P<view_key>\w+)/$', 'surveyapp.views.view_survey'),
    url(r'^response/(?P<responseID>\w+)/$', 'surveyapp.views.response_survey'),
    url(r'^print_survey/(?P<view_key>\w+)/$', 'surveyapp.views.print_survey'),

    url(r'^account/register/$',  'surveyapp.account_views.register'),
    url(r'^account/confirm/(.*)/(.*)',  'surveyapp.account_views.confirm'),
    url(r'^account/login/$',  'surveyapp.account_views.login_view'),
    url(r'^account/signup/$', 'surveyapp.views.signup'),
    url(r'^account/check_username/$', 'surveyapp.account_views.check_username'),
    url(r'^account/check_email/$', 'surveyapp.account_views.check_email'),
    url(r'^account/password_reset/$', 'django.contrib.auth.views.password_reset'),
    url(r'^account/edit_profile/',  'surveyapp.account_views.edit_profile'),
    url(r'^account/logout/$', 'surveyapp.account_views.logout_view'),
    url(r'^account/change_password/$', 'surveyapp.account_views.change_password_view'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^test/$', 'surveyapp.views.test_view'),
    url(r'^$', 'surveyapp.views.home'),
    url(r'^account/$', 'surveyapp.views.account'),
    url(r'^edit_survey/$', 'surveyapp.views.edit_survey'),
    url(r'^edit_survey/(\w+)/$', 'surveyapp.views.edit_survey'),
    url(r'^analyse/(\w+)/$', 'surveyapp.views.analyse'),
    url(r'^(\d+)/save_survey/$','surveyapp.views.save_survey'),
    url(r'^create_survey/$','surveyapp.views.create_survey'),
    url(r'^delete_survey/(?P<survey_key>\w+)/$','surveyapp.views.delete_survey'),
    url(r'^delete_survey/$','surveyapp.views.delete_survey'),

    url(r'^account/analyse/$', 'surveyapp.views.analyse'),

    url(r'^respondent/$', 'surveyapp.views.respondent'),
    url(r'^about/$', 'surveyapp.views.about'),
    url(r'^account/display_users_function/$', 'surveyapp.account_views.get_users_list'),
    url(r'^account/display_users/$', 'surveyapp.account_views.get_users_list_index'),
    url(r'^publish/(\w+)/$','surveyapp.views.publish'),
    url(r'^error_jump/(\w+)/$',"surveyapp.views.error_jump"),
    url(r'^validate_answer/$',"surveyapp.views.validate_answer"),
    url(r'^validate_survey/$',"surveyapp.views.validate_survey"),
    url(r'^complete/(\w+)/$', 'surveyapp.views.complete'),

    url(r'^collaborate/invite/$',  'surveyapp.collaborate_views.invite'),
    url(r'^collaborate/accept/(.*)',  'surveyapp.collaborate_views.accept'),
    url(r'^collaborate/delete/(.*)$','surveyapp.collaborate_views.delete'),
    url(r'^collaborate/remove_collaborator/(.*)/(.*)$','surveyapp.collaborate_views.remove_collaborator'),
    url(r'^share_survey/$','surveyapp.views.share_survey'),

    url(r'/$',"surveyapp.views.error_jump",{'error_type':'404'}),



    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

]

handler404 = 'survey.views.error_jump'
