from django.shortcuts import render
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:  # pragma: no cover
    # Not required for Django <= 1.9, see:
    # https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware
    MiddlewareMixin = object  # pragma: no cover


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        req_sortby = request.GET.get('sortby', '')
        req_order = request.GET.get('order', '')
        order = '-' if req_order == 'desc' else ''
        if req_sortby:
            params = request.GET.copy()
            params.setdefault('ordering', order + req_sortby)
            request.GET = params

    # def process_response(self, request, response):
    #     return response
