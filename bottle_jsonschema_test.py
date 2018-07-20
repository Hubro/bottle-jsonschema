
import pytest

from bottle_jsonschema import JSONSchemaPlugin, SchemaValidationError

def test_get_schema_names(mocker):
    subject = JSONSchemaPlugin()._get_schema_names

    assert subject("/login", "PUT") == [
        "schemas/login.PUT.json",
        "schemas/login.json",
    ]

    assert subject("/admin/users/", "POST") == [
        "schemas/admin.users.POST.json",
        "schemas/admin.users.json",
    ]

    assert subject("/admin/users/<id>", "POST") == [
        "schemas/admin.users.id.POST.json",
        "schemas/admin.users.id.json",
    ]

    assert subject("/admin/users/<id:int>", "POST") == [
        "schemas/admin.users.id.POST.json",
        "schemas/admin.users.id.json",
    ]

    assert subject("/admin/users/<username:re:\w+(@\w+)?>", "PATCH") == [
        "schemas/admin.users.username.PATCH.json",
        "schemas/admin.users.username.json",
    ]
