from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from manager.views import EntryListView
from django.contrib.auth.decorators import login_required

from manager.views import entry_search

admin.autodiscover()
admin.site.site_header = settings.SITE_NAME

urlpatterns = [
    url(r'^$', entry_search, name='home'),
    url(r'^admin42/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^', include('manager.urls')),

]