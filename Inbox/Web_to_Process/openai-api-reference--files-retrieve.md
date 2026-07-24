---
source_url: https://developers.openai.com/api/reference/resources/files/methods/retrieve
title: "Retrieve file"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve file

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Files](/api/reference/resources/files)

# Retrieve file

GET /files/{file_id}

Returns information about a specific file.

##### P ath Parameters Expand Collapse

file_id : string

[](#(resource)%20files%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20file_id%20%3E%20(schema))

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

### Retrieve file

```
curl https://api.openai.com/v1/files/file-abc123 \
-H "Authorization: Bearer $OPENAI_API_KEY"
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
Source: https://developers.openai.com/api/reference/resources/files/methods/retrieve
