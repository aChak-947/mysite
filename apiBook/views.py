from rest_framework.views import APIView
from .API import bookAPI

# Create your views here.
class UpsertBook(APIView):
    def put(self, request):

        response_post = bookAPI.upsertBook(self,request.data)
        return response_post

class DeleteBook(APIView):
    def post(self, request):

        response_delete = bookAPI.deleteBook(self,request.data)
        return response_delete

class ListBooks(APIView):
    def post(self, request):

        response_list = bookAPI.listBooks(self,request.data)
        return response_list
