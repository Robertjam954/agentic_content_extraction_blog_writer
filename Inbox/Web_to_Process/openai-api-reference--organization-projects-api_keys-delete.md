---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/api_keys/methods/delete
title: "Delete project API key"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete project API key

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

# Delete project API key

DELETE /organization/projects/{project_id}/api_keys/{api_key_id}

Deletes an API key from the project.

Returns confirmation of the key deletion, or an error if the key belonged to
a service account.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

api_key_id : string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20api_key_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.project.api_key.deleted"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete project API key

```
curl -X DELETE https://api.openai.com/v1/organization/projects/proj_abc/api_keys/key_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "organization.project.api_key.deleted",
"id": "key_abc",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "organization.project.api_key.deleted",
"id": "key_abc",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/api_keys/methods/delete
