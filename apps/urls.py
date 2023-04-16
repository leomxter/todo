from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DeleteAllTodoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, format=None):
        todos = Todo.objects.filter(owner=request.user)
        todos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
