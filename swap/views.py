from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import paho.mqtt.publish as publish

class MQTTPublishView(APIView):
    def post(self, request):
        topic = request.data.get("topic", "test/topic")
        message = request.data.get("message", "Hello from Django")
        publish.single(topic, message, hostname="broker.hivemq.com")
        return Response({"status": "Message sent", "topic": topic})
