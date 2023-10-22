from django.urls import path

from zahid_test.users.views import (
    celery_debugging_view,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
    path("celery/tasks/", view=celery_debugging_view, name="celery-tasks"),
]
