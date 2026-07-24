---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/api_keys
title: "API Keys"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# API Keys

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# API Keys

##### [List project API keys](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

GET /organization/projects/{project_id}/api_keys

##### [Retrieve project API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

GET /organization/projects/{project_id}/api_keys/{api_key_id}

##### [Delete project API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

DELETE /organization/projects/{project_id}/api_keys/{api_key_id}

##### Models Expand Collapse

ProjectAPIKey object { id , created_at , last_used_at , 5 more }

Represents an individual API key in a project.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the API key was created

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20created_at)

last_used_at : number

The Unix timestamp (in seconds) of when the API key was last used.

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20last_used_at)

name : string

The name of the API key

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.api_key"

The object type, which is always `organization.project.api_key`

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20object)

owner : object { service_account , type , user }

service_account : optional object { id , created_at , name , role }

The service account that owns a project API key.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the service account was created.

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20created_at)

name : string

The name of the service account.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20name)

role : string

The service account’s project role.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account)

type : optional "user" or "service_account"

`user` or `service_account`

One of the following:

"user"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20type%20%3E%20(member)%200)

"service_account"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20type)

user : optional object { id , created_at , email , 2 more }

The user that owns a project API key.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the user was created.

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20created_at)

email : string

The email address of the user.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20email)

name : string

The name of the user.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20name)

role : string

The user’s project role.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner)

owner_project_access : "active" or "inactive"

Whether the API key’s owner currently has effective access to the project.

One of the following:

"active"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner_project_access%20%3E%20(member)%200)

"inactive"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner_project_access%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner_project_access)

redacted_value : string

The redacted value of the API key

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20redacted_value)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))

APIKeyDeleteResponse object { id , deleted , object }

id : string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.project.api_key.deleted"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/api_keys
