from django.conf.urls import patterns, url
from soda import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^search/$', views.search, name="search"),
    url(r'^company/(?P<company_id>[-\w]+)/$', views.company, name="company"),
    url(r'^preview/(?P<company_id>[-\w]+)/$', views.company_preview, name="preview"),
    url(r'^apply/(?P<company_id>[-\w]+)/$', views.apply, name="apply"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^coverletter/$', views.coverletter, name="coverletter"),
    url(r'^signup/$', views.signup, name="signup"),

    url(r'^fb_signin/$', views.fb_signin, name="fbsignin1"),
    url(r'^fb_signin/(?P<fb_id>[-\w]+)/$', views.fb_signin, name="fbsignin2"),

    url(r'^signin/$', views.signin, name="signin"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^history/$', views.history, name="history"),
    url(r'^confirm_app/$', views.confirm_app, name="confirm_app"),
    url(r'^share/(?P<user_id>[-\w]+)/$', views.share, name="share"),

    url(r'^data/$', views.data, name="data"),
)