from django.urls import path
from .views import CreateTestView, ListTestView, UpdateDestroyTestView, GetTestView


urlpatterns = [
    path('test/create/', CreateTestView.as_view()),
    path('test/list/', ListTestView.as_view()),
    path('test/detail/<int:pk>', GetTestView.as_view()),
    path('test/updelete/<int:pk>', UpdateDestroyTestView.as_view()),

]