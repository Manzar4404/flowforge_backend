from rest_framework.routers import DefaultRouter
from flowforge_backend.account.api.views import UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet, basename="user")

urlpatterns = router.urls
