---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/users/methods/list
title: "List users"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List users

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Users](/api/reference/resources/admin/subresources/organization/subresources/users)

# List users

GET /organization/users

Lists all of the users in the organization.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

emails : optional array of string

Filter by the email address of users.

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20emails%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [OrganizationUser](/api/reference/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id , added_at , object , 13 more }

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20id)

added_at : number

The Unix timestamp (in seconds) of when the user was added.

format unixtime

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20added_at)

object : "organization.user"

The object type, which is always `organization.user`

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20object)

api_key_last_used_at : optional number

The Unix timestamp (in seconds) of the user’s last API key usage.

format unixtime

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20api_key_last_used_at)

created : optional number

The Unix timestamp (in seconds) of when the user was created.

format unixtime

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20created)

developer_persona : optional string

The developer persona metadata for the user.

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20developer_persona)

email : optional string

The email address of the user

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20email)

is_default : optional boolean

Whether this is the organization’s default user.

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20is_default)

is_scale_tier_authorized_purchaser : optional boolean

Whether the user is an authorized purchaser for Scale Tier.

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20is_scale_tier_authorized_purchaser)

is_scim_managed : optional boolean

Whether the user is managed through SCIM.

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20is_scim_managed)

is_service_account : optional boolean

Whether the user is a service account.

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20is_service_account)

name : optional string

The name of the user

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20name)

projects : optional object { data , object }

Projects associated with the user, if included.

data : array of object { id , name , role }

id : optional string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20id)

name : optional string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20name)

role : optional string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(property)%20data)

object : "list"

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20projects)

role : optional string

`owner` or `reader`

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20role)

technical_level : optional string

The technical level metadata for the user.

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20technical_level)

user : optional object { id , object , banned , 5 more }

Nested user details.

id : string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20id)

object : "user"

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20object)

banned : optional boolean

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20banned)

banned_at : optional number

format unixtime

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20banned_at)

email : optional string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20email)

enabled : optional boolean

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20enabled)

name : optional string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20name)

picture : optional string

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20picture)

[](#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)%20%3E%20(property)%20user)

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20admin.organization.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List users

```
curl https://api.openai.com/v1/organization/users?after=user_abc&limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "organization.user",
"id": "user_abc",
"name": "First Last",
"email": "user@example.com",
"role": "owner",
"added_at": 1711471533
}
],
"first_id": "user-abc",
"last_id": "user-xyz",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "organization.user",
"id": "user_abc",
"name": "First Last",
"email": "user@example.com",
"role": "owner",
"added_at": 1711471533
}
],
"first_id": "user-abc",
"last_id": "user-xyz",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/users/methods/list
