---
source_url: https://developers.openai.com/api/reference/resources/containers
title: "Containers"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Containers

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Containers

##### [List containers](/api/reference/resources/containers/methods/list)

GET /containers

##### [Create container](/api/reference/resources/containers/methods/create)

POST /containers

##### [Retrieve container](/api/reference/resources/containers/methods/retrieve)

GET /containers/{container_id}

##### [Delete a container](/api/reference/resources/containers/methods/delete)

DELETE /containers/{container_id}

##### Models Expand Collapse

ContainerListResponse object { id , created_at , name , 6 more }

id : string

Unique identifier for the container.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the container was created.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Name of the container.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : string

The type of this object.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

status : string

Status of the container (e.g., active, deleted).

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20status)

expires_after : optional object { anchor , minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor : optional "last_active_at"

The reference point for the expiration.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

minutes : optional number

The number of minutes after the anchor before the container expires.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20minutes)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_after)

last_active_at : optional number

Unix timestamp (in seconds) when the container was last active.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit)

network_policy : optional object { type , allowed_domains }

Network access policy for the container.

type : "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%200)

"disabled"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type)

allowed_domains : optional array of string

Allowed outbound domains when `type` is `allowlist`.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20allowed_domains)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema))

ContainerCreateResponse object { id , created_at , name , 6 more }

id : string

Unique identifier for the container.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the container was created.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Name of the container.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : string

The type of this object.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

status : string

Status of the container (e.g., active, deleted).

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20status)

expires_after : optional object { anchor , minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor : optional "last_active_at"

The reference point for the expiration.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

minutes : optional number

The number of minutes after the anchor before the container expires.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20minutes)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_after)

last_active_at : optional number

Unix timestamp (in seconds) when the container was last active.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit)

network_policy : optional object { type , allowed_domains }

Network access policy for the container.

type : "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%200)

"disabled"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type)

allowed_domains : optional array of string

Allowed outbound domains when `type` is `allowlist`.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20allowed_domains)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema))

ContainerRetrieveResponse object { id , created_at , name , 6 more }

id : string

Unique identifier for the container.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the container was created.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Name of the container.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : string

The type of this object.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20object)

status : string

Status of the container (e.g., active, deleted).

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20status)

expires_after : optional object { anchor , minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor : optional "last_active_at"

The reference point for the expiration.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

minutes : optional number

The number of minutes after the anchor before the container expires.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20minutes)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20expires_after)

last_active_at : optional number

Unix timestamp (in seconds) when the container was last active.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit)

network_policy : optional object { type , allowed_domains }

Network access policy for the container.

type : "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%200)

"disabled"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type)

allowed_domains : optional array of string

Allowed outbound domains when `type` is `allowlist`.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20allowed_domains)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema))

#### Containers Files

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

#### Containers Files Content

##### [Retrieve container file content](/api/reference/resources/containers/subresources/files/subresources/content/methods/retrieve)

GET /containers/{container_id}/files/{file_id}/content

---
Source: https://developers.openai.com/api/reference/resources/containers
