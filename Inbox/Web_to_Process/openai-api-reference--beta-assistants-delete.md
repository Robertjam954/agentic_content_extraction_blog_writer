---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/methods/delete
title: "Delete assistant"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete assistant

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Assistants](/api/reference/resources/beta/subresources/assistants)

# Delete assistant

Deprecated

DELETE /assistants/{assistant_id}

Delete an assistant.

##### P ath Parameters Expand Collapse

assistant_id : string

[](#(resource)%20beta.assistants%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20assistant_id%20%3E%20(schema))

##### Returns Expand Collapse

AssistantDeleted object { id , deleted , object }

id : string

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "assistant.deleted"

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema))

### Delete assistant

```
curl https://api.openai.com/v1/assistants/asst_abc123 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2" \
-X DELETE
```

```
{
"id": "asst_abc123",
"object": "assistant.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "asst_abc123",
"object": "assistant.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/methods/delete
