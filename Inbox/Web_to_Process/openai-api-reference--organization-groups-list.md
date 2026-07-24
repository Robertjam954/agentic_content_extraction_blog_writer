---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/list
title: "List groups"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List groups

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

# List groups

GET /organization/groups

Lists all groups in the organization.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is a group ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with group_abc, your subsequent call can include `after=group_abc` in order to fetch the next page of the list.

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of groups to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum 0

maximum 1000

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Specifies the sort order of the returned groups.

One of the following:

"asc"

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [Group](/api/reference/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id , created_at , group_type , 2 more }

Groups returned in the current page.

id : string

Identifier for the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the group was created.

format unixtime

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20created_at)

group_type : "group" or "tenant_group"

The type of the group.

One of the following:

"group"

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%200)

"tenant_group"

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20group_type)

is_scim_managed : boolean

Whether the group is managed through SCIM and controlled by your identity provider.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20is_scim_managed)

name : string

Display name of the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

Whether additional groups are available when paginating.

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

next : string

Cursor to fetch the next page of results, or `null` if there are no more results.

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20next)

object : "list"

Always `list`.

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List groups

```
curl https://api.openai.com/v1/organization/groups?limit=20&order=asc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "group",
"id": "group_01J1F8ABCDXYZ",
"name": "Support Team",
"created_at": 1711471533,
"is_scim_managed": false
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
"object": "group",
"id": "group_01J1F8ABCDXYZ",
"name": "Support Team",
"created_at": 1711471533,
"is_scim_managed": false
}
],
"has_more": false,
"next": null
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/list
