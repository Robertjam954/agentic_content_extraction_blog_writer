---
source_url: https://developers.openai.com/api/reference/resources/containers/methods/delete
title: "Delete a container"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete a container

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

# Delete a container

DELETE /containers/{container_id}

Delete Container

##### P ath Parameters Expand Collapse

container_id : string

[](#(resource)%20containers%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20container_id%20%3E%20(schema))

### Delete a container

```
curl -X DELETE https://api.openai.com/v1/containers/cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863 \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
"object": "container.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
"object": "container.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/containers/methods/delete
