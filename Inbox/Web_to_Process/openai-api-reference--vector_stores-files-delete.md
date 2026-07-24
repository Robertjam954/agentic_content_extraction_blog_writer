---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/methods/delete
title: "Delete vector store file"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete vector store file

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

[Files](/api/reference/resources/vector_stores/subresources/files)

# Delete vector store file

DELETE /vector_stores/{vector_store_id}/files/{file_id}

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](/docs/api-reference/files/delete) endpoint.

##### P ath Parameters Expand Collapse

vector_store_id : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20vector_store_id%20%3E%20(schema))

file_id : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20file_id%20%3E%20(schema))

##### Returns Expand Collapse

VectorStoreFileDeleted object { id , deleted , object }

id : string

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "vector_store.file.deleted"

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema))

### Delete vector store file

```
curl https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123 \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2" \
-X DELETE
```

```
{
id: "file-abc123",
object: "vector_store.file.deleted",
deleted: true
}
```

##### Returns Examples

```
{
id: "file-abc123",
object: "vector_store.file.deleted",
deleted: true
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/methods/delete
