from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ShowLists(LoginRequiredMixin, ListAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        # print("get is called") --> for testing
        return super(ShowLists, self).get(request, *args, **kwargs)
