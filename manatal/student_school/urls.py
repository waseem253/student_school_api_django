from .views import StudentView, SchoolView, StudentSchoolView
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'school', SchoolView, 'school-view')
router.register(r'student', StudentView, 'student=view')

school_router = routers.NestedDefaultRouter(router, r'school', lookup='school')
school_router.register(r'students', StudentSchoolView, basename='student-school')
urlpatterns = router.urls
