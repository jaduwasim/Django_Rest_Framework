import json
from django.core.serializers import serialize
from django.http import HttpResponse

class SerializeMixins(object):
    def Serialize(self, emp_list):
        emp_json = serialize('json',emp_list)
        emp_dict = json.loads(emp_json)
        final_list = []
        for obj in emp_dict:
            final_list.append(obj['fields'])
        emp_json = json.dumps(final_list)        
        return emp_json

class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type ='application/json', status=status)