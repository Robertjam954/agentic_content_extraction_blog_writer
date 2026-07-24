---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users/methods/create
title: "Add group user"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Add group user

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users)

# Add group user

POST /organization/groups/{group_id}/users

Adds a user to a group.

##### P ath Parameters Expand Collapse

group_id : string

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

user_id : string

Identifier of the user to add to the group.

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20user_id%20%3E%20(schema))

##### Returns Expand Collapse

group_id : string

Identifier of the group the user was added to.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)%20%3E%20(property)%20group_id)

object : "group.user"

Always `group.user`.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

user_id : string

Identifier of the user that was added.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)%20%3E%20(property)%20user_id)

### Add group user

```
curl -X POST https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ/users \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"user_id": "user_abc123"
}'
```

```
{
"object": "group.user",
"user_id": "user_abc123",
"group_id": "group_01J1F8ABCDXYZ"
}
```

##### Returns Examples

```
{
"object": "group.user",
"user_id": "user_abc123",
"group_id": "group_01J1F8ABCDXYZ"
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users/methods/create
