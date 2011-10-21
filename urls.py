from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("",
				url(r'^$','loggin.views.home',name='main-page'),
				(r'^signin/$','loggin.views.signin'),
				(r'^signout/$','loggin.views.signout'),
				(r'^signup/$','loggin.views.signup'),
				(r'^thanks/$','loggin.views.thanks'),
				)