from django.core.serializers import serialize
import json
from django.http import HttpResponse
class SerializeMixins(object):
    def serialize(self, qs):
        json_string = serialize('json',qs)
        pdata = json.loads(json_string)
        p_list = []
        for i in pdata:
            p_list.append(i['fields'])
        json_string = json.dumps(p_list)
        return json_string
    
class HttpResponseMixins(object):
    def render_to_http_response(self, json_string, status=200):
        return HttpResponse(json_string, content_type='application/json', status=status)