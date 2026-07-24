---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users/methods/list
title: "List group users"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List group users

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users)

# List group users

GET /organization/groups/{group_id}/users

Lists the users assigned to a group.

##### P ath Parameters Expand Collapse

group_id : string

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. Provide the ID of the last user from the previous list response to retrieve the next page.

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of users to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum 0

maximum 1000

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Specifies the sort order of users in the list.

One of the following:

"asc"

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [OrganizationGroupUser](/api/reference/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id , email , name }

Users in the current page.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)%20%3E%20(property)%20id)

email : string

The email address of the user.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)%20%3E%20(property)%20email)

name : string

The name of the user.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

Whether more users are available when paginating.

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

next : string

Cursor to fetch the next page of results, or `null` when no further users are available.

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20next)

object : "list"

Always `list`.

[](#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List group users

```
curl https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ/users?limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"id": "user_abc123",
"name": "Ada Lovelace",
"email": "ada@example.com"
}
],
"has_more": false,
"next": null
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "user_abc123",
"name": "Ada Lovelace",
"email": "ada@example.com"
}
],
"has_more": false,
"next": null
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users/methods/list
