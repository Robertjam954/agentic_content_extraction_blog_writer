---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/methods/content
title: "Retrieve vector store file content"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve vector store file content

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

[Files](/api/reference/resources/vector_stores/subresources/files)

# Retrieve vector store file content

GET /vector_stores/{vector_store_id}/files/{file_id}/content

Retrieve the parsed contents of a vector store file.

##### P ath Parameters Expand Collapse

vector_store_id : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20content%20%3E%20(params)%20default%20%3E%20(param)%20vector_store_id%20%3E%20(schema))

file_id : string

[](#(resource)%20vector_stores.files%20%3E%20(method)%20content%20%3E%20(params)%20default%20%3E%20(param)%20file_id%20%3E%20(schema))

##### Returns Expand Collapse

data : array of object { text , type }

Parsed content of the file.

text : optional string

The text content

[](#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)%20%3E%20(property)%20text)

type : optional string

The content type (currently only `"text"`)

[](#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores.files%20%3E%20(method)%20content%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

Indicates if there are more content pages to fetch.

[](#(resource)%20vector_stores.files%20%3E%20(method)%20content%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

next_page : string

The token for the next page, if any.

[](#(resource)%20vector_stores.files%20%3E%20(method)%20content%20%3E%20(network%20schema)%20%3E%20(property)%20next_page)

object : "vector_store.file_content.page"

The object type, which is always `vector_store.file_content.page`

[](#(resource)%20vector_stores.files%20%3E%20(method)%20content%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### Retrieve vector store file content

```
curl \
https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123/content \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"file_id": "file-abc123",
"filename": "example.txt",
"attributes": {"key": "value"},
"content": [
{"type": "text", "text": "..."},
...
]
}
```

##### Returns Examples

```
{
"file_id": "file-abc123",
"filename": "example.txt",
"attributes": {"key": "value"},
"content": [
{"type": "text", "text": "..."},
...
]
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/methods/content
