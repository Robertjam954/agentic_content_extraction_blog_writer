---
source_url: https://developers.openai.com/api/reference/resources/evals/methods/delete
title: "Delete an eval"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete an eval

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Evals](/api/reference/resources/evals)

# Delete an eval

DELETE /evals/{eval_id}

Delete an evaluation.

##### P ath Parameters Expand Collapse

eval_id : string

[](#(resource)%20evals%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20eval_id%20%3E%20(schema))

##### Returns Expand Collapse

deleted : boolean

[](#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

eval_id : string

[](#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)%20%3E%20(property)%20eval_id)

object : string

[](#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete an eval

```
curl https://api.openai.com/v1/evals/eval_abc123 \
-X DELETE \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"object": "eval.deleted",
"deleted": true,
"eval_id": "eval_abc123"
}
```

##### Returns Examples

```
{
"object": "eval.deleted",
"deleted": true,
"eval_id": "eval_abc123"
}
```

---
Source: https://developers.openai.com/api/reference/resources/evals/methods/delete
