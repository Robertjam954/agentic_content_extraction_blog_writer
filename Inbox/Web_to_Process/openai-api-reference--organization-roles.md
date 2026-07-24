---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/roles
title: "Roles"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Roles

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# Roles

##### [List organization roles](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/list)

GET /organization/roles

##### [Create organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/create)

POST /organization/roles

##### [Retrieve organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

GET /organization/roles/{role_id}

##### [Update organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/update)

POST /organization/roles/{role_id}

##### [Delete organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/delete)

DELETE /organization/roles/{role_id}

##### Models Expand Collapse

Role object { id , description , name , 4 more }

Details about a role that can be assigned through the public Roles API.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20id)

description : string

Optional description of the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20description)

name : string

Unique name for the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20name)

object : "role"

Always `role`.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20object)

permissions : array of string

Permissions granted by the role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined and managed by OpenAI.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role is bound to (for example `api.organization` or `api.project`).

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)%20%3E%20(property)%20resource_type)

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

RoleDeleteResponse object { id , deleted , object }

Confirmation payload returned after deleting a role.

id : string

Identifier of the deleted role.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the role was deleted.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "role.deleted"

Always `role.deleted`.

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/roles
