---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/delete
title: "Delete ChatKit thread"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete ChatKit thread

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads)

# Delete ChatKit thread

DELETE /chatkit/threads/{thread_id}

Delete a ChatKit thread along with its items and stored attachments.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.chatkit.threads%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20thread_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Identifier of the deleted thread.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Indicates that the thread has been deleted.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.

[](#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete ChatKit thread

```
curl https://api.openai.com/v1/chatkit/threads/$THREAD_ID \
-X DELETE \
-H 'OpenAI-Beta: chatkit_beta=v1' \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "id",
"deleted": true,
"object": "chatkit.thread.deleted"
}
```

##### Returns Examples

```
{
"id": "id",
"deleted": true,
"object": "chatkit.thread.deleted"
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/delete
