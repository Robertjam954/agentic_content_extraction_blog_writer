---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/methods/list
title: "List vector store files"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List vector store files

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

[Files](/api/reference/resources/vector_stores/subresources/files)

# List vector store files

GET /vector_stores/{vector_store_id}/files

Returns a list of vector store files.

##### P ath Parameters Expand Collapse

vector_store_id : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20vector_store_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

before : optional string

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20before%20%3E%20(schema))

filter : optional "in_progress" or "completed" or "failed" or "cancelled"

Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

One of the following:

"in_progress"

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)%20%3E%20(member)%200)

"completed"

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)%20%3E%20(member)%201)

"failed"

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)%20%3E%20(member)%202)

"cancelled"

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema)%20%3E%20(member)%203)

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20filter%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [VectorStoreFile](/api/reference/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file%20%3E%20(schema)) { id , created_at , last_error , 6 more }

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

chunk_overlap_tokens : number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20static%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20chunk_overlap_tokens)

max_chunk_size_tokens : number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum 100

maximum 4096

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20static%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20max_chunk_size_tokens)

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

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

first_id : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

has_more : boolean

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

last_id : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

object : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List vector store files

```
curl https://api.openai.com/v1/vector_stores/vs_abc123/files \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2"
```

```
{
"object": "list",
"data": [
{
"id": "file-abc123",
"object": "vector_store.file",
"created_at": 1699061776,
"vector_store_id": "vs_abc123"
},
{
"id": "file-abc456",
"object": "vector_store.file",
"created_at": 1699061776,
"vector_store_id": "vs_abc123"
}
],
"first_id": "file-abc123",
"last_id": "file-abc456",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "file-abc123",
"object": "vector_store.file",
"created_at": 1699061776,
"vector_store_id": "vs_abc123"
},
{
"id": "file-abc456",
"object": "vector_store.file",
"created_at": 1699061776,
"vector_store_id": "vs_abc123"
}
],
"first_id": "file-abc123",
"last_id": "file-abc456",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/methods/list
