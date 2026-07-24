---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/users/subresources/roles/methods/list
title: "List user organization role assignments"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List user organization role assignments

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Users](/api/reference/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles)

# List user organization role assignments

GET /organization/users/{user_id}/roles

Lists the organization roles assigned to a user within the organization.

##### P ath Parameters Expand Collapse

user_id : string

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20user_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing organization roles.

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of organization role assignments to return.

minimum 0

maximum 1000

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order for the returned organization roles.

One of the following:

"asc"

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of object { id , assignment_sources , created_at , 9 more }

Role assignments returned in the current page.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

assignment_sources : array of object { principal_id , principal_type }

Principals from which the role assignment is inherited, when available.

principal_id : string

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_id)

principal_type : string

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_type)

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources)

created_at : number

When the role was created.

format unixtime

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

created_by : string

Identifier of the actor who created the role.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by)

created_by_user_obj : map [ unknown ]

User details for the actor that created the role, when available.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by_user_obj)

description : string

Description of the role.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20description)

metadata : map [ unknown ]

Arbitrary metadata stored on the role.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

Name of the role.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

permissions : array of string

Permissions associated with the role.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined by OpenAI.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role applies to.

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type)

updated_at : number

When the role was last updated.

format unixtime

[](#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at)

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

Whether additional assignments are available when paginating.

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

next : string

Cursor to fetch the next page of results, or `null` when there are no more assignments.

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20next)

object : "list"

Always `list`.

[](#(resource)%20admin.organization.users.roles%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List user organization role assignments

```
curl https://api.openai.com/v1/organization/users/user_abc123/roles \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"id": "role_01J1F8ROLE01",
"name": "API Group Manager",
"permissions": [
"api.groups.read",
"api.groups.write"
],
"resource_type": "api.organization",
"predefined_role": false,
"description": "Allows managing organization groups",
"created_at": 1711471533,
"updated_at": 1711472599,
"created_by": "user_abc123",
"created_by_user_obj": {
"id": "user_abc123",
"name": "Ada Lovelace",
"email": "ada@example.com"
},
"metadata": {}
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
"id": "role_01J1F8ROLE01",
"name": "API Group Manager",
"permissions": [
"api.groups.read",
"api.groups.write"
],
"resource_type": "api.organization",
"predefined_role": false,
"description": "Allows managing organization groups",
"created_at": 1711471533,
"updated_at": 1711472599,
"created_by": "user_abc123",
"created_by_user_obj": {
"id": "user_abc123",
"name": "Ada Lovelace",
"email": "ada@example.com"
},
"metadata": {}
}
],
"has_more": false,
"next": null
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/users/subresources/roles/methods/list
