from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ResponseSerializer, RequestSerializer
from .services import *


@api_view(['POST'])
def weather_json(request):
    request_serializer = RequestSerializer(data=request.data, many=True)

    if request_serializer.is_valid():
        data = request_serializer.validated_data

        response_form = []
        weather_list = get_multi_doy(data)
        events = get_request_events(data)

        get_response_info(response_form, weather_list, events)

        resp_serializer = ResponseSerializer(response_form, many=True)

        save_response(resp_serializer)

        return Response(resp_serializer.data)
    else:
        return Response(request_serializer.errors)


