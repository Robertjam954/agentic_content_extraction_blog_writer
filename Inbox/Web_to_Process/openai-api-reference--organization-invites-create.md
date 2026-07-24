---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/invites/methods/create
title: "Create invite"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create invite

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Invites](/api/reference/resources/admin/subresources/organization/subresources/invites)

# Create invite

POST /organization/invites

Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.

##### Body Parameters JSON Expand Collapse

email : string

Send an email to this address

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20email%20%3E%20(schema))

role : "reader" or "owner"

`owner` or `reader`

One of the following:

"reader"

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20role%20%3E%20(schema)%20%3E%20(member)%200)

"owner"

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20role%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20role%20%3E%20(schema))

projects : optional array of object { id , role }

An array of projects to which membership is granted at the same time the org invite is accepted. If omitted, the user will be invited to the default project for compatibility with legacy behavior. If empty list is passed, the user will not be invited to any projects, including the default one.

id : string

Project’s public ID

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20projects%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id)

role : "member" or "owner"

Project membership role

One of the following:

"member"

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20projects%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"owner"

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20projects%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20projects%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20projects%20%3E%20(schema))

##### Returns Expand Collapse

Invite object { id , created_at , email , 6 more }

Represents an individual `invite` to the organization.

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

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))

### Create invite

```
curl -X POST https://api.openai.com/v1/organization/invites \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"email": "anotheruser@example.com",
"role": "reader",
"projects": [
{
"id": "project-xyz",
"role": "member"
},
{
"id": "project-abc",
"role": "owner"
}
]
}'
```

```
{
"object": "organization.invite",
"id": "invite-def",
"email": "anotheruser@example.com",
"role": "reader",
"status": "pending",
"created_at": 1711471533,
"expires_at": 1711471533,
"accepted_at": null,
"projects": [
{
"id": "project-xyz",
"role": "member"
},
{
"id": "project-abc",
"role": "owner"
}
]
}
```

##### Returns Examples

```
{
"object": "organization.invite",
"id": "invite-def",
"email": "anotheruser@example.com",
"role": "reader",
"status": "pending",
"created_at": 1711471533,
"expires_at": 1711471533,
"accepted_at": null,
"projects": [
{
"id": "project-xyz",
"role": "member"
},
{
"id": "project-abc",
"role": "owner"
}
]
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/invites/methods/create
