from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    doy = serializers.IntegerField()
    temperature = serializers.FloatField()
    wetting = serializers.IntegerField()
    humidity = serializers.FloatField()
    rain = serializers.FloatField()

class EventSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    x = serializers.FloatField()


class RequestSerializer(WeatherSerializer):
    events = EventSerializer(many=True, required=False)


class ResponseSerializer(serializers.Serializer):
    doy = serializers.IntegerField()
    events = EventSerializer(many=True)
