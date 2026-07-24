---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/retrieve
title: "Retrieve project"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve project

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Retrieve project

GET /organization/projects/{project_id}

Retrieves a project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Returns Expand Collapse

Project object { id , created_at , object , 4 more }

Represents an individual project.

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

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

### Retrieve project

```
curl https://api.openai.com/v1/organization/projects/proj_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"id": "proj_abc",
"object": "organization.project",
"name": "Project example",
"created_at": 1711471533,
"archived_at": null,
"status": "active"
}
```

##### Returns Examples

```
{
"id": "proj_abc",
"object": "organization.project",
"name": "Project example",
"created_at": 1711471533,
"archived_at": null,
"status": "active"
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/retrieve
