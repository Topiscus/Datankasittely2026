def validate_items(items):
    # Basic validation: check required fields and uniqueness.

    if not isinstance(items, list):
        raise ValueError("Data must be a list.")

    ids = set()
    for item in items:
        if not isinstance(item.get("id"), int):
            raise ValueError(f"Missing or invalid id: {item}")
        if not item.get("title"):
            raise ValueError(f"Missing title for item {item.get('id')}")
        if item["id"] in ids:
            raise ValueError(f"Duplicate id {item['id']}")
        ids.add(item["id"])
    return True