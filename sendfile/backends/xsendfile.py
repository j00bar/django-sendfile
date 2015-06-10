import os

from django.conf import settings
from django.http import HttpResponse


def sendfile(request, filename, **kwargs):
    response = HttpResponse()
    # If SENDFILE_ROOT is defined, the filename to use should be relative to 
    # SENDFILE_ROOT instead of MEDIA_ROOT
    if getattr(settings, 'SENDFILE_ROOT', None):
        filename = os.path.join(settings.SENDFILE_ROOT,
                                os.path.relpath(filename, settings.MEDIA_ROOT))
    response['X-Sendfile'] = unicode(filename).encode('utf-8')

    return response
