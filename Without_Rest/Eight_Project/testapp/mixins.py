from django.core.serializers import serialize
import json
from django.http import HttpResponse

class SerializeMixins(object):
    def serialize(self, Query):
        json_data = serialize('json', Query) #converitng Employee object to json
        p_dict = json.loads(json_data) #converting json to python dict
        final_list = []
        for obj in p_dict:
            final_list.append(obj['fields'])
        json_string = json.dumps(final_list)
        return json_string
        

class HttpResponseMixins(object):
    def render_to_http_response(self, json_string, status= 200):
        return HttpResponse(json_string, content_type= 'application/json', status = status)
        