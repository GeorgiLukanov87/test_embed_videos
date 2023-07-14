from django.urls import path

from test_embed_videos.video_web.views import home_page

urlpatterns = (
    path('', home_page, name='home_page'),
)
