---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/delete
title: "Delete thread"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete thread

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

# Delete thread

DELETE /threads/{thread_id}

Delete a thread.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.threads%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20thread_id%20%3E%20(schema))

##### Returns Expand Collapse

ThreadDeleted object { id , deleted , object }

id : string

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "thread.deleted"

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema))

### Delete thread

```
curl https://api.openai.com/v1/threads/thread_abc123 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2" \
-X DELETE
```

```
{
"id": "thread_abc123",
"object": "thread.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "thread_abc123",
"object": "thread.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/delete
