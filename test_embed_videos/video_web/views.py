from django.shortcuts import render

from test_embed_videos.video_web.models import Video


def index(request):
    videos = Video.objects.all()

    context = {
        'videos': videos,
    }

    return render(request, 'embed_video/index-videos.html', context, )
