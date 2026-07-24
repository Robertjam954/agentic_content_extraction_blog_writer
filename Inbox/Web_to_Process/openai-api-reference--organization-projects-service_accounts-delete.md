---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/delete
title: "Delete project service account"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete project service account

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# Delete project service account

DELETE /organization/projects/{project_id}/service_accounts/{service_account_id}

Deletes a service account from the project.

Returns confirmation of service account deletion, or an error if the project
is archived (archived projects have no service accounts).

##### P ath Parameters Expand Collapse

project_id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20project_id%20%3E%20(schema))

service_account_id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20service_account_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.project.service_account.deleted"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete project service account

```
curl -X DELETE https://api.openai.com/v1/organization/projects/proj_abc/service_accounts/svc_acct_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "organization.project.service_account.deleted",
"id": "svc_acct_abc",
"deleted": true
}
```

##### Returns Examples

```
{
"object": "organization.project.service_account.deleted",
"id": "svc_acct_abc",
"deleted": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/service_accounts/methods/delete
