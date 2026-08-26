from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import WeatherSerializer, ResponseSerializer
from .services import *


@api_view(['POST'])
def weather_json(request):
    weather_serializer = WeatherSerializer(data=request.data)

    if weather_serializer.is_valid():
        data = weather_serializer.validated_data

        weather_input = weather_data_build(data)
        events = get_request_events(request)
        event_x_update(events)

        new_index = len(events)
        new_event = event_create(weather_input, new_index)

        if new_event:
            events.append(new_event)

        resp_serializer = ResponseSerializer(
            {
                "doy": weather_input.doy,
                "events": events
            }
        )
        return Response(resp_serializer.data)
    else:
        return Response(weather_serializer.errors)


