---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/users
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

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Users

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

#### Users Roles

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

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/users
