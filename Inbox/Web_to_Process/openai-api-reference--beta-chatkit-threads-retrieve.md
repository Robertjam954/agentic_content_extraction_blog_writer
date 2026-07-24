---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve
title: "Retrieve ChatKit thread"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve ChatKit thread

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads)

# Retrieve ChatKit thread

GET /chatkit/threads/{thread_id}

Retrieve a ChatKit thread by its identifier.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20thread_id%20%3E%20(schema))

##### Returns Expand Collapse

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

### Retrieve ChatKit thread

```
curl https://api.openai.com/v1/chatkit/threads/cthr_abc123 \
-H "OpenAI-Beta: chatkit_beta=v1" \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "cthr_abc123",
"object": "chatkit.thread",
"title": "Customer escalation",
"items": {
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
"has_more": false
}
}
```

##### Returns Examples

```
{
"id": "cthr_abc123",
"object": "chatkit.thread",
"title": "Customer escalation",
"items": {
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
"has_more": false
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve
