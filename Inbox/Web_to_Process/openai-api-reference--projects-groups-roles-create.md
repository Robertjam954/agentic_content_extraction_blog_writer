---
source_url: https://developers.openai.com/api/reference/resources/projects/subresources/groups/subresources/roles/methods/create
title: "Assign project role to group"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Assign project role to group

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles)

# Assign project role to group

POST /projects/{project_id}/groups/{group_id}/roles

Assigns a project role to a group within a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

group_id : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

role_id : string

Identifier of the role to assign.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20role_id%20%3E%20(schema))

##### Returns Expand Collapse

group : object { id , created_at , name , 2 more }

Summary information about a group returned in role assignment responses.

id : string

Identifier for the group.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the group was created.

format unixtime

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20created_at)

name : string

Display name of the group.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20name)

object : "group"

Always `group`.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20object)

scim_managed : boolean

Whether the group is managed through SCIM.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20scim_managed)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group)

object : "group.role"

Always `group.role`.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

role : [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id , description , name , 4 more }

Details about a role that can be assigned through the public Roles API.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%2B%20(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20id)

description : string

Optional description of the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%2B%20(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20description)

name : string

Unique name for the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%2B%20(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20name)

object : "role"

Always `role`.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%2B%20(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20object)

permissions : array of string

Permissions granted by the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%2B%20(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined and managed by OpenAI.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%2B%20(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role is bound to (for example `api.organization` or `api.project`).

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%2B%20(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20resource_type)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role)

### Assign project role to group

```
curl -X POST https://api.openai.com/v1/projects/proj_abc123/groups/group_01J1F8ABCDXYZ/roles \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"role_id": "role_01J1F8PROJ"
}'
```

```
{
"object": "group.role",
"group": {
"object": "group",
"id": "group_01J1F8ABCDXYZ",
"name": "Support Team",
"created_at": 1711471533,
"scim_managed": false
},
"role": {
"object": "role",
"id": "role_01J1F8PROJ",
"name": "API Project Key Manager",
"description": "Allows managing API keys for the project",
"permissions": [
"api.organization.projects.api_keys.read",
"api.organization.projects.api_keys.write"
],
"resource_type": "api.project",
"predefined_role": false
}
}
```

##### Returns Examples

```
{
"object": "group.role",
"group": {
"object": "group",
"id": "group_01J1F8ABCDXYZ",
"name": "Support Team",
"created_at": 1711471533,
"scim_managed": false
},
"role": {
"object": "role",
"id": "role_01J1F8PROJ",
"name": "API Project Key Manager",
"description": "Allows managing API keys for the project",
"permissions": [
"api.organization.projects.api_keys.read",
"api.organization.projects.api_keys.write"
],
"resource_type": "api.project",
"predefined_role": false
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/projects/subresources/groups/subresources/roles/methods/create
