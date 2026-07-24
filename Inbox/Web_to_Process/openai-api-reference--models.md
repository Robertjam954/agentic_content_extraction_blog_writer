---
source_url: https://developers.openai.com/api/reference/resources/models
title: "Models"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Models

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/resources/models/methods/list)

GET /models

##### [Retrieve model](/api/reference/resources/models/methods/retrieve)

GET /models/{model}

##### [Delete a fine-tuned model](/api/reference/resources/models/methods/delete)

DELETE /models/{model}

##### Models Expand Collapse

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

ModelDeleted object { id , deleted , object }

id : string

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : string

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/models
