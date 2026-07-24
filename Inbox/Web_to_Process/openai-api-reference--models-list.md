---
source_url: https://developers.openai.com/api/reference/resources/models/methods/list
title: "List models"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List models

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Models](/api/reference/resources/models)

# List models

GET /models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

##### Returns Expand Collapse

data : array of [Model](/api/reference/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id , created , object , owned_by }

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

[](#(resource)%20models%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

object : "list"

[](#(resource)%20models%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List models

```
curl https://api.openai.com/v1/models \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"object": "list",
"data": [
{
"id": "model-id-0",
"object": "model",
"created": 1686935002,
"owned_by": "organization-owner"
},
{
"id": "model-id-1",
"object": "model",
"created": 1686935002,
"owned_by": "organization-owner",
},
{
"id": "model-id-2",
"object": "model",
"created": 1686935002,
"owned_by": "openai"
},
]
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "model-id-0",
"object": "model",
"created": 1686935002,
"owned_by": "organization-owner"
},
{
"id": "model-id-1",
"object": "model",
"created": 1686935002,
"owned_by": "organization-owner",
},
{
"id": "model-id-2",
"object": "model",
"created": 1686935002,
"owned_by": "openai"
},
]
}
```

---
Source: https://developers.openai.com/api/reference/resources/models/methods/list
