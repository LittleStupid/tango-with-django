from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', views.serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]
#
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#

# if settings.DEBUG:
#     urlpatterns += [
#         url('django.views.static', views.index),
#         url(r'^media/(?P<path>.*)', views.index),
#         url('serve', views.index),
#         url({'document_root': settings.MEDIA_ROOT}, views.index)]
#
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
