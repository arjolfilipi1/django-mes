from django.urls import include, path
import selfhelp.views

urlpatterns = [
    path("<model>/<object_id>/pay", selfhelp.views.pay_action),
]
