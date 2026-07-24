---
source_url: https://developers.openai.com/api/reference/resources/conversations/methods/delete
title: "Delete a conversation"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete a conversation

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Conversations](/api/reference/resources/conversations)

# Delete a conversation

DELETE /conversations/{conversation_id}

Delete a conversation. Items in the conversation will not be deleted.

##### P ath Parameters Expand Collapse

conversation_id : string

[](#(resource)%20conversations%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20conversation_id%20%3E%20(schema))

##### Returns Expand Collapse

ConversationDeletedResource object { id , deleted , object }

id : string

[](#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "conversation.deleted"

[](#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema))

### Delete a conversation

```
curl -X DELETE https://api.openai.com/v1/conversations/conv_123 \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "conv_123",
"object": "conversation.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "conv_123",
"object": "conversation.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/conversations/methods/delete
