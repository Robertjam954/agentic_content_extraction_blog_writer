---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files
title: "Files"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Files

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

# Files

##### [List vector store files](/api/reference/resources/vector_stores/subresources/files/methods/list)

GET /vector_stores/{vector_store_id}/files

##### [Create vector store file](/api/reference/resources/vector_stores/subresources/files/methods/create)

POST /vector_stores/{vector_store_id}/files

##### [Update vector store file attributes](/api/reference/resources/vector_stores/subresources/files/methods/update)

POST /vector_stores/{vector_store_id}/files/{file_id}

##### [Retrieve vector store file](/api/reference/resources/vector_stores/subresources/files/methods/retrieve)

GET /vector_stores/{vector_store_id}/files/{file_id}

##### [Delete vector store file](/api/reference/resources/vector_stores/subresources/files/methods/delete)

DELETE /vector_stores/{vector_store_id}/files/{file_id}

##### [Retrieve vector store file content](/api/reference/resources/vector_stores/subresources/files/methods/content)

GET /vector_stores/{vector_store_id}/files/{file_id}/content

##### Models Expand Collapse

VectorStoreFile object { id , created_at , last_error , 6 more }

A list of files attached to a vector store.

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the vector store file was created.

format unixtime

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20created_at)

last_error : object { code , message }

The last error associated with this vector store file. Will be `null` if there are no errors.

code : "server_error" or "unsupported_file" or "invalid_file"

One of `server_error`, `unsupported_file`, or `invalid_file`.

One of the following:

"server_error"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%200)

"unsupported_file"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%201)

"invalid_file"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%202)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code)

message : string

A human-readable description of the error.

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20message)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20last_error)

object : "vector_store.file"

The object type, which is always `vector_store.file`.

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20object)

status : "in_progress" or "completed" or "cancelled" or "failed"

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

One of the following:

"in_progress"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"completed"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"cancelled"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"failed"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20status)

usage_bytes : number

The total vector store usage in bytes. Note that this may be different from the original file size.

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20usage_bytes)

vector_store_id : string

The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to.

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20vector_store_id)

attributes : optional map [ string or number or boolean ]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%201)

boolean

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20attributes)

chunking_strategy : optional [StaticFileChunkingStrategyObject](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)) { static , type } or [OtherFileChunkingStrategyObject](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)) { type }

The strategy used to chunk the file.

One of the following:

StaticFileChunkingStrategyObject object { static , type }

static : [StaticFileChunkingStrategy](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk_overlap_tokens , max_chunk_size_tokens }

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema))

OtherFileChunkingStrategyObject object { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type : "other"

Always `other`.

[](#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema))

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)%20%3E%20(property)%20chunking_strategy)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema))

VectorStoreFileDeleted object { id , deleted , object }

id : string

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "vector_store.file.deleted"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema))

FileContentResponse object { text , type }

text : optional string

The text content

[](#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)%20%3E%20(property)%20text)

type : optional string

The content type (currently only `"text"`)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files
