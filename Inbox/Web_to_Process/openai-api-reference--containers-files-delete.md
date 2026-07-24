---
source_url: https://developers.openai.com/api/reference/resources/containers/subresources/files/methods/delete
title: "Delete a container file"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete a container file

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

[Files](/api/reference/resources/containers/subresources/files)

# Delete a container file

DELETE /containers/{container_id}/files/{file_id}

Delete Container File

##### P ath Parameters Expand Collapse

container_id : string

[](#(resource)%20containers.files%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20container_id%20%3E%20(schema))

file_id : string

[](#(resource)%20containers.files%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20file_id%20%3E%20(schema))

### Delete a container file

```
curl -X DELETE https://api.openai.com/v1/containers/cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863/files/cfile_682e0e8a43c88191a7978f477a09bdf5 \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"object": "container.file.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"object": "container.file.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/containers/subresources/files/methods/delete
