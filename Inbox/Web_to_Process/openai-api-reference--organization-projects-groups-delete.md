---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/groups/methods/delete
title: "Remove project group"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Remove project group

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups)

# Remove project group

DELETE /organization/projects/{project_id}/groups/{group_id}

Revokes a group’s access to a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

group_id : string

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

##### Returns Expand Collapse

deleted : boolean

Whether the group membership in the project was removed.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "project.group.deleted"

Always `project.group.deleted`.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Remove project group

```
curl -X DELETE https://api.openai.com/v1/organization/projects/proj_abc123/groups/group_01J1F8ABCDXYZ \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "project.group.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "project.group.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/groups/methods/delete
