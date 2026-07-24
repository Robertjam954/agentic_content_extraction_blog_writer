---
source_url: https://developers.openai.com/api/reference/resources/containers/subresources/files
title: "Files"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Files

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

# Files

##### [List container files](/api/reference/resources/containers/subresources/files/methods/list)

GET /containers/{container_id}/files

##### [Create container file](/api/reference/resources/containers/subresources/files/methods/create)

POST /containers/{container_id}/files

##### [Retrieve container file](/api/reference/resources/containers/subresources/files/methods/retrieve)

GET /containers/{container_id}/files/{file_id}

##### [Delete a container file](/api/reference/resources/containers/subresources/files/methods/delete)

DELETE /containers/{container_id}/files/{file_id}

##### Models Expand Collapse

FileListResponse object { id , bytes , container_id , 4 more }

id : string

Unique identifier for the file.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

bytes : number

Size of the file in bytes.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20bytes)

container_id : string

The container this file belongs to.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20container_id)

created_at : number

Unix timestamp (in seconds) when the file was created.

format unixtime

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : string

The type of this object (`container.file`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

path : string

Path of the file in the container.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20path)

source : string

Source of the file (e.g., `user`, `assistant`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20source)

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema))

FileCreateResponse object { id , bytes , container_id , 4 more }

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

[](#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema))

FileRetrieveResponse object { id , bytes , container_id , 4 more }

id : string

Unique identifier for the file.

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

bytes : number

Size of the file in bytes.

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20bytes)

container_id : string

The container this file belongs to.

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20container_id)

created_at : number

Unix timestamp (in seconds) when the file was created.

format unixtime

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : string

The type of this object (`container.file`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20object)

path : string

Path of the file in the container.

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20path)

source : string

Source of the file (e.g., `user`, `assistant`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20source)

[](#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema))

#### Files Content

##### [Retrieve container file content](/api/reference/resources/containers/subresources/files/subresources/content/methods/retrieve)

GET /containers/{container_id}/files/{file_id}/content

---
Source: https://developers.openai.com/api/reference/resources/containers/subresources/files
