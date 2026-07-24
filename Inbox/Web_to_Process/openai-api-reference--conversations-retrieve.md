---
source_url: https://developers.openai.com/api/reference/resources/conversations/methods/retrieve
title: "Retrieve a conversation"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve a conversation

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Conversations](/api/reference/resources/conversations)

# Retrieve a conversation

GET /conversations/{conversation_id}

Get a conversation

##### P ath Parameters Expand Collapse

conversation_id : string

[](#(resource)%20conversations%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20conversation_id%20%3E%20(schema))

##### Returns Expand Collapse

Conversation object { id , created_at , metadata , object }

id : string

The unique ID of the conversation.

[](#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The time at which the conversation was created, measured in seconds since the Unix epoch.

format unixtime

[](#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)%20%3E%20(property)%20created_at)

metadata : unknown

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

[](#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)%20%3E%20(property)%20metadata)

object : "conversation"

The object type, which is always `conversation`.

[](#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema))

### Retrieve a conversation

```
curl https://api.openai.com/v1/conversations/conv_123 \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "conv_123",
"object": "conversation",
"created_at": 1741900000,
"metadata": {"topic": "demo"}
}
```

##### Returns Examples

```
{
"id": "conv_123",
"object": "conversation",
"created_at": 1741900000,
"metadata": {"topic": "demo"}
}
```

---
Source: https://developers.openai.com/api/reference/resources/conversations/methods/retrieve
