---
source_url: https://developers.openai.com/api/reference/resources/models/methods/delete
title: "Delete a fine-tuned model"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete a fine-tuned model

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Models](/api/reference/resources/models)

# Delete a fine-tuned model

DELETE /models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

##### P ath Parameters Expand Collapse

model : string

[](#(resource)%20models%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20model%20%3E%20(schema))

##### Returns Expand Collapse

ModelDeleted object { id , deleted , object }

id : string

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : string

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema))

### Delete a fine-tuned model

```
curl https://api.openai.com/v1/models/ft:gpt-4o-mini:acemeco:suffix:abc123 \
-X DELETE \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
"object": "model",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
"object": "model",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/models/methods/delete
