---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/api_keys/methods/list
title: "List project API keys"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List project API keys

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

# List project API keys

GET /organization/projects/{project_id}/api_keys

Returns a list of API keys in the project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

owner_project_access : optional "active" or "inactive" or "any"

Filter API keys by whether the owner currently has effective access to the project. Use `active` for owners with access, `inactive` for owners without access, or `any` for all enabled project API keys. If omitted, the endpoint applies its existing membership-based visibility rules, which may exclude some enabled keys.

One of the following:

"active"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20owner_project_access%20%3E%20(schema)%20%3E%20(member)%200)

"inactive"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20owner_project_access%20%3E%20(schema)%20%3E%20(member)%201)

"any"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20owner_project_access%20%3E%20(schema)%20%3E%20(member)%202)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20owner_project_access%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [ProjectAPIKey](/api/reference/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id , created_at , last_used_at , 5 more }

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

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List project API keys

```
curl https://api.openai.com/v1/organization/projects/proj_abc/api_keys?after=key_abc&limit=20&owner_project_access=any \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "organization.project.api_key",
"redacted_value": "sk-abc...def",
"name": "My API Key",
"created_at": 1711471533,
"last_used_at": 1711471534,
"id": "key_abc",
"owner_project_access": "active",
"owner": {
"type": "user",
"user": {
"id": "user_abc",
"name": "First Last",
"email": "user@example.com",
"role": "owner",
"created_at": 1711471533
}
}
}
],
"first_id": "key_abc",
"last_id": "key_xyz",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "organization.project.api_key",
"redacted_value": "sk-abc...def",
"name": "My API Key",
"created_at": 1711471533,
"last_used_at": 1711471534,
"id": "key_abc",
"owner_project_access": "active",
"owner": {
"type": "user",
"user": {
"id": "user_abc",
"name": "First Last",
"email": "user@example.com",
"role": "owner",
"created_at": 1711471533
}
}
}
],
"first_id": "key_abc",
"last_id": "key_xyz",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/api_keys/methods/list
