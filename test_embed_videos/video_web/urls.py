from django.urls import path

from test_embed_videos.video_web.views import index

urlpatterns = (
    path('', index, name='index'),
)
