---
source_url: https://developers.openai.com/api/reference/resources/uploads/methods/create
title: "Create upload"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create upload

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Uploads](/api/reference/resources/uploads)

# Create upload

POST /uploads

Creates an intermediate [Upload](/docs/api-reference/uploads/object) object
that you can add [Parts](/docs/api-reference/uploads/part-object) to.
Currently, an Upload can accept at most 8 GB in total and expires after an
hour after you create it.

Once you complete the Upload, we will create a
[File](/docs/api-reference/files/object) object that contains all the parts
you uploaded. This File is usable in the rest of our platform as a regular
File object.

For certain `purpose` values, the correct `mime_type` must be specified.
Please refer to documentation for the
[supported MIME types for your use case](/docs/assistants/tools/file-search#supported-files).

For guidance on the proper filename extensions for each purpose, please
follow the documentation on [creating a
File](/docs/api-reference/files/create).

Returns the Upload object with status `pending`.

##### Body Parameters JSON Expand Collapse

bytes : number

The number of bytes in the file you are uploading.

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20bytes%20%3E%20(schema))

filename : string

The name of the file to upload.

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20filename%20%3E%20(schema))

mime_type : string

The MIME type of the file.

This must fall within the supported MIME types for your file purpose. See
the supported MIME types for assistants and vision.

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20mime_type%20%3E%20(schema))

purpose : "assistants" or "batch" or "fine-tune" or "vision"

The intended purpose of the uploaded file.

See the [documentation on File
purposes](/docs/api-reference/files/create#files-create-purpose).

One of the following:

"assistants"

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%200)

"batch"

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%201)

"fine-tune"

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%202)

"vision"

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema)%20%3E%20(member)%203)

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20purpose%20%3E%20(schema))

expires_after : optional object { anchor , seconds }

The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

anchor : "created_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20anchor)

seconds : number

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

format int64

minimum 3600

maximum 2592000

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20seconds)

[](#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema))

##### Returns Expand Collapse

Upload object { id , bytes , created_at , 6 more }

The Upload object can accept byte chunks in the form of Parts.

id : string

The Upload unique identifier, which can be referenced in API endpoints.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20id)

bytes : number

The intended number of bytes to be uploaded.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20bytes)

created_at : number

The Unix timestamp (in seconds) for when the Upload was created.

format unixtime

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20created_at)

expires_at : number

The Unix timestamp (in seconds) for when the Upload will expire.

format unixtime

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20expires_at)

filename : string

The name of the file to be uploaded.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20filename)

purpose : string

The intended purpose of the file. [Please refer here](/docs/api-reference/files/object#files/object-purpose) for acceptable values.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20purpose)

status : "pending" or "completed" or "cancelled" or "expired"

The status of the Upload.

One of the following:

"pending"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"completed"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"cancelled"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"expired"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20status)

file : optional [FileObject](/api/reference/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id , bytes , created_at , 6 more }

The `File` object represents a document that has been uploaded to OpenAI.

id : string

The file identifier, which can be referenced in the API endpoints.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20id)

bytes : number

The size of the file, in bytes.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20bytes)

created_at : number

The Unix timestamp (in seconds) for when the file was created.

format unixtime

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20created_at)

filename : string

The name of the file.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20filename)

object : "file"

The object type, which is always `file`.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20object)

purpose : "assistants" or "assistants_output" or "batch" or 5 more

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

"assistants"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%200)

"assistants_output"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%201)

"batch"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%202)

"batch_output"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%203)

"fine-tune"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%204)

"fine-tune-results"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%205)

"vision"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%206)

"user_data"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose%20%3E%20(member)%207)

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20purpose)

Deprecated status : "uploaded" or "processed" or "error"

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

"uploaded"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"processed"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"error"

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status)

expires_at : optional number

The Unix timestamp (in seconds) for when the file will expire.

format unixtime

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20expires_at)

Deprecated status_details : optional string

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file%20%2B%20(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)%20%3E%20(property)%20status_details)

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20file)

object : optional "upload"

The object type, which is always “upload”.

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema))

### Create upload

```
curl https://api.openai.com/v1/uploads \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
"purpose": "fine-tune",
"filename": "training_examples.jsonl",
"bytes": 2147483648,
"mime_type": "text/jsonl",
"expires_after": {
"anchor": "created_at",
"seconds": 3600
}
}'
```

```
{
"id": "upload_abc123",
"object": "upload",
"bytes": 2147483648,
"created_at": 1719184911,
"filename": "training_examples.jsonl",
"purpose": "fine-tune",
"status": "pending",
"expires_at": 1719127296
}
```

##### Returns Examples

```
{
"id": "upload_abc123",
"object": "upload",
"bytes": 2147483648,
"created_at": 1719184911,
"filename": "training_examples.jsonl",
"purpose": "fine-tune",
"status": "pending",
"expires_at": 1719127296
}
```

---
Source: https://developers.openai.com/api/reference/resources/uploads/methods/create
