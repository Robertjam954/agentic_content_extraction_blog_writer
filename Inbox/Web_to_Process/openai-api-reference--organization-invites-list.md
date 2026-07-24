---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/invites/methods/list
title: "List invites"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List invites

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Invites](/api/reference/resources/admin/subresources/organization/subresources/invites)

# List invites

GET /organization/invites

Returns a list of invites in the organization.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [Invite](/api/reference/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id , created_at , email , 6 more }

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the invite was sent.

format unixtime

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20created_at)

email : string

The email address of the individual to whom the invite was sent

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20email)

object : "organization.invite"

The object type, which is always `organization.invite`

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20object)

projects : array of object { id , role }

The projects that were granted membership upon acceptance of the invite.

id : string

Project’s public ID

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(items)%20%3E%20(property)%20id)

role : "member" or "owner"

Project membership role

One of the following:

"member"

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"owner"

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20projects%20%3E%20(items)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20projects)

role : "owner" or "reader"

`owner` or `reader`

One of the following:

"owner"

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"reader"

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20role)

status : "accepted" or "expired" or "pending"

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"expired"

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"pending"

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20status)

accepted_at : optional number

The Unix timestamp (in seconds) of when the invite was accepted.

format unixtime

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20accepted_at)

expires_at : optional number

The Unix timestamp (in seconds) of when the invite expires.

format unixtime

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)%20%3E%20(property)%20expires_at)

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

The `has_more` property is used for pagination to indicate there are additional results.

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

The object type, which is always `list`

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

The first `invite_id` in the retrieved `list`

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

The last `invite_id` in the retrieved `list`

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List invites

```
curl https://api.openai.com/v1/organization/invites?after=invite-abc&limit=20 \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "list",
"data": [
{
"object": "organization.invite",
"id": "invite-abc",
"email": "user@example.com",
"role": "owner",
"status": "accepted",
"created_at": 1711471533,
"expires_at": 1711471533,
"accepted_at": 1711471533
}
],
"first_id": "invite-abc",
"last_id": "invite-abc",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "organization.invite",
"id": "invite-abc",
"email": "user@example.com",
"role": "owner",
"status": "accepted",
"created_at": 1711471533,
"expires_at": 1711471533,
"accepted_at": 1711471533
}
],
"first_id": "invite-abc",
"last_id": "invite-abc",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/invites/methods/list
