---
source_url: https://developers.openai.com/api/reference/resources/projects/subresources/groups/subresources/roles/methods/delete
title: "Unassign project role from group"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Unassign project role from group

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles)

# Unassign project role from group

DELETE /projects/{project_id}/groups/{group_id}/roles/{role_id}

Unassigns a project role from a group within a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

group_id : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

role_id : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20role_id%20%3E%20(schema))

##### Returns Expand Collapse

deleted : boolean

Whether the assignment was removed.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Unassign project role from group

```
curl -X DELETE https://api.openai.com/v1/projects/proj_abc123/groups/group_01J1F8ABCDXYZ/roles/role_01J1F8PROJ \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "group.role.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "group.role.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/projects/subresources/groups/subresources/roles/methods/delete
