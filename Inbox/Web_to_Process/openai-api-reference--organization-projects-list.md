---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/list
title: "List projects"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List projects

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# List projects

GET /organization/projects

Returns a list of projects.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

include_archived : optional boolean

If `true` returns all projects including those that have been `archived`. Archived projects are not included by default.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20include_archived%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [Project](/api/reference/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id , created_at , object , 4 more }

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the project was created.

format unixtime

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "organization.project"

The object type, which is always `organization.project`

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20object)

archived_at : optional number

The Unix timestamp (in seconds) of when the project was archived or `null`.

format unixtime

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20archived_at)

external_key_id : optional string

The external key associated with the project.

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20external_key_id)

name : optional string

The name of the project. This appears in reporting.

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20name)

status : optional string

`active` or `archived`

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List projects

```
curl https://api.openai.com/v1/organization/projects?after=proj_abc&limit=20&include_archived=false \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"id": "proj_abc",
"object": "organization.project",
"name": "Project example",
"created_at": 1711471533,
"archived_at": null,
"status": "active"
}
],
"first_id": "proj-abc",
"last_id": "proj-xyz",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "proj_abc",
"object": "organization.project",
"name": "Project example",
"created_at": 1711471533,
"archived_at": null,
"status": "active"
}
],
"first_id": "proj-abc",
"last_id": "proj-xyz",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/list
