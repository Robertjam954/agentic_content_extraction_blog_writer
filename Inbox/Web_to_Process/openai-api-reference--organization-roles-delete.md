---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/roles/methods/delete
title: "Delete organization role"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete organization role

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/roles)

# Delete organization role

DELETE /organization/roles/{role_id}

Deletes a custom role from the organization.

##### P ath Parameters Expand Collapse

role_id : string

[](#(resource)%20admin.organization.roles%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20role_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Identifier of the deleted role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the role was deleted.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "role.deleted"

Always `role.deleted`.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete organization role

```
curl -X DELETE https://api.openai.com/v1/organization/roles/role_01J1F8ROLE01 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "role.deleted",
"id": "role_01J1F8ROLE01",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "role.deleted",
"id": "role_01J1F8ROLE01",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/roles/methods/delete
