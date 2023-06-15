from django.core.serializers import serialize
import json
from django.http import HttpResponse

class SerializeMixin(object):
    def serialize(self, Query):
        json_string = serialize('json',Query)
        p_dict = json.loads(json_string)
        final_list = []
        for e in p_dict:
            final_list.append(e['fields'])
        json_srting = json.dumps(final_list)
        return json_srting
    
class HttpResponseMixins(object):
    def render_to_http_response(self, json_string, status=200):
        return HttpResponse(json_string, content_type = 'application/json', status=status)