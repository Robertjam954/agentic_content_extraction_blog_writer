---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/delete
title: "Delete group"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete group

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

# Delete group

DELETE /organization/groups/{group_id}

Deletes a group from the organization.

##### P ath Parameters Expand Collapse

group_id : string

[](#(resource)%20admin.organization.groups%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20group_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Identifier of the deleted group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the group was deleted.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "group.deleted"

Always `group.deleted`.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete group

```
curl -X DELETE https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "group.deleted",
"id": "group_01J1F8ABCDXYZ",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "group.deleted",
"id": "group_01J1F8ABCDXYZ",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/methods/delete
