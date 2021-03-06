from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^comments/', include('django_comments.urls')),
  )
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
