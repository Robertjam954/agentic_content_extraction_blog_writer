---
source_url: https://developers.openai.com/api/reference/resources/batches/methods/list
title: "List batches"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List batches

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Batches](/api/reference/resources/batches)

# List batches

GET /batches

List your organization’s batches.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20batches%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20batches%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [Batch](/api/reference/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)) { id , completion_window , created_at , 19 more }

id : string

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20id)

completion_window : string

The time frame within which the batch should be processed.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20completion_window)

created_at : number

The Unix timestamp (in seconds) for when the batch was created.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20created_at)

endpoint : string

The OpenAI API endpoint used by the batch.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20endpoint)

input_file_id : string

The ID of the input file for the batch.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20input_file_id)

object : "batch"

The object type, which is always `batch`.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20object)

status : "validating" or "failed" or "in_progress" or 5 more

The current status of the batch.

One of the following:

"validating"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"failed"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"finalizing"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

"completed"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204)

"expired"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205)

"cancelling"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206)

"cancelled"

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20status)

cancelled_at : optional number

The Unix timestamp (in seconds) for when the batch was cancelled.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20cancelled_at)

cancelling_at : optional number

The Unix timestamp (in seconds) for when the batch started cancelling.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20cancelling_at)

completed_at : optional number

The Unix timestamp (in seconds) for when the batch was completed.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20completed_at)

error_file_id : optional string

The ID of the file containing the outputs of requests with errors.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20error_file_id)

errors : optional object { data , object }

data : optional array of [BatchError](/api/reference/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)) { code , line , message , param }

code : optional string

An error code identifying the error type.

[](#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)%20%3E%20(property)%20code)

line : optional number

The line number of the input file where the error occurred, if applicable.

[](#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)%20%3E%20(property)%20line)

message : optional string

A human-readable message providing more details about the error.

[](#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)%20%3E%20(property)%20message)

param : optional string

The name of the parameter that caused the error, if applicable.

[](#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)%20%3E%20(property)%20param)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(property)%20data)

object : optional string

The object type, which is always `list`.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(property)%20object)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20errors)

expired_at : optional number

The Unix timestamp (in seconds) for when the batch expired.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20expired_at)

expires_at : optional number

The Unix timestamp (in seconds) for when the batch will expire.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20expires_at)

failed_at : optional number

The Unix timestamp (in seconds) for when the batch failed.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20failed_at)

finalizing_at : optional number

The Unix timestamp (in seconds) for when the batch started finalizing.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20finalizing_at)

in_progress_at : optional number

The Unix timestamp (in seconds) for when the batch started processing.

format unixtime

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20in_progress_at)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20metadata)

model : optional string

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](/docs/models) to browse and compare available models.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20model)

output_file_id : optional string

The ID of the file containing the outputs of successfully executed requests.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20output_file_id)

request_counts : optional [BatchRequestCounts](/api/reference/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)) { completed , failed , total }

The request counts for different statuses within the batch.

completed : number

Number of requests that have been completed successfully.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20request_counts%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)%20%3E%20(property)%20completed)

failed : number

Number of requests that have failed.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20request_counts%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)%20%3E%20(property)%20failed)

total : number

Total number of requests in the batch.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20request_counts%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)%20%3E%20(property)%20total)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20request_counts)

usage : optional [BatchUsage](/api/reference/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)) { input_tokens , input_tokens_details , output_tokens , 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input_tokens : number

The number of input tokens.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20input_tokens)

input_tokens_details : object { cached_tokens }

A detailed breakdown of the input tokens.

cached_tokens : number

The number of tokens that were retrieved from the cache. [More on
prompt caching](/docs/guides/prompt-caching).

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20input_tokens_details%20%3E%20(property)%20cached_tokens)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20input_tokens_details)

output_tokens : number

The number of output tokens.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20output_tokens)

output_tokens_details : object { reasoning_tokens }

A detailed breakdown of the output tokens.

reasoning_tokens : number

The number of reasoning tokens.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20output_tokens_details%20%3E%20(property)%20reasoning_tokens)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20output_tokens_details)

total_tokens : number

The total number of tokens used.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20total_tokens)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20batches%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20batches%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20batches%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20batches%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20batches%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List batches

```
curl https://api.openai.com/v1/batches?limit=2 \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"id": "batch_abc123",
"object": "batch",
"endpoint": "/v1/chat/completions",
"errors": null,
"input_file_id": "file-abc123",
"completion_window": "24h",
"status": "completed",
"output_file_id": "file-cvaTdG",
"error_file_id": "file-HOWS94",
"created_at": 1711471533,
"in_progress_at": 1711471538,
"expires_at": 1711557933,
"finalizing_at": 1711493133,
"completed_at": 1711493163,
"failed_at": null,
"expired_at": null,
"cancelling_at": null,
"cancelled_at": null,
"request_counts": {
"total": 100,
"completed": 95,
"failed": 5
},
"metadata": {
"customer_id": "user_123456789",
"batch_description": "Nightly job",
}
},
{ ... },
],
"first_id": "batch_abc123",
"last_id": "batch_abc456",
"has_more": true
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "batch_abc123",
"object": "batch",
"endpoint": "/v1/chat/completions",
"errors": null,
"input_file_id": "file-abc123",
"completion_window": "24h",
"status": "completed",
"output_file_id": "file-cvaTdG",
"error_file_id": "file-HOWS94",
"created_at": 1711471533,
"in_progress_at": 1711471538,
"expires_at": 1711557933,
"finalizing_at": 1711493133,
"completed_at": 1711493163,
"failed_at": null,
"expired_at": null,
"cancelling_at": null,
"cancelled_at": null,
"request_counts": {
"total": 100,
"completed": 95,
"failed": 5
},
"metadata": {
"customer_id": "user_123456789",
"batch_description": "Nightly job",
}
},
{ ... },
],
"first_id": "batch_abc123",
"last_id": "batch_abc456",
"has_more": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/batches/methods/list
