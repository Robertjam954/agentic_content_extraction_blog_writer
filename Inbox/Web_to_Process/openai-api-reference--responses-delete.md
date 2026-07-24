---
source_url: https://developers.openai.com/api/reference/resources/responses/methods/delete
title: "Delete a model response"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete a model response

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Responses](/api/reference/resources/responses)

# Delete a model response

DELETE /responses/{response_id}

Deletes a model response with the given ID.

##### P ath Parameters Expand Collapse

response_id : string

[](#(resource)%20responses%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20response_id%20%3E%20(schema))

### Delete a model response

```
curl -X DELETE https://api.openai.com/v1/responses/resp_123 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "resp_6786a1bec27481909a17d673315b29f6",
"object": "response",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "resp_6786a1bec27481909a17d673315b29f6",
"object": "response",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/responses/methods/delete
