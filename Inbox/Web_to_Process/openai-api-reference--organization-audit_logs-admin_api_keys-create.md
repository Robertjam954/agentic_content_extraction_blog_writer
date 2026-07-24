---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys/methods/create
title: "Create admin API key"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create admin API key

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys)

# Create admin API key

POST /organization/admin_api_keys

Create an organization admin API key

##### Body Parameters JSON Expand Collapse

name : string

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

expires_in_seconds : optional number

The number of seconds until the API key expires. Omit this field for a key that does not expire.

minimum 1

maximum 31536000

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_in_seconds%20%3E%20(schema))

##### Returns Expand Collapse

value : string

The value of the API key. Only shown on create.

[](#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20value)

### Create admin API key

```
curl -X POST https://api.openai.com/v1/organization/admin_api_keys \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "New Admin Key",
"expires_in_seconds": 2592000
}'
```

```
{
"object": "organization.admin_api_key",
"id": "key_xyz",
"name": "New Admin Key",
"redacted_value": "sk-admin...xyz",
"created_at": 1711471533,
"expires_at": 1714063533,
"last_used_at": 1711471534,
"owner": {
"type": "user",
"object": "organization.user",
"id": "user_123",
"name": "John Doe",
"created_at": 1711471533,
"role": "owner"
},
"value": "sk-admin-1234abcd"
}
```

##### Returns Examples

```
{
"object": "organization.admin_api_key",
"id": "key_xyz",
"name": "New Admin Key",
"redacted_value": "sk-admin...xyz",
"created_at": 1711471533,
"expires_at": 1714063533,
"last_used_at": 1711471534,
"owner": {
"type": "user",
"object": "organization.user",
"id": "user_123",
"name": "John Doe",
"created_at": 1711471533,
"role": "owner"
},
"value": "sk-admin-1234abcd"
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/admin_api_keys/methods/create
