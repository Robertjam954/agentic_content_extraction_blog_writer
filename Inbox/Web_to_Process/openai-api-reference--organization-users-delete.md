---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/users/methods/delete
title: "Delete user"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete user

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Users](/api/reference/resources/admin/subresources/organization/subresources/users)

# Delete user

DELETE /organization/users/{user_id}

Deletes a user from the organization.

##### P ath Parameters Expand Collapse

user_id : string

[](#(resource)%20admin.organization.users%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20user_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.user.deleted"

[](#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete user

```
curl -X DELETE https://api.openai.com/v1/organization/users/user_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "organization.user.deleted",
"id": "user_abc",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "organization.user.deleted",
"id": "user_abc",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/users/methods/delete
