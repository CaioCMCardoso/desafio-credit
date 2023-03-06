from rest_framework.routers import DefaultRouter
from api.views import CardViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'card', CardViewSet)

urlpatterns = router.urls