from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_category/$', views.add_category,
        name='add_category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.category, name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)
#
# if settings.DEBUG:
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'media/(?P<path>.*)',
#          'serve',
#          {'document_root': settings.MEDIA_ROOT}),)

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
