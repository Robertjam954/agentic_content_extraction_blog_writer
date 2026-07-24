---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/update
title: "Modify project"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Modify project

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Modify project

POST /organization/projects/{project_id}

Modifies a project in the organization.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

external_key_id : optional string

External key ID to associate with the project.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20external_key_id%20%3E%20(schema))

geography : optional string

Geography for the project.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20geography%20%3E%20(schema))

name : optional string

The updated name of the project, this name appears in reports.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

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

### Modify project

```
curl -X POST https://api.openai.com/v1/organization/projects/proj_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "Project DEF"
}'
```

```
{
"id": "id",
"created_at": 0,
"object": "organization.project",
"archived_at": 0,
"external_key_id": "external_key_id",
"name": "name",
"status": "status"
}
```

##### Returns Examples

```
{
"id": "id",
"created_at": 0,
"object": "organization.project",
"archived_at": 0,
"external_key_id": "external_key_id",
"name": "name",
"status": "status"
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/update
