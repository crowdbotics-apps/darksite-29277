from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ForwardedMessageViewSet,
    MessageViewSet,
    ThreadMemberViewSet,
    MessageActionViewSet,
    ThreadViewSet,
    ThreadActionViewSet,
)

router = DefaultRouter()
router.register("threadaction", ThreadActionViewSet)
router.register("message", MessageViewSet)
router.register("thread", ThreadViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("threadmember", ThreadMemberViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
