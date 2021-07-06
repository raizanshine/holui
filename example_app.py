from src.connections.database import get_database_connection
from src.engines.flask import FlaskStandaloneEngine
from src.pages import AdminPage
from src.site import AdminSite

admin_site = AdminSite(
    name="Test application",
    connection=get_database_connection(
        "postgresql://ledger:ledger@127.0.0.1:5432/ledger"
    ),
)


class UserAdminPage(AdminPage):
    pass


admin_site.register("users", UserAdminPage)

engine = FlaskStandaloneEngine(admin_site)
engine.run_app()
