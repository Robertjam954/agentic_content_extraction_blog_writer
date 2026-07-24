---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys
title: "Admin API Keys"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Admin API Keys

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# Admin API Keys

##### [List all organization and project API keys.](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

GET /organization/admin_api_keys

##### [Create admin API key](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

POST /organization/admin_api_keys

##### [Retrieve admin API key](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

GET /organization/admin_api_keys/{key_id}

##### [Delete admin API key](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

DELETE /organization/admin_api_keys/{key_id}

##### Models Expand Collapse

AdminAPIKey object { id , created_at , expires_at , 5 more }

Represents an individual Admin API key in an org.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the API key was created

format unixtime

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20created_at)

expires_at : number

The Unix timestamp (in seconds) of when the API key expires

format unixtime

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20expires_at)

object : "organization.admin_api_key"

The object type, which is always `organization.admin_api_key`

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20object)

owner : object { id , created_at , name , 3 more }

id : optional string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20id)

created_at : optional number

The Unix timestamp (in seconds) of when the user was created

format unixtime

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20created_at)

name : optional string

The name of the user

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20name)

object : optional string

The object type, which is always organization.user

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20object)

role : optional string

Always `owner`

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20role)

type : optional string

Always `user`

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20type)

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20owner)

redacted_value : string

The redacted value of the API key

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20redacted_value)

last_used_at : optional number

The Unix timestamp (in seconds) of when the API key was last used

format unixtime

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20last_used_at)

name : optional string

The name of the API key

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))

AdminAPIKeyCreateResponse = [AdminAPIKey](/api/reference/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id , created_at , expires_at , 5 more }

Represents an individual Admin API key in an org.

value : string

The value of the API key. Only shown on create.

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema))

AdminAPIKeyDeleteResponse object { id , deleted , object }

id : string

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.admin_api_key.deleted"

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys
