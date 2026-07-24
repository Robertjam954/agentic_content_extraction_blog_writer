---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/messages/methods/delete
title: "Delete message"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete message

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

[Messages](/api/reference/resources/beta/subresources/threads/subresources/messages)

# Delete message

DELETE /threads/{thread_id}/messages/{message_id}

Deletes a message.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.threads.messages%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20thread_id%20%3E%20(schema))

message_id : string

[](#(resource)%20beta.threads.messages%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20message_id%20%3E%20(schema))

##### Returns Expand Collapse

MessageDeleted object { id , deleted , object }

id : string

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "thread.message.deleted"

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema))

### Delete message

```
curl -X DELETE https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2"
```

```
{
"id": "msg_abc123",
"object": "thread.message.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "msg_abc123",
"object": "thread.message.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/messages/methods/delete
