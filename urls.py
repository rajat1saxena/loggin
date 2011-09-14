from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("",
				(r'^$','loggin.views.home'),
				(r'^signin/$','loggin.views.signin'),
				(r'^signout/$','loggin.views.signout'),
				(r'^signup/$','loggin.views.signup'),
				(r'^thanks','loggin.views.thanks'),
				)