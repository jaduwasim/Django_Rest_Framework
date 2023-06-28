from django.http import HttpResponse

class HttpResponseMixins(object):
    def render_to_http_response(self, json_string, stauts= 200):
        return HttpResponse(json_string, content_type='application/json', status=stauts)
        