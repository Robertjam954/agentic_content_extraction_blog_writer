---
source_url: https://developers.openai.com/api/reference/resources/vector_stores
title: "Vector Stores"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Vector Stores

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Vector Stores

##### [List vector stores](/api/reference/resources/vector_stores/methods/list)

GET /vector_stores

##### [Create vector store](/api/reference/resources/vector_stores/methods/create)

POST /vector_stores

##### [Retrieve vector store](/api/reference/resources/vector_stores/methods/retrieve)

GET /vector_stores/{vector_store_id}

##### [Modify vector store](/api/reference/resources/vector_stores/methods/update)

POST /vector_stores/{vector_store_id}

##### [Delete vector store](/api/reference/resources/vector_stores/methods/delete)

DELETE /vector_stores/{vector_store_id}

##### [Search vector store](/api/reference/resources/vector_stores/methods/search)

POST /vector_stores/{vector_store_id}/search

##### Models Expand Collapse

AutoFileChunkingStrategyParam object { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type : "auto"

Always `auto`.

[](#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema))

FileChunkingStrategyParam = [AutoFileChunkingStrategyParam](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20auto_file_chunking_strategy_param%20%3E%20(schema)) { type } or [StaticFileChunkingStrategyObjectParam](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)) { static , type }

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

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

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema))

[](#(resource)%20vector_stores%20%3E%20(model)%20file_chunking_strategy_param%20%3E%20(schema))

OtherFileChunkingStrategyObject object { type }

This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

type : "other"

Always `other`.

[](#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20other_file_chunking_strategy_object%20%3E%20(schema))

StaticFileChunkingStrategy object { chunk_overlap_tokens , max_chunk_size_tokens }

chunk_overlap_tokens : number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20chunk_overlap_tokens)

max_chunk_size_tokens : number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum 100

maximum 4096

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)%20%3E%20(property)%20max_chunk_size_tokens)

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema))

StaticFileChunkingStrategyObject object { static , type }

static : [StaticFileChunkingStrategy](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk_overlap_tokens , max_chunk_size_tokens }

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object%20%3E%20(schema))

StaticFileChunkingStrategyObjectParam object { static , type }

Customize your own chunking strategy by setting chunk size and chunk overlap.

static : [StaticFileChunkingStrategy](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy%20%3E%20(schema)) { chunk_overlap_tokens , max_chunk_size_tokens }

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20static_file_chunking_strategy_object_param%20%3E%20(schema))

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

VectorStoreDeleted object { id , deleted , object }

id : string

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "vector_store.deleted"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema))

VectorStoreSearchResponse object { attributes , content , file_id , 2 more }

attributes : map [ string or number or boolean ]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%201)

boolean

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes)

content : array of object { text , type }

Content chunks from the file.

text : string

The text content returned from search.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : "text"

The type of content.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20content)

file_id : string

The ID of the vector store file.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20file_id)

filename : string

The name of the vector store file.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20filename)

score : number

The similarity score for the result.

minimum 0

maximum 1

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20score)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema))

#### Vector Stores Files

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

#### Vector Stores File Batches

##### [Create vector store file batch](/api/reference/resources/vector_stores/subresources/file_batches/methods/create)

POST /vector_stores/{vector_store_id}/file_batches

##### [Retrieve vector store file batch](/api/reference/resources/vector_stores/subresources/file_batches/methods/retrieve)

GET /vector_stores/{vector_store_id}/file_batches/{batch_id}

##### [Cancel vector store file batch](/api/reference/resources/vector_stores/subresources/file_batches/methods/cancel)

POST /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel

##### [List vector store files in a batch](/api/reference/resources/vector_stores/subresources/file_batches/methods/list_files)

GET /vector_stores/{vector_store_id}/file_batches/{batch_id}/files

##### Models Expand Collapse

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

---
Source: https://developers.openai.com/api/reference/resources/vector_stores
