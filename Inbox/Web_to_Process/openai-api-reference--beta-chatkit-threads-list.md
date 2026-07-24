---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list
title: "List ChatKit threads"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List ChatKit threads

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads)

# List ChatKit threads

GET /chatkit/threads

List ChatKit threads with optional pagination and user filters.

##### Q uery Parameters Expand Collapse

after : optional string

List items created after this thread item ID. Defaults to null for the first page.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

before : optional string

List items created before this thread item ID. Defaults to null for the newest results.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20before%20%3E%20(schema))

limit : optional number

Maximum number of thread items to return. Defaults to 20.

minimum 0

maximum 100

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order for results by creation time. Defaults to `desc`.

One of the following:

"asc"

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

user : optional string

Filter threads that belong to this user identifier. Defaults to null to return all users.

minLength 1

maxLength 512

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20user%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [ChatKitThread](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id , created_at , object , 3 more }

A list of items

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

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

first_id : string

The ID of the first item in the list.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

has_more : boolean

Whether there are more items available.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

last_id : string

The ID of the last item in the list.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

object : "list"

The type of object returned, must be `list`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List ChatKit threads

```
curl "https://api.openai.com/v1/chatkit/threads?limit=2&order=desc" \
-H "OpenAI-Beta: chatkit_beta=v1" \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"data": [
{
"id": "cthr_abc123",
"object": "chatkit.thread",
"title": "Customer escalation"
},
{
"id": "cthr_def456",
"object": "chatkit.thread",
"title": "Demo feedback"
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
"id": "cthr_abc123",
"object": "chatkit.thread",
"title": "Customer escalation"
},
{
"id": "cthr_def456",
"object": "chatkit.thread",
"title": "Demo feedback"
}
],
"has_more": false,
"object": "list"
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list
