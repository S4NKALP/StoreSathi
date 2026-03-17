"""generated with djinit"""
import importlib

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from ninja import NinjaAPI, Redoc

api = NinjaAPI(
    title="StoreSathi API",
    version="1.0.0",
    docs=Redoc(),
    docs_decorator=login_required,
    urls_namespace="api",
)


def autodiscover_api():
    """Automatically discover and register api from apps/ directory."""
    apps_dir = settings.BASE_DIR / "apps"
    if not apps_dir.exists():
        return

    for app_path in apps_dir.iterdir():
        if not app_path.is_dir() or app_path.name == "__pycache__":
            continue

        api_file = app_path / "api.py"
        if not api_file.exists():
            continue

        app_name = app_path.name

        try:
            module = importlib.import_module(f"apps.{app_name}.api")
            # Look for 'router' or '{app_name}_router' in api.py
            router = getattr(module, "router", getattr(module, f"{app_name}_router", None))

            if router:
                api.add_router(f"/{app_name}/", router)
        except ImportError:
            pass


autodiscover_api()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
