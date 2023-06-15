from django.core.serializers import serialize
import json
from django.http import HttpResponse

class SerializeMixins(object):
    def Serialize(self, Query):
        json_string = serialize('json',Query)
        p_dict = json.loads(json_string)
        final_list = []
        for obj in p_dict:
            final_list.append(obj['fields'])
        json_string = json.dumps(final_list)
        return json_string
    
class HttpResponseMixin(object):
    def render_to_http_response(self, json_string, status=200):
        return HttpResponse(json_string, content_type = 'application/json')