from django.conf.urls import patterns, include, url
from django.contrib import admin
from proj.routers import DefaultRouter

from app.views import DeviceView, TalkViewSet


admin.autodiscover()

router = DefaultRouter()
router.register(r'talk', TalkViewSet)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       url(r'^api/device/', DeviceView.as_view())
                       )
