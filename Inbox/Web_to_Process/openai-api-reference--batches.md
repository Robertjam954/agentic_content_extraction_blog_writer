---
source_url: https://developers.openai.com/api/reference/resources/batches
title: "Batches"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Batches

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Batches

Create large batches of API requests to run asynchronously.

##### [Create batch](/api/reference/resources/batches/methods/create)

POST /batches

##### [Retrieve batch](/api/reference/resources/batches/methods/retrieve)

GET /batches/{batch_id}

##### [Cancel batch](/api/reference/resources/batches/methods/cancel)

POST /batches/{batch_id}/cancel

##### [List batches](/api/reference/resources/batches/methods/list)

GET /batches

##### Models Expand Collapse

Batch object { id , completion_window , created_at , 19 more }

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

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20request_counts)

usage : optional [BatchUsage](/api/reference/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)) { input_tokens , input_tokens_details , output_tokens , 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema))

BatchError object { code , line , message , param }

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

[](#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema))

BatchRequestCounts object { completed , failed , total }

The request counts for different statuses within the batch.

completed : number

Number of requests that have been completed successfully.

[](#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)%20%3E%20(property)%20completed)

failed : number

Number of requests that have failed.

[](#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)%20%3E%20(property)%20failed)

total : number

Total number of requests in the batch.

[](#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)%20%3E%20(property)%20total)

[](#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema))

BatchUsage object { input_tokens , input_tokens_details , output_tokens , 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input_tokens : number

The number of input tokens.

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20input_tokens)

input_tokens_details : object { cached_tokens }

A detailed breakdown of the input tokens.

cached_tokens : number

The number of tokens that were retrieved from the cache. [More on
prompt caching](/docs/guides/prompt-caching).

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20input_tokens_details%20%3E%20(property)%20cached_tokens)

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20input_tokens_details)

output_tokens : number

The number of output tokens.

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20output_tokens)

output_tokens_details : object { reasoning_tokens }

A detailed breakdown of the output tokens.

reasoning_tokens : number

The number of reasoning tokens.

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20output_tokens_details%20%3E%20(property)%20reasoning_tokens)

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20output_tokens_details)

total_tokens : number

The total number of tokens used.

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)%20%3E%20(property)%20total_tokens)

[](#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/batches
