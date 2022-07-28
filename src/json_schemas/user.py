"""
JSON Schema — стандарт описания структуры данных.
В данном проекте не используется, приведен для примера.
"""

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data":
            {
                "id": {"type": "number"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"}
            },
        "support": {
            "text": {"type": "string"},
            "url": {"type": "string"}
        }
    },
    "required": ["data"]  # Обязательные properties
}
