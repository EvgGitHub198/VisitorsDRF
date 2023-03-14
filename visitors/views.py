from rest_framework.response import Response
from rest_framework.views import APIView
from visitors.serializers import VisitorSerializer
from django.http.response import JsonResponse, Http404
from .models import Visitors



class VisitorView(APIView):

    def get_visitor(self, pk):
        try:
            visitor = Visitors.objects.get(visitorId=pk)
            return visitor
        except Visitors.DoesNotExist():
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_visitor(pk)
            serializer = VisitorSerializer(data)
        else:
            data = Visitors.objects.all()
            serializer = VisitorSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = VisitorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Visitor created!", safe=False)
        return JsonResponse("Failed to create Visitor!", safe=False)

    def put(self, request, pk=None):
        visitor_to_update = Visitors.objects.get(visitorId=pk)
        serializer = VisitorSerializer(instance=visitor_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Visitor updated!", safe=False)
        return JsonResponse("Failed to update Visitor!")

    def delete(self, request, pk=None):
        visitor_to_delete = Visitors.objects.get(visitorId=pk)
        visitor_to_delete.delete()
        return JsonResponse("Visitor Deleted!", safe=False)