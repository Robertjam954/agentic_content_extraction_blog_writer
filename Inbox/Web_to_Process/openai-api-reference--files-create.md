---
source_url: https://developers.openai.com/api/reference/resources/files/methods/create
title: "Upload file"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Upload file

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Files](/api/reference/resources/files)

# Upload file

POST /files

Upload a file that can be used across various endpoints. Individual files
can be up to 512 MB, and each project can store up to 2.5 TB of files in
total. There is no organization-wide storage limit. Uploads to this
endpoint are rate-limited to 1,000 requests per minute per authenticated
user.

- The Assistants API supports files up to 2 million tokens and of specific
file types. See the [Assistants Tools guide](/docs/assistants/tools) for
details.

- The Fine-tuning API only supports `.jsonl` files. The input also has
certain required formats for fine-tuning
[chat](/docs/api-reference/fine-tuning/chat-input) or
[completions](/docs/api-reference/fine-tuning/completions-input) models.

- The Batch API only supports `.jsonl` files up to 200 MB in size. The input
also has a specific required
[format](/docs/api-reference/batch/request-input).

- For Retrieval or `file_search` ingestion, upload files here first. If
you need to attach multiple uploaded files to the same vector store, use
[/vector_stores/{vector_store_id}/file_batches](/docs/api-reference/vector-stores-file-batches/createBatch)
instead of attaching them one by one. Vector store attachment has separate
limits from file upload, including 2,000 attached files per minute per
organization.

Please [contact us](https://help.openai.com/) if you need to increase these
storage limits.

##### Body Parameters Form Data Expand Collapse

file : file

The File object (not file name) to be uploaded.

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20file%20%3E%20(schema))

purpose : "assistants" or "batch" or "fine-tune" or 3 more

The intended purpose of the uploaded file. One of:

- `assistants`: Used in the Assistants API

- `batch`: Used in the Batch API

- `fine-tune`: Used for fine-tuning

- `vision`: Images used for vision fine-tuning

- `user_data`: Flexible file type for any purpose

- `evals`: Used for eval data sets

One of the following:

"assistants"

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%200)

"batch"

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%201)

"fine-tune"

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%202)

"vision"

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%203)

"user_data"

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%204)

"evals"

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%205)

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema))

expires_after : optional object { anchor , seconds }

The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

anchor : "created_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20anchor)

seconds : number

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

format int64

minimum 3600

maximum 2592000

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20seconds)

[](#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema))

##### Returns Expand Collapse

FileObject object { id , bytes , created_at , 6 more }

The `File` object represents a document that has been uploaded to OpenAI.

id : string

The file identifier, which can be referenced in the API endpoints.

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20id)

bytes : number

The size of the file, in bytes.

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20bytes)

created_at : number

The Unix timestamp (in seconds) for when the file was created.

format unixtime

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20created_at)

filename : string

The name of the file.

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20filename)

object : "file"

The object type, which is always `file`.

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20object)

purpose : "assistants" or "assistants_output" or "batch" or 5 more

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

"assistants"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%200)

"assistants_output"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%201)

"batch"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%202)

"batch_output"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%203)

"fine-tune"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%204)

"fine-tune-results"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%205)

"vision"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%206)

"user_data"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%207)

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose)

Deprecated status : "uploaded" or "processed" or "error"

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

"uploaded"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"processed"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"error"

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status)

expires_at : optional number

The Unix timestamp (in seconds) for when the file will expire.

format unixtime

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20expires_at)

Deprecated status_details : optional string

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status_details)

[](#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))

### Upload file

```
curl https://api.openai.com/v1/files \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-F purpose="fine-tune" \
-F file="@mydata.jsonl"
-F expires_after[anchor]="created_at"
-F expires_after[seconds]=2592000
```

```
{
"id": "file-abc123",
"object": "file",
"bytes": 120000,
"created_at": 1677610602,
"expires_at": 1677614202,
"filename": "mydata.jsonl",
"purpose": "fine-tune",
}
```

##### Returns Examples

```
{
"id": "file-abc123",
"object": "file",
"bytes": 120000,
"created_at": 1677610602,
"expires_at": 1677614202,
"filename": "mydata.jsonl",
"purpose": "fine-tune",
}
```

---
Source: https://developers.openai.com/api/reference/resources/files/methods/create
