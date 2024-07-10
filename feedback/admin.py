
# Register your models here.
from django.contrib import admin
from feedback.models import Feedback
import bcrypt

# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'doador', 'descricao', 'stars')