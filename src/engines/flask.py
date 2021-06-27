from functools import partial, update_wrapper

from flask import Flask


def describe_field(name, field):
    return {
        "name": name,
        "type": field.__class__.__name__,
    }


def list_pages(admin_site):
    return {
        "siteName": admin_site.name,
        "pages": [
            {"label": label, "fields": [describe_field(name, field) for name, field in page.get_fields().items()]} for label, page in admin_site
        ],
    }


class FlaskStandaloneEngine:
    def __init__(self, admin_site):
        self.admin = admin_site
        self.create_app(self.admin)

    def create_app(self, admin):
        self.app = Flask(admin.name)
        self.register_endpoints()

    def register_endpoints(self):
        self.app.route("/api/schema.json")(
            update_wrapper(partial(list_pages, self.admin), list_pages)
        )

    def run_app(self):
        self.app.run()
