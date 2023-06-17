from django.core.serializers import serialize
import json
from django.http import HttpResponse

class SerializationMixins(object):
    def serialization(self, Stu_data):
        stu_json = serialize('json', Stu_data)
        p_dict = json.loads(stu_json)
        final_list = []
        for obj in p_dict:
            final_list.append(obj['fields'])
        json_data = json.dumps(final_list)
        return json_data
    
class HttpResponseMxins(object):
    def render_to_http_response(self, json_string, status= 200):
        return HttpResponse(json_string, content_type = 'application/json', status=status)