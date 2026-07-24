---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads
title: "Threads"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Threads

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

# Threads

Build Assistants that can call models and use tools.

##### [Create thread](/api/reference/resources/beta/subresources/threads/methods/create)

Deprecated

POST /threads

##### [Create thread and run](/api/reference/resources/beta/subresources/threads/methods/create_and_run)

Deprecated

POST /threads/runs

##### [Retrieve thread](/api/reference/resources/beta/subresources/threads/methods/retrieve)

Deprecated

GET /threads/{thread_id}

##### [Modify thread](/api/reference/resources/beta/subresources/threads/methods/update)

Deprecated

POST /threads/{thread_id}

##### [Delete thread](/api/reference/resources/beta/subresources/threads/methods/delete)

Deprecated

DELETE /threads/{thread_id}

##### Models Expand Collapse

AssistantResponseFormatOption = "auto" or [ResponseFormatText](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type } or [ResponseFormatJSONObject](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type } or [ResponseFormatJSONSchema](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json_schema , type }

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

"auto"

`auto` is the default value

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)%20%3E%20(variant)%200)

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

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

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

AssistantToolChoice object { type , function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type : "function" or "code_interpreter" or "file_search"

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"code_interpreter"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"file_search"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

function : optional [AssistantToolChoiceFunction](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema))

AssistantToolChoiceFunction object { name }

name : string

The name of the function to call.

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema))

AssistantToolChoiceOption = "none" or "auto" or "required" or [AssistantToolChoice](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)) { type , function }

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

"none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%200)

"auto"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%201)

"required"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%202)

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200)

AssistantToolChoice object { type , function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type : "function" or "code_interpreter" or "file_search"

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"code_interpreter"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"file_search"

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

function : optional [AssistantToolChoiceFunction](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema))

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Thread object { id , created_at , metadata , 2 more }

Represents a thread that contains [messages](/docs/api-reference/messages).

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the thread was created.

format unixtime

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20created_at)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20metadata)

object : "thread"

The object type, which is always `thread`.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20object)

tool_resources : object { code_interpreter , file_search }

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code_interpreter : optional object { file_ids }

file_ids : optional array of string

A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20file_ids)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20code_interpreter)

file_search : optional object { vector_store_ids }

vector_store_ids : optional array of string

The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_store_ids)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20file_search)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

ThreadDeleted object { id , deleted , object }

id : string

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "thread.deleted"

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema))

#### Threads Runs

Build Assistants that can call models and use tools.

##### [List runs](/api/reference/resources/beta/subresources/threads/subresources/runs/methods/list)

Deprecated

GET /threads/{thread_id}/runs

##### [Create run](/api/reference/resources/beta/subresources/threads/subresources/runs/methods/create)

Deprecated

POST /threads/{thread_id}/runs

##### [Retrieve run](/api/reference/resources/beta/subresources/threads/subresources/runs/methods/retrieve)

Deprecated

GET /threads/{thread_id}/runs/{run_id}

##### [Modify run](/api/reference/resources/beta/subresources/threads/subresources/runs/methods/update)

Deprecated

POST /threads/{thread_id}/runs/{run_id}

##### [Submit tool outputs to run](/api/reference/resources/beta/subresources/threads/subresources/runs/methods/submit_tool_outputs)

Deprecated

POST /threads/{thread_id}/runs/{run_id}/submit_tool_outputs

##### [Cancel a run](/api/reference/resources/beta/subresources/threads/subresources/runs/methods/cancel)

Deprecated

POST /threads/{thread_id}/runs/{run_id}/cancel

##### Models Expand Collapse

RequiredActionFunctionToolCall object { id , function , type }

Tool call objects

id : string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](/docs/api-reference/runs/submitToolOutputs) endpoint.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function definition.

arguments : string

The arguments that the model expects you to pass to the function.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call the output is required for. For now, this is always `function`.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))

Run object { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20id)

assistant_id : string

The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20assistant_id)

cancelled_at : number

The Unix timestamp (in seconds) for when the run was cancelled.

format unixtime

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20cancelled_at)

completed_at : number

The Unix timestamp (in seconds) for when the run was completed.

format unixtime

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20completed_at)

created_at : number

The Unix timestamp (in seconds) for when the run was created.

format unixtime

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20created_at)

expires_at : number

The Unix timestamp (in seconds) for when the run will expire.

format unixtime

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20expires_at)

failed_at : number

The Unix timestamp (in seconds) for when the run failed.

format unixtime

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20failed_at)

incomplete_details : object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason : optional "max_completion_tokens" or "max_prompt_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max_completion_tokens"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason%20%3E%20(member)%200)

"max_prompt_tokens"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20incomplete_details)

instructions : string

The instructions that the [assistant](/docs/api-reference/assistants) used for this run.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20instructions)

last_error : object { code , message }

The last error associated with this run. Will be `null` if there are no errors.

code : "server_error" or "rate_limit_exceeded" or "invalid_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server_error"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%200)

"rate_limit_exceeded"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%201)

"invalid_prompt"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%202)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code)

message : string

A human-readable description of the error.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20message)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20last_error)

max_completion_tokens : number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum 256

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20max_completion_tokens)

max_prompt_tokens : number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum 256

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20max_prompt_tokens)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20metadata)

model : string

The model that the [assistant](/docs/api-reference/assistants) used for this run.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20model)

object : "thread.run"

The object type, which is always `thread.run`.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20object)

parallel_tool_calls : boolean

Whether to enable [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20parallel_tool_calls)

required_action : object { submit_tool_outputs , type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit_tool_outputs : object { tool_calls }

Details on the tool outputs needed for this run to continue.

tool_calls : array of [RequiredActionFunctionToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id , function , type }

A list of the relevant tool calls.

id : string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](/docs/api-reference/runs/submitToolOutputs) endpoint.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function definition.

arguments : string

The arguments that the model expects you to pass to the function.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call the output is required for. For now, this is always `function`.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20required_action%20%3E%20(property)%20submit_tool_outputs%20%3E%20(property)%20tool_calls)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20required_action%20%3E%20(property)%20submit_tool_outputs)

type : "submit_tool_outputs"

For now, this is always `submit_tool_outputs`.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20required_action%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20required_action)

response_format : [AssistantResponseFormatOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format)

started_at : number

The Unix timestamp (in seconds) for when the run was started.

format unixtime

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20started_at)

status : "queued" or "in_progress" or "requires_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

One of the following:

"queued"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"in_progress"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"requires_action"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"cancelling"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

"cancelled"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204)

"failed"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205)

"completed"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206)

"incomplete"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207)

"expired"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%208)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20status)

thread_id : string

The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20thread_id)

tool_choice : [AssistantToolChoiceOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice)

tools : array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type } or [FileSearchTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type , file_search } or [FunctionTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function , type }

The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.

One of the following:

CodeInterpreterTool object { type }

type : "code_interpreter"

The type of tool being defined: `code_interpreter`

[](#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema))

FileSearchTool object { type , file_search }

type : "file_search"

The type of tool being defined: `file_search`

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20type)

file_search : optional object { max_num_results , ranking_options }

Overrides for the file search tool.

max_num_results : optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum 1

maximum 50

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20max_num_results)

ranking_options : optional object { score_threshold , ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score_threshold : number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

ranker : optional "auto" or "default_2024_08_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default_2024_08_21"

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options)

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)%20%3E%20(property)%20file_search)

[](#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema))

FunctionTool object { function , type }

function : [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name , description , parameters , strict }

[](#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool being defined: `function`

[](#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema))

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tools)

truncation_strategy : object { type , last_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type : "auto" or "last_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20truncation_strategy%20%3E%20(property)%20type%20%3E%20(member)%200)

"last_messages"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20truncation_strategy%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20truncation_strategy%20%3E%20(property)%20type)

last_messages : optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum 1

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20truncation_strategy%20%3E%20(property)%20last_messages)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20truncation_strategy)

usage : object { completion_tokens , prompt_tokens , total_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion_tokens : number

Number of completion tokens used over the course of the run.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20completion_tokens)

prompt_tokens : number

Number of prompt tokens used over the course of the run.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20prompt_tokens)

total_tokens : number

Total number of tokens used (prompt + completion).

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20total_tokens)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20usage)

temperature : optional number

The sampling temperature used for this run. If not set, defaults to 1.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20temperature)

top_p : optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20top_p)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

#### Threads Runs Steps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

GET /threads/{thread_id}/runs/{run_id}/steps

##### [Retrieve run step](/api/reference/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

GET /threads/{thread_id}/runs/{run_id}/steps/{step_id}

##### Models Expand Collapse

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

CodeInterpreterToolCall object { id , code_interpreter , type }

Details of the Code Interpreter tool call the run step was involved in.

id : string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : object { input , outputs }

The Code Interpreter tool call definition.

input : string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : array of object { logs , type } or object { image , type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogOutput object { logs , type }

Text output from the Code Interpreter tool call as part of a run step.

logs : string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20logs)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200)

CodeInterpreterImageOutput object { image , type }

image : object { file_id }

file_id : string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema))

CodeInterpreterToolCallDelta object { index , type , id , code_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : optional object { input , outputs }

The Code Interpreter tool call definition.

input : optional string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : optional array of [CodeInterpreterLogs](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index , type , logs } or [CodeInterpreterOutputImage](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index , type , image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema))

FileSearchToolCall object { id , file_search , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

file_search : object { ranking_options , results }

For now, this is always going to be an empty object.

ranking_options : optional object { ranker , score_threshold }

The ranking options for the file search.

ranker : "auto" or "default_2024_08_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default_2024_08_21"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

score_threshold : number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options)

results : optional array of object { file_id , file_name , score , content }

The results of the file search.

file_id : string

The ID of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_id)

file_name : string

The name of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_name)

score : number

The score of the result. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score)

content : optional array of object { text , type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text : optional string

The text content of the file.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "text"

The type of the content.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema))

FileSearchToolCallDelta object { file_search , index , type , id }

file_search : unknown

For now, this is always going to be an empty object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20file_search)

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema))

FunctionToolCall object { id , function , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name , output }

The definition of the function that was called.

arguments : string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema))

FunctionToolCallDelta object { index , type , id , function }

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

function : optional object { arguments , name , output }

The definition of the function that was called.

arguments : optional string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : optional string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : optional string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema))

MessageCreationStepDetails object { message_creation , type }

Details of the message creation by the run step.

message_creation : object { message_id }

message_id : string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation)

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema))

RunStep object { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

id : string

The identifier of the run step, which can be referenced in API endpoints.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20id)

assistant_id : string

The ID of the [assistant](/docs/api-reference/assistants) associated with the run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20assistant_id)

cancelled_at : number

The Unix timestamp (in seconds) for when the run step was cancelled.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20cancelled_at)

completed_at : number

The Unix timestamp (in seconds) for when the run step completed.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20completed_at)

created_at : number

The Unix timestamp (in seconds) for when the run step was created.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20created_at)

expired_at : number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20expired_at)

failed_at : number

The Unix timestamp (in seconds) for when the run step failed.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20failed_at)

last_error : object { code , message }

The last error associated with this run step. Will be `null` if there are no errors.

code : "server_error" or "rate_limit_exceeded"

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server_error"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%200)

"rate_limit_exceeded"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code)

message : string

A human-readable description of the error.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20message)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20metadata)

object : "thread.run.step"

The object type, which is always `thread.run.step`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20object)

run_id : string

The ID of the [run](/docs/api-reference/runs) that this run step is a part of.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20run_id)

status : "in_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in_progress"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"cancelled"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"failed"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"completed"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

"expired"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status)

step_details : [MessageCreationStepDetails](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message_creation , type } or [ToolCallsStepDetails](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool_calls , type }

The details of the run step.

One of the following:

MessageCreationStepDetails object { message_creation , type }

Details of the message creation by the run step.

message_creation : object { message_id }

message_id : string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation)

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema))

ToolCallsStepDetails object { tool_calls , type }

Details of the tool call.

tool_calls : array of [CodeInterpreterToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id , code_interpreter , type } or [FileSearchToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id , file_search , type } or [FunctionToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id , function , type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall object { id , code_interpreter , type }

Details of the Code Interpreter tool call the run step was involved in.

id : string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : object { input , outputs }

The Code Interpreter tool call definition.

input : string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : array of object { logs , type } or object { image , type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogOutput object { logs , type }

Text output from the Code Interpreter tool call as part of a run step.

logs : string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20logs)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200)

CodeInterpreterImageOutput object { image , type }

image : object { file_id }

file_id : string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema))

FileSearchToolCall object { id , file_search , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

file_search : object { ranking_options , results }

For now, this is always going to be an empty object.

ranking_options : optional object { ranker , score_threshold }

The ranking options for the file search.

ranker : "auto" or "default_2024_08_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default_2024_08_21"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

score_threshold : number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options)

results : optional array of object { file_id , file_name , score , content }

The results of the file search.

file_id : string

The ID of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_id)

file_name : string

The name of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_name)

score : number

The score of the result. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score)

content : optional array of object { text , type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text : optional string

The text content of the file.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "text"

The type of the content.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema))

FunctionToolCall object { id , function , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name , output }

The definition of the function that was called.

arguments : string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20step_details)

thread_id : string

The ID of the [thread](/docs/api-reference/threads) that was run.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20thread_id)

type : "message_creation" or "tool_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message_creation"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"tool_calls"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20type)

usage : object { completion_tokens , prompt_tokens , total_tokens }

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion_tokens : number

Number of completion tokens used over the course of the run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20completion_tokens)

prompt_tokens : number

Number of prompt tokens used over the course of the run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20prompt_tokens)

total_tokens : number

Total number of tokens used (prompt + completion).

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20total_tokens)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

RunStepDeltaEvent object { id , delta , object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

id : string

The identifier of the run step, which can be referenced in API endpoints.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20id)

delta : object { step_details }

The delta containing the fields that have changed on the run step.

step_details : optional [RunStepDeltaMessageDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type , message_creation } or [ToolCallDeltaObject](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type , tool_calls }

The details of the run step.

One of the following:

RunStepDeltaMessageDelta object { type , message_creation }

Details of the message creation by the run step.

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20type)

message_creation : optional object { message_id }

message_id : optional string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema))

ToolCallDeltaObject object { type , tool_calls }

Details of the tool call.

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20type)

tool_calls : optional array of [CodeInterpreterToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index , type , id , code_interpreter } or [FileSearchToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file_search , index , type , id } or [FunctionToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index , type , id , function }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta object { index , type , id , code_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : optional object { input , outputs }

The Code Interpreter tool call definition.

input : optional string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : optional array of [CodeInterpreterLogs](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index , type , logs } or [CodeInterpreterOutputImage](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index , type , image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema))

FileSearchToolCallDelta object { file_search , index , type , id }

file_search : unknown

For now, this is always going to be an empty object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20file_search)

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema))

FunctionToolCallDelta object { index , type , id , function }

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

function : optional object { arguments , name , output }

The definition of the function that was called.

arguments : optional string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : optional string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : optional string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta%20%3E%20(property)%20step_details)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta)

object : "thread.run.step.delta"

The object type, which is always `thread.run.step.delta`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

RunStepDeltaMessageDelta object { type , message_creation }

Details of the message creation by the run step.

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20type)

message_creation : optional object { message_id }

message_id : optional string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema))

RunStepInclude = "step_details.tool_calls[*].file_search.results[*].content"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_include%20%3E%20(schema))

ToolCallDeltaObject object { type , tool_calls }

Details of the tool call.

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20type)

tool_calls : optional array of [CodeInterpreterToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index , type , id , code_interpreter } or [FileSearchToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file_search , index , type , id } or [FunctionToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index , type , id , function }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta object { index , type , id , code_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : optional object { input , outputs }

The Code Interpreter tool call definition.

input : optional string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : optional array of [CodeInterpreterLogs](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index , type , logs } or [CodeInterpreterOutputImage](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index , type , image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema))

FileSearchToolCallDelta object { file_search , index , type , id }

file_search : unknown

For now, this is always going to be an empty object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20file_search)

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema))

FunctionToolCallDelta object { index , type , id , function }

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

function : optional object { arguments , name , output }

The definition of the function that was called.

arguments : optional string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : optional string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : optional string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema))

ToolCallsStepDetails object { tool_calls , type }

Details of the tool call.

tool_calls : array of [CodeInterpreterToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id , code_interpreter , type } or [FileSearchToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id , file_search , type } or [FunctionToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id , function , type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall object { id , code_interpreter , type }

Details of the Code Interpreter tool call the run step was involved in.

id : string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : object { input , outputs }

The Code Interpreter tool call definition.

input : string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : array of object { logs , type } or object { image , type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogOutput object { logs , type }

Text output from the Code Interpreter tool call as part of a run step.

logs : string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20logs)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200)

CodeInterpreterImageOutput object { image , type }

image : object { file_id }

file_id : string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema))

FileSearchToolCall object { id , file_search , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

file_search : object { ranking_options , results }

For now, this is always going to be an empty object.

ranking_options : optional object { ranker , score_threshold }

The ranking options for the file search.

ranker : "auto" or "default_2024_08_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default_2024_08_21"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

score_threshold : number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options)

results : optional array of object { file_id , file_name , score , content }

The results of the file search.

file_id : string

The ID of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_id)

file_name : string

The name of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_name)

score : number

The score of the result. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score)

content : optional array of object { text , type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text : optional string

The text content of the file.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "text"

The type of the content.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema))

FunctionToolCall object { id , function , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name , output }

The definition of the function that was called.

arguments : string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema))

#### Threads Messages

Build Assistants that can call models and use tools.

##### [List messages](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/list)

Deprecated

GET /threads/{thread_id}/messages

##### [Create message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/create)

Deprecated

POST /threads/{thread_id}/messages

##### [Modify message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/update)

Deprecated

POST /threads/{thread_id}/messages/{message_id}

##### [Retrieve message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/retrieve)

Deprecated

GET /threads/{thread_id}/messages/{message_id}

##### [Delete message](/api/reference/resources/beta/subresources/threads/subresources/messages/methods/delete)

Deprecated

DELETE /threads/{thread_id}/messages/{message_id}

##### Models Expand Collapse

FileCitationAnnotation object { end_index , file_citation , start_index , 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file_search” tool to search files.

end_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_citation : object { file_id }

file_id : string

The ID of the specific File the citation is from.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation)

start_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

type : "file_citation"

Always `file_citation`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema))

FileCitationDeltaAnnotation object { index , type , end_index , 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file_search” tool to search files.

index : number

The index of the annotation in the text content part.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_citation"

Always `file_citation`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

end_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_citation : optional object { file_id , quote }

file_id : optional string

The ID of the specific File the citation is from.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation%20%3E%20(property)%20file_id)

quote : optional string

The specific quote in the file.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation%20%3E%20(property)%20quote)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation)

start_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : optional string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema))

FilePathAnnotation object { end_index , file_path , start_index , 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_path : object { file_id }

file_id : string

The ID of the file that was generated.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path)

start_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

type : "file_path"

Always `file_path`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema))

FilePathDeltaAnnotation object { index , type , end_index , 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index : number

The index of the annotation in the text content part.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_path"

Always `file_path`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

end_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_path : optional object { file_id }

file_id : optional string

The ID of the file that was generated.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path)

start_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : optional string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema))

ImageFile object { file_id , detail }

file_id : string

The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20file_id)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

ImageFileContentBlock object { image_file , type }

References an image [File](/docs/api-reference/files) in the content of a message.

image_file : [ImageFile](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file_id , detail }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file)

type : "image_file"

Always `image_file`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema))

ImageFileDelta object { detail , file_id }

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)%20%3E%20(property)%20detail)

file_id : optional string

The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema))

ImageFileDeltaBlock object { index , type , image_file }

References an image [File](/docs/api-reference/files) in the content of a message.

index : number

The index of the content part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image_file"

Always `image_file`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

image_file : optional [ImageFileDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail , file_id }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)%20%3E%20(property)%20image_file)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema))

ImageURL object { url , detail }

url : string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

format uri

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20url)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

ImageURLContentBlock object { image_url , type }

References an image URL in the content of a message.

image_url : [ImageURL](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url , detail }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema))

ImageURLDelta object { detail , url }

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)%20%3E%20(property)%20detail)

url : optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

format uri

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)%20%3E%20(property)%20url)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema))

ImageURLDeltaBlock object { index , type , image_url }

References an image URL in the content of a message.

index : number

The index of the content part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image_url"

Always `image_url`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

image_url : optional [ImageURLDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail , url }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)%20%3E%20(property)%20image_url)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema))

Message object { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20id)

assistant_id : string

If applicable, the ID of the [assistant](/docs/api-reference/assistants) that authored this message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20assistant_id)

attachments : array of object { file_id , tools }

A list of files attached to the message, and the tools they were added to.

file_id : optional string

The ID of the file to attach to the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20file_id)

tools : optional array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type } or object { type }

The tools to add this file to.

One of the following:

CodeInterpreterTool object { type }

type : "code_interpreter"

The type of tool being defined: `code_interpreter`

[](#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema))

FileSearchTool object { type }

type : "file_search"

The type of tool being defined: `file_search`

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20attachments)

completed_at : number

The Unix timestamp (in seconds) for when the message was completed.

format unixtime

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20completed_at)

content : array of [ImageFileContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image_file , type } or [ImageURLContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image_url , type } or [TextContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text , type } or [RefusalContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal , type }

The content of the message in array of text and/or images.

One of the following:

ImageFileContentBlock object { image_file , type }

References an image [File](/docs/api-reference/files) in the content of a message.

image_file : [ImageFile](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file_id , detail }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file)

type : "image_file"

Always `image_file`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema))

ImageURLContentBlock object { image_url , type }

References an image URL in the content of a message.

image_url : [ImageURL](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url , detail }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema))

TextContentBlock object { text , type }

The text content that is part of a message.

text : [Text](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations , value }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

Always `text`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema))

RefusalContentBlock object { refusal , type }

The refusal content generated by the assistant.

refusal : string

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)%20%3E%20(property)%20refusal)

type : "refusal"

Always `refusal`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema))

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20content)

created_at : number

The Unix timestamp (in seconds) for when the message was created.

format unixtime

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20created_at)

incomplete_at : number

The Unix timestamp (in seconds) for when the message was marked as incomplete.

format unixtime

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_at)

incomplete_details : object { reason }

On an incomplete message, details about why the message is incomplete.

reason : "content_filter" or "max_tokens" or "run_cancelled" or 2 more

The reason the message is incomplete.

One of the following:

"content_filter"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason%20%3E%20(member)%200)

"max_tokens"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason%20%3E%20(member)%201)

"run_cancelled"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason%20%3E%20(member)%202)

"run_expired"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason%20%3E%20(member)%203)

"run_failed"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason%20%3E%20(member)%204)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_details%20%3E%20(property)%20reason)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20incomplete_details)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20metadata)

object : "thread.message"

The object type, which is always `thread.message`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20object)

role : "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20role)

run_id : string

The ID of the [run](/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20run_id)

status : "in_progress" or "incomplete" or "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in_progress"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"completed"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20status)

thread_id : string

The [thread](/docs/api-reference/threads) ID that this message belongs to.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20thread_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

MessageDeleted object { id , deleted , object }

id : string

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "thread.message.deleted"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema))

MessageDelta object { content , role }

The delta containing the fields that have changed on the Message.

content : optional array of [ImageFileDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)) { index , type , image_file } or [TextDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)) { index , type , text } or [RefusalDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)) { index , type , refusal } or [ImageURLDeltaBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)) { index , type , image_url }

The content of the message in array of text and/or images.

One of the following:

ImageFileDeltaBlock object { index , type , image_file }

References an image [File](/docs/api-reference/files) in the content of a message.

index : number

The index of the content part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image_file"

Always `image_file`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

image_file : optional [ImageFileDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail , file_id }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)%20%3E%20(property)%20image_file)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema))

TextDeltaBlock object { index , type , text }

The text content that is part of a message.

index : number

The index of the content part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "text"

Always `text`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

text : optional [TextDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations , value }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema))

RefusalDeltaBlock object { index , type , refusal }

The refusal content that is part of a message.

index : number

The index of the refusal part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "refusal"

Always `refusal`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

refusal : optional string

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)%20%3E%20(property)%20refusal)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema))

ImageURLDeltaBlock object { index , type , image_url }

References an image URL in the content of a message.

index : number

The index of the content part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image_url"

Always `image_url`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

image_url : optional [ImageURLDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail , url }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)%20%3E%20(property)%20image_url)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema))

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)%20%3E%20(property)%20content)

role : optional "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema))

MessageDeltaEvent object { id , delta , object }

Represents a message delta i.e. any changed fields on a message during streaming.

id : string

The identifier of the message, which can be referenced in API endpoints.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)%20%3E%20(property)%20id)

delta : [MessageDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)) { content , role }

The delta containing the fields that have changed on the Message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta)

object : "thread.message.delta"

The object type, which is always `thread.message.delta`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

RefusalContentBlock object { refusal , type }

The refusal content generated by the assistant.

refusal : string

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)%20%3E%20(property)%20refusal)

type : "refusal"

Always `refusal`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema))

RefusalDeltaBlock object { index , type , refusal }

The refusal content that is part of a message.

index : number

The index of the refusal part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "refusal"

Always `refusal`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

refusal : optional string

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)%20%3E%20(property)%20refusal)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema))

Text object { annotations , value }

annotations : array of [FileCitationAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end_index , file_citation , start_index , 2 more } or [FilePathAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end_index , file_path , start_index , 2 more }

One of the following:

FileCitationAnnotation object { end_index , file_citation , start_index , 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file_search” tool to search files.

end_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_citation : object { file_id }

file_id : string

The ID of the specific File the citation is from.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation)

start_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

type : "file_citation"

Always `file_citation`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema))

FilePathAnnotation object { end_index , file_path , start_index , 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_path : object { file_id }

file_id : string

The ID of the file that was generated.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path)

start_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

type : "file_path"

Always `file_path`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema))

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)%20%3E%20(property)%20annotations)

value : string

The data that makes up the text.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

TextContentBlock object { text , type }

The text content that is part of a message.

text : [Text](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations , value }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

Always `text`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema))

TextContentBlockParam object { text , type }

The text content that is part of a message.

text : string

Text content to be sent to the model

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

Always `text`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema))

TextDelta object { annotations , value }

annotations : optional array of [FileCitationDeltaAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)) { index , type , end_index , 3 more } or [FilePathDeltaAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)) { index , type , end_index , 3 more }

One of the following:

FileCitationDeltaAnnotation object { index , type , end_index , 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file_search” tool to search files.

index : number

The index of the annotation in the text content part.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_citation"

Always `file_citation`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

end_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_citation : optional object { file_id , quote }

file_id : optional string

The ID of the specific File the citation is from.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation%20%3E%20(property)%20file_id)

quote : optional string

The specific quote in the file.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation%20%3E%20(property)%20quote)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation)

start_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : optional string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema))

FilePathDeltaAnnotation object { index , type , end_index , 3 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index : number

The index of the annotation in the text content part.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_path"

Always `file_path`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

end_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_path : optional object { file_id }

file_id : optional string

The ID of the file that was generated.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path)

start_index : optional number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : optional string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema))

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)%20%3E%20(property)%20annotations)

value : optional string

The data that makes up the text.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema))

TextDeltaBlock object { index , type , text }

The text content that is part of a message.

index : number

The index of the content part in the message.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)%20%3E%20(property)%20index)

type : "text"

Always `text`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)%20%3E%20(property)%20type)

text : optional [TextDelta](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations , value }

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads
