---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/methods/create
title: "Create vector store"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create vector store

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

# Create vector store

POST /vector_stores

Create a vector store.

##### Body Parameters JSON Expand Collapse

chunking_strategy : optional [AutoFileChunkingStrategyParam](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)) { type } or [StaticFileChunkingStrategyObjectParam](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)) { static , type }

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

One of the following:

AutoFileChunkingStrategyParam object { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type : "auto"

Always `auto`.

[](#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema))

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

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema))

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chunking_strategy%20%3E%20(schema))

description : optional string

A description for the vector store. Can be used to describe the vector store’s purpose.

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20description%20%3E%20(schema))

expires_after : optional object { anchor , days }

The expiration policy for a vector store.

anchor : "last_active_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20anchor)

days : number

The number of days after the anchor time that the vector store will expire.

minimum 1

maximum 365

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20days)

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema))

file_ids : optional array of string

A list of [File](/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20file_ids%20%3E%20(schema))

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20metadata%20%3E%20(schema))

name : optional string

The name of the vector store.

[](#(resource)%20vector_stores%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

##### Returns Expand Collapse

VectorStore object { id , created_at , file_counts , 8 more }

A vector store is a collection of processed files can be used by the `file_search` tool.

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the vector store was created.

format unixtime

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20created_at)

file_counts : object { cancelled , completed , failed , 2 more }

cancelled : number

The number of files that were cancelled.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20cancelled)

completed : number

The number of files that have been successfully processed.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20completed)

failed : number

The number of files that have failed to process.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20failed)

in_progress : number

The number of files that are currently being processed.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20in_progress)

total : number

The total number of files.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20total)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts)

last_active_at : number

The Unix timestamp (in seconds) for when the vector store was last active.

format unixtime

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

The name of the vector store.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20name)

object : "vector_store"

The object type, which is always `vector_store`.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20object)

status : "expired" or "in_progress" or "completed"

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

"expired"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"in_progress"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"completed"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status)

usage_bytes : number

The total number of bytes used by the files in the vector store.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20usage_bytes)

expires_after : optional object { anchor , days }

The expiration policy for a vector store.

anchor : "last_active_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

days : number

The number of days after the anchor time that the vector store will expire.

minimum 1

maximum 365

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20days)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_after)

expires_at : optional number

The Unix timestamp (in seconds) for when the vector store will expire.

format unixtime

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_at)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema))

### Create vector store

```
curl https://api.openai.com/v1/vector_stores \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"name": "Support FAQ"
}'
```

```
{
"id": "vs_abc123",
"object": "vector_store",
"created_at": 1699061776,
"name": "Support FAQ",
"description": "Contains commonly asked questions and answers, organized by topic.",
"bytes": 139920,
"file_counts": {
"in_progress": 0,
"completed": 3,
"failed": 0,
"cancelled": 0,
"total": 3
}
}
```

##### Returns Examples

```
{
"id": "vs_abc123",
"object": "vector_store",
"created_at": 1699061776,
"name": "Support FAQ",
"description": "Contains commonly asked questions and answers, organized by topic.",
"bytes": 139920,
"file_counts": {
"in_progress": 0,
"completed": 3,
"failed": 0,
"cancelled": 0,
"total": 3
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/methods/create
