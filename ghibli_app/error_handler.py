from django.conf import settings
from django.http import HttpResponse


class ErrorHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if not settings.DEBUG:
            return HttpResponse("Ooops... something went wrong :( please wait and try to reload the page", status=500)
