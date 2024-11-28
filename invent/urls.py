from django.urls import include, path
import invent.views

urlpatterns = [
    path("stockin/<object_id>/cin", invent.views.action_in),
    path("initialinventory/<object_id>/cin", invent.views.action_init),
    path("stockout/<object_id>/out", invent.views.action_out),
    path("warereturn/<object_id>/cin", invent.views.action_return),
    path("wareadjust/<object_id>/adjust", invent.views.action_adjust),
]
