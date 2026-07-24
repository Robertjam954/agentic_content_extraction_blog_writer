---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users
title: "Users"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Users

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

# Users

##### [List group users](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

GET /organization/groups/{group_id}/users

##### [Add group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

POST /organization/groups/{group_id}/users

##### [Retrieve group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

GET /organization/groups/{group_id}/users/{user_id}

##### [Remove group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

DELETE /organization/groups/{group_id}/users/{user_id}

##### Models Expand Collapse

OrganizationGroupUser object { id , email , name }

Represents an individual user returned when inspecting group membership.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)%20%3E%20(property)%20id)

email : string

The email address of the user.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)%20%3E%20(property)%20email)

name : string

The name of the user.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema))

UserCreateResponse object { group_id , object , user_id }

Confirmation payload returned after adding a user to a group.

group_id : string

Identifier of the group the user was added to.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)%20%3E%20(property)%20group_id)

object : "group.user"

Always `group.user`.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

user_id : string

Identifier of the user that was added.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema))

UserRetrieveResponse object { id , email , is_service_account , 3 more }

Details about a user returned from an organization group membership lookup.

id : string

Identifier for the user.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

email : string

Email address of the user, or `null` for users without an email.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20email)

is_service_account : boolean

Whether the user is a service account.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20is_service_account)

name : string

Display name of the user.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

picture : string

URL of the user’s profile picture, if available.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20picture)

user_type : "user" or "tenant_user"

The type of user.

One of the following:

"user"

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20user_type%20%3E%20(member)%200)

"tenant_user"

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20user_type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20user_type)

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema))

UserDeleteResponse object { deleted , object }

Confirmation payload returned after removing a user from a group.

deleted : boolean

Whether the group membership was removed.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "group.user.deleted"

Always `group.user.deleted`.

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups/subresources/users
