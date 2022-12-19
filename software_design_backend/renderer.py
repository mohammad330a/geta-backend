from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        response = {"response": None, "status": status_code, "errors": None}
        if str(status_code).startswith('2'):
            response['response'] = {"data": data}
        else:
            response['errors'] = data
        return super().render(response)
