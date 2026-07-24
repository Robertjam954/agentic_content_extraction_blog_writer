---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches/methods/create
title: "Create vector store file batch"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create vector store file batch

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

[File Batches](/api/reference/resources/vector_stores/subresources/file_batches)

# Create vector store file batch

POST /vector_stores/{vector_store_id}/file_batches

Create a vector store file batch.

##### P ath Parameters Expand Collapse

vector_store_id : string

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20vector_store_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

attributes : optional map [ string or number or boolean ]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20attributes%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20attributes%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201)

boolean

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20attributes%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20attributes%20%3E%20(schema))

chunking_strategy : optional [FileChunkingStrategyParam](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

One of the following:

AutoFileChunkingStrategyParam object { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type : "auto"

Always `auto`.

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chunking_strategy%20%3E%20(schema)%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chunking_strategy%20%3E%20(schema)%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema))

StaticFileChunkingStrategyObjectParam object { static , type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static : [StaticFileChunkingStrategy](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk_overlap_tokens , max_chunk_size_tokens }

chunk_overlap_tokens : number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20chunk_overlap_tokens)

max_chunk_size_tokens : number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum 100

maximum 4096

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20max_chunk_size_tokens)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chunking_strategy%20%3E%20(schema)%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chunking_strategy%20%3E%20(schema)%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chunking_strategy%20%3E%20(schema)%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema))

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chunking_strategy%20%3E%20(schema))

file_ids : optional array of string

A list of [File](/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files. If `attributes` or `chunking_strategy` are provided, they will be applied to all files in the batch. The maximum batch size is 2000 files. This endpoint is recommended for multi-file ingestion and helps reduce per-vector-store write request pressure. Mutually exclusive with `files`.

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20file_ids%20%3E%20(schema))

files : optional array of object { file_id , attributes , chunking_strategy }

A list of objects that each include a `file_id` plus optional `attributes` or `chunking_strategy`. Use this when you need to override metadata for specific files. The global `attributes` or `chunking_strategy` will be ignored and must be specified for each file. The maximum batch size is 2000 files. This endpoint is recommended for multi-file ingestion and helps reduce per-vector-store write request pressure. Mutually exclusive with `file_ids`.

file_id : string

A [File](/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files. For multi-file ingestion, we recommend [file_batches](/docs/api-reference/vector-stores-file-batches/createBatch) to minimize per-vector-store write requests.

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20file_id)

attributes : optional map [ string or number or boolean ]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%201)

boolean

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attributes)

chunking_strategy : optional [FileChunkingStrategyParam](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

One of the following:

AutoFileChunkingStrategyParam object { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type : "auto"

Always `auto`.

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema))

StaticFileChunkingStrategyObjectParam object { static , type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static : [StaticFileChunkingStrategy](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk_overlap_tokens , max_chunk_size_tokens }

chunk_overlap_tokens : number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20chunk_overlap_tokens)

max_chunk_size_tokens : number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum 100

maximum 4096

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20max_chunk_size_tokens)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%2B%20(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema))

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20chunking_strategy)

[](#(resource)%20vector_stores.file_batches%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20files%20%3E%20(schema))

##### Returns Expand Collapse

VectorStoreFileBatch object { id , created_at , file_counts , 3 more }

A batch of files attached to a vector store.

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the vector store files batch was created.

format unixtime

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20created_at)

file_counts : object { cancelled , completed , failed , 2 more }

cancelled : number

The number of files that where cancelled.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20cancelled)

completed : number

The number of files that have been processed.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20completed)

failed : number

The number of files that have failed to process.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20failed)

in_progress : number

The number of files that are currently being processed.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20in_progress)

total : number

The total number of files.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20total)

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20file_counts)

object : "vector_store.files_batch"

The object type, which is always `vector_store.file_batch`.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20object)

status : "in_progress" or "completed" or "cancelled" or "failed"

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

One of the following:

"in_progress"

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"completed"

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"cancelled"

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"failed"

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20status)

vector_store_id : string

The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to.

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema)%20%3E%20(property)%20vector_store_id)

[](#(resource)%20vector_stores.file_batches%20%3E%20(model)%20vector_store_file_batch%20%3E%20(schema))

### Create vector store file batch

```
curl https://api.openai.com/v1/vector_stores/vs_abc123/file_batches \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"files": [
{
"file_id": "file-abc123",
"attributes": {"category": "finance"}
},
{
"file_id": "file-abc456",
"chunking_strategy": {
"type": "static",
"max_chunk_size_tokens": 1200,
"chunk_overlap_tokens": 200
}
}
]
}'
```

```
{
"id": "vsfb_abc123",
"object": "vector_store.file_batch",
"created_at": 1699061776,
"vector_store_id": "vs_abc123",
"status": "in_progress",
"file_counts": {
"in_progress": 1,
"completed": 1,
"failed": 0,
"cancelled": 0,
"total": 0,
}
}
```

##### Returns Examples

```
{
"id": "vsfb_abc123",
"object": "vector_store.file_batch",
"created_at": 1699061776,
"vector_store_id": "vs_abc123",
"status": "in_progress",
"file_counts": {
"in_progress": 1,
"completed": 1,
"failed": 0,
"cancelled": 0,
"total": 0,
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches/methods/create
