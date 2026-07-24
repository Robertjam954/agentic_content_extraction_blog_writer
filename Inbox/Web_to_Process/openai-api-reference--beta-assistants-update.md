---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/methods/update
title: "Modify assistant"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Modify assistant

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Assistants](/api/reference/resources/beta/subresources/assistants)

# Modify assistant

Deprecated

POST /assistants/{assistant_id}

Modifies an assistant.

##### P ath Parameters Expand Collapse

assistant_id : string

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20assistant_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

description : optional string

The description of the assistant. The maximum length is 512 characters.

maxLength 512

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20description%20%3E%20(schema))

instructions : optional string

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength 256000

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20instructions%20%3E%20(schema))

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20metadata%20%3E%20(schema))

model : optional string or "gpt-5" or "gpt-5-mini" or "gpt-5-nano" or 39 more

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models) for descriptions of them.

One of the following:

string

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%200)

AssistantSupportedModels = "gpt-5" or "gpt-5-mini" or "gpt-5-nano" or 39 more

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models) for descriptions of them.

One of the following:

"gpt-5"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%200)

"gpt-5-mini"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%201)

"gpt-5-nano"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%202)

"gpt-5-2025-08-07"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%203)

"gpt-5-mini-2025-08-07"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%204)

"gpt-5-nano-2025-08-07"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%205)

"gpt-4.1"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%206)

"gpt-4.1-mini"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%207)

"gpt-4.1-nano"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%208)

"gpt-4.1-2025-04-14"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%209)

"gpt-4.1-mini-2025-04-14"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2010)

"gpt-4.1-nano-2025-04-14"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2011)

"o3-mini"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2012)

"o3-mini-2025-01-31"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2013)

"o1"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2014)

"o1-2024-12-17"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2015)

"gpt-4o"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2016)

"gpt-4o-2024-11-20"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2017)

"gpt-4o-2024-08-06"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2018)

"gpt-4o-2024-05-13"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2019)

"gpt-4o-mini"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2020)

"gpt-4o-mini-2024-07-18"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2021)

"gpt-4.5-preview"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2022)

"gpt-4.5-preview-2025-02-27"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2023)

"gpt-4-turbo"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2024)

"gpt-4-turbo-2024-04-09"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2025)

"gpt-4-0125-preview"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2026)

"gpt-4-turbo-preview"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2027)

"gpt-4-1106-preview"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2028)

"gpt-4-vision-preview"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2029)

"gpt-4"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2030)

"gpt-4-0314"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2031)

"gpt-4-0613"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2032)

"gpt-4-32k"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2033)

"gpt-4-32k-0314"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2034)

"gpt-4-32k-0613"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2035)

"gpt-3.5-turbo"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2036)

"gpt-3.5-turbo-16k"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2037)

"gpt-3.5-turbo-0613"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2038)

"gpt-3.5-turbo-1106"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2039)

"gpt-3.5-turbo-0125"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2040)

"gpt-3.5-turbo-16k-0613"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2041)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema))

name : optional string

The name of the assistant. The maximum length is 256 characters.

maxLength 256

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

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

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"minimal"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"low"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"medium"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"high"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

"xhigh"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%205)

"max"

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%206)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20reasoning_effort%20%3E%20(schema))

response_format : optional [AssistantResponseFormatOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

"auto"

`auto` is the default value

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)%20%3E%20(variant)%200)

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

ResponseFormatJSONSchema object { json_schema , type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json_schema : object { name , description , schema , strict }

Structured Outputs configuration options, including a JSON Schema.

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20name)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20description)

schema : optional map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20schema)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20strict)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema))

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema))

temperature : optional number

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum 0

maximum 2

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20temperature%20%3E%20(schema))

tool_resources : optional object { code_interpreter , file_search }

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code_interpreter : optional object { file_ids }

file_ids : optional array of string

Overrides the list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20file_ids)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

file_search : optional object { vector_store_ids }

vector_store_ids : optional array of string

Overrides the [vector store](/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_store_ids)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search)

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema))

tools : optional array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type } or [FileSearchTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type , file_search } or [FunctionTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function , type }

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

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tools%20%3E%20(schema))

top_p : optional number

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum 0

maximum 1

[](#(resource)%20beta.assistants%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20top_p%20%3E%20(schema))

##### Returns Expand Collapse

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

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

### Modify assistant

```
curl https://api.openai.com/v1/assistants/asst_abc123 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
"tools": [{"type": "file_search"}],
"model": "gpt-4o"
}'
```

```
{
"id": "asst_123",
"object": "assistant",
"created_at": 1699009709,
"name": "HR Helper",
"description": null,
"model": "gpt-4o",
"instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
"tools": [
{
"type": "file_search"
}
],
"tool_resources": {
"file_search": {
"vector_store_ids": []
}
},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
}
```

##### Returns Examples

```
{
"id": "asst_123",
"object": "assistant",
"created_at": 1699009709,
"name": "HR Helper",
"description": null,
"model": "gpt-4o",
"instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
"tools": [
{
"type": "file_search"
}
],
"tool_resources": {
"file_search": {
"vector_store_ids": []
}
},
"metadata": {},
"top_p": 1.0,
"temperature": 1.0,
"response_format": "auto"
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/methods/update
