---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/create
title: "Create group"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create group

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

# Create group

POST /organization/groups

Creates a new group in the organization.

##### Body Parameters JSON Expand Collapse

name : string

Human readable name for the group.

minLength 1

maxLength 255

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

##### Returns Expand Collapse

Group object { id , created_at , group_type , 2 more }

Details about an organization group.

id : string

Identifier for the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the group was created.

format unixtime

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20created_at)

group_type : "group" or "tenant_group"

The type of the group.

One of the following:

"group"

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%200)

"tenant_group"

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20group_type)

is_scim_managed : boolean

Whether the group is managed through SCIM and controlled by your identity provider.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20is_scim_managed)

name : string

Display name of the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))

### Create group

```
curl -X POST https://api.openai.com/v1/organization/groups \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "Support Team"
}'
```

```
{
"object": "group",
"id": "group_01J1F8ABCDXYZ",
"name": "Support Team",
"created_at": 1711471533,
"is_scim_managed": false
}
```

##### Returns Examples

```
{
"object": "group",
"id": "group_01J1F8ABCDXYZ",
"name": "Support Team",
"created_at": 1711471533,
"is_scim_managed": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/create
