import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Update


def update_example_view(request):
    data = {
        'count': 1000,
        'content': 'Some content'
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some content'
        }
        return JsonResponse(data)


class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context
