---
source_url: https://developers.openai.com/api/reference/resources/videos/methods/delete
title: "Delete video"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete video

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Videos](/api/reference/resources/videos)

# Delete video

DELETE /videos/{video_id}

Permanently delete a completed or failed video and its stored assets.

##### P ath Parameters Expand Collapse

video_id : string

[](#(resource)%20videos%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20video_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Identifier of the deleted video.

[](#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Indicates that the video resource was deleted.

[](#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "video.deleted"

The object type that signals the deletion response.

[](#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete video

```
curl https://api.openai.com/v1/videos/$VIDEO_ID \
-X DELETE \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "id",
"deleted": true,
"object": "video.deleted"
}
```

##### Returns Examples

```
{
"id": "id",
"deleted": true,
"object": "video.deleted"
}
```

---
Source: https://developers.openai.com/api/reference/resources/videos/methods/delete
