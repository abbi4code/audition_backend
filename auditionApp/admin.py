from django.contrib import admin
from auditionApp.models import AuditionPortal,DesignWorkshop,ValorantGaming,BgmiGaming
from import_export.admin import ExportActionMixin

# Register your models here.
class AuditionPortalAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("name", "roll_no", "contact_number", "email", "department")

class DesignWorkshopAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("name", "roll_no", "contact_number", "email", "department","year","payment_proof")

class ValorantGamingAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("name", "contact_number", "email","payment_proof")

class BgmiGamingAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("name", "contact_number", "email","payment_proof")

admin.site.register(AuditionPortal, AuditionPortalAdmin)
admin.site.register(DesignWorkshop, DesignWorkshopAdmin)
admin.site.register(ValorantGaming, ValorantGamingAdmin)
admin.site.register(BgmiGaming, BgmiGamingAdmin)