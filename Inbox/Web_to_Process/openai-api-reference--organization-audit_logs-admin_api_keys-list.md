---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys/methods/list
title: "List all organization and project API keys."
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List all organization and project API keys.

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys)

# List all organization and project API keys.

GET /organization/admin_api_keys

List organization API keys

##### Q uery Parameters Expand Collapse

after : optional string

Return keys with IDs that come after this ID in the pagination order.

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

Maximum number of keys to return.

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Order results by creation time, ascending or descending.

One of the following:

"asc"

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [AdminAPIKey](/api/reference/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id , created_at , expires_at , 5 more }

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

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List all organization and project API keys.

```
curl https://api.openai.com/v1/organization/admin_api_keys?after=key_abc&limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "organization.admin_api_key",
"id": "key_abc",
"name": "Main Admin Key",
"redacted_value": "sk-admin...def",
"created_at": 1711471533,
"expires_at": 1714063533,
"last_used_at": 1711471534,
"owner": {
"type": "service_account",
"object": "organization.service_account",
"id": "sa_456",
"name": "My Service Account",
"created_at": 1711471533,
"role": "member"
}
}
],
"first_id": "key_abc",
"last_id": "key_abc",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "organization.admin_api_key",
"id": "key_abc",
"name": "Main Admin Key",
"redacted_value": "sk-admin...def",
"created_at": 1711471533,
"expires_at": 1714063533,
"last_used_at": 1711471534,
"owner": {
"type": "service_account",
"object": "organization.service_account",
"id": "sa_456",
"name": "My Service Account",
"created_at": 1711471533,
"role": "member"
}
}
],
"first_id": "key_abc",
"last_id": "key_abc",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys/methods/list
