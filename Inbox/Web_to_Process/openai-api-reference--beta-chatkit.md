---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit
title: "ChatKit"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# ChatKit

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

# ChatKit

##### Models Expand Collapse

ChatKitWorkflow object { id , state_variables , tracing , version }

Workflow metadata and state returned for the session.

id : string

Identifier of the workflow backing the session.

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20id)

state_variables : map [ string or boolean or number ]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

string

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%200)

boolean

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%201)

number

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables)

tracing : object { enabled }

Tracing settings applied to the workflow.

enabled : boolean

Indicates whether tracing is enabled.

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20tracing%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20tracing)

version : string

Specific workflow version used for the session. Defaults to null when using the latest deployment.

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20version)

[](#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema))

#### ChatKit Sessions

##### [Cancel chat session](/api/reference/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

POST /chatkit/sessions/{session_id}/cancel

##### [Create ChatKit session](/api/reference/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

POST /chatkit/sessions

#### ChatKit Threads

##### [List ChatKit thread items](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)

GET /chatkit/threads/{thread_id}/items

##### [Retrieve ChatKit thread](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve)

GET /chatkit/threads/{thread_id}

##### [Delete ChatKit thread](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/delete)

DELETE /chatkit/threads/{thread_id}

##### [List ChatKit threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list)

GET /chatkit/threads

##### Models Expand Collapse

ChatSession object { id , chatkit_configuration , client_secret , 7 more }

Represents a ChatKit session and its resolved configuration.

id : string

Identifier for the ChatKit session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20id)

chatkit_configuration : [ChatSessionChatKitConfiguration](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) { automatic_thread_titling , file_upload , history }

Resolved ChatKit feature configuration for the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20chatkit_configuration)

client_secret : string

Ephemeral client secret that authenticates session requests.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20client_secret)

expires_at : number

Unix timestamp (in seconds) for when the session expires.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20expires_at)

max_requests_per_1_minute : number

Convenience copy of the per-minute request limit.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_minute)

object : "chatkit.session"

Type discriminator that is always `chatkit.session`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20object)

rate_limits : [ChatSessionRateLimits](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) { max_requests_per_1_minute }

Resolved rate limit values.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20rate_limits)

status : [ChatSessionStatus](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20status)

user : string

User identifier associated with the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20user)

workflow : [ChatKitWorkflow](/api/reference/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) { id , state_variables , tracing , version }

Workflow metadata for the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema))

ChatSessionAutomaticThreadTitling object { enabled }

Automatic thread title preferences for the session.

enabled : boolean

Whether automatic thread titling is enabled.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema))

ChatSessionChatKitConfiguration object { automatic_thread_titling , file_upload , history }

ChatKit configuration for the session.

automatic_thread_titling : [ChatSessionAutomaticThreadTitling](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) { enabled }

Automatic thread titling preferences.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20automatic_thread_titling)

file_upload : [ChatSessionFileUpload](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) { enabled , max_file_size , max_files }

Upload settings for the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20file_upload)

history : [ChatSessionHistory](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) { enabled , recent_threads }

History retention configuration.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20history)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema))

ChatSessionChatKitConfigurationParam object { automatic_thread_titling , file_upload , history }

Optional per-session configuration settings for ChatKit behavior.

automatic_thread_titling : optional object { enabled }

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

enabled : optional boolean

Enable automatic thread title generation. Defaults to true.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20automatic_thread_titling%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20automatic_thread_titling)

file_upload : optional object { enabled , max_file_size , max_files }

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max_files 10, max_file_size 512 MB).

enabled : optional boolean

Enable uploads for this session. Defaults to false.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%3E%20(property)%20enabled)

max_file_size : optional number

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum 512

minimum 1

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%3E%20(property)%20max_file_size)

max_files : optional number

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum 1

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%3E%20(property)%20max_files)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload)

history : optional object { enabled , recent_threads }

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent_threads (null).

enabled : optional boolean

Enables chat users to access previous ChatKit threads. Defaults to true.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(property)%20enabled)

recent_threads : optional number

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum 1

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(property)%20recent_threads)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20history)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema))

ChatSessionExpiresAfterParam object { anchor , seconds }

Controls when the session expires relative to an anchor timestamp.

anchor : "created_at"

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema)%20%3E%20(property)%20anchor)

seconds : number

Number of seconds after the anchor when the session expires.

maximum 600

minimum 1

format int64

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema)%20%3E%20(property)%20seconds)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema))

ChatSessionFileUpload object { enabled , max_file_size , max_files }

Upload permissions and limits applied to the session.

enabled : boolean

Indicates if uploads are enabled for the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)%20%3E%20(property)%20enabled)

max_file_size : number

Maximum upload size in megabytes.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)%20%3E%20(property)%20max_file_size)

max_files : number

Maximum number of uploads allowed during the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)%20%3E%20(property)%20max_files)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema))

ChatSessionHistory object { enabled , recent_threads }

History retention preferences returned for the session.

enabled : boolean

Indicates if chat history is persisted for the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)%20%3E%20(property)%20enabled)

recent_threads : number

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)%20%3E%20(property)%20recent_threads)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema))

ChatSessionRateLimits object { max_requests_per_1_minute }

Active per-minute request limit for the session.

max_requests_per_1_minute : number

Maximum allowed requests per one-minute window.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_minute)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema))

ChatSessionRateLimitsParam object { max_requests_per_1_minute }

Controls request rate limits for the session.

max_requests_per_1_minute : optional number

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum 1

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits_param%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_minute)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits_param%20%3E%20(schema))

ChatSessionStatus = "active" or "expired" or "cancelled"

One of the following:

"active"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)%20%3E%20(member)%200)

"expired"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)%20%3E%20(member)%201)

"cancelled"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)%20%3E%20(member)%202)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

ChatSessionWorkflowParam object { id , state_variables , tracing , version }

Workflow reference and overrides applied to the chat session.

id : string

Identifier for the workflow invoked by the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20id)

state_variables : optional map [ string or boolean or number ]

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

string

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%200)

boolean

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%201)

number

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables)

tracing : optional object { enabled }

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

enabled : optional boolean

Whether tracing is enabled during the session. Defaults to true.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20tracing%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20tracing)

version : optional string

Specific workflow version to run. Defaults to the latest deployed version.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20version)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema))

ChatKitAttachment object { id , mime_type , name , 2 more }

Attachment metadata included on thread items.

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

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_attachment%20%3E%20(schema))

ChatKitResponseOutputText object { annotations , text , type }

Assistant response text accompanied by optional annotations.

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

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_response_output_text%20%3E%20(schema))

ChatKitThread object { id , created_at , object , 3 more }

Represents a ChatKit thread and its current status.

id : string

Identifier of the thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) for when the thread was created.

format unixtime

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "chatkit.thread"

Type discriminator that is always `chatkit.thread`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20object)

status : object { type } or object { reason , type } or object { reason , type }

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

Active object { type }

Indicates that a thread is active.

type : "active"

Status discriminator that is always `active`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%200)

Locked object { reason , type }

Indicates that a thread is locked and cannot accept new input.

reason : string

Reason that the thread was locked. Defaults to null when no reason is recorded.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%201%20%3E%20(property)%20reason)

type : "locked"

Status discriminator that is always `locked`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%201)

Closed object { reason , type }

Indicates that a thread has been closed.

reason : string

Reason that the thread was closed. Defaults to null when no reason is recorded.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%202%20%3E%20(property)%20reason)

type : "closed"

Status discriminator that is always `closed`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(variant)%202)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20status)

title : string

Optional human-readable title for the thread. Defaults to null when no title has been generated.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20title)

user : string

Free-form string that identifies your end user who owns the thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)%20%3E%20(property)%20user)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema))

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

ThreadDeleteResponse object { id , deleted , object }

Confirmation payload returned after deleting a thread.

id : string

Identifier of the deleted thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Indicates that the thread has been deleted.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit
