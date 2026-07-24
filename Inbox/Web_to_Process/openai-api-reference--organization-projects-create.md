---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/create
title: "Create project"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create project

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Create project

POST /organization/projects

Create a new project in the organization. Projects can be created and archived, but cannot be deleted.

##### Body Parameters JSON Expand Collapse

name : string

The friendly name of the project, this name appears in reports.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

external_key_id : optional string

External key ID to associate with the project.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20external_key_id%20%3E%20(schema))

geography : optional string

Create the project with the specified data residency region. Your organization must have access to Data residency functionality in order to use. See [data residency controls](/docs/guides/your-data#data-residency-controls) to review the functionality and limitations of setting this field.

[](#(resource)%20admin.organization.projects%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20geography%20%3E%20(schema))

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

### Create project

```
curl -X POST https://api.openai.com/v1/organization/projects \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "Project ABC"
}'
```

```
{
"id": "proj_abc",
"object": "organization.project",
"name": "Project ABC",
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
"name": "Project ABC",
"created_at": 1711471533,
"archived_at": null,
"status": "active"
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/methods/create
