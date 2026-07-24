---
source_url: https://developers.openai.com/api/reference/resources/containers/subresources/files/methods/create
title: "Create container file"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create container file

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

[Files](/api/reference/resources/containers/subresources/files)

# Create container file

POST /containers/{container_id}/files

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

##### P ath Parameters Expand Collapse

container_id : string

[](#(resource)%20containers.files%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20container_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

file : optional file

The File object (not file name) to be uploaded.

[](#(resource)%20containers.files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20file%20%3E%20(schema))

file_id : optional string

Name of the file to create.

[](#(resource)%20containers.files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20file_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Unique identifier for the file.

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

bytes : number

Size of the file in bytes.

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)%20%3E%20(property)%20bytes)

container_id : string

The container this file belongs to.

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)%20%3E%20(property)%20container_id)

created_at : number

Unix timestamp (in seconds) when the file was created.

format unixtime

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : string

The type of this object (`container.file`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

path : string

Path of the file in the container.

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)%20%3E%20(property)%20path)

source : string

Source of the file (e.g., `user`, `assistant`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)%20%3E%20(property)%20source)

### Create container file

```
curl https://api.openai.com/v1/containers/cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04/files \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-F file="@example.txt"
```

```
{
"id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"object": "container.file",
"created_at": 1747848842,
"bytes": 880,
"container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
"path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
"source": "user"
}
```

##### Returns Examples

```
{
"id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"object": "container.file",
"created_at": 1747848842,
"bytes": 880,
"container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
"path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
"source": "user"
}
```

---
Source: https://developers.openai.com/api/reference/resources/containers/subresources/files/methods/create
