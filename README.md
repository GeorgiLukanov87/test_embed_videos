# test_embed_videos

Installation & Setup
Installation
The simpliest way is to use pip to install package:

pip install django-embed-video
If you want latest version, you may use Git. It is fresh, but unstable.

pip install git+https://github.com/jazzband/django-embed-video
Setup
Add embed_video to INSTALLED_APPS in your Django settings.

INSTALLED_APPS = (
    ...

    'embed_video',
)
To detect HTTP/S you must use request context processor:

TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'django.template.context_processors.request',
)
Full doc here- > https://django-embed-video.readthedocs.io/en/latest/
