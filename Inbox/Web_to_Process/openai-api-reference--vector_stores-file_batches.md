---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches
title: "File Batches"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# File Batches

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

# File Batches

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
Source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches
