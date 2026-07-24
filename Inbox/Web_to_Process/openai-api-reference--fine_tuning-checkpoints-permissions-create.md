---
source_url: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create
title: "Create checkpoint permissions"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create checkpoint permissions

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

[Checkpoints](/api/reference/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

# Create checkpoint permissions

POST /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### P ath Parameters Expand Collapse

fine_tuned_model_checkpoint : string

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20fine_tuned_model_checkpoint%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

project_ids : array of string

The project identifiers to grant access to.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20project_ids%20%3E%20(schema))

##### Returns Expand Collapse

data : array of object { id , created_at , object , project_id }

id : string

The permission identifier, which can be referenced in the API endpoints.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the permission was created.

format unixtime

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

project_id : string

The project identifier that the permission is for.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20project_id)

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20create%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20create%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20create%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20create%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20create%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### Create checkpoint permissions

```
curl https://api.openai.com/v1/fine_tuning/checkpoints/ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd/permissions \
-H "Authorization: Bearer $OPENAI_API_KEY"
-d '{"project_ids": ["proj_abGMw1llN8IrBb6SvvY5A1iH"]}'
```

```
{
"object": "list",
"data": [
{
"object": "checkpoint.permission",
"id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"created_at": 1721764867,
"project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
}
],
"first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "checkpoint.permission",
"id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"created_at": 1721764867,
"project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
}
],
"first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create
