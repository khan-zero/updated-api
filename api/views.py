from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, serializers, status
#from rest_framework.views import APIView

from main.models import Teacher, Subject
#from django.db.models import Q
from .serializers import (
    #TeacherSerializer,
    TeacherDetailSerializer, 
    #TeacherListSerializer,
    #SubjectDetailSerializer,
    #SubjectListSerializer,
    SubjectSerializer,
    TeacherSerializer,
)

from django.http import HttpResponse


# Teacher create +
# Teacher list +
# Teacher detail +
# Teacher update +
# Teacher search +
# Teacher delete +

"""
@api_view(['GET'])
def teacher_list(request):
    q = request.GET.get('q')
    if q:
        teachers = Teacher.objects.filter(
            Q(full_name__icontains = q) |
            Q(phone__icontains = q))
    else:
        teachers = Teacher.objects.all() # QS
    serializer_data = TeacherListSerializer(teachers, many=True) # JSON
    return Response(serializer_data.data)


@api_view(['GET'])
def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)
    ser_data = TeacherDetailSerializer(teacher).data
    return Response(ser_data)


@api_view(['POST'])
def teacher_create(request):
    ser_data = TeacherDetailSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()
    return Response({'status':201})


@api_view(['PUT'])
def teacher_update(request, id):
    teacher = Teacher.objects.get(id=id)
    ser_data = TeacherDetailSerializer(teacher, data=request.data)
    if ser_data.is_valid():
        ser_data.save()
    return Response({'status':201})

# @api_view(['PUT'])
# def teacher_update(request, id):
#     teacher = Teacher.objects.get(id=id)
#     teacher.full_name = request.data['full_name']
#     teacher.age = request.data['age']
#     teacher.english_certificate = request.data['english_certificate']
#     teacher.phone = request.data['phone']
#     teacher.save()
#     return Response({'status':201})

@api_view(['DELETE'])
def teacher_delete(request, id):
    Teacher.objects.get(id=id).delete()
    return Response({'status':200})

@api_view(['GET'])
def subject_list(request):
    queryset = Subject.objects.all()
    ser_data = SubjectListSerializer(queryset, many=True)
    return Response(ser_data.data)

@api_view(['GET'])
def subject_detail(request, id):
    queryset = Subject.objects.get(id=id)
    teacher = Teacher.objects.filter(subject=queryset)
    ser_data = SubjectListSerializer(queryset)
    teacher_ser_data = TeacherListSerializer(teacher, many=True)
    # context = [ser_data.data, teacher_ser_data.data]
    context = {
        'subject':ser_data.data,
        'teachers':teacher_ser_data.data
    }
    return Response(context) #dict -> JSON # Teacher -> JSON ---

"""
# @api_view(['GET'])
# def subject_detail(request, id):
#     queryset = Subject.objects.get(id=id)
#     ser_data = SubjectListSerializer(queryset)
#     context = {
#         'subject':ser_data.data
#     }
#     return Response(context) #dict -> JSON # Teacher -> JSON ---

# @api_view(['GET'])
# def subject_detail(request, id):
#     queryset = Subject.objects.get(id=id)
#     ser_data = SubjectDetailSerializer(queryset)
#     return Response(ser_data.data) #dict -> JSON # Teacher -> JSON ---

# @api_view(['GET'])
# def subject_detail(request, id):
#     queryset = Subject.objects.get(id=id)
#     ser_data = SubjectDetailSerializer(queryset)
#     return Response(ser_data.data) #dict -> JSON # Teacher -> JSON ---

"""
class TeacherView(APIView):
    serializer = TeacherDetailSerializer
    queryset = Teacher

    def get(self, request):
        return Response({
            self.serializer(
                self.queryset.objects.all(), 
                many=True
                ).data})
    
    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, id):
        queryset = Teacher.objects.get(id=id)
        serializer_data =TeacherDetailSerializer(
            queryset, 
            data=request.data
            )
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
    
    def delete(self, request, id):
        queryset = Teacher.objects.get(id=id)
        queryset.delete()
        return Response({'condition':'success'})
"""

@api_view(['GET'])
def test_request(request):
    try:
        # raise ValueError
        data = {'code':200}
        status_code = status.HTTP_200_OK
    except:
        data = {'code':400}
        status_code = status.HTTP_400_BAD_REQUEST
    return Response(data, status=status_code)


# class TeacherClassView(generics.ListAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherDetailSerializer


# class TeacherClassView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherDetailSerializer

class TeacherClassView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        if q:
            # way1
        #     result = self.get_queryset().filter(full_name__icontains=q)
        #     return Response(self.serializer_class(result, many=True).data)
        # return Response(self.serializer_class(self.get_queryset(), many=True).data)
            # way 2
            self.queryset = self.get_queryset().filter(full_name__icontains=q)
        return Response(self.serializer_class(self.get_queryset(), many=True).data)


@api_view(['GET', 'POST'])
def subject_list(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
