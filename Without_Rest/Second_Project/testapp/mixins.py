from django.http import HttpResponse

class JsonResponseMixin(object):
    def render_to_json_response(self, json_data, **kwargs):
        return HttpResponse(json_data, content_type = 'application/json')