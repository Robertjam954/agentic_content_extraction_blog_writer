---
source_url: https://developers.openai.com/api/reference/resources/projects/subresources/roles/methods/list
title: "List project roles"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List project roles

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles)

# List project roles

GET /projects/{project_id}/roles

Lists the roles configured for a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing roles.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of roles to return. Defaults to 1000.

minimum 0

maximum 1000

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order for the returned roles.

One of the following:

"asc"

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id , description , name , 4 more }

Roles returned in the current page.

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

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

Whether more roles are available when paginating.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

next : string

Cursor to fetch the next page of results, or `null` when there are no additional roles.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20next)

object : "list"

Always `list`.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List project roles

```
curl https://api.openai.com/v1/projects/proj_abc123/roles?limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
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
],
"has_more": false,
"next": null
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
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
],
"has_more": false,
"next": null
}
```

---
Source: https://developers.openai.com/api/reference/resources/projects/subresources/roles/methods/list
