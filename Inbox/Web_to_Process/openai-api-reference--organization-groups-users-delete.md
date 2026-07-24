---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users/methods/delete
title: "Remove group user"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Remove group user

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users)

# Remove group user

DELETE /organization/groups/{group_id}/users/{user_id}

Removes a user from a group.

##### P ath Parameters Expand Collapse

group_id : string

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

user_id : string

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20user_id%20%3E%20(schema))

##### Returns Expand Collapse

deleted : boolean

Whether the group membership was removed.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "group.user.deleted"

Always `group.user.deleted`.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Remove group user

```
curl -X DELETE https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ/users/user_abc123 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "group.user.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "group.user.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users/methods/delete
