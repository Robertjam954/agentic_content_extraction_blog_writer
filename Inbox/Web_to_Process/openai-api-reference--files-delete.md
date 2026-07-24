---
source_url: https://developers.openai.com/api/reference/resources/files/methods/delete
title: "Delete file"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete file

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Files](/api/reference/resources/files)

# Delete file

DELETE /files/{file_id}

Delete a file and remove it from all vector stores.

##### P ath Parameters Expand Collapse

file_id : string

[](#(resource)%20files%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20file_id%20%3E%20(schema))

##### Returns Expand Collapse

FileDeleted object { id , deleted , object }

id : string

[](#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "file"

[](#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema))

### Delete file

```
curl https://api.openai.com/v1/files/file-abc123 \
-X DELETE \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "file-abc123",
"object": "file",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "file-abc123",
"object": "file",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/files/methods/delete
