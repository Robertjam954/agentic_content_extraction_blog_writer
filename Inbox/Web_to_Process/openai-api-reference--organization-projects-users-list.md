---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/users/methods/list
title: "List project users"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List project users

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users)

# List project users

GET /organization/projects/{project_id}/users

Returns a list of users in the project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [ProjectUser](/api/reference/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id , added_at , object , 3 more }

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20id)

added_at : number

The Unix timestamp (in seconds) of when the project was added.

format unixtime

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20added_at)

object : "organization.project.user"

The object type, which is always `organization.project.user`

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20object)

role : string

`owner` or `member`

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20role)

email : optional string

The email address of the user

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20email)

name : optional string

The name of the user

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : string

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List project users

```
curl https://api.openai.com/v1/organization/projects/proj_abc/users?after=user_abc&limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "organization.project.user",
"id": "user_abc",
"name": "First Last",
"email": "user@example.com",
"role": "owner",
"added_at": 1711471533
}
],
"first_id": "user-abc",
"last_id": "user-xyz",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "organization.project.user",
"id": "user_abc",
"name": "First Last",
"email": "user@example.com",
"role": "owner",
"added_at": 1711471533
}
],
"first_id": "user-abc",
"last_id": "user-xyz",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/users/methods/list
