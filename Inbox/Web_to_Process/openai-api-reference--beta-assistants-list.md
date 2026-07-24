---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/methods/list
title: "List assistants"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List assistants

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Assistants](/api/reference/resources/beta/subresources/assistants)

# List assistants

Deprecated

GET /assistants

Returns a list of assistants.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

before : optional string

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20before%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [Assistant](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) { id , created_at , description , 10 more }

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

name : string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

[](#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20name)

description : optional string

A description of what the function does, used by the model to choose when and how to call the function.

[](#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20description)

parameters : optional [FunctionParameters](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

[](#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20parameters)

strict : optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](/docs/guides/function-calling).

[](#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)%20%3E%20(property)%20strict)

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

One of the following:

"auto"

`auto` is the default value

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)%20%3E%20(variant)%200)

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

ResponseFormatJSONSchema object { json_schema , type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json_schema : object { name , description , schema , strict }

Structured Outputs configuration options, including a JSON Schema.

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20name)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20description)

schema : optional map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20schema)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20strict)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema))

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

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

first_id : string

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

has_more : boolean

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

last_id : string

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

object : string

[](#(resource)%20beta.assistants%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List assistants

```
curl "https://api.openai.com/v1/assistants?order=desc&limit=20" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2"
```

```
{
"object": "list",
"data": [
{
"id": "asst_abc123",
"object": "assistant",
"created_at": 1698982736,
"name": "Coding Tutor",
"description": null,
"model": "gpt-4o",
"instructions": "You are a helpful assistant designed to make me better at coding!",
"tools": [],
"tool_resources": {},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
},
{
"id": "asst_abc456",
"object": "assistant",
"created_at": 1698982718,
"name": "My Assistant",
"description": null,
"model": "gpt-4o",
"instructions": "You are a helpful assistant designed to make me better at coding!",
"tools": [],
"tool_resources": {},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
},
{
"id": "asst_abc789",
"object": "assistant",
"created_at": 1698982643,
"name": null,
"description": null,
"model": "gpt-4o",
"instructions": null,
"tools": [],
"tool_resources": {},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
}
],
"first_id": "asst_abc123",
"last_id": "asst_abc789",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "asst_abc123",
"object": "assistant",
"created_at": 1698982736,
"name": "Coding Tutor",
"description": null,
"model": "gpt-4o",
"instructions": "You are a helpful assistant designed to make me better at coding!",
"tools": [],
"tool_resources": {},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
},
{
"id": "asst_abc456",
"object": "assistant",
"created_at": 1698982718,
"name": "My Assistant",
"description": null,
"model": "gpt-4o",
"instructions": "You are a helpful assistant designed to make me better at coding!",
"tools": [],
"tool_resources": {},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
},
{
"id": "asst_abc789",
"object": "assistant",
"created_at": 1698982643,
"name": null,
"description": null,
"model": "gpt-4o",
"instructions": null,
"tools": [],
"tool_resources": {},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
}
],
"first_id": "asst_abc123",
"last_id": "asst_abc789",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/methods/list
