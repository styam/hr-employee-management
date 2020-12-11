from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User, EmployeeDetails
from .serializers import UserSerializer, EmployeeDetailsSerializer


class HRRegistration(APIView):
    def post(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeAPIView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = EmployeeDetailsSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        employees = EmployeeDetails.objects.all()
        serializer = EmployeeDetailsSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeUpdateAPIView(APIView):

    def get_object(self, pk):
        try:
            return EmployeeDetails.objects.get(pk=pk)

        except EmployeeDetails.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        emp_obj = self.get_object(pk)
        serializer = EmployeeDetailsSerializer(emp_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        emp_obj = self.get_object(pk)
        serializer = EmployeeDetailsSerializer(emp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emp_obj = self.get_object(pk)
        emp_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

