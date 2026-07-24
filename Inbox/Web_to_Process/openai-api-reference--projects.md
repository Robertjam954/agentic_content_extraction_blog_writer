---
source_url: https://developers.openai.com/api/reference/resources/projects
title: "Projects"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Projects

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# Projects

##### [List projects](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/list)

GET /organization/projects

##### [Create project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/create)

POST /organization/projects

##### [Retrieve project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

GET /organization/projects/{project_id}

##### [Modify project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/update)

POST /organization/projects/{project_id}

##### [Archive project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/archive)

POST /organization/projects/{project_id}/archive

##### Models Expand Collapse

Project object { id , created_at , object , 4 more }

Represents an individual project.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the project was created.

format unixtime

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "organization.project"

The object type, which is always `organization.project`

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20object)

archived_at : optional number

The Unix timestamp (in seconds) of when the project was archived or `null`.

format unixtime

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20archived_at)

external_key_id : optional string

The external key associated with the project.

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20external_key_id)

name : optional string

The name of the project. This appears in reporting.

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20name)

status : optional string

`active` or `archived`

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

#### Projects Users

##### [List project users](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

GET /organization/projects/{project_id}/users

##### [Create project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

POST /organization/projects/{project_id}/users

##### [Retrieve project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

GET /organization/projects/{project_id}/users/{user_id}

##### [Modify project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

POST /organization/projects/{project_id}/users/{user_id}

##### [Delete project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

DELETE /organization/projects/{project_id}/users/{user_id}

##### Models Expand Collapse

ProjectUser object { id , added_at , object , 3 more }

Represents an individual user in a project.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20id)

added_at : number

The Unix timestamp (in seconds) of when the project was added.

format unixtime

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20added_at)

object : "organization.project.user"

The object type, which is always `organization.project.user`

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20object)

role : string

`owner` or `member`

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20role)

email : optional string

The email address of the user

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20email)

name : optional string

The name of the user

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))

UserDeleteResponse object { id , deleted , object }

id : string

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.project.user.deleted"

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

#### Projects Users Roles

##### [List project user role assignments](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

GET /projects/{project_id}/users/{user_id}/roles

##### [Assign project role to user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

POST /projects/{project_id}/users/{user_id}/roles

##### [Retrieve project user role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

GET /projects/{project_id}/users/{user_id}/roles/{role_id}

##### [Unassign project role from user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

DELETE /projects/{project_id}/users/{user_id}/roles/{role_id}

##### Models Expand Collapse

RoleListResponse object { id , assignment_sources , created_at , 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

assignment_sources : array of object { principal_id , principal_type }

Principals from which the role assignment is inherited, when available.

principal_id : string

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_id)

principal_type : string

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_type)

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources)

created_at : number

When the role was created.

format unixtime

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

created_by : string

Identifier of the actor who created the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by)

created_by_user_obj : map [ unknown ]

User details for the actor that created the role, when available.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by_user_obj)

description : string

Description of the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20description)

metadata : map [ unknown ]

Arbitrary metadata stored on the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

Name of the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

permissions : array of string

Permissions associated with the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined by OpenAI.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role applies to.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type)

updated_at : number

When the role was last updated.

format unixtime

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at)

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))

RoleCreateResponse object { object , role , user }

Role assignment linking a user to a role.

object : "user.role"

Always `user.role`.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

role : [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id , description , name , 4 more }

Details about a role that can be assigned through the public Roles API.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role)

user : [OrganizationUser](/api/reference/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id , added_at , object , 13 more }

Represents an individual `user` within an organization.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20user)

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

RoleRetrieveResponse object { id , assignment_sources , created_at , 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

assignment_sources : array of object { principal_id , principal_type }

Principals from which the role assignment is inherited, when available.

principal_id : string

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_id)

principal_type : string

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_type)

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources)

created_at : number

When the role was created.

format unixtime

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

created_by : string

Identifier of the actor who created the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_by)

created_by_user_obj : map [ unknown ]

User details for the actor that created the role, when available.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_by_user_obj)

description : string

Description of the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20description)

metadata : map [ unknown ]

Arbitrary metadata stored on the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

Name of the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

permissions : array of string

Permissions associated with the role.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined by OpenAI.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role applies to.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20resource_type)

updated_at : number

When the role was last updated.

format unixtime

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20updated_at)

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

RoleDeleteResponse object { deleted , object }

Confirmation payload returned after unassigning a role.

deleted : boolean

Whether the assignment was removed.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

#### Projects Service Accounts

##### [List project service accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

GET /organization/projects/{project_id}/service_accounts

##### [Create project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

POST /organization/projects/{project_id}/service_accounts

##### [Retrieve project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

GET /organization/projects/{project_id}/service_accounts/{service_account_id}

##### [Update project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

POST /organization/projects/{project_id}/service_accounts/{service_account_id}

##### [Delete project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

DELETE /organization/projects/{project_id}/service_accounts/{service_account_id}

##### Models Expand Collapse

ProjectServiceAccount object { id , created_at , name , 2 more }

Represents an individual service account in a project.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the service account was created

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the service account

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.service_account"

The object type, which is always `organization.project.service_account`

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20object)

role : "owner" or "member" or "none"

`owner`, `member`, or `none`

One of the following:

"owner"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"member"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

"none"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%202)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))

ServiceAccountCreateResponse object { id , api_key , created_at , 3 more }

id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

api_key : object { id , created_at , name , 2 more }

id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20id)

created_at : number

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20created_at)

name : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20name)

object : "organization.project.service_account.api_key"

The object type, which is always `organization.project.service_account.api_key`

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20object)

value : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20api_key)

created_at : number

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.service_account"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

role : "member" or "none"

Service accounts created with default project membership have role `member`. Accounts created with `create_service_account_only` have role `none`.

One of the following:

"member"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"none"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema))

ServiceAccountDeleteResponse object { id , deleted , object }

id : string

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.project.service_account.deleted"

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema))

#### Projects Service Accounts API Keys

##### [Create project service account API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create)

POST /organization/projects/{project_id}/service_accounts/{service_account_id}/api_keys

##### Models Expand Collapse

APIKeyCreateResponse object { id , created_at , name , 2 more }

id : string

The identifier of the API key.

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) when the API key was created.

format unixtime

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the API key.

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.service_account.api_key"

The object type, which is always `organization.project.service_account.api_key`

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

value : string

The unredacted API key value.

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema))

#### Projects API Keys

##### [List project API keys](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

GET /organization/projects/{project_id}/api_keys

##### [Retrieve project API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

GET /organization/projects/{project_id}/api_keys/{api_key_id}

##### [Delete project API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

DELETE /organization/projects/{project_id}/api_keys/{api_key_id}

##### Models Expand Collapse

ProjectAPIKey object { id , created_at , last_used_at , 5 more }

Represents an individual API key in a project.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the API key was created

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20created_at)

last_used_at : number

The Unix timestamp (in seconds) of when the API key was last used.

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20last_used_at)

name : string

The name of the API key

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.api_key"

The object type, which is always `organization.project.api_key`

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20object)

owner : object { service_account , type , user }

service_account : optional object { id , created_at , name , role }

The service account that owns a project API key.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the service account was created.

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20created_at)

name : string

The name of the service account.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20name)

role : string

The service account’s project role.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20service_account)

type : optional "user" or "service_account"

`user` or `service_account`

One of the following:

"user"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20type%20%3E%20(member)%200)

"service_account"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20type)

user : optional object { id , created_at , email , 2 more }

The user that owns a project API key.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) of when the user was created.

format unixtime

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20created_at)

email : string

The email address of the user.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20email)

name : string

The name of the user.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20name)

role : string

The user’s project role.

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner%20%3E%20(property)%20user)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner)

owner_project_access : "active" or "inactive"

Whether the API key’s owner currently has effective access to the project.

One of the following:

"active"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner_project_access%20%3E%20(member)%200)

"inactive"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner_project_access%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20owner_project_access)

redacted_value : string

The redacted value of the API key

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)%20%3E%20(property)%20redacted_value)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))

APIKeyDeleteResponse object { id , deleted , object }

id : string

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "organization.project.api_key.deleted"

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema))

#### Projects Rate Limits

##### [List project rate limits](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

GET /organization/projects/{project_id}/rate_limits

##### [Modify project rate limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

POST /organization/projects/{project_id}/rate_limits/{rate_limit_id}

##### Models Expand Collapse

ProjectRateLimit object { id , max_requests_per_1_minute , max_tokens_per_1_minute , 6 more }

Represents a project rate limit config.

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20id)

max_requests_per_1_minute : number

The maximum requests per minute.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_minute)

max_tokens_per_1_minute : number

The maximum tokens per minute.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_tokens_per_1_minute)

model : string

The model this rate limit applies to.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20model)

object : "project.rate_limit"

The object type, which is always `project.rate_limit`

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20object)

batch_1_day_max_input_tokens : optional number

The maximum batch input tokens per day. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20batch_1_day_max_input_tokens)

max_audio_megabytes_per_1_minute : optional number

The maximum audio megabytes per minute. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_audio_megabytes_per_1_minute)

max_images_per_1_minute : optional number

The maximum images per minute. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_images_per_1_minute)

max_requests_per_1_day : optional number

The maximum requests per day. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_day)

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))

#### Projects Model Permissions

##### [Retrieve project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

GET /organization/projects/{project_id}/model_permissions

##### [Modify project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

POST /organization/projects/{project_id}/model_permissions

##### [Delete project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

DELETE /organization/projects/{project_id}/model_permissions

##### Models Expand Collapse

ProjectModelPermissions object { mode , model_ids , object }

Represents the model allowlist or denylist policy for a project.

mode : "allow_list" or "deny_list"

Whether the project uses an allowlist or a denylist.

One of the following:

"allow_list"

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200)

"deny_list"

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)%20%3E%20(property)%20mode)

model_ids : array of string

The model IDs included in the model permissions policy.

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)%20%3E%20(property)%20model_ids)

object : "project.model_permissions"

The object type, which is always `project.model_permissions`.

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema))

ProjectModelPermissionsDeleted object { deleted , object }

Confirmation payload returned after deleting project model permissions.

deleted : boolean

Whether the project model permissions were deleted.

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "project.model_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema))

#### Projects Hosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

GET /organization/projects/{project_id}/hosted_tool_permissions

##### [Modify project hosted tool permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

POST /organization/projects/{project_id}/hosted_tool_permissions

##### Models Expand Collapse

ProjectHostedToolPermissions object { code_interpreter , file_search , image_generation , 2 more }

Represents hosted tool permissions for a project.

code_interpreter : object { enabled }

Permission state for a single hosted tool on a project.

enabled : boolean

Whether the hosted tool is enabled for the project.

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20enabled)

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

file_search : object { enabled }

Permission state for a single hosted tool on a project.

enabled : boolean

Whether the hosted tool is enabled for the project.

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20enabled)

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20file_search)

image_generation : object { enabled }

Permission state for a single hosted tool on a project.

enabled : boolean

Whether the hosted tool is enabled for the project.

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20image_generation%20%3E%20(property)%20enabled)

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20image_generation)

mcp : object { enabled }

Permission state for a single hosted tool on a project.

enabled : boolean

Whether the hosted tool is enabled for the project.

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20mcp%20%3E%20(property)%20enabled)

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20mcp)

web_search : object { enabled }

Permission state for a single hosted tool on a project.

enabled : boolean

Whether the hosted tool is enabled for the project.

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20web_search%20%3E%20(property)%20enabled)

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)%20%3E%20(property)%20web_search)

[](#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema))

#### Projects Groups

##### [List project groups](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

GET /organization/projects/{project_id}/groups

##### [Add project group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

POST /organization/projects/{project_id}/groups

##### [Retrieve project group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

GET /organization/projects/{project_id}/groups/{group_id}

##### [Remove project group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

DELETE /organization/projects/{project_id}/groups/{group_id}

##### Models Expand Collapse

ProjectGroup object { created_at , group_id , group_name , 3 more }

Details about a group’s membership in a project.

created_at : number

Unix timestamp (in seconds) when the group was granted project access.

format unixtime

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20created_at)

group_id : string

Identifier of the group that has access to the project.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_id)

group_name : string

Display name of the group.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_name)

group_type : "group" or "tenant_group"

The type of the group.

One of the following:

"group"

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%200)

"tenant_group"

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20group_type)

object : "project.group"

Always `project.group`.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20object)

project_id : string

Identifier of the project.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))

GroupDeleteResponse object { deleted , object }

Confirmation payload returned after removing a group from a project.

deleted : boolean

Whether the group membership in the project was removed.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "project.group.deleted"

Always `project.group.deleted`.

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema))

#### Projects Groups Roles

##### [List project group role assignments](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

GET /projects/{project_id}/groups/{group_id}/roles

##### [Assign project role to group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

POST /projects/{project_id}/groups/{group_id}/roles

##### [Retrieve project group role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

GET /projects/{project_id}/groups/{group_id}/roles/{role_id}

##### [Unassign project role from group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

DELETE /projects/{project_id}/groups/{group_id}/roles/{role_id}

##### Models Expand Collapse

RoleListResponse object { id , assignment_sources , created_at , 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

assignment_sources : array of object { principal_id , principal_type }

Principals from which the role assignment is inherited, when available.

principal_id : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_id)

principal_type : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_type)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources)

created_at : number

When the role was created.

format unixtime

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

created_by : string

Identifier of the actor who created the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by)

created_by_user_obj : map [ unknown ]

User details for the actor that created the role, when available.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by_user_obj)

description : string

Description of the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20description)

metadata : map [ unknown ]

Arbitrary metadata stored on the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

Name of the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

permissions : array of string

Permissions associated with the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined by OpenAI.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role applies to.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type)

updated_at : number

When the role was last updated.

format unixtime

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))

RoleCreateResponse object { group , object , role }

Role assignment linking a group to a role.

group : object { id , created_at , name , 2 more }

Summary information about a group returned in role assignment responses.

id : string

Identifier for the group.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the group was created.

format unixtime

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20created_at)

name : string

Display name of the group.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20name)

object : "group"

Always `group`.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20object)

scim_managed : boolean

Whether the group is managed through SCIM.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group%20%3E%20(property)%20scim_managed)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20group)

object : "group.role"

Always `group.role`.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

role : [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id , description , name , 4 more }

Details about a role that can be assigned through the public Roles API.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

RoleRetrieveResponse object { id , assignment_sources , created_at , 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id : string

Identifier for the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

assignment_sources : array of object { principal_id , principal_type }

Principals from which the role assignment is inherited, when available.

principal_id : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_id)

principal_type : string

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources%20%3E%20(items)%20%3E%20(property)%20principal_type)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20assignment_sources)

created_at : number

When the role was created.

format unixtime

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

created_by : string

Identifier of the actor who created the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_by)

created_by_user_obj : map [ unknown ]

User details for the actor that created the role, when available.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_by_user_obj)

description : string

Description of the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20description)

metadata : map [ unknown ]

Arbitrary metadata stored on the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

Name of the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

permissions : array of string

Permissions associated with the role.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20permissions)

predefined_role : boolean

Whether the role is predefined by OpenAI.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20predefined_role)

resource_type : string

Resource type the role applies to.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20resource_type)

updated_at : number

When the role was last updated.

format unixtime

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20updated_at)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

RoleDeleteResponse object { deleted , object }

Confirmation payload returned after unassigning a role.

deleted : boolean

Whether the assignment was removed.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

#### Projects Roles

##### [List project roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

GET /projects/{project_id}/roles

##### [Create project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

POST /projects/{project_id}/roles

##### [Retrieve project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

GET /projects/{project_id}/roles/{role_id}

##### [Update project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

POST /projects/{project_id}/roles/{role_id}

##### [Delete project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

DELETE /projects/{project_id}/roles/{role_id}

##### Models Expand Collapse

RoleDeleteResponse object { id , deleted , object }

Confirmation payload returned after deleting a role.

id : string

Identifier of the deleted role.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the role was deleted.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "role.deleted"

Always `role.deleted`.

[](#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

#### Projects Data Retention

##### [Retrieve project data retention](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

GET /organization/projects/{project_id}/data_retention

##### [Update project data retention](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

POST /organization/projects/{project_id}/data_retention

##### Models Expand Collapse

ProjectDataRetention object { object , type }

Represents a project’s data retention control setting.

object : "project.data_retention"

The object type, which is always `project.data_retention`.

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20object)

type : "organization_default" or "none" or "zero_data_retention" or 3 more

The configured project data retention type.

One of the following:

"organization_default"

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"none"

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"zero_data_retention"

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

"modified_abuse_monitoring"

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203)

"enhanced_zero_data_retention"

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204)

"enhanced_modified_abuse_monitoring"

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205)

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema))

#### Projects Spend Limit

##### [Retrieve project spend limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

GET /organization/projects/{project_id}/spend_limit

##### [Update project spend limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

POST /organization/projects/{project_id}/spend_limit

##### [Delete project spend limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

DELETE /organization/projects/{project_id}/spend_limit

##### Models Expand Collapse

ProjectSpendLimit object { currency , enforcement , interval , 2 more }

Represents a hard spend limit configured at the project level.

currency : string or "USD"

The currency for the threshold amount. Currently, only `USD` is supported.

One of the following:

string

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20currency%20%3E%20(variant)%200)

"USD"

The currency for the threshold amount. Currently, only `USD` is supported.

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20currency%20%3E%20(variant)%201)

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20currency)

enforcement : object { status }

The current enforcement state of the hard spend limit.

status : string or "inactive" or "enforcing"

Whether the hard spend limit is currently enforcing.

One of the following:

string

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20enforcement%20%3E%20(property)%20status%20%3E%20(variant)%200)

"inactive" or "enforcing"

Whether the hard spend limit is currently enforcing.

One of the following:

"inactive"

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20enforcement%20%3E%20(property)%20status%20%3E%20(variant)%201%20%3E%20(member)%200)

"enforcing"

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20enforcement%20%3E%20(property)%20status%20%3E%20(variant)%201%20%3E%20(member)%201)

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20enforcement%20%3E%20(property)%20status%20%3E%20(variant)%201)

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20enforcement%20%3E%20(property)%20status)

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20enforcement)

interval : string or "month"

The time interval for evaluating spend against the threshold. Currently, only `month` is supported.

One of the following:

string

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20interval%20%3E%20(variant)%200)

"month"

The time interval for evaluating spend against the threshold. Currently, only `month` is supported.

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20interval%20%3E%20(variant)%201)

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20interval)

object : "project.spend_limit"

The object type, which is always `project.spend_limit`.

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20object)

threshold_amount : number

The hard spend limit amount, in cents.

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)%20%3E%20(property)%20threshold_amount)

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema))

ProjectSpendLimitDeleted object { deleted , object }

Confirmation payload returned after deleting a project hard spend limit.

deleted : boolean

Whether the hard spend limit was deleted.

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "project.spend_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema))

#### Projects Spend Alerts

##### [List project spend alerts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

GET /organization/projects/{project_id}/spend_alerts

##### [Create project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

POST /organization/projects/{project_id}/spend_alerts

##### [Retrieve project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

GET /organization/projects/{project_id}/spend_alerts/{alert_id}

##### [Update project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

POST /organization/projects/{project_id}/spend_alerts/{alert_id}

##### [Delete project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

DELETE /organization/projects/{project_id}/spend_alerts/{alert_id}

##### Models Expand Collapse

ProjectSpendAlert object { id , currency , interval , 3 more }

Represents a spend alert configured at the project level.

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20id)

currency : "USD"

The currency for the threshold amount.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20currency)

interval : "month"

The time interval for evaluating spend against the threshold.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20interval)

notification_channel : object { recipients , type , subject_prefix }

Email notification settings for a spend alert.

recipients : array of string

Email addresses that receive the spend alert notification.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20notification_channel%20%3E%20(property)%20recipients)

type : "email"

The notification channel type. Currently only `email` is supported.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20notification_channel%20%3E%20(property)%20type)

subject_prefix : optional string

Optional subject prefix for alert emails.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20notification_channel%20%3E%20(property)%20subject_prefix)

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20notification_channel)

object : "project.spend_alert"

The object type, which is always `project.spend_alert`.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20object)

threshold_amount : number

The alert threshold amount, in cents.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)%20%3E%20(property)%20threshold_amount)

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

ProjectSpendAlertDeleted object { id , deleted , object }

Confirmation payload returned after deleting a project spend alert.

id : string

The deleted spend alert ID.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the spend alert was deleted.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "project.spend_alert.deleted"

Always `project.spend_alert.deleted`.

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema))

#### Projects Certificates

##### [List project certificates](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

GET /organization/projects/{project_id}/certificates

##### [Activate certificates for project](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

POST /organization/projects/{project_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

POST /organization/projects/{project_id}/certificates/deactivate

##### Models Expand Collapse

CertificateListResponse object { id , active , certificate_details , 3 more }

Represents an individual certificate configured at the project level.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

active : boolean

Whether the certificate is currently active at the project level.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20active)

certificate_details : object { expires_at , valid_at }

expires_at : optional number

The Unix timestamp (in seconds) of when the certificate expires.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details%20%3E%20(property)%20expires_at)

valid_at : optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details%20%3E%20(property)%20valid_at)

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details)

created_at : number

The Unix timestamp (in seconds) of when the certificate was uploaded.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the certificate.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema))

CertificateActivateResponse object { id , active , certificate_details , 3 more }

Represents an individual certificate configured at the project level.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20id)

active : boolean

Whether the certificate is currently active at the project level.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20active)

certificate_details : object { expires_at , valid_at }

expires_at : optional number

The Unix timestamp (in seconds) of when the certificate expires.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details%20%3E%20(property)%20expires_at)

valid_at : optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details%20%3E%20(property)%20valid_at)

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details)

created_at : number

The Unix timestamp (in seconds) of when the certificate was uploaded.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the certificate.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema))

CertificateDeactivateResponse object { id , active , certificate_details , 3 more }

Represents an individual certificate configured at the project level.

id : string

The identifier, which can be referenced in API endpoints

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20id)

active : boolean

Whether the certificate is currently active at the project level.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20active)

certificate_details : object { expires_at , valid_at }

expires_at : optional number

The Unix timestamp (in seconds) of when the certificate expires.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details%20%3E%20(property)%20expires_at)

valid_at : optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details%20%3E%20(property)%20valid_at)

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20certificate_details)

created_at : number

The Unix timestamp (in seconds) of when the certificate was uploaded.

format unixtime

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the certificate.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/projects
