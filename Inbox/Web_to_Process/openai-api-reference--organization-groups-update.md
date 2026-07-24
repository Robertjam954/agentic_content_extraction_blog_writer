---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/update
title: "Update group"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Update group

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

# Update group

POST /organization/groups/{group_id}

Updates a group’s information.

##### P ath Parameters Expand Collapse

group_id : string

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

name : string

New display name for the group.

minLength 1

maxLength 255

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Identifier for the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the group was created.

format unixtime

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

is_scim_managed : boolean

Whether the group is managed through SCIM and controlled by your identity provider.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20is_scim_managed)

name : string

Updated display name for the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20name)

### Update group

```
curl -X POST https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "Escalations"
}'
```

```
{
"id": "group_01J1F8ABCDXYZ",
"name": "Escalations",
"created_at": 1711471533,
"is_scim_managed": false
}
```

##### Returns Examples

```
{
"id": "group_01J1F8ABCDXYZ",
"name": "Escalations",
"created_at": 1711471533,
"is_scim_managed": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/update
