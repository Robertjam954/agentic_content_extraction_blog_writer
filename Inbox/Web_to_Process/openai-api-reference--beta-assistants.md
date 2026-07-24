---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/assistants
title: "Assistants"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Assistants

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

# Assistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/resources/beta/subresources/assistants/methods/list)

Deprecated

GET /assistants

##### [Create assistant](/api/reference/resources/beta/subresources/assistants/methods/create)

Deprecated

POST /assistants

##### [Retrieve assistant](/api/reference/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

GET /assistants/{assistant_id}

##### [Modify assistant](/api/reference/resources/beta/subresources/assistants/methods/update)

Deprecated

POST /assistants/{assistant_id}

##### [Delete assistant](/api/reference/resources/beta/subresources/assistants/methods/delete)

Deprecated

DELETE /assistants/{assistant_id}

##### Models Expand Collapse

Assistant object { id , created_at , description , 10 more }

Represents an `assistant` that can call the model and use tools.

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the assistant was created.

format unixtime

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20created_at)

description : string

The description of the assistant. The maximum length is 512 characters.

maxLength 512

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20description)

instructions : string

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength 256000

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20instructions)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20metadata)

model : string

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models) for descriptions of them.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the assistant. The maximum length is 256 characters.

maxLength 256

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20name)

object : "assistant"

The object type, which is always `assistant`.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20object)

tools : array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type } or [FileSearchTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type , file_search } or [FunctionTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function , type }

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

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

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20tools)

response_format : optional [AssistantResponseFormatOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format)

temperature : optional number

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum 0

maximum 2

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20temperature)

tool_resources : optional object { code_interpreter , file_search }

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code_interpreter : optional object { file_ids }

file_ids : optional array of string

A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20file_ids)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20code_interpreter)

file_search : optional object { vector_store_ids }

vector_store_ids : optional array of string

The ID of the [vector store](/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_store_ids)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20file_search)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20tool_resources)

top_p : optional number

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum 0

maximum 1

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20top_p)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

AssistantDeleted object { id , deleted , object }

id : string

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "assistant.deleted"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema))

AssistantStreamEvent = object { data , event , enabled } or object { data , event } or object { data , event } or 22 more

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

```
event: thread.created
data: {"id": "thread_123", "object": "thread", ...}
```

We emit events whenever a new object is created, transitions to a new state, or is being
streamed in parts (deltas). For example, we emit `thread.run.created` when a new run
is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses
to create a message during a run, we emit a `thread.message.created event`, a
`thread.message.in_progress` event, many `thread.message.delta` events, and finally a
`thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully
in your code. See the [Assistants API quickstart](/docs/assistants/overview) to learn how to
integrate the Assistants API with streaming.

One of the following:

object { data , event , enabled }

Occurs when a new [thread](/docs/api-reference/threads/object) is created.

data : [Thread](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id , created_at , metadata , 2 more }

Represents a thread that contains [messages](/docs/api-reference/messages).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20data)

event : "thread.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20event)

enabled : optional boolean

Whether to enable input audio transcription.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20enabled)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%200)

object { data , event }

Occurs when a new [run](/docs/api-reference/runs/object) is created.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20data)

event : "thread.run.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%201)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `queued` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20data)

event : "thread.run.queued"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%202)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to an `in_progress` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20data)

event : "thread.run.in_progress"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%203)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `requires_action` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20data)

event : "thread.run.requires_action"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%204)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) is completed.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%205%20%3E%20(property)%20data)

event : "thread.run.completed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%205%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%205)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) ends with status `incomplete`.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20data)

event : "thread.run.incomplete"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%206)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) fails.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%207%20%3E%20(property)%20data)

event : "thread.run.failed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%207%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%207)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `cancelling` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%208%20%3E%20(property)%20data)

event : "thread.run.cancelling"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%208%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%208)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) is cancelled.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20data)

event : "thread.run.cancelled"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%209)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) expires.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2010%20%3E%20(property)%20data)

event : "thread.run.expired"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2010%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2010)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is created.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20data)

event : "thread.run.step.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2011)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2012%20%3E%20(property)%20data)

event : "thread.run.step.in_progress"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2012%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2012)

object { data , event }

Occurs when parts of a [run step](/docs/api-reference/run-steps/step-object) are being streamed.

data : [RunStepDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) { id , delta , object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2013%20%3E%20(property)%20data)

event : "thread.run.step.delta"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2013%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2013)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is completed.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2014%20%3E%20(property)%20data)

event : "thread.run.step.completed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2014%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2014)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) fails.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2015%20%3E%20(property)%20data)

event : "thread.run.step.failed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2015%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2015)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is cancelled.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2016%20%3E%20(property)%20data)

event : "thread.run.step.cancelled"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2016%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2016)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) expires.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2017%20%3E%20(property)%20data)

event : "thread.run.step.expired"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2017%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2017)

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) is created.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2018%20%3E%20(property)%20data)

event : "thread.message.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2018%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2018)

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) moves to an `in_progress` state.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20data)

event : "thread.message.in_progress"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2019)

object { data , event }

Occurs when parts of a [Message](/docs/api-reference/messages/object) are being streamed.

data : [MessageDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) { id , delta , object }

Represents a message delta i.e. any changed fields on a message during streaming.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2020%20%3E%20(property)%20data)

event : "thread.message.delta"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2020%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2020)

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) is completed.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2021%20%3E%20(property)%20data)

event : "thread.message.completed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2021%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2021)

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) ends before it is completed.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2022%20%3E%20(property)%20data)

event : "thread.message.incomplete"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2022%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2022)

ErrorEvent object { data , event }

Occurs when an [error](/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

data : [ErrorObject](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema)) { code , message , param , type }

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2023%20%3E%20(property)%20data)

event : "error"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2023%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2023)

DoneEvent object { data , event }

Occurs when a stream ends.

data : "[DONE]"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2024%20%3E%20(property)%20data)

event : "done"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2024%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema)%20%3E%20(variant)%2024)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))

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

MessageStreamEvent = object { data , event } or object { data , event } or object { data , event } or 2 more

Occurs when a [message](/docs/api-reference/messages/object) is created.

One of the following:

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) is created.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20data)

event : "thread.message.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%200)

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) moves to an `in_progress` state.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20data)

event : "thread.message.in_progress"

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%201)

object { data , event }

Occurs when parts of a [Message](/docs/api-reference/messages/object) are being streamed.

data : [MessageDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) { id , delta , object }

Represents a message delta i.e. any changed fields on a message during streaming.

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20data)

event : "thread.message.delta"

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%202)

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) is completed.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20data)

event : "thread.message.completed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%203)

object { data , event }

Occurs when a [message](/docs/api-reference/messages/object) ends before it is completed.

data : [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id , assistant_id , attachments , 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20data)

event : "thread.message.incomplete"

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema)%20%3E%20(variant)%204)

[](#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema))

RunStepStreamEvent = object { data , event } or object { data , event } or object { data , event } or 4 more

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is created.

One of the following:

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is created.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20data)

event : "thread.run.step.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%200)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20data)

event : "thread.run.step.in_progress"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%201)

object { data , event }

Occurs when parts of a [run step](/docs/api-reference/run-steps/step-object) are being streamed.

data : [RunStepDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) { id , delta , object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20data)

event : "thread.run.step.delta"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%202)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is completed.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20data)

event : "thread.run.step.completed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%203)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) fails.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20data)

event : "thread.run.step.failed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%204)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is cancelled.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%205%20%3E%20(property)%20data)

event : "thread.run.step.cancelled"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%205%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%205)

object { data , event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) expires.

data : [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20data)

event : "thread.run.step.expired"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema)%20%3E%20(variant)%206)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema))

RunStreamEvent = object { data , event } or object { data , event } or object { data , event } or 7 more

Occurs when a new [run](/docs/api-reference/runs/object) is created.

One of the following:

object { data , event }

Occurs when a new [run](/docs/api-reference/runs/object) is created.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20data)

event : "thread.run.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%200)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `queued` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20data)

event : "thread.run.queued"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%201)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to an `in_progress` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20data)

event : "thread.run.in_progress"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%202)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `requires_action` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20data)

event : "thread.run.requires_action"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%203)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) is completed.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20data)

event : "thread.run.completed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%204%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%204)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) ends with status `incomplete`.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%205%20%3E%20(property)%20data)

event : "thread.run.incomplete"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%205%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%205)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) fails.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20data)

event : "thread.run.failed"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%206)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `cancelling` status.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%207%20%3E%20(property)%20data)

event : "thread.run.cancelling"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%207%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%207)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) is cancelled.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%208%20%3E%20(property)%20data)

event : "thread.run.cancelled"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%208%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%208)

object { data , event }

Occurs when a [run](/docs/api-reference/runs/object) expires.

data : [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id , assistant_id , cancelled_at , 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20data)

event : "thread.run.expired"

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20event)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema)%20%3E%20(variant)%209)

[](#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema))

ThreadStreamEvent object { data , event , enabled }

Occurs when a new [thread](/docs/api-reference/threads/object) is created.

data : [Thread](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id , created_at , metadata , 2 more }

Represents a thread that contains [messages](/docs/api-reference/messages).

[](#(resource)%20beta.assistants%20%3E%20(model)%20thread_stream_event%20%3E%20(schema)%20%3E%20(property)%20data)

event : "thread.created"

[](#(resource)%20beta.assistants%20%3E%20(model)%20thread_stream_event%20%3E%20(schema)%20%3E%20(property)%20event)

enabled : optional boolean

Whether to enable input audio transcription.

[](#(resource)%20beta.assistants%20%3E%20(model)%20thread_stream_event%20%3E%20(schema)%20%3E%20(property)%20enabled)

[](#(resource)%20beta.assistants%20%3E%20(model)%20thread_stream_event%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/assistants
