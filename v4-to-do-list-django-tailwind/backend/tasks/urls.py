from rest_framework import routers
from .api import TaskViewset


router = routers.DefaultRouter()
router.register("api/tasks", TaskViewset, "tasks")

urlpatterns = router.urls