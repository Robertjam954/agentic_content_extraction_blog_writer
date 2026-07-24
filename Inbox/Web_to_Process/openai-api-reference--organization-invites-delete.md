---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/invites/methods/delete
title: "Delete invite"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete invite

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Invites](/api/reference/resources/admin/subresources/organization/subresources/invites)

# Delete invite

DELETE /organization/invites/{invite_id}

Delete an invite. If the invite has already been accepted, it cannot be deleted.

##### P ath Parameters Expand Collapse

invite_id : string

[](#(resource)%20admin.organization.invites%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20invite_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`

[](#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete invite

```
curl -X DELETE https://api.openai.com/v1/organization/invites/invite-abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "organization.invite.deleted",
"id": "invite-abc",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "organization.invite.deleted",
"id": "invite-abc",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/invites/methods/delete
