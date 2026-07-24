---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/groups
title: "Groups"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Groups

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# Groups

##### [List groups](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/list)

GET /organization/groups

##### [Create group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/create)

POST /organization/groups

##### [Retrieve group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

GET /organization/groups/{group_id}

##### [Update group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/update)

POST /organization/groups/{group_id}

##### [Delete group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/delete)

DELETE /organization/groups/{group_id}

##### Models Expand Collapse

Group object { id , created_at , group_type , 2 more }

Details about an organization group.

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

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))

GroupUpdateResponse object { id , created_at , is_scim_managed , name }

Response returned after updating a group.

id : string

Identifier for the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the group was created.

format unixtime

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

is_scim_managed : boolean

Whether the group is managed through SCIM and controlled by your identity provider.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20is_scim_managed)

name : string

Updated display name for the group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema))

GroupDeleteResponse object { id , deleted , object }

Confirmation payload returned after deleting a group.

id : string

Identifier of the deleted group.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the group was deleted.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "group.deleted"

Always `group.deleted`.

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema))

#### Groups Users

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

#### Groups Roles

##### [List group organization role assignments](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

GET /organization/groups/{group_id}/roles

##### [Assign organization role to group](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

POST /organization/groups/{group_id}/roles

##### [Retrieve group organization role](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

GET /organization/groups/{group_id}/roles/{role_id}

##### [Unassign organization role from group](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

DELETE /organization/groups/{group_id}/roles/{role_id}

##### Models Expand Collapse

RoleListResponse object { id , assignment_sources , created_at , 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

assignment_sources : array of object { principal_id , principal_type }

Principals from which the role assignment is inherited, when available.

principal_id : string

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_id)

principal_type : string

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_type)

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources)

created_at : number

When the role was created.

format unixtime

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

created_by : string

Identifier of the actor who created the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by)

created_by_user_obj : map [ unknown ]

User details for the actor that created the role, when available.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by_user_obj)

description : string

Description of the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20description)

metadata : map [ unknown ]

Arbitrary metadata stored on the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

Name of the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

permissions : array of string

Permissions associated with the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined by OpenAI.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role applies to.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type)

updated_at : number

When the role was last updated.

format unixtime

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at)

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))

RoleCreateResponse object { group , object , role }

Role assignment linking a group to a role.

group : object { id , created_at , name , 2 more }

Summary information about a group returned in role assignment responses.

id : string

Identifier for the group.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the group was created.

format unixtime

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20created_at)

name : string

Display name of the group.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20name)

object : "group"

Always `group`.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20object)

scim_managed : boolean

Whether the group is managed through SCIM.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20scim_managed)

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group)

object : "group.role"

Always `group.role`.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

role : [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id , description , name , 4 more }

Details about a role that can be assigned through the public Roles API.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

RoleRetrieveResponse object { id , assignment_sources , created_at , 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

assignment_sources : array of object { principal_id , principal_type }

Principals from which the role assignment is inherited, when available.

principal_id : string

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_id)

principal_type : string

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_type)

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources)

created_at : number

When the role was created.

format unixtime

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

created_by : string

Identifier of the actor who created the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_by)

created_by_user_obj : map [ unknown ]

User details for the actor that created the role, when available.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_by_user_obj)

description : string

Description of the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20description)

metadata : map [ unknown ]

Arbitrary metadata stored on the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

Name of the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

permissions : array of string

Permissions associated with the role.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined by OpenAI.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role applies to.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20resource_type)

updated_at : number

When the role was last updated.

format unixtime

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20updated_at)

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

RoleDeleteResponse object { deleted , object }

Confirmation payload returned after unassigning a role.

deleted : boolean

Whether the assignment was removed.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/groups
