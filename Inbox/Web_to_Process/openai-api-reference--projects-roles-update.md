---
source_url: https://developers.openai.com/api/reference/resources/projects/subresources/roles/methods/update
title: "Update project role"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Update project role

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles)

# Update project role

POST /projects/{project_id}/roles/{role_id}

Updates an existing project role.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

role_id : string

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20role_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

description : optional string

New description for the role.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20description%20%3E%20(schema))

permissions : optional array of string

Updated set of permissions for the role.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20permissions%20%3E%20(schema))

role_name : optional string

New name for the role.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20role_name%20%3E%20(schema))

##### Returns Expand Collapse

Role object { id , description , name , 4 more }

Details about a role that can be assigned through the public Roles API.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20id)

description : string

Optional description of the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20description)

name : string

Unique name for the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20name)

object : "role"

Always `role`.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20object)

permissions : array of string

Permissions granted by the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined and managed by OpenAI.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role is bound to (for example `api.organization` or `api.project`).

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20resource_type)

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

### Update project role

```
curl -X POST https://api.openai.com/v1/projects/proj_abc123/roles/role_01J1F8PROJ \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"role_name": "API Project Key Manager",
"permissions": [
"api.organization.projects.api_keys.read",
"api.organization.projects.api_keys.write"
],
"description": "Allows managing API keys for the project"
}'
```

```
{
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
```

##### Returns Examples

```
{
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
```

---
Source: https://developers.openai.com/api/reference/resources/projects/subresources/roles/methods/update
