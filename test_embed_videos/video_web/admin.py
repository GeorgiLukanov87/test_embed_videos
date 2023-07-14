from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from test_embed_videos.video_web.models import Video


@admin.register(Video)
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
