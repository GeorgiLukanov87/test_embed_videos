from django.shortcuts import render

from test_embed_videos.video_web.models import Video


def index(request):
    videos = Video.objects.all()

    test1 = Video.objects.all()[0]
    test2 = Video.objects.all()[1]

    context = {
        'videos': videos,
        'video1': test1,
        'video2': test2,
    }

    return render(request, 'embed_video/index-videos.html', context, )
