from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from scribble.views import ScribbleView, ScribbleListView, CommentView

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'scribbler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^home/', ScribbleListView.as_view()),
    url(r'^$', ScribbleListView.as_view()),
    url(r'^scribble/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<date>[0-9]{2})/(?P<title>[a-zA-Z0-9_-]+)',
        ScribbleView.as_view(), name='scribble'),
    url(r'^comment/', CommentView.as_view(), name='comment'),
    url(r'^get-comments/?', CommentView.as_view(), name='comment'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
