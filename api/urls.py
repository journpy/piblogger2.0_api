from rest_framework.routers import SimpleRouter
from .views import CustomUserViewSet, PostViewSet

router = SimpleRouter()

router.register('users', CustomUserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls