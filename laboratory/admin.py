from django.contrib import admin
from .models import Laboratory
from analyze.models import PriceAnalyzeToLaboratory, Category


class PriceAnalyzeToLaboratoryAdmin(admin.TabularInline):
    model = PriceAnalyzeToLaboratory
    extra = 0


# class CategoryAdmin(admin.TabularInline):
#     model = Category


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    inlines = [PriceAnalyzeToLaboratoryAdmin, ]
