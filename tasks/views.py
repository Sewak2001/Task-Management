from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Task
from .serializers import TaskSerializer

CustomUser = get_user_model()

# Task get and create
class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    # Retrieve list of all tasks
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new task
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Task details 
class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # Retrieve details of a specific task
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update an existing task (full update)
    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a task
    def patch(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Remove a task
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Task status update
class TaskStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        status_value = request.data.get("status")
        if status_value not in ["Todo", "Inprogress", "Done"]:
            return Response(
                {"error": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        task.status = status_value
        task.save()
        return Response(
          {"message": "Task status updated"},
          status=status.HTTP_200_OK
        )

# Task memeber add/remove
class TaskMemberView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        user_id = request.data.get("user_id")

        user = get_object_or_404(CustomUser, id=user_id)
        task.members.add(user)
        return Response(
            {"message": "Member added successfully"},
            status=status.HTTP_200_OK
        )

    def delete(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        user_id = request.data.get("user_id")

        user = get_object_or_404(CustomUser, id=user_id)
        task.members.remove(user)
        return Response(
            {"message": "Member removed successfully"},
            status=status.HTTP_200_OK
        )

# Task members list
class TaskMembersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        members = task.members.all()
        members_data = [
            {"id": user.id, "username": user.username, "email": user.email} for user in members
        ]
        return Response(members_data, status=status.HTTP_200_OK)
