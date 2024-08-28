from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ShowListsView(ListAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    @method_decorator(cache_page(60 * 30))
    def get(self, request, *args, **kwargs):
        # print("get is called") --> for testing
        return super(ShowListsView, self).get(request, *args, **kwargs)
