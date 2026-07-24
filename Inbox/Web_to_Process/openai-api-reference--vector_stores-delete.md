---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/methods/delete
title: "Delete vector store"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete vector store

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

# Delete vector store

DELETE /vector_stores/{vector_store_id}

Delete a vector store.

##### P ath Parameters Expand Collapse

vector_store_id : string

[](#(resource)%20vector_stores%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20vector_store_id%20%3E%20(schema))

##### Returns Expand Collapse

VectorStoreDeleted object { id , deleted , object }

id : string

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "vector_store.deleted"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema))

### Delete vector store

```
curl https://api.openai.com/v1/vector_stores/vs_abc123 \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2" \
-X DELETE
```

```
{
id: "vs_abc123",
object: "vector_store.deleted",
deleted: true
}
```

##### Returns Examples

```
{
id: "vs_abc123",
object: "vector_store.deleted",
deleted: true
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/methods/delete
