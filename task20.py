permissions = {"read": True, "write": False, "delete": True}

for key, value in permissions.items():
    if value:
        print(key)