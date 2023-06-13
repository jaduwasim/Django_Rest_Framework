from django.core.serializers import serialize
from django.http import HttpResponse
import json

class SerializeMixin(object):
    def serialize(self, emp_list):
        json_emp = serialize('json',emp_list)
        p_dict = json.loads(json_emp)
        final_list = []
        for obj in p_dict:
            final_list.append(obj['fields'])
        json_emp = json.dumps(final_list)
        return json_emp
    
class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type ='application/json', status=status)