---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/users/methods/create
title: "Create project user"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create project user

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users)

# Create project user

POST /organization/projects/{project_id}/users

Adds a user to the project. Users must already be members of the organization to be added to a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

role : string

`owner` or `member`

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20role%20%3E%20(schema))

email : optional string

Email of the user to add.

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20email%20%3E%20(schema))

user_id : optional string

The ID of the user.

[](#(resource)%20admin.organization.projects.users%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20user_id%20%3E%20(schema))

##### Returns Expand Collapse

ProjectUser object { id , added_at , object , 3 more }

Represents an individual user in a project.

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

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))

### Create project user

```
curl -X POST https://api.openai.com/v1/organization/projects/proj_abc/users \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"user_id": "user_abc",
"role": "member"
}'
```

```
{
"object": "organization.project.user",
"id": "user_abc",
"email": "user@example.com",
"role": "owner",
"added_at": 1711471533
}
```

##### Returns Examples

```
{
"object": "organization.project.user",
"id": "user_abc",
"email": "user@example.com",
"role": "owner",
"added_at": 1711471533
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/users/methods/create
