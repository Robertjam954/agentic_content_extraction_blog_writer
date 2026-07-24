---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/groups/methods/list
title: "List project groups"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List project groups

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups)

# List project groups

GET /organization/projects/{project_id}/groups

Lists the groups that have access to a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

Cursor for pagination. Provide the ID of the last group from the previous response to fetch the next page.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of project groups to return. Defaults to 20.

minimum 0

maximum 100

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order for the returned groups.

One of the following:

"asc"

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [ProjectGroup](/api/reference/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created_at , group_id , group_name , 3 more }

Project group memberships returned in the current page.

created_at : number

Unix timestamp (in seconds) when the group was granted project access.

format unixtime

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20created_at)

group_id : string

Identifier of the group that has access to the project.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_id)

group_name : string

Display name of the group.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_name)

group_type : "group" or "tenant_group"

The type of the group.

One of the following:

"group"

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%200)

"tenant_group"

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_type)

object : "project.group"

Always `project.group`.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20object)

project_id : string

Identifier of the project.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

Whether additional project group memberships are available.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

next : string

Cursor to fetch the next page of results, or `null` when there are no more results.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20next)

object : "list"

Always `list`.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List project groups

```
curl https://api.openai.com/v1/organization/projects/proj_abc123/groups?limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "project.group",
"project_id": "proj_abc123",
"group_id": "group_01J1F8ABCDXYZ",
"group_name": "Support Team",
"created_at": 1711471533
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
"object": "project.group",
"project_id": "proj_abc123",
"group_id": "group_01J1F8ABCDXYZ",
"group_name": "Support Team",
"created_at": 1711471533
}
],
"has_more": false,
"next": null
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/groups/methods/list
