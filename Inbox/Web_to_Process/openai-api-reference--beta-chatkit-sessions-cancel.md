---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel
title: "Cancel chat session"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Cancel chat session

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Sessions](/api/reference/resources/beta/subresources/chatkit/subresources/sessions)

# Cancel chat session

POST /chatkit/sessions/{session_id}/cancel

Cancel an active ChatKit session and return its most recent metadata.

Cancelling prevents new requests from using the issued client secret.

##### P ath Parameters Expand Collapse

session_id : string

[](#(resource)%20beta.chatkit.sessions%20%3E%20(method)%20cancel%20%3E%20(params)%20default%20%3E%20(param)%20session_id%20%3E%20(schema))

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

### Cancel chat session

```
curl -X POST \
https://api.openai.com/v1/chatkit/sessions/cksess_123/cancel \
-H "OpenAI-Beta: chatkit_beta=v1" \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "cksess_123",
"object": "chatkit.session",
"workflow": {
"id": "workflow_alpha",
"version": "1"
},
"scope": {
"customer_id": "cust_456"
},
"max_requests_per_1_minute": 30,
"ttl_seconds": 900,
"status": "cancelled",
"cancelled_at": 1712345678
}
```

##### Returns Examples

```
{
"id": "cksess_123",
"object": "chatkit.session",
"workflow": {
"id": "workflow_alpha",
"version": "1"
},
"scope": {
"customer_id": "cust_456"
},
"max_requests_per_1_minute": 30,
"ttl_seconds": 900,
"status": "cancelled",
"cancelled_at": 1712345678
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel
