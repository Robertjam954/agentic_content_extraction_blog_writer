---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/users/subresources/roles/methods/delete
title: "Unassign organization role from user"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Unassign organization role from user

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Users](/api/reference/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles)

# Unassign organization role from user

DELETE /organization/users/{user_id}/roles/{role_id}

Unassigns an organization role from a user within the organization.

##### P ath Parameters Expand Collapse

user_id : string

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20user_id%20%3E%20(schema))

role_id : string

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20role_id%20%3E%20(schema))

##### Returns Expand Collapse

deleted : boolean

Whether the assignment was removed.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Unassign organization role from user

```
curl -X DELETE https://api.openai.com/v1/organization/users/user_abc123/roles/role_01J1F8ROLE01 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "user.role.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "user.role.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/users/subresources/roles/methods/delete
