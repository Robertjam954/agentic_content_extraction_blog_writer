---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/create
title: "Create thread"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create thread

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

# Create thread

POST /threads

Create a thread.

##### Body Parameters JSON Expand Collapse

messages : optional array of object { content , role , attachments , metadata }

A list of [messages](/docs/api-reference/messages) to start the thread with.

content : string or array of [ImageFileContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image_file , type } or [ImageURLContentBlock](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image_url , type } or [TextContentBlockParam](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block_param%20%3E%20(schema)) { text , type }

The text contents of the message.

One of the following:

TextContent = string

The text contents of the message.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

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

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant"

The role of the entity that is creating the message. Allowed values include:

- `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.

- `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

One of the following:

"user"

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role)

attachments : optional array of object { file_id , tools }

A list of files attached to the message, and the tools they should be added to.

file_id : optional string

The ID of the file to attach to the message.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20file_id)

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

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20tools)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attachments)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20metadata)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20messages%20%3E%20(schema))

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20metadata%20%3E%20(schema))

tool_resources : optional object { code_interpreter , file_search }

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code_interpreter : optional object { file_ids }

file_ids : optional array of string

A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20file_ids)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

file_search : optional object { vector_store_ids , vector_stores }

vector_store_ids : optional array of string

The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_store_ids)

vector_stores : optional array of object { chunking_strategy , file_ids , metadata }

A helper to create a [vector store](/docs/api-reference/vector-stores/object) with file_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread.

chunking_strategy : optional object { type } or object { static , type }

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

One of the following:

AutoChunkingStrategy object { type }

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type : "auto"

Always `auto`.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%3E%20(variant)%200)

StaticChunkingStrategy object { static , type }

static : object { chunk_overlap_tokens , max_chunk_size_tokens }

chunk_overlap_tokens : number

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%3E%20(variant)%201%20%3E%20(property)%20static%20%3E%20(property)%20chunk_overlap_tokens)

max_chunk_size_tokens : number

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum 100

maximum 4096

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%3E%20(variant)%201%20%3E%20(property)%20static%20%3E%20(property)%20max_chunk_size_tokens)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%3E%20(variant)%201%20%3E%20(property)%20static)

type : "static"

Always `static`.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy%20%3E%20(variant)%201)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20chunking_strategy)

file_ids : optional array of string

A list of [file](/docs/api-reference/files) IDs to add to the vector store. For vector stores created before Nov 2025, there can be a maximum of 10,000 files in a vector store. For vector stores created starting in Nov 2025, the limit is 100,000,000 files.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20file_ids)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores%20%3E%20(items)%20%3E%20(property)%20metadata)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_stores)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search)

[](#(resource)%20beta.threads%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema))

##### Returns Expand Collapse

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

Empty Messages

### Create thread

```
curl https://api.openai.com/v1/threads \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2" \
-d ''
```

```
{
"id": "thread_abc123",
"object": "thread",
"created_at": 1699012949,
"metadata": {},
"tool_resources": {}
}
```

### Create thread

```
curl https://api.openai.com/v1/threads \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"messages": [{
"role": "user",
"content": "Hello, what is AI?"
}, {
"role": "user",
"content": "How does AI work? Explain it in simple terms."
}]
}'
```

```
{
"id": "thread_abc123",
"object": "thread",
"created_at": 1699014083,
"metadata": {},
"tool_resources": {}
}
```

##### Returns Examples

```
{
"id": "id",
"created_at": 0,
"metadata": {
"foo": "string"
},
"object": "thread",
"tool_resources": {
"code_interpreter": {
"file_ids": [
"string"
]
},
"file_search": {
"vector_store_ids": [
"string"
]
}
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/create
