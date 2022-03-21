from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from ilp.views import User_level,Level_challenge,Challenge_media
from ilp import views
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'level', LevelViewSet)
# router.register(r'challenge', ChallengeViewSet)
# router.register(r'media', MediaViewSet)
# router.register(r'token', TokenViewSet)

urlpatterns = [    
    # url(r'^', include(router.urls)),
    path('mylevel',User_level.as_view()),
    path('mychallenge',Level_challenge.as_view()),
    path('mymedia',Challenge_media.as_view()),
]