import datetime
import json

def handler(event, context):
    # Someday....
    # posts = s3.readPosts()

    return [
        {
            "id": 2,
            "title": "Post about something",
            "body": "This is my body content",
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat(),
            "created_by": "Emily"
        },
        {
            "id": 1,
            "title": "Post about another thing",
            "body": "你好世界",
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat(),
            "created_by": "Robert"
        }
    ]
