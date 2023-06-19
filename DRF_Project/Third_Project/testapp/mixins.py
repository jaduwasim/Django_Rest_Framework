from django.http import HttpResponse

class HttpResponseMixins(object):
    def render_to_http_response(self, json_string, status = 200):
        return HttpResponse(json_string, content_type = 'application/json', status=status)