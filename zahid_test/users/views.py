import logging
from celery import chord
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from zahid_test.users.tasks import get_publishing_task, get_task_1, get_task_2

logger = logging.getLogger(__name__)
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


class CeleryDebugging(LoginRequiredMixin, APIView):

    def get(self, request, format=None):
        logger.info('***************************************')
        logger.info('*********** chord start ***************')
        logger.info('***************************************')

        callback = get_publishing_task.s()
        header = [get_task_1.s(), get_task_2.s()]
        result = chord(header)(callback)
        result.get()

        logger.info('***************************************')
        logger.info('*********** chord end ***************')
        logger.info('***************************************')

        return Response({'message': 'success'}, status=status.HTTP_200_OK)


celery_debugging_view = CeleryDebugging.as_view()
