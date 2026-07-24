---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/sessions/methods/create
title: "Create ChatKit session"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create ChatKit session

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Sessions](/api/reference/resources/beta/subresources/chatkit/subresources/sessions)

# Create ChatKit session

POST /chatkit/sessions

Create a ChatKit session.

##### Body Parameters JSON Expand Collapse

user : string

A free-form string that identifies your end user; ensures this Session can access other objects that have the same `user` scope.

minLength 1

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20user%20%3E%20(schema))

workflow : [ChatSessionWorkflowParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)) { id , state_variables , tracing , version }

Workflow that powers the session.

id : string

Identifier for the workflow invoked by the session.

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20id)

state_variables : optional map [ string or boolean or number ]

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

string

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%200)

boolean

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%201)

number

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20state_variables)

tracing : optional object { enabled }

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

enabled : optional boolean

Whether tracing is enabled during the session. Defaults to true.

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20tracing%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20tracing)

version : optional string

Specific workflow version to run. Defaults to the latest deployed version.

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)%20%3E%20(property)%20version)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20workflow%20%3E%20(schema))

chatkit_configuration : optional [ChatSessionChatKitConfigurationParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)) { automatic_thread_titling , file_upload , history }

Optional overrides for ChatKit runtime configuration features

automatic_thread_titling : optional object { enabled }

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

enabled : optional boolean

Enable automatic thread title generation. Defaults to true.

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20automatic_thread_titling%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20automatic_thread_titling)

file_upload : optional object { enabled , max_file_size , max_files }

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max_files 10, max_file_size 512 MB).

enabled : optional boolean

Enable uploads for this session. Defaults to false.

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%3E%20(property)%20enabled)

max_file_size : optional number

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum 512

minimum 1

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%3E%20(property)%20max_file_size)

max_files : optional number

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum 1

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%3E%20(property)%20max_files)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20file_upload)

history : optional object { enabled , recent_threads }

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent_threads (null).

enabled : optional boolean

Enables chat users to access previous ChatKit threads. Defaults to true.

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(property)%20enabled)

recent_threads : optional number

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum 1

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(property)%20recent_threads)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)%20%3E%20(property)%20history)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20chatkit_configuration%20%3E%20(schema))

expires_after : optional [ChatSessionExpiresAfterParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema)) { anchor , seconds }

Optional override for session expiration timing in seconds from creation. Defaults to 10 minutes.

anchor : "created_at"

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema)%20%3E%20(property)%20anchor)

seconds : number

Number of seconds after the anchor when the session expires.

maximum 600

minimum 1

format int64

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema)%20%3E%20(property)%20seconds)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema))

rate_limits : optional [ChatSessionRateLimitsParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits_param%20%3E%20(schema)) { max_requests_per_1_minute }

Optional override for per-minute request limits. When omitted, defaults to 10.

max_requests_per_1_minute : optional number

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum 1

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20rate_limits%20%3E%20(schema)%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits_param%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_minute)

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20rate_limits%20%3E%20(schema))

##### Returns Expand Collapse

ChatSession object { id , chatkit_configuration , client_secret , 7 more }

Represents a ChatKit session and its resolved configuration.

id : string

Identifier for the ChatKit session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20id)

chatkit_configuration : [ChatSessionChatKitConfiguration](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) { automatic_thread_titling , file_upload , history }

Resolved ChatKit feature configuration for the session.

automatic_thread_titling : [ChatSessionAutomaticThreadTitling](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) { enabled }

Automatic thread titling preferences.

enabled : boolean

Whether automatic thread titling is enabled.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20automatic_thread_titling%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20chatkit_configuration%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20automatic_thread_titling)

file_upload : [ChatSessionFileUpload](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) { enabled , max_file_size , max_files }

Upload settings for the session.

enabled : boolean

Indicates if uploads are enabled for the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)%20%3E%20(property)%20enabled)

max_file_size : number

Maximum upload size in megabytes.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)%20%3E%20(property)%20max_file_size)

max_files : number

Maximum number of uploads allowed during the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20file_upload%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)%20%3E%20(property)%20max_files)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20chatkit_configuration%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20file_upload)

history : [ChatSessionHistory](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) { enabled , recent_threads }

History retention configuration.

enabled : boolean

Indicates if chat history is persisted for the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20history%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)%20%3E%20(property)%20enabled)

recent_threads : number

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20history%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)%20%3E%20(property)%20recent_threads)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20chatkit_configuration%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)%20%3E%20(property)%20history)

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

max_requests_per_1_minute : number

Maximum allowed requests per one-minute window.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20rate_limits%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_minute)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20rate_limits)

status : [ChatSessionStatus](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

One of the following:

"active"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20status%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)%20%3E%20(member)%200)

"expired"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20status%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)%20%3E%20(member)%201)

"cancelled"

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20status%20%2B%20(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)%20%3E%20(member)%202)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20status)

user : string

User identifier associated with the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20user)

workflow : [ChatKitWorkflow](/api/reference/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) { id , state_variables , tracing , version }

Workflow metadata for the session.

id : string

Identifier of the workflow backing the session.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20id)

state_variables : map [ string or boolean or number ]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

string

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%200)

boolean

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%201)

number

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20state_variables)

tracing : object { enabled }

Tracing settings applied to the workflow.

enabled : boolean

Indicates whether tracing is enabled.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20tracing%20%3E%20(property)%20enabled)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20tracing)

version : string

Specific workflow version used for the session. Defaults to null when using the latest deployment.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow%20%2B%20(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)%20%3E%20(property)%20version)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)%20%3E%20(property)%20workflow)

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema))

### Create ChatKit session

```
curl https://api.openai.com/v1/chatkit/sessions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: chatkit_beta=v1" \
-d '{
"workflow": {
"id": "workflow_alpha",
"version": "2024-10-01"
},
"scope": {
"project": "alpha",
"environment": "staging"
},
"expires_after": 1800,
"max_requests_per_1_minute": 60,
"max_requests_per_session": 500
}'
```

```
{
"client_secret": "chatkit_token_123",
"expires_at": 1735689600,
"workflow": {
"id": "workflow_alpha",
"version": "2024-10-01"
},
"scope": {
"project": "alpha",
"environment": "staging"
},
"max_requests_per_1_minute": 60,
"max_requests_per_session": 500,
"status": "active"
}
```

##### Returns Examples

```
{
"client_secret": "chatkit_token_123",
"expires_at": 1735689600,
"workflow": {
"id": "workflow_alpha",
"version": "2024-10-01"
},
"scope": {
"project": "alpha",
"environment": "staging"
},
"max_requests_per_1_minute": 60,
"max_requests_per_session": 500,
"status": "active"
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/sessions/methods/create
