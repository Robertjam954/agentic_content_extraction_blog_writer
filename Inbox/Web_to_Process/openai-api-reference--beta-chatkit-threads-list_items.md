---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list_items
title: "List ChatKit thread items"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List ChatKit thread items

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads)

# List ChatKit thread items

GET /chatkit/threads/{thread_id}/items

List items that belong to a ChatKit thread.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20thread_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

List items created after this thread item ID. Defaults to null for the first page.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

before : optional string

List items created before this thread item ID. Defaults to null for the newest results.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20before%20%3E%20(schema))

limit : optional number

Maximum number of thread items to return. Defaults to 20.

minimum 0

maximum 100

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order for results by creation time. Defaults to `desc`.

One of the following:

"asc"

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list_items%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

ChatKitThreadItemList object { data , first_id , has_more , 2 more }

A paginated list of thread items rendered for the ChatKit API.

data : array of [ChatKitThreadUserMessageItem](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)) { id , attachments , content , 5 more } or [ChatKitThreadAssistantMessageItem](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)) { id , content , created_at , 3 more } or [ChatKitWidgetItem](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)) { id , created_at , object , 3 more } or 3 more

A list of items

One of the following:

ChatKitThreadUserMessageItem object { id , attachments , content , 5 more }

User-authored messages within a thread.

id : string

Identifier of the thread item.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20id)

attachments : array of [ChatKitAttachment](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)) { id , mime_type , name , 2 more }

Attachments associated with the user message. Defaults to an empty list.

id : string

Identifier for the attachment.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)%20%3E%20(property)%20id)

mime_type : string

MIME type of the attachment.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)%20%3E%20(property)%20mime_type)

name : string

Original display name for the attachment.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)%20%3E%20(property)%20name)

preview_url : string

Preview URL for rendering the attachment inline.

format uri

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)%20%3E%20(property)%20preview_url)

type : "image" or "file"

Attachment discriminator.

One of the following:

"image"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"file"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20attachments)

content : array of object { text , type } or object { text , type }

Ordered content elements supplied by the user.

One of the following:

InputText object { text , type }

Text block that a user contributed to the thread.

text : string

Plain-text content supplied by the user.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20text)

type : "input_text"

Type discriminator that is always `input_text`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(variant)%200)

QuotedText object { text , type }

Quoted snippet that the user referenced in their message.

text : string

Quoted text content.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20text)

type : "quoted_text"

Type discriminator that is always `quoted_text`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20content)

created_at : number

Unix timestamp (in seconds) for when the item was created.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20created_at)

inference_options : object { model , tool_choice }

Inference overrides applied to the message. Defaults to null when unset.

model : string

Model name that generated the response. Defaults to null when using the session default.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20inference_options%20%3E%20(property)%20model)

tool_choice : object { id }

Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

id : string

Identifier of the requested tool.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20inference_options%20%3E%20(property)%20tool_choice%20%3E%20(property)%20id)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20inference_options%20%3E%20(property)%20tool_choice)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20inference_options)

object : "chatkit.thread_item"

Type discriminator that is always `chatkit.thread_item`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20object)

thread_id : string

Identifier of the parent thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20thread_id)

type : "chatkit.user_message"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_user_message_item%20%3E%20(schema))

ChatKitThreadAssistantMessageItem object { id , content , created_at , 3 more }

Assistant-authored message within a thread.

id : string

Identifier of the thread item.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)%20%3E%20(property)%20id)

content : array of [ChatKitResponseOutputText](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)) { annotations , text , type }

Ordered assistant response segments.

annotations : array of object { source , type } or object { source , type }

Ordered list of annotations attached to the response text.

One of the following:

File object { source , type }

Annotation that references an uploaded file.

source : object { filename , type }

File attachment referenced by the annotation.

filename : string

Filename referenced by the annotation.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20source%20%3E%20(property)%20filename)

type : "file"

Type discriminator that is always `file`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20source%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20source)

type : "file"

Type discriminator that is always `file` for this annotation.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%200)

URL object { source , type }

Annotation that references a URL.

source : object { type , url }

URL referenced by the annotation.

type : "url"

Type discriminator that is always `url`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20source%20%3E%20(property)%20type)

url : string

URL referenced by the annotation.

format uri

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20source%20%3E%20(property)%20url)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20source)

type : "url"

Type discriminator that is always `url` for this annotation.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20annotations)

text : string

Assistant generated text.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "output_text"

Type discriminator that is always `output_text`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)%20%3E%20(property)%20content)

created_at : number

Unix timestamp (in seconds) for when the item was created.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "chatkit.thread_item"

Type discriminator that is always `chatkit.thread_item`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)%20%3E%20(property)%20object)

thread_id : string

Identifier of the parent thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)%20%3E%20(property)%20thread_id)

type : "chatkit.assistant_message"

Type discriminator that is always `chatkit.assistant_message`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_assistant_message_item%20%3E%20(schema))

ChatKitWidgetItem object { id , created_at , object , 3 more }

Thread item that renders a widget payload.

id : string

Identifier of the thread item.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) for when the item was created.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "chatkit.thread_item"

Type discriminator that is always `chatkit.thread_item`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)%20%3E%20(property)%20object)

thread_id : string

Identifier of the parent thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)%20%3E%20(property)%20thread_id)

type : "chatkit.widget"

Type discriminator that is always `chatkit.widget`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)%20%3E%20(property)%20type)

widget : string

Serialized widget payload rendered in the UI.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema)%20%3E%20(property)%20widget)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_widget_item%20%3E%20(schema))

ChatKitClientToolCall object { id , arguments , call_id , 7 more }

Record of a client side tool invocation initiated by the assistant.

id : string

Identifier of the thread item.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id)

arguments : string

JSON-encoded arguments that were sent to the tool.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20arguments)

call_id : string

Identifier for the client tool call.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20call_id)

created_at : number

Unix timestamp (in seconds) for when the item was created.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20created_at)

name : string

Tool name that was invoked.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20name)

object : "chatkit.thread_item"

Type discriminator that is always `chatkit.thread_item`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20object)

output : string

JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20output)

status : "in_progress" or "completed"

Execution status for the tool call.

One of the following:

"in_progress"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%200)

"completed"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20status)

thread_id : string

Identifier of the parent thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20thread_id)

type : "chatkit.client_tool_call"

Type discriminator that is always `chatkit.client_tool_call`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%203)

ChatKitTask object { id , created_at , heading , 5 more }

Task emitted by the workflow to show progress and status updates.

id : string

Identifier of the thread item.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) for when the item was created.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20created_at)

heading : string

Optional heading for the task. Defaults to null when not provided.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20heading)

object : "chatkit.thread_item"

Type discriminator that is always `chatkit.thread_item`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20object)

summary : string

Optional summary that describes the task. Defaults to null when omitted.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20summary)

task_type : "custom" or "thought"

Subtype for the task.

One of the following:

"custom"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20task_type%20%3E%20(member)%200)

"thought"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20task_type%20%3E%20(member)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20task_type)

thread_id : string

Identifier of the parent thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20thread_id)

type : "chatkit.task"

Type discriminator that is always `chatkit.task`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%204)

ChatKitTaskGroup object { id , created_at , object , 3 more }

Collection of workflow tasks grouped together in the thread.

id : string

Identifier of the thread item.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) for when the item was created.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20created_at)

object : "chatkit.thread_item"

Type discriminator that is always `chatkit.thread_item`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20object)

tasks : array of object { heading , summary , type }

Tasks included in the group.

heading : string

Optional heading for the grouped task. Defaults to null when not provided.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20tasks%20%3E%20(items)%20%3E%20(property)%20heading)

summary : string

Optional summary that describes the grouped task. Defaults to null when omitted.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20tasks%20%3E%20(items)%20%3E%20(property)%20summary)

type : "custom" or "thought"

Subtype for the grouped task.

One of the following:

"custom"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20tasks%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"thought"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20tasks%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20tasks%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20tasks)

thread_id : string

Identifier of the parent thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20thread_id)

type : "chatkit.task_group"

Type discriminator that is always `chatkit.task_group`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(variant)%205)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20data)

first_id : string

The ID of the first item in the list.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20first_id)

has_more : boolean

Whether there are more items available.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20has_more)

last_id : string

The ID of the last item in the list.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20last_id)

object : "list"

The type of object returned, must be `list`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread_item_list%20%3E%20(schema))

### List ChatKit thread items

```
curl "https://api.openai.com/v1/chatkit/threads/cthr_abc123/items?limit=3" \
-H "OpenAI-Beta: chatkit_beta=v1" \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"data": [
{
"id": "cthi_user_001",
"object": "chatkit.thread_item",
"type": "user_message",
"content": [
{
"type": "input_text",
"text": "I need help debugging an onboarding issue."
}
],
"attachments": []
},
{
"id": "cthi_assistant_002",
"object": "chatkit.thread_item",
"type": "assistant_message",
"content": [
{
"type": "output_text",
"text": "Let's start by confirming the workflow version you deployed."
}
]
}
],
"has_more": false,
"object": "list"
}
```

##### Returns Examples

```
{
"data": [
{
"id": "cthi_user_001",
"object": "chatkit.thread_item",
"type": "user_message",
"content": [
{
"type": "input_text",
"text": "I need help debugging an onboarding issue."
}
],
"attachments": []
},
{
"id": "cthi_assistant_002",
"object": "chatkit.thread_item",
"type": "assistant_message",
"content": [
{
"type": "output_text",
"text": "Let's start by confirming the workflow version you deployed."
}
]
}
],
"has_more": false,
"object": "list"
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list_items
