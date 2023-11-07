from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TodoSerializer, TimingTodoSerializer
from .models import Todo, TimingTodo
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class homeView(APIView):
    def get(self, request, formant=None):
        return Response({
            'status':'200',
            'message': 'DJango rest framework is  working get method'
        })

    def post(self, reqest, format=None):
        return Response({
            'status':'200',
            'message': 'DJango rest framework is  working Post method'
        })

class todoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        data['user'] = request.user.id
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response({
                'status': True,
                'message': 'Success todo created',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'invalid Data',
            'data': serializer.errors
        })
    
    def get(self, request, format=None):
        print(request.user)
        todo_objs = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todo_objs, many=True)

        return Response({
            'status': True,
            'message': 'Todo fetched',
            'data': serializer.data
        })
    
    def patch(self, request, format=None):
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data': {}
            })
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Success data',
                'data': serializer.data
            })
        
        return Response({
            'status': False,
            'message': 'Invalid uid',
            'data': serializer.errors
        })
    
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['get'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'status': True,
            'message': 'Timing Todo fetched',
            'data': serializer.data
        })

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Success data',
                    'data': serializer.data
                })
            
            return Response({
                'status': False,
                'message': 'Invalid uid',
                'data': serializer.errors
            })
        
        except:
            return Response({
                'status': False,
                'message': 'Something went wrong'
            })
        