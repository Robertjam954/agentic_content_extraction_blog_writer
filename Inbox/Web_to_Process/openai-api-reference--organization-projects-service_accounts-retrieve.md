---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/retrieve
title: "Retrieve project service account"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve project service account

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# Retrieve project service account

GET /organization/projects/{project_id}/service_accounts/{service_account_id}

Retrieves a service account in the project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

service_account_id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20service_account_id%20%3E%20(schema))

##### Returns Expand Collapse

ProjectServiceAccount object { id , created_at , name , 2 more }

Represents an individual service account in a project.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the service account was created

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the service account

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.service_account"

The object type, which is always `organization.project.service_account`

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20object)

role : "owner" or "member" or "none"

`owner`, `member`, or `none`

One of the following:

"owner"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"member"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

"none"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%202)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))

### Retrieve project service account

```
curl https://api.openai.com/v1/organization/projects/proj_abc/service_accounts/svc_acct_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "organization.project.service_account",
"id": "svc_acct_abc",
"name": "Service Account",
"role": "owner",
"created_at": 1711471533
}
```

##### Returns Examples

```
{
"object": "organization.project.service_account",
"id": "svc_acct_abc",
"name": "Service Account",
"role": "owner",
"created_at": 1711471533
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/retrieve
