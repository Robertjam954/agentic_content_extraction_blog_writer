---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/runs/methods/create
title: "Create run"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create run

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

[Runs](/api/reference/resources/beta/subresources/threads/subresources/runs)

# Create run

POST /threads/{thread_id}/runs

Create a run.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20thread_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

include : optional array of [RunStepInclude](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_include%20%3E%20(schema))

A list of additional fields to include in the response. Currently the only supported value is `step_details.tool_calls[*].file_search.results[*].content` to fetch the file search result content.

See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20include%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

assistant_id : string

The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20assistant_id%20%3E%20(schema))

additional_instructions : optional string

Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_instructions%20%3E%20(schema))

additional_messages : optional array of object { content , role , attachments , metadata }

Adds additional messages to the thread before creating the run.

content : string or array of [ImageFileContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image_file , type } or [ImageURLContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image_url , type } or [TextContentBlockParam](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)) { text , type }

The text contents of the message.

One of the following:

TextContent = string

The text contents of the message.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ImageFileContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image_file , type } or [ImageURLContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image_url , type } or [TextContentBlockParam](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)) { text , type }

An array of content parts with a defined type, each can be of type `text` or images can be passed with `image_url` or `image_file`. Image types are only supported on [Vision-compatible models](/docs/models).

One of the following:

ImageFileContentBlock object { image_file , type }

References an image [File](/docs/api-reference/files) in the content of a message.

image_file : [ImageFile](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file_id , detail }

file_id : string

The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20file_id)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)%20%3E%20(property)%20detail)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20image_file)

type : "image_file"

Always `image_file`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema))

ImageURLContentBlock object { image_url , type }

References an image URL in the content of a message.

image_url : [ImageURL](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url , detail }

url : string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

format uri

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20url)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)%20%3E%20(property)%20detail)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema))

TextContentBlockParam object { text , type }

The text content that is part of a message.

text : string

Text content to be sent to the model

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

Always `text`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema))

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant"

The role of the entity that is creating the message. Allowed values include:

- `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.

- `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

One of the following:

"user"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role)

attachments : optional array of object { file_id , tools }

A list of files attached to the message, and the tools they should be added to.

file_id : optional string

The ID of the file to attach to the message.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20file_id)

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

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20metadata)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20additional_messages%20%3E%20(schema))

instructions : optional string

Overrides the [instructions](/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20instructions%20%3E%20(schema))

max_completion_tokens : optional number

The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

minimum 256

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20max_completion_tokens%20%3E%20(schema))

max_prompt_tokens : optional number

The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

minimum 256

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20max_prompt_tokens%20%3E%20(schema))

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20metadata%20%3E%20(schema))

model : optional string or "gpt-5" or "gpt-5-mini" or "gpt-5-nano" or 39 more

The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

One of the following:

string

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%200)

AssistantSupportedModels = "gpt-5" or "gpt-5-mini" or "gpt-5-nano" or 39 more

The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

One of the following:

"gpt-5"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%200)

"gpt-5-mini"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%201)

"gpt-5-nano"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%202)

"gpt-5-2025-08-07"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%203)

"gpt-5-mini-2025-08-07"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%204)

"gpt-5-nano-2025-08-07"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%205)

"gpt-4.1"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%206)

"gpt-4.1-mini"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%207)

"gpt-4.1-nano"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%208)

"gpt-4.1-2025-04-14"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%209)

"gpt-4.1-mini-2025-04-14"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2010)

"gpt-4.1-nano-2025-04-14"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2011)

"o3-mini"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2012)

"o3-mini-2025-01-31"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2013)

"o1"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2014)

"o1-2024-12-17"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2015)

"gpt-4o"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2016)

"gpt-4o-2024-11-20"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2017)

"gpt-4o-2024-08-06"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2018)

"gpt-4o-2024-05-13"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2019)

"gpt-4o-mini"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2020)

"gpt-4o-mini-2024-07-18"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2021)

"gpt-4.5-preview"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2022)

"gpt-4.5-preview-2025-02-27"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2023)

"gpt-4-turbo"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2024)

"gpt-4-turbo-2024-04-09"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2025)

"gpt-4-0125-preview"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2026)

"gpt-4-turbo-preview"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2027)

"gpt-4-1106-preview"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2028)

"gpt-4-vision-preview"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2029)

"gpt-4"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2030)

"gpt-4-0314"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2031)

"gpt-4-0613"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2032)

"gpt-4-32k"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2033)

"gpt-4-32k-0314"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2034)

"gpt-4-32k-0613"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2035)

"gpt-3.5-turbo"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2036)

"gpt-3.5-turbo-16k"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2037)

"gpt-3.5-turbo-0613"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2038)

"gpt-3.5-turbo-1106"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2039)

"gpt-3.5-turbo-0125"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2040)

"gpt-3.5-turbo-16k-0613"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%2041)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema))

parallel_tool_calls : optional boolean

Whether to enable [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20parallel_tool_calls%20%3E%20(schema))

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

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"minimal"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"low"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"medium"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"high"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

"xhigh"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%205)

"max"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%206)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema))

response_format : optional [AssistantResponseFormatOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

"auto"

`auto` is the default value

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)%20%3E%20(variant)%200)

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

ResponseFormatJSONSchema object { json_schema , type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json_schema : object { name , description , schema , strict }

Structured Outputs configuration options, including a JSON Schema.

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20name)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20description)

schema : optional map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20schema)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20strict)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema))

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema))

stream : optional boolean

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream%20%3E%20(schema))

temperature : optional number

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum 0

maximum 2

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20temperature%20%3E%20(schema))

tool_choice : optional [AssistantToolChoiceOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

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

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%200)

"auto"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%201)

"required"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%202)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200)

AssistantToolChoice object { type , function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type : "function" or "code_interpreter" or "file_search"

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"code_interpreter"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"file_search"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

function : optional [AssistantToolChoiceFunction](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name : string

The name of the function to call.

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema))

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema))

tools : optional array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type } or [FileSearchTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type , file_search } or [FunctionTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function , type }

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

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

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tools%20%3E%20(schema))

top_p : optional number

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20top_p%20%3E%20(schema))

truncation_strategy : optional object { type , last_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type : "auto" or "last_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20truncation_strategy%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"last_messages"

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20truncation_strategy%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20truncation_strategy%20%3E%20(schema)%20%3E%20(property)%20type)

last_messages : optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum 1

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20truncation_strategy%20%3E%20(schema)%20%3E%20(property)%20last_messages)

[](#(resource)%20beta.threads.runs%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20truncation_strategy%20%3E%20(schema))

##### Returns Expand Collapse

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

One of the following:

"auto"

`auto` is the default value

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)%20%3E%20(variant)%200)

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

ResponseFormatJSONSchema object { json_schema , type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json_schema : object { name , description , schema , strict }

Structured Outputs configuration options, including a JSON Schema.

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20name)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20description)

schema : optional map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20schema)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20strict)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20response_format%20%2B%20(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema))

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

One of the following:

"none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%200)

"auto"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%201)

"required"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%202)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200)

AssistantToolChoice object { type , function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type : "function" or "code_interpreter" or "file_search"

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"code_interpreter"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"file_search"

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

function : optional [AssistantToolChoiceFunction](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name : string

The name of the function to call.

[](#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)%20%3E%20(property)%20tool_choice%20%2B%20(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice%20%3E%20(schema))

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

Default Streaming Streaming with Functions

### Create run

```
curl https://api.openai.com/v1/threads/thread_abc123/runs \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"assistant_id": "asst_abc123"
}'
```

```
{
"id": "run_abc123",
"object": "thread.run",
"created_at": 1699063290,
"assistant_id": "asst_abc123",
"thread_id": "thread_abc123",
"status": "queued",
"started_at": 1699063290,
"expires_at": null,
"cancelled_at": null,
"failed_at": null,
"completed_at": 1699063291,
"last_error": null,
"model": "gpt-4o",
"instructions": null,
"incomplete_details": null,
"tools": [
{
"type": "code_interpreter"
}
],
"metadata": {},
"usage": null,
"temperature": 1.0,
"top_p": 1.0,
"max_prompt_tokens": 1000,
"max_completion_tokens": 1000,
"truncation_strategy": {
"type": "auto",
"last_messages": null
},
"response_format": "auto",
"tool_choice": "auto",
"parallel_tool_calls": true
}
```

### Create run

```
curl https://api.openai.com/v1/threads/thread_123/runs \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"assistant_id": "asst_123",
"stream": true
}'
```

```
event: thread.run.created
data: {"id":"run_123","object":"thread.run","created_at":1710330640,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710331240,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.queued
data: {"id":"run_123","object":"thread.run","created_at":1710330640,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710331240,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.in_progress
data: {"id":"run_123","object":"thread.run","created_at":1710330640,"assistant_id":"asst_123","thread_id":"thread_123","status":"in_progress","started_at":1710330641,"expires_at":1710331240,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.step.created
data: {"id":"step_001","object":"thread.run.step","created_at":1710330641,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710331240,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":null}

event: thread.run.step.in_progress
data: {"id":"step_001","object":"thread.run.step","created_at":1710330641,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710331240,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":null}

event: thread.message.created
data: {"id":"msg_001","object":"thread.message","created_at":1710330641,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"in_progress","incomplete_details":null,"incomplete_at":null,"completed_at":null,"role":"assistant","content":[],"metadata":{}}

event: thread.message.in_progress
data: {"id":"msg_001","object":"thread.message","created_at":1710330641,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"in_progress","incomplete_details":null,"incomplete_at":null,"completed_at":null,"role":"assistant","content":[],"metadata":{}}

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":"Hello","annotations":[]}}]}}

...

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":" today"}}]}}

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":"?"}}]}}

event: thread.message.completed
data: {"id":"msg_001","object":"thread.message","created_at":1710330641,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"completed","incomplete_details":null,"incomplete_at":null,"completed_at":1710330642,"role":"assistant","content":[{"type":"text","text":{"value":"Hello! How can I assist you today?","annotations":[]}}],"metadata":{}}

event: thread.run.step.completed
data: {"id":"step_001","object":"thread.run.step","created_at":1710330641,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"completed","cancelled_at":null,"completed_at":1710330642,"expires_at":1710331240,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":{"prompt_tokens":20,"completion_tokens":11,"total_tokens":31}}

event: thread.run.completed
data: {"id":"run_123","object":"thread.run","created_at":1710330640,"assistant_id":"asst_123","thread_id":"thread_123","status":"completed","started_at":1710330641,"expires_at":null,"cancelled_at":null,"failed_at":null,"completed_at":1710330642,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":{"prompt_tokens":20,"completion_tokens":11,"total_tokens":31},"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: done
data: [DONE]
```

### Create run

```
curl https://api.openai.com/v1/threads/thread_abc123/runs \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"assistant_id": "asst_abc123",
"tools": [
{
"type": "function",
"function": {
"name": "get_current_weather",
"description": "Get the current weather in a given location",
"parameters": {
"type": "object",
"properties": {
"location": {
"type": "string",
"description": "The city and state, e.g. San Francisco, CA"
},
"unit": {
"type": "string",
"enum": ["celsius", "fahrenheit"]
}
},
"required": ["location"]
}
}
}
],
"stream": true
}'
```

```
event: thread.run.created
data: {"id":"run_123","object":"thread.run","created_at":1710348075,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710348675,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.queued
data: {"id":"run_123","object":"thread.run","created_at":1710348075,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710348675,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.in_progress
data: {"id":"run_123","object":"thread.run","created_at":1710348075,"assistant_id":"asst_123","thread_id":"thread_123","status":"in_progress","started_at":1710348075,"expires_at":1710348675,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.step.created
data: {"id":"step_001","object":"thread.run.step","created_at":1710348076,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710348675,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":null}

event: thread.run.step.in_progress
data: {"id":"step_001","object":"thread.run.step","created_at":1710348076,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710348675,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":null}

event: thread.message.created
data: {"id":"msg_001","object":"thread.message","created_at":1710348076,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"in_progress","incomplete_details":null,"incomplete_at":null,"completed_at":null,"role":"assistant","content":[],"metadata":{}}

event: thread.message.in_progress
data: {"id":"msg_001","object":"thread.message","created_at":1710348076,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"in_progress","incomplete_details":null,"incomplete_at":null,"completed_at":null,"role":"assistant","content":[],"metadata":{}}

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":"Hello","annotations":[]}}]}}

...

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":" today"}}]}}

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":"?"}}]}}

event: thread.message.completed
data: {"id":"msg_001","object":"thread.message","created_at":1710348076,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"completed","incomplete_details":null,"incomplete_at":null,"completed_at":1710348077,"role":"assistant","content":[{"type":"text","text":{"value":"Hello! How can I assist you today?","annotations":[]}}],"metadata":{}}

event: thread.run.step.completed
data: {"id":"step_001","object":"thread.run.step","created_at":1710348076,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"completed","cancelled_at":null,"completed_at":1710348077,"expires_at":1710348675,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":{"prompt_tokens":20,"completion_tokens":11,"total_tokens":31}}

event: thread.run.completed
data: {"id":"run_123","object":"thread.run","created_at":1710348075,"assistant_id":"asst_123","thread_id":"thread_123","status":"completed","started_at":1710348075,"expires_at":null,"cancelled_at":null,"failed_at":null,"completed_at":1710348077,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":{"prompt_tokens":20,"completion_tokens":11,"total_tokens":31},"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: done
data: [DONE]
```

##### Returns Examples

```
{
"id": "run_abc123",
"object": "thread.run",
"created_at": 1699063290,
"assistant_id": "asst_abc123",
"thread_id": "thread_abc123",
"status": "queued",
"started_at": 1699063290,
"expires_at": null,
"cancelled_at": null,
"failed_at": null,
"completed_at": 1699063291,
"last_error": null,
"model": "gpt-4o",
"instructions": null,
"incomplete_details": null,
"tools": [
{
"type": "code_interpreter"
}
],
"metadata": {},
"usage": null,
"temperature": 1.0,
"top_p": 1.0,
"max_prompt_tokens": 1000,
"max_completion_tokens": 1000,
"truncation_strategy": {
"type": "auto",
"last_messages": null
},
"response_format": "auto",
"tool_choice": "auto",
"parallel_tool_calls": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/runs/methods/create
