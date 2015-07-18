from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import TalkViewSet
from proj.routers import DefaultRouter


admin.autodiscover()

router = DefaultRouter()
router.register(r'talk', TalkViewSet)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       )
