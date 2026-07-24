---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/list
title: "List project service accounts"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List project service accounts

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# List project service accounts

GET /organization/projects/{project_id}/service_accounts

Returns a list of service accounts in the project.

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [ProjectServiceAccount](/api/reference/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id , created_at , name , 2 more }

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

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List project service accounts

```
curl https://api.openai.com/v1/organization/projects/proj_abc/service_accounts?after=custom_id&limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "organization.project.service_account",
"id": "svc_acct_abc",
"name": "Service Account",
"role": "owner",
"created_at": 1711471533
}
],
"first_id": "svc_acct_abc",
"last_id": "svc_acct_xyz",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "organization.project.service_account",
"id": "svc_acct_abc",
"name": "Service Account",
"role": "owner",
"created_at": 1711471533
}
],
"first_id": "svc_acct_abc",
"last_id": "svc_acct_xyz",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/list
