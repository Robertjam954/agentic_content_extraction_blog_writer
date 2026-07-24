---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys/methods/delete
title: "Delete admin API key"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete admin API key

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys)

# Delete admin API key

DELETE /organization/admin_api_keys/{key_id}

Delete an organization admin API key

##### P ath Parameters Expand Collapse

key_id : string

The ID of the API key to be deleted.

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20key_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.admin_api_key.deleted"

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete admin API key

```
curl -X DELETE https://api.openai.com/v1/organization/admin_api_keys/key_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"id": "key_abc",
"object": "organization.admin_api_key.deleted",
"deleted": true
}
```

##### Returns Examples

```
{
"id": "key_abc",
"object": "organization.admin_api_key.deleted",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys/methods/delete
