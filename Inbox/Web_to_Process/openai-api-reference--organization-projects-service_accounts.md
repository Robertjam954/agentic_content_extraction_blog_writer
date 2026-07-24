---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts
title: "Service Accounts"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Service Accounts

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Service Accounts

##### [List project service accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

GET /organization/projects/{project_id}/service_accounts

##### [Create project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

POST /organization/projects/{project_id}/service_accounts

##### [Retrieve project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

GET /organization/projects/{project_id}/service_accounts/{service_account_id}

##### [Update project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

POST /organization/projects/{project_id}/service_accounts/{service_account_id}

##### [Delete project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

DELETE /organization/projects/{project_id}/service_accounts/{service_account_id}

##### Models Expand Collapse

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

ServiceAccountCreateResponse object { id , api_key , created_at , 3 more }

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

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema))

ServiceAccountDeleteResponse object { id , deleted , object }

id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.project.service_account.deleted"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema))

#### Service Accounts API Keys

##### [Create project service account API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create)

POST /organization/projects/{project_id}/service_accounts/{service_account_id}/api_keys

##### Models Expand Collapse

APIKeyCreateResponse object { id , created_at , name , 2 more }

id : string

The identifier of the API key.

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) when the API key was created.

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the API key.

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.service_account.api_key"

The object type, which is always `organization.project.service_account.api_key`

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

value : string

The unredacted API key value.

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts
