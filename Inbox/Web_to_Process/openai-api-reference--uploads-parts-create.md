---
source_url: https://developers.openai.com/api/reference/resources/uploads/subresources/parts/methods/create
title: "Add upload part"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Add upload part

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Uploads](/api/reference/resources/uploads)

[Parts](/api/reference/resources/uploads/subresources/parts)

# Add upload part

POST /uploads/{upload_id}/parts

Adds a [Part](/docs/api-reference/uploads/part-object) to an [Upload](/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](/docs/api-reference/uploads/complete).

##### P ath Parameters Expand Collapse

upload_id : string

[](#(resource)%20uploads.parts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20upload_id%20%3E%20(schema))

##### Body Parameters Form Data Expand Collapse

data : file

The chunk of bytes for this Part.

[](#(resource)%20uploads.parts%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data%20%3E%20(schema))

##### Returns Expand Collapse

UploadPart object { id , created_at , object , upload_id }

The upload Part represents a chunk of bytes we can add to an Upload object.

id : string

The upload Part unique identifier, which can be referenced in API endpoints.

[](#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the Part was created.

format unixtime

[](#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "upload.part"

The object type, which is always `upload.part`.

[](#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)%20%3E%20(property)%20object)

upload_id : string

The ID of the Upload object that this Part was added to.

[](#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)%20%3E%20(property)%20upload_id)

[](#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema))

### Add upload part

```
curl https://api.openai.com/v1/uploads/upload_abc123/parts
-F data="aHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MS91cGxvYWRz..."
```

```
{
"id": "part_def456",
"object": "upload.part",
"created_at": 1719185911,
"upload_id": "upload_abc123"
}
```

##### Returns Examples

```
{
"id": "part_def456",
"object": "upload.part",
"created_at": 1719185911,
"upload_id": "upload_abc123"
}
```

---
Source: https://developers.openai.com/api/reference/resources/uploads/subresources/parts/methods/create
