from django.shortcuts import render
from .mixins import JsonResponseMixin
from django.views.generic import View
import json
# Create your views here.

class JsonCBV(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg':'This Response from GET Method'})
        return self.render_to_json_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg':'This Response from PUT Method'})
        return self.render_to_json_response(json_data)
    
    def patch(self, request, *args, **kwargs):
            json_data = json.dumps({'msg':'This Response from PATCH Method'})
            return self.render_to_json_response(json_data)
    
    def Post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg':'This Response from POST Method'})
        return self.render_to_json_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg':'This Response from DELETE Method'})
        return self.render_to_json_response(json_data)

