---
source_url: https://developers.openai.com/api/reference/resources/projects/subresources/roles/methods/delete
title: "Delete project role"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete project role

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles)

# Delete project role

DELETE /projects/{project_id}/roles/{role_id}

Deletes a custom role from a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

role_id : string

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20role_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Identifier of the deleted role.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the role was deleted.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "role.deleted"

Always `role.deleted`.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete project role

```
curl -X DELETE https://api.openai.com/v1/projects/proj_abc123/roles/role_01J1F8PROJ \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "role.deleted",
"id": "role_01J1F8PROJ",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "role.deleted",
"id": "role_01J1F8PROJ",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/projects/subresources/roles/methods/delete
