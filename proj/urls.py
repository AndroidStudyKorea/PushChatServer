from django.conf.urls import patterns, include, url
from django.contrib import admin
import rest_framework_nested
from rest_framework_nested.routers import SimpleRouter

from proj.routers import DefaultRouter
from app.views import SnippetViewSet
# from app.views import UserViewSet
from notice.views import UserViewSet
from notice.views import ArticleViewSet
from notice.views import CommentViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)
router.register(r'notice', ArticleViewSet, base_name='donations')

nested_router = rest_framework_nested.routers.NestedSimpleRouter(router, r'notice', lookup='donations')
nested_router.register(r'comment', CommentViewSet)

urlpatterns = patterns('',
                       url(r'^api/v1/', include(router.urls)),
                       url(r'^api/v1/', include(nested_router.urls)),
                       url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       )