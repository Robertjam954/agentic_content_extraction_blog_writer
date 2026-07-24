---
source_url: https://developers.openai.com/api/reference/resources/models/methods/retrieve
title: "Retrieve model"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve model

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Models](/api/reference/resources/models)

# Retrieve model

GET /models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### P ath Parameters Expand Collapse

model : string

[](#(resource)%20models%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20model%20%3E%20(schema))

##### Returns Expand Collapse

Model object { id , created , object , owned_by }

Describes an OpenAI model offering that can be used with the API.

id : string

The model identifier, which can be referenced in the API endpoints.

[](#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)%20%3E%20(property)%20id)

created : number

The Unix timestamp (in seconds) when the model was created.

format unixtime

[](#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)%20%3E%20(property)%20created)

object : "model"

The object type, which is always “model”.

[](#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)%20%3E%20(property)%20object)

owned_by : string

The organization that owns the model.

[](#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)%20%3E%20(property)%20owned_by)

[](#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema))

### Retrieve model

```
curl https://api.openai.com/v1/models/VAR_chat_model_id \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "VAR_chat_model_id",
"object": "model",
"created": 1686935002,
"owned_by": "openai"
}
```

##### Returns Examples

```
{
"id": "VAR_chat_model_id",
"object": "model",
"created": 1686935002,
"owned_by": "openai"
}
```

---
Source: https://developers.openai.com/api/reference/resources/models/methods/retrieve
