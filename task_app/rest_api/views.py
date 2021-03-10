from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination
from django.test import TestCase


# Create your views here.


# Welcome
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to the Task App!"}
    return JsonResponse(content)


# Get tasks by user with pagination
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_tasks(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1
    user = request.user.id
    tasks = Task.objects.filter(owner=user)
    result_page = paginator.paginate_queryset(tasks, request)
    serializer = TaskSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Add task
@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_task(request):
    aux = json.dumps(request.data)
    data = json.loads(aux)
    user = request.user
    try:
        title_val = data['title']
    except:
        return JsonResponse({'error': 'Task must have title'}, safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        description_val = data['description']
    except:
        return JsonResponse({'error': 'Task must have description'}, safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        state_val = data['status']
    except:
        state_val = False

    try:
        task = Task.objects.create(
            title=title_val,
            description=description_val,
            status=state_val,
            owner=user
        )
        serializer = TaskSerializer(task)
        return JsonResponse({'tasks': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as exc:
        return JsonResponse({'error': str(exc)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Update task
@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_task(request, task_id):
    aux = json.dumps(request.data)
    data = json.loads(aux)
    user = request.user
    try:
        task_obj = Task.objects.filter(id=task_id, owner=user)
        task_obj.update(**data)
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task)
        return JsonResponse({'task': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'An error has occurred'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Delete task
@api_view(['DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_task(request, task_id):
    user = request.user
    try:
        task = Task.objects.get(id=task_id, owner=user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'An error has occurred'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Search task by description
@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def search_by_description(request):
    aux = json.dumps(request.data)
    data = json.loads(aux)
    user = request.user
    try:
        task = Task.objects.filter(owner=user, description__icontains=data['description'])
        serializer = TaskSerializer(task, many=True)
        return JsonResponse({'task': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'An error has occurred'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Change status task
@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def change_status_task(request, task_id):
    aux = json.dumps(request.data)
    data = json.loads(aux)
    user = request.user
    try:
        task_obj = Task.objects.get(id=task_id, owner=user)
        task_obj.status = data['status']
        task_obj.save(update_fields=['status'])
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task)
        return JsonResponse({'task': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'An error has occurred'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
