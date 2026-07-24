---
source_url: https://developers.openai.com/api/reference/resources/projects/subresources/groups
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

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Groups

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

#### Groups Roles

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

---
Source: https://developers.openai.com/api/reference/resources/projects/subresources/groups
