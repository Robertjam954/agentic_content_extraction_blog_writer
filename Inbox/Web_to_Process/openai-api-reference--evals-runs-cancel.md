---
source_url: https://developers.openai.com/api/reference/resources/evals/subresources/runs/methods/cancel
title: "Cancel eval run"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Cancel eval run

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Evals](/api/reference/resources/evals)

[Runs](/api/reference/resources/evals/subresources/runs)

# Cancel eval run

POST /evals/{eval_id}/runs/{run_id}

Cancel an ongoing evaluation run.

##### P ath Parameters Expand Collapse

eval_id : string

[](#(resource)%20evals.runs%20%3E%20(method)%20cancel%20%3E%20(params)%20default%20%3E%20(param)%20eval_id%20%3E%20(schema))

run_id : string

[](#(resource)%20evals.runs%20%3E%20(method)%20cancel%20%3E%20(params)%20default%20%3E%20(param)%20run_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Unique identifier for the evaluation run.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the evaluation run was created.

format unixtime

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

data_source : [CreateEvalJSONLRunDataSource](/api/reference/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source , type } or [CreateEvalCompletionsRunDataSource](/api/reference/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source , type , input_messages , 2 more } or object { source , type , input_messages , 2 more }

Information about the run’s data source.

One of the following:

CreateEvalJSONLRunDataSource object { source , type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source : object { content , type } or object { id , type }

Determines what populates the `item` namespace in the data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source)

type : "jsonl"

The type of data source. Always `jsonl`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema))

CreateEvalCompletionsRunDataSource object { source , type , input_messages , 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source : object { content , type } or object { id , type } or object { type , created_after , created_before , 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201)

StoredCompletionsRunDataSource object { type , created_after , created_before , 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type : "stored_completions"

The type of source. Always `stored_completions`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type)

created_after : optional number

An optional Unix timestamp to filter items created after this time.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_after)

created_before : optional number

An optional Unix timestamp to filter items created before this time.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_before)

limit : optional number

An optional maximum number of items to return.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20limit)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20metadata)

model : optional string

An optional model to filter by (e.g., ‘gpt-4o’).

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20model)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source)

type : "completions"

The type of run data source. Always `completions`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20type)

input_messages : optional object { template , type } or object { item_reference , type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

TemplateInputMessages object { template , type }

template : array of [EasyInputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content , role , phase , type } or object { content , role , type }

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage object { content , role , phase , type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content : string or [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , , }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputMessageContentList = array of [ResponseInputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

One of the following:

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

ResponseInputImage object { detail , type , file_id , 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

detail : "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"high"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"auto"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

"original"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%203)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail)

type : "input_image"

The type of the input item. Always `input_image`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20type)

file_id : optional string

The ID of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20file_id)

image_url : optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

format uri

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema))

ResponseInputFile object { type , detail , file_data , 4 more }

A file input to the model.

type : "input_file"

The type of the input item. Always `input_file`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20type)

detail : optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

One of the following:

"auto"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail)

file_data : optional string

The content of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_data)

file_id : optional string

The ID of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_id)

file_url : optional string

The URL of the file to be sent to the model.

format uri

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_url)

filename : optional string

The name of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20filename)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role)

phase : optional "commentary" or "final_answer"

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase%20%3E%20(member)%200)

"final_answer"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema))

EvalMessageObject object { content , role , type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template)

type : "template"

The type of input messages. Always `template`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200)

ItemReferenceInputMessages object { item_reference , type }

item_reference : string

A reference to a variable in the `item` namespace. Ie, “item.input_trajectory”

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20item_reference)

type : "item_reference"

The type of input messages. Always `item_reference`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages)

model : optional string

The name of the model to use for generating completions (e.g. “o3-mini”).

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20model)

sampling_params : optional object { max_completion_tokens , reasoning_effort , response_format , 4 more }

max_completion_tokens : optional number

The maximum number of tokens in the generated output.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completion_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

One of the following:

"none"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"minimal"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"medium"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"high"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

"xhigh"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%205)

"max"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%206)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

response_format : optional [ResponseFormatText](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type } or [ResponseFormatJSONSchema](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json_schema , type } or [ResponseFormatJSONObject](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONSchema object { json_schema , type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json_schema : object { name , description , schema , strict }

Structured Outputs configuration options, including a JSON Schema.

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20name)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20description)

schema : optional map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20schema)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20strict)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20response_format)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

tools : optional array of [ChatCompletionFunctionTool](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function , type }

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function : [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name , description , parameters , strict }

name : string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20name)

description : optional string

A description of what the function does, used by the model to choose when and how to call the function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20description)

parameters : optional [FunctionParameters](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20parameters)

strict : optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](/docs/guides/function-calling).

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20strict)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema))

ResponsesRunDataSource object { source , type , input_messages , 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source : object { content , type } or object { id , type } or object { type , created_after , created_before , 8 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%201)

EvalResponsesSource object { type , created_after , created_before , 8 more }

A EvalResponsesSource object describing a run data source configuration.

type : "responses"

The type of run data source. Always `responses`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type)

created_after : optional number

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum 0

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_after)

created_before : optional number

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum 0

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_before)

instructions_search : optional string

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20instructions_search)

metadata : optional unknown

Metadata filter for the responses. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20metadata)

model : optional string

The name of the model to find responses for. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20model)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

One of the following:

"none"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"minimal"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"medium"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"high"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

"xhigh"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%205)

"max"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%206)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort)

temperature : optional number

Sampling temperature. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20temperature)

tools : optional array of string

List of tool names. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20tools)

top_p : optional number

Nucleus sampling parameter. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20top_p)

users : optional array of string

List of user identifiers. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20users)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source)

type : "responses"

The type of run data source. Always `responses`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20type)

input_messages : optional object { template , type } or object { item_reference , type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

InputMessagesTemplate object { template , type }

template : array of object { content , role } or object { content , role , type }

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

ChatMessage object { content , role }

content : string

The content of the message.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20content)

role : string

The role of the message (e.g. “system”, “assistant”, “user”).

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20role)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%200)

EvalMessageObject object { content , role , type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template)

type : "template"

The type of input messages. Always `template`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200)

InputMessagesItemReference object { item_reference , type }

item_reference : string

A reference to a variable in the `item` namespace. Ie, “item.name”

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20item_reference)

type : "item_reference"

The type of input messages. Always `item_reference`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages)

model : optional string

The name of the model to use for generating completions (e.g. “o3-mini”).

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20model)

sampling_params : optional object { max_completion_tokens , reasoning_effort , seed , 4 more }

max_completion_tokens : optional number

The maximum number of tokens in the generated output.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completion_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

One of the following:

"none"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"minimal"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"medium"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"high"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

"xhigh"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%205)

"max"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%206)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

text : optional object { format }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

- [Text inputs and outputs](/docs/guides/text)

- [Structured Outputs](/docs/guides/structured-outputs)

format : optional [ResponseFormatTextConfig](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatTextJSONSchemaConfig object { name , schema , type , 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20responses%20%3E%20(model)%20response_format_text_json_schema_config%20%3E%20(schema)%20%3E%20(property)%20name)

schema : map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20responses%20%3E%20(model)%20response_format_text_json_schema_config%20%3E%20(schema)%20%3E%20(property)%20schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20responses%20%3E%20(model)%20response_format_text_json_schema_config%20%3E%20(schema)%20%3E%20(property)%20type)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20responses%20%3E%20(model)%20response_format_text_json_schema_config%20%3E%20(schema)%20%3E%20(property)%20description)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20responses%20%3E%20(model)%20response_format_text_json_schema_config%20%3E%20(schema)%20%3E%20(property)%20strict)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20responses%20%3E%20(model)%20response_format_text_json_schema_config%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text%20%3E%20(property)%20format)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20text)

tools : optional array of object { name , parameters , strict , 5 more } or object { type , vector_store_ids , filters , 2 more } or object { type } or 13 more

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

- **Built-in tools**: Tools that are provided by OpenAI that extend the
model’s capabilities, like [web search](/docs/guides/tools-web-search)
or [file search](/docs/guides/tools-file-search). Learn more about
[built-in tools](/docs/guides/tools).

- **Function calls (custom tools)**: Functions that are defined by you,
enabling the model to call your own code. Learn more about
[function calling](/docs/guides/function-calling).

One of the following:

Function object { name , parameters , strict , 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name : string

The name of the function to call.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name)

parameters : map [ unknown ]

A JSON schema object describing the parameters of the function.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20parameters)

strict : boolean

Whether strict parameter validation is enforced for this function tool.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20strict)

type : "function"

The type of the function tool. Always `function`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20allowed_callers)

defer_loading : optional boolean

Whether this function is deferred and loaded via tool search.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20defer_loading)

description : optional string

A description of the function. Used by the model to determine whether or not to call the function.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20description)

output_schema : optional map [ unknown ]

A JSON schema object describing the JSON value encoded in string outputs for this function.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_schema)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200)

FileSearch object { type , vector_store_ids , filters , 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type : "file_search"

The type of the file search tool. Always `file_search`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

vector_store_ids : array of string

The IDs of the vector stores to search.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20vector_store_ids)

filters : optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key , type , value } or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters , type }

A filter to apply.

One of the following:

ComparisonFilter object { key , type , value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key : string

The key to compare against the value.

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20key)

type : "eq" or "ne" or "gt" or 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

- `eq`: equals

- `ne`: not equal

- `gt`: greater than

- `gte`: greater than or equal

- `lt`: less than

- `lte`: less than or equal

- `in`: in

- `nin`: not in

One of the following:

"eq"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"ne"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"gt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

"gte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203)

"lt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204)

"lte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205)

"in"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206)

"nin"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type)

value : string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%201)

boolean

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%202)

array of string or number

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

CompoundFilter object { filters , type }

Combine multiple filters using `and` or `or`.

filters : array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key , type , value } or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

ComparisonFilter object { key , type , value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key : string

The key to compare against the value.

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20key)

type : "eq" or "ne" or "gt" or 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

- `eq`: equals

- `ne`: not equal

- `gt`: greater than

- `gte`: greater than or equal

- `lt`: less than

- `lte`: less than or equal

- `in`: in

- `nin`: not in

One of the following:

"eq"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"ne"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"gt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

"gte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203)

"lt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204)

"lte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205)

"in"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206)

"nin"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type)

value : string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%201)

boolean

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%202)

array of string or number

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

unknown

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20filters)

type : "and" or "or"

Type of operation: `and` or `or`.

One of the following:

"and"

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"or"

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20filters)

max_num_results : optional number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20max_num_results)

ranking_options : optional object { hybrid_search , ranker , score_threshold }

Ranking options for search.

hybrid_search : optional object { embedding_weight , text_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding_weight : number

The weight of the embedding in the reciprocal ranking fusion.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options%20%3E%20(property)%20hybrid_search%20%3E%20(property)%20embedding_weight)

text_weight : number

The weight of the text in the reciprocal ranking fusion.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options%20%3E%20(property)%20hybrid_search%20%3E%20(property)%20text_weight)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options%20%3E%20(property)%20hybrid_search)

ranker : optional "auto" or "default-2024-11-15"

The ranker to use for the file search.

One of the following:

"auto"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default-2024-11-15"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

score_threshold : optional number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ranking_options)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201)

Computer object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type : "computer"

The type of the computer tool. Always `computer`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%202)

ComputerUsePreview object { display_height , display_width , environment , type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display_height : number

The height of the computer display.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20display_height)

display_width : number

The width of the computer display.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20display_width)

environment : "windows" or "mac" or "linux" or 2 more

The type of computer environment to control.

One of the following:

"windows"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20environment%20%3E%20(member)%200)

"mac"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20environment%20%3E%20(member)%201)

"linux"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20environment%20%3E%20(member)%202)

"ubuntu"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20environment%20%3E%20(member)%203)

"browser"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20environment%20%3E%20(member)%204)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20environment)

type : "computer_use_preview"

The type of the computer use tool. Always `computer_use_preview`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%203)

WebSearch object { type , filters , search_context_size , user_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](/docs/guides/tools-web-search).

type : "web_search" or "web_search_2025_08_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web_search"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type%20%3E%20(member)%200)

"web_search_2025_08_26"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type)

filters : optional object { allowed_domains }

Filters for the search.

allowed_domains : optional array of string

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20filters%20%3E%20(property)%20allowed_domains)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20filters)

search_context_size : optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20search_context_size%20%3E%20(member)%200)

"medium"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20search_context_size%20%3E%20(member)%201)

"high"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20search_context_size%20%3E%20(member)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20search_context_size)

user_location : optional object { city , country , region , 2 more }

The approximate location of the user.

city : optional string

Free text input for the city of the user, e.g. `San Francisco`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_location%20%3E%20(property)%20city)

country : optional string

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_location%20%3E%20(property)%20country)

region : optional string

Free text input for the region of the user, e.g. `California`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_location%20%3E%20(property)%20region)

timezone : optional string

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_location%20%3E%20(property)%20timezone)

type : optional "approximate"

The type of location approximation. Always `approximate`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_location%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_location)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%204)

Mcp object { server_label , type , allowed_callers , 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server_label : string

A label for this MCP server, used to identify it in tool calls.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20server_label)

type : "mcp"

The type of the MCP tool. Always `mcp`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_callers)

allowed_tools : optional array of string or object { read_only , tool_names }

List of allowed tool names or a filter object.

One of the following:

McpAllowedTools = array of string

A string array of allowed tool names

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_tools%20%3E%20(variant)%200)

McpToolFilter object { read_only , tool_names }

A filter object to specify which tools are allowed.

read_only : optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with readOnlyHint](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_tools%20%3E%20(variant)%201%20%3E%20(property)%20read_only)

tool_names : optional array of string

List of allowed tool names.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_tools%20%3E%20(variant)%201%20%3E%20(property)%20tool_names)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_tools%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20allowed_tools)

authorization : optional string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20authorization)

connector_id : optional "connector_dropbox" or "connector_gmail" or "connector_googlecalendar" or 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

- Dropbox: `connector_dropbox`

- Gmail: `connector_gmail`

- Google Calendar: `connector_googlecalendar`

- Google Drive: `connector_googledrive`

- Microsoft Teams: `connector_microsoftteams`

- Outlook Calendar: `connector_outlookcalendar`

- Outlook Email: `connector_outlookemail`

- SharePoint: `connector_sharepoint`

One of the following:

"connector_dropbox"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%200)

"connector_gmail"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%201)

"connector_googlecalendar"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%202)

"connector_googledrive"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%203)

"connector_microsoftteams"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%204)

"connector_outlookcalendar"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%205)

"connector_outlookemail"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%206)

"connector_sharepoint"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id%20%3E%20(member)%207)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20connector_id)

defer_loading : optional boolean

Whether this MCP tool is deferred and discovered via tool search.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20defer_loading)

headers : optional map [ string ]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20headers)

require_approval : optional object { always , never } or "always" or "never"

Specify which of the MCP server’s tools require approval.

One of the following:

McpToolApprovalFilter object { always , never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always : optional object { read_only , tool_names }

A filter object to specify which tools are allowed.

read_only : optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with readOnlyHint](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%200%20%3E%20(property)%20always%20%3E%20(property)%20read_only)

tool_names : optional array of string

List of allowed tool names.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%200%20%3E%20(property)%20always%20%3E%20(property)%20tool_names)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%200%20%3E%20(property)%20always)

never : optional object { read_only , tool_names }

A filter object to specify which tools are allowed.

read_only : optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with readOnlyHint](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%200%20%3E%20(property)%20never%20%3E%20(property)%20read_only)

tool_names : optional array of string

List of allowed tool names.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%200%20%3E%20(property)%20never%20%3E%20(property)%20tool_names)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%200%20%3E%20(property)%20never)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%200)

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

"always"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%201%20%3E%20(member)%200)

"never"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%201%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20require_approval)

server_description : optional string

Optional description of the MCP server, used to provide more context.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20server_description)

server_url : optional string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

format uri

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20server_url)

tunnel_id : optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20tunnel_id)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%205)

CodeInterpreter object { container , type , allowed_callers }

A tool that runs Python code to help generate a response to a prompt.

container : string or object { type , file_ids , memory_limit , network_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

The container ID.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%200)

CodeInterpreterToolAuto object { type , file_ids , memory_limit , network_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type : "auto"

Always `auto`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20type)

file_ids : optional array of string

An optional list of uploaded files to make available to your code.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20file_ids)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit for the code interpreter container.

One of the following:

"1g"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20memory_limit)

network_policy : optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type } or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed_domains , type , domain_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled object { type }

type : "disabled"

Disable outbound network access. Always `disabled`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema))

ContainerNetworkPolicyAllowlist object { allowed_domains , type , domain_secrets }

allowed_domains : array of string

A list of allowed domains when type is `allowlist`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20allowed_domains)

type : "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20type)

domain_secrets : optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain , name , value }

Optional domain-scoped secrets for allowlisted domains.

domain : string

The domain associated with the secret.

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20domain)

name : string

The name of the secret to inject for the domain.

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20name)

value : string

The secret value to inject for the domain.

maxLength 10485760

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20domain_secrets)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201%20%3E%20(property)%20network_policy)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20container)

type : "code_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20allowed_callers)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%206)

ProgrammaticToolCalling object { type }

type : "programmatic_tool_calling"

The type of the tool. Always `programmatic_tool_calling`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%207)

ImageGeneration object { type , action , background , 9 more }

A tool that generates images using the GPT image models.

type : "image_generation"

The type of the image generation tool. Always `image_generation`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20type)

action : optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20action%20%3E%20(member)%200)

"edit"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20action%20%3E%20(member)%201)

"auto"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20action%20%3E%20(member)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20action)

background : optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

One of the following:

"transparent"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20background%20%3E%20(member)%200)

"opaque"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20background%20%3E%20(member)%201)

"auto"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20background%20%3E%20(member)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20background)

input_fidelity : optional "high" or "low"

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20input_fidelity%20%3E%20(member)%200)

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20input_fidelity%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20input_fidelity)

input_image_mask : optional object { file_id , image_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file_id : optional string

File ID for the mask image.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20input_image_mask%20%3E%20(property)%20file_id)

image_url : optional string

Base64-encoded mask image.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20input_image_mask%20%3E%20(property)%20image_url)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20input_image_mask)

model : optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

The image generation model to use. Default: `gpt-image-1`.

One of the following:

string

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20model%20%3E%20(variant)%200)

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

The image generation model to use. Default: `gpt-image-1`.

One of the following:

"gpt-image-1"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%200)

"gpt-image-1-mini"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%201)

"gpt-image-1.5"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20model%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20model)

moderation : optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20moderation%20%3E%20(member)%200)

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20moderation%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20moderation)

output_compression : optional number

Compression level for the output image. Default: 100.

minimum 0

maximum 100

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20output_compression)

output_format : optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20output_format%20%3E%20(member)%200)

"webp"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20output_format%20%3E%20(member)%201)

"jpeg"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20output_format%20%3E%20(member)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20output_format)

partial_images : optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum 0

maximum 3

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20partial_images)

quality : optional "low" or "medium" or "high" or "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20quality%20%3E%20(member)%200)

"medium"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20quality%20%3E%20(member)%201)

"high"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20quality%20%3E%20(member)%202)

"auto"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20quality%20%3E%20(member)%203)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20quality)

size : optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20size%20%3E%20(variant)%200)

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

"1024x1024"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20size%20%3E%20(variant)%201%20%3E%20(member)%200)

"1024x1536"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20size%20%3E%20(variant)%201%20%3E%20(member)%201)

"1536x1024"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20size%20%3E%20(variant)%201%20%3E%20(member)%202)

"auto"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20size%20%3E%20(variant)%201%20%3E%20(member)%203)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20size%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20size)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%208)

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type : "local_shell"

The type of the local shell tool. Always `local_shell`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%209)

Shell object { type , allowed_callers , environment }

A tool that allows the model to execute shell commands.

type : "shell"

The type of the shell tool. Always `shell`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20allowed_callers)

environment : optional [ContainerAuto](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type , file_ids , memory_limit , 2 more } or [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type , skills } or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container_id , type }

One of the following:

ContainerAuto object { type , file_ids , memory_limit , 2 more }

type : "container_auto"

Automatically creates a container for this request

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20type)

file_ids : optional array of string

An optional list of uploaded files to make available to your code.

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20file_ids)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit for the container.

One of the following:

"1g"

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20memory_limit)

network_policy : optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type } or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed_domains , type , domain_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled object { type }

type : "disabled"

Disable outbound network access. Always `disabled`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema))

ContainerNetworkPolicyAllowlist object { allowed_domains , type , domain_secrets }

allowed_domains : array of string

A list of allowed domains when type is `allowlist`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20allowed_domains)

type : "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20type)

domain_secrets : optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain , name , value }

Optional domain-scoped secrets for allowlisted domains.

domain : string

The domain associated with the secret.

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20domain)

name : string

The name of the secret to inject for the domain.

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20name)

value : string

The secret value to inject for the domain.

maxLength 10485760

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20domain_secrets)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20network_policy)

skills : optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill_id , type , version } or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description , name , source , type }

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference object { skill_id , type , version }

skill_id : string

The ID of the referenced skill.

maxLength 64

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)%20%3E%20(property)%20skill_id)

type : "skill_reference"

References a skill created with the /v1/skills endpoint.

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)%20%3E%20(property)%20type)

version : optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)%20%3E%20(property)%20version)

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema))

InlineSkill object { description , name , source , type }

description : string

The description of the skill.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20description)

name : string

The name of the skill.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20name)

source : [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data , media_type , type }

Inline skill payload

data : string

Base64-encoded skill zip bundle.

maxLength 70254592

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source%20%2B%20(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)%20%3E%20(property)%20data)

media_type : "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source%20%2B%20(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)%20%3E%20(property)%20media_type)

type : "base64"

The type of the inline skill source. Must be `base64`.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source%20%2B%20(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source)

type : "inline"

Defines an inline skill for this request.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)%20%3E%20(property)%20skills)

[](#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema))

LocalEnvironment object { type , skills }

type : "local"

Use a local computer environment.

[](#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)%20%3E%20(property)%20type)

skills : optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description , name , path }

An optional list of skills.

description : string

The description of the skill.

[](#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)%20%3E%20(property)%20description)

name : string

The name of the skill.

[](#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)%20%3E%20(property)%20name)

path : string

The path to the directory containing the skill.

[](#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)%20%3E%20(property)%20path)

[](#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)%20%3E%20(property)%20skills)

[](#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema))

ContainerReference object { container_id , type }

container_id : string

The ID of the referenced container.

[](#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)%20%3E%20(property)%20container_id)

type : "container_reference"

References a container created with the /v1/containers endpoint

[](#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20environment)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2010)

Custom object { name , type , allowed_callers , 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name : string

The name of the custom tool, used to identify it in tool calls.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20name)

type : "custom"

The type of the custom tool. Always `custom`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20allowed_callers)

defer_loading : optional boolean

Whether this tool should be deferred and discovered via tool search.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20defer_loading)

description : optional string

Optional description of the custom tool, used to provide more context.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20description)

format : optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

Text object { type }

Unconstrained free-form text.

type : "text"

Unconstrained text format. Always `text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%200)

Grammar object { definition , syntax , type }

A grammar defined by the user.

definition : string

The grammar definition.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20definition)

syntax : "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20syntax%20%3E%20(member)%200)

"regex"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20syntax%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20syntax)

type : "grammar"

Grammar format. Always `grammar`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20format)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2011)

Namespace object { description , name , tools , type }

Groups function/custom tools under a shared namespace.

description : string

A description of the namespace shown to the model.

minLength 1

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20description)

name : string

The namespace name used in tool calls (for example, `crm`).

minLength 1

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20name)

tools : array of object { name , type , allowed_callers , 5 more } or object { name , type , allowed_callers , 3 more }

The function/custom tools available inside this namespace.

One of the following:

Function object { name , type , allowed_callers , 5 more }

name : string

maxLength 128

minLength 1

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name)

type : "function"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20allowed_callers)

defer_loading : optional boolean

Whether this function should be deferred and discovered via tool search.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20defer_loading)

description : optional string

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20description)

output_schema : optional map [ unknown ]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_schema)

parameters : optional unknown

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20parameters)

strict : optional boolean

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20strict)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%200)

Custom object { name , type , allowed_callers , 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name : string

The name of the custom tool, used to identify it in tool calls.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name)

type : "custom"

The type of the custom tool. Always `custom`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20allowed_callers)

defer_loading : optional boolean

Whether this tool should be deferred and discovered via tool search.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20defer_loading)

description : optional string

Optional description of the custom tool, used to provide more context.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20description)

format : optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

Text object { type }

Unconstrained free-form text.

type : "text"

Unconstrained text format. Always `text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%200)

Grammar object { definition , syntax , type }

A grammar defined by the user.

definition : string

The grammar definition.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20definition)

syntax : "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20syntax%20%3E%20(member)%200)

"regex"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20syntax%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20syntax)

type : "grammar"

Grammar format. Always `grammar`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20tools)

type : "namespace"

The type of the tool. Always `namespace`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2012)

ToolSearch object { type , description , execution , parameters }

Hosted or BYOT tool search configuration for deferred tools.

type : "tool_search"

The type of the tool. Always `tool_search`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20type)

description : optional string

Description shown to the model for a client-executed tool search tool.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20description)

execution : optional "server" or "client"

Whether tool search is executed by the server or by the client.

One of the following:

"server"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20execution%20%3E%20(member)%200)

"client"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20execution%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20execution)

parameters : optional unknown

Parameter schema for a client-executed tool search tool.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20parameters)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2013)

WebSearchPreview object { type , search_content_types , search_context_size , user_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type : "web_search_preview" or "web_search_preview_2025_03_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web_search_preview"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20type%20%3E%20(member)%200)

"web_search_preview_2025_03_11"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20type)

search_content_types : optional array of "text" or "image"

One of the following:

"text"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20search_content_types%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20search_content_types%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20search_content_types)

search_context_size : optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20search_context_size%20%3E%20(member)%200)

"medium"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20search_context_size%20%3E%20(member)%201)

"high"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20search_context_size%20%3E%20(member)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20search_context_size)

user_location : optional object { type , city , country , 2 more }

The user’s location.

type : "approximate"

The type of location approximation. Always `approximate`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20user_location%20%3E%20(property)%20type)

city : optional string

Free text input for the city of the user, e.g. `San Francisco`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20user_location%20%3E%20(property)%20city)

country : optional string

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20user_location%20%3E%20(property)%20country)

region : optional string

Free text input for the region of the user, e.g. `California`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20user_location%20%3E%20(property)%20region)

timezone : optional string

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20user_location%20%3E%20(property)%20timezone)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20user_location)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2014)

ApplyPatch object { type , allowed_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type : "apply_patch"

The type of the tool. Always `apply_patch`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20type)

allowed_callers : optional array of "direct" or "programmatic"

The tool invocation context(s).

One of the following:

"direct"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%200)

"programmatic"

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20allowed_callers%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20allowed_callers)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%2015)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20sampling_params)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20data_source)

error : [EvalAPIError](/api/reference/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code , message }

An object representing an error response from the Eval API.

code : string

The error code.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)%20%3E%20(property)%20error%20%2B%20(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

The

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/evals/subresources/runs/methods/cancel
