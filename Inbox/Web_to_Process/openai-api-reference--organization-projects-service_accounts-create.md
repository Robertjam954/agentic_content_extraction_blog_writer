---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/create
title: "Create project service account"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create project service account

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# Create project service account

POST /organization/projects/{project_id}/service_accounts

Creates a new service account in the project. By default, this also returns an unredacted API key for the service account.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

name : string

The name of the service account being created.

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

create_service_account_only : optional boolean

Create the service account without default roles or an API key.

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20create_service_account_only%20%3E%20(schema))

##### Returns Expand Collapse

id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

api_key : object { id , created_at , name , 2 more }

id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20id)

created_at : number

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20created_at)

name : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20name)

object : "organization.project.service_account.api_key"

The object type, which is always `organization.project.service_account.api_key`

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20object)

value : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key)

created_at : number

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.service_account"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

role : "member" or "none"

Service accounts created with default project membership have role `member`. Accounts created with `create_service_account_only` have role `none`.

One of the following:

"member"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"none"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20role)

### Create project service account

```
curl -X POST https://api.openai.com/v1/organization/projects/proj_abc/service_accounts \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "Production App"
}'
```

```
{
"object": "organization.project.service_account",
"id": "svc_acct_abc",
"name": "Production App",
"role": "member",
"created_at": 1711471533,
"api_key": {
"object": "organization.project.service_account.api_key",
"value": "sk-abcdefghijklmnop123",
"name": "Secret Key",
"created_at": 1711471533,
"id": "key_abc"
}
}
```

##### Returns Examples

```
{
"object": "organization.project.service_account",
"id": "svc_acct_abc",
"name": "Production App",
"role": "member",
"created_at": 1711471533,
"api_key": {
"object": "organization.project.service_account.api_key",
"value": "sk-abcdefghijklmnop123",
"name": "Secret Key",
"created_at": 1711471533,
"id": "key_abc"
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/create
