
from rest_framework.views import APIView
from rest_framework.response import Response

from .service import scrape_data
from .paginator import PageNumberPagination

class ListQuestionsApi(APIView):
    
    authentication_classes = []
    permission_classes = []
    paginator_class = PageNumberPagination

    def get(self, request, format=None):
        
        tag = request.query_params.get('tag')
        if tag != "":
            questions = scrape_data(tag)
        else:
            questions = scrape_data('django')
        
        return Response({"data": questions})
    
