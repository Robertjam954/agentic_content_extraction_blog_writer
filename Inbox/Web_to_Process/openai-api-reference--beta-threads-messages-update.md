---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/messages/methods/update
title: "Modify message"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Modify message

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

[Messages](/api/reference/resources/beta/subresources/threads/subresources/messages)

# Modify message

POST /threads/{thread_id}/messages/{message_id}

Modifies a message.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.threads.messages%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20thread_id%20%3E%20(schema))

message_id : string

[](#(resource)%20beta.threads.messages%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20message_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads.messages%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20metadata%20%3E%20(schema))

##### Returns Expand Collapse

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

TextContentBlock object { text , type }

The text content that is part of a message.

text : [Text](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations , value }

annotations : array of [FileCitationAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end_index , file_citation , start_index , 2 more } or [FilePathAnnotation](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end_index , file_path , start_index , 2 more }

One of the following:

FileCitationAnnotation object { end_index , file_citation , start_index , 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file_search” tool to search files.

end_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_citation : object { file_id }

file_id : string

The ID of the specific File the citation is from.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20file_citation)

start_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

type : "file_citation"

Always `file_citation`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema))

FilePathAnnotation object { end_index , file_path , start_index , 2 more }

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20end_index)

file_path : object { file_id }

file_id : string

The ID of the file that was generated.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20file_path)

start_index : number

minimum 0

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20start_index)

text : string

The text in the message content that needs to be replaced.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20text)

type : "file_path"

Always `file_path`.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema))

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)%20%3E%20(property)%20annotations)

value : string

The data that makes up the text.

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)%20%3E%20(property)%20text%20%2B%20(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)%20%3E%20(property)%20value)

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

### Modify message

```
curl https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"metadata": {
"modified": "true",
"user": "abc123"
}
}'
```

```
{
"id": "msg_abc123",
"object": "thread.message",
"created_at": 1699017614,
"assistant_id": null,
"thread_id": "thread_abc123",
"run_id": null,
"role": "user",
"content": [
{
"type": "text",
"text": {
"value": "How does AI work? Explain it in simple terms.",
"annotations": []
}
}
],
"file_ids": [],
"metadata": {
"modified": "true",
"user": "abc123"
}
}
```

##### Returns Examples

```
{
"id": "msg_abc123",
"object": "thread.message",
"created_at": 1699017614,
"assistant_id": null,
"thread_id": "thread_abc123",
"run_id": null,
"role": "user",
"content": [
{
"type": "text",
"text": {
"value": "How does AI work? Explain it in simple terms.",
"annotations": []
}
}
],
"file_ids": [],
"metadata": {
"modified": "true",
"user": "abc123"
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/messages/methods/update
