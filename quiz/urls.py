from django.urls import path
from . import views

urlpatterns = [
	path('start/<int:m_id>',views.start_quiz,name="start_quiz"),
	path('result/<int:module>',views.result,name="quiz_result"),
	path('quiz/',views.insert_quiz,name="insert_quiz"),
]