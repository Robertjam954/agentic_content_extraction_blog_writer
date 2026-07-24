---
source_url: https://developers.openai.com/api/reference/resources/uploads/methods/cancel
title: "Cancel upload"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Cancel upload

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Uploads](/api/reference/resources/uploads)

# Cancel upload

POST /uploads/{upload_id}/cancel

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

##### P ath Parameters Expand Collapse

upload_id : string

[](#(resource)%20uploads%20%3E%20(method)%20cancel%20%3E%20(params)%20default%20%3E%20(param)%20upload_id%20%3E%20(schema))

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

### Cancel upload

```
curl https://api.openai.com/v1/uploads/upload_abc123/cancel
```

```
{
"id": "upload_abc123",
"object": "upload",
"bytes": 2147483648,
"created_at": 1719184911,
"filename": "training_examples.jsonl",
"purpose": "fine-tune",
"status": "cancelled",
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
"status": "cancelled",
"expires_at": 1719127296
}
```

---
Source: https://developers.openai.com/api/reference/resources/uploads/methods/cancel
