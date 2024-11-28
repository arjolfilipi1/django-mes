from django.urls import include, path
import basedata.views

urlpatterns = [
    path(r"dataimport/<object_id>/action", basedata.views.action_import),
]
