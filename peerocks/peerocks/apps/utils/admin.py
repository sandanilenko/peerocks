from django.contrib import (
    admin,
)


def register_app_in_admin_panel(app):
    """
    Регистрация приложения в панеле администратора
    """
    for model_name, model in app.models.items():
        # Не имеет смысла отображать прокси-модели
        if model._meta.proxy:
            continue

        model_admin = type(str(model_name + "Admin"), (admin.ModelAdmin,), {})

        model_admin.list_display = (
            model.admin_list_display if
            hasattr(model, 'admin_list_display') else
            tuple([field.name for field in model._meta.fields])
        )
        model_admin.list_filter = (
            model.admin_list_filter if
            hasattr(model, 'admin_list_filter') else
            model_admin.list_display
        )
        model_admin.list_display_links = (
            model.admin_list_display_links if
            hasattr(model, 'admin_list_display_links') else
            ()
        )
        model_admin.list_editable = (
            model.admin_list_editable if
            hasattr(model, 'admin_list_editable') else
            ()
        )
        model_admin.search_fields = (
            model.admin_search_fields if
            hasattr(model, 'admin_search_fields') else
            ()
        )
        model_admin.ordering = (
            model._meta.ordering if
            hasattr(model._meta, 'ordering') else
            ()
        )

        admin.site.register(model, model_admin)
