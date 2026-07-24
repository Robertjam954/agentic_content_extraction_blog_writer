---
source_url: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete
title: "Delete checkpoint permission"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete checkpoint permission

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

[Checkpoints](/api/reference/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

# Delete checkpoint permission

DELETE /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### P ath Parameters Expand Collapse

fine_tuned_model_checkpoint : string

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20fine_tuned_model_checkpoint%20%3E%20(schema))

permission_id : string

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20permission_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

The ID of the fine-tuned model checkpoint permission that was deleted.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the fine-tuned model checkpoint permission was successfully deleted.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete checkpoint permission

```
curl https://api.openai.com/v1/fine_tuning/checkpoints/ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd/permissions/cp_zc4Q7MP6XxulcVzj4MZdwsAB \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"object": "checkpoint.permission",
"id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "checkpoint.permission",
"id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete
