---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs
title: "Audit Logs"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Audit Logs

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# Audit Logs

List user actions and configuration changes within this organization.

##### [List audit logs](/api/reference/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

GET /organization/audit_logs

##### Models Expand Collapse

AuditLogListResponse object { id , effective_at , type , 57 more }

A log of a user action or configuration change within this organization.

id : string

The ID of this log.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

effective_at : number

The Unix timestamp (in seconds) of the event.

format unixtime

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20effective_at)

type : "api_key.created" or "api_key.updated" or "api_key.deleted" or 140 more

The event type.

One of the following:

"api_key.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"api_key.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"api_key.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

"certificate.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203)

"certificate.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204)

"certificate.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205)

"certificates.activated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206)

"certificates.deactivated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207)

"checkpoint.permission.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208)

"checkpoint.permission.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%209)

"external_key.registered"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2010)

"external_key.removed"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2011)

"group.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2012)

"group.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2013)

"group.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2014)

"invite.sent"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2015)

"invite.accepted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2016)

"invite.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2017)

"ip_allowlist.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2018)

"ip_allowlist.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2019)

"ip_allowlist.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2020)

"ip_allowlist.config.activated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2021)

"ip_allowlist.config.deactivated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2022)

"login.succeeded"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2023)

"login.failed"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2024)

"logout.succeeded"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2025)

"logout.failed"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2026)

"organization.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2027)

"project.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2028)

"project.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2029)

"project.archived"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2030)

"project.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2031)

"rate_limit.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2032)

"rate_limit.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2033)

"resource.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2034)

"tunnel.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2035)

"tunnel.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2036)

"tunnel.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2037)

"workload_identity_provider.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2038)

"workload_identity_provider.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2039)

"workload_identity_provider.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2040)

"workload_identity_provider_mapping.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2041)

"workload_identity_provider_mapping.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2042)

"workload_identity_provider_mapping.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2043)

"role.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2044)

"role.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2045)

"role.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2046)

"role.assignment.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2047)

"role.assignment.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2048)

"role.bound_to_resource"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2049)

"role.unbound_from_resource"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2050)

"scim.enabled"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2051)

"scim.disabled"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2052)

"service_account.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2053)

"service_account.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2054)

"service_account.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2055)

"user.added"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2056)

"user.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2057)

"user.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2058)

"tenant.metadata.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2059)

"tenant.microsoft_entra_mapping.upserted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2060)

"tenant.microsoft_entra_mapping.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2061)

"tenant.workload_identity.provider.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2062)

"tenant.workload_identity.provider.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2063)

"tenant.workload_identity.provider.archived"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2064)

"tenant.workload_identity.mapping.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2065)

"tenant.workload_identity.mapping.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2066)

"tenant.workload_identity.mapping.archived"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2067)

"tenant.workload_identity.binding.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2068)

"tenant.workload_identity.principal.provisioned"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2069)

"tenant.admin_api_key.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2070)

"tenant.admin_api_key.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2071)

"tenant.admin_api_key.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2072)

"tenant.project_api_key.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2073)

"tenant.chatgpt_access_token.revoked"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2074)

"tenant.migration.completed"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2075)

"tenant.sso.migrated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2076)

"tenant.domains.migrated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2077)

"tenant.sso_connection.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2078)

"tenant.sso_connection.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2079)

"tenant.sso_connection.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2080)

"tenant.sso_connection.setup.started"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2081)

"tenant.policy.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2082)

"tenant.policy.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2083)

"tenant.policy.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2084)

"tenant.policy.attached"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2085)

"tenant.policy.detached"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2086)

"tenant.principal_authentication_policy.resolved"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2087)

"tenant.scim.setup.started"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2088)

"tenant.scim.deletion.requested"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2089)

"tenant.scim.directory.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2090)

"tenant.product_access_policy.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2091)

"tenant.resource_share_grant.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2092)

"tenant.resource_share_grant.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2093)

"tenant.resource_share_grant.accepted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2094)

"tenant.resource_share_grant.declined"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2095)

"tenant.resource_share_grant.revoked"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2096)

"tenant.resource_share_grant.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2097)

"tenant.service_account.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2098)

"tenant.service_account.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2099)

"tenant.service_account.token.revoked"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20100)

"tenant.billing.overage_limit.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20101)

"tenant.billing.alerts.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20102)

"tenant.billing.info.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20103)

"tenant.usage_limit.workspace.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20104)

"tenant.usage_limit.group.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20105)

"tenant.usage_limit.user.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20106)

"tenant.usage_limit.increase_request.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20107)

"tenant.usage_limit.increase_request.resolved"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20108)

"tenant.group.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20109)

"tenant.group.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20110)

"tenant.group.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20111)

"tenant.group.member.added"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20112)

"tenant.group.member.removed"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20113)

"tenant.migration_rollout.status.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20114)

"tenant.migration_rollout.tier.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20115)

"tenant.role.metadata.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20116)

"tenant.custom_role.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20117)

"tenant.custom_role.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20118)

"tenant.custom_role.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20119)

"tenant.role_assignment.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20120)

"tenant.role_assignment.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20121)

"tenant.resource_role_assignment.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20122)

"tenant.resource_role_assignment.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20123)

"tenant.resource_access.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20124)

"tenant.resource_access.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20125)

"tenant.session_policy.created"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20126)

"tenant.session_policy.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20127)

"tenant.session_policy.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20128)

"tenant.session_revocation.started"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20129)

"tenant.third_party_app_policy.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20130)

"tenant.user.added"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20131)

"tenant.user.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20132)

"tenant.user.removed"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20133)

"tenant.user.looked_up"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20134)

"tenant.user.invited"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20135)

"tenant.membership.revoked"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20136)

"tenant.api_organization_invite.upserted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20137)

"tenant.api_organization_invite.deleted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20138)

"tenant.chatgpt_workspace_invite.upserted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20139)

"tenant.membership.accepted"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20140)

"tenant.membership.declined"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20141)

"tenant.workspace_invite_email_settings.updated"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%20142)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20type)

actor : optional object { api_key , session , type }

The actor who performed the audit logged action.

api_key : optional object { id , service_account , type , user }

The API Key used to perform the audit logged action.

id : optional string

The tracking id of the API key.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20id)

service_account : optional object { id }

The service account that performed the audit logged action.

id : optional string

The service account id.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20service_account%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20service_account)

type : optional "user" or "service_account"

The type of API key. Can be either `user` or `service_account`.

One of the following:

"user"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20type%20%3E%20(member)%200)

"service_account"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20type)

user : optional object { id , email }

The user who performed the audit logged action.

id : optional string

The user id.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20user%20%3E%20(property)%20id)

email : optional string

The user email.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20user%20%3E%20(property)%20email)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key%20%3E%20(property)%20user)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20api_key)

session : optional object { ip_address , user }

The session in which the audit logged action was performed.

ip_address : optional string

The IP address from which the action was performed.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20session%20%3E%20(property)%20ip_address)

user : optional object { id , email }

The user who performed the audit logged action.

id : optional string

The user id.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20session%20%3E%20(property)%20user%20%3E%20(property)%20id)

email : optional string

The user email.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20session%20%3E%20(property)%20user%20%3E%20(property)%20email)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20session%20%3E%20(property)%20user)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20session)

type : optional "session" or "api_key"

The type of actor. Is either `session` or `api_key`.

One of the following:

"session"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%200)

"api_key"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20actor)

"api_key.created" : optional object { id , data }

The details for events with this `type`.

id : optional string

The tracking ID of the API key.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.created%20%3E%20(property)%20id)

data : optional object { scopes }

The payload used to create the API key.

scopes : optional array of string

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.created%20%3E%20(property)%20data%20%3E%20(property)%20scopes)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.created%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.created)

"api_key.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The tracking ID of the API key.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.deleted)

"api_key.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The tracking ID of the API key.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.updated%20%3E%20(property)%20id)

changes_requested : optional object { scopes }

The payload used to update the API key.

scopes : optional array of string

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20scopes)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20api_key.updated)

"certificate.created" : optional object { id , name }

The details for events with this `type`.

id : optional string

The certificate ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.created%20%3E%20(property)%20id)

name : optional string

The name of the certificate.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.created%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.created)

"certificate.deleted" : optional object { id , certificate , name }

The details for events with this `type`.

id : optional string

The certificate ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.deleted%20%3E%20(property)%20id)

certificate : optional string

The certificate content in PEM format.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.deleted%20%3E%20(property)%20certificate)

name : optional string

The name of the certificate.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.deleted%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.deleted)

"certificate.updated" : optional object { id , name }

The details for events with this `type`.

id : optional string

The certificate ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.updated%20%3E%20(property)%20id)

name : optional string

The name of the certificate.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.updated%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate.updated)

"certificates.activated" : optional object { certificates }

The details for events with this `type`.

certificates : optional array of object { id , name }

id : optional string

The certificate ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.activated%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20id)

name : optional string

The name of the certificate.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.activated%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.activated%20%3E%20(property)%20certificates)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.activated)

"certificates.deactivated" : optional object { certificates }

The details for events with this `type`.

certificates : optional array of object { id , name }

id : optional string

The certificate ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.deactivated%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20id)

name : optional string

The name of the certificate.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.deactivated%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.deactivated%20%3E%20(property)%20certificates)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates.deactivated)

"checkpoint.permission.created" : optional object { id , data }

The project and fine-tuned model checkpoint that the checkpoint permission was created for.

id : optional string

The ID of the checkpoint permission.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20checkpoint.permission.created%20%3E%20(property)%20id)

data : optional object { fine_tuned_model_checkpoint , project_id }

The payload used to create the checkpoint permission.

fine_tuned_model_checkpoint : optional string

The ID of the fine-tuned model checkpoint.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20checkpoint.permission.created%20%3E%20(property)%20data%20%3E%20(property)%20fine_tuned_model_checkpoint)

project_id : optional string

The ID of the project that the checkpoint permission was created for.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20checkpoint.permission.created%20%3E%20(property)%20data%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20checkpoint.permission.created%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20checkpoint.permission.created)

"checkpoint.permission.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The ID of the checkpoint permission.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20checkpoint.permission.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20checkpoint.permission.deleted)

"external_key.registered" : optional object { id , data }

The details for events with this `type`.

id : optional string

The ID of the external key configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20external_key.registered%20%3E%20(property)%20id)

data : optional unknown

The configuration for the external key.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20external_key.registered%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20external_key.registered)

"external_key.removed" : optional object { id }

The details for events with this `type`.

id : optional string

The ID of the external key configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20external_key.removed%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20external_key.removed)

"group.created" : optional object { id , data }

The details for events with this `type`.

id : optional string

The ID of the group.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.created%20%3E%20(property)%20id)

data : optional object { group_name }

Information about the created group.

group_name : optional string

The group name.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.created%20%3E%20(property)%20data%20%3E%20(property)%20group_name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.created%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.created)

"group.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The ID of the group.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.deleted)

"group.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The ID of the group.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.updated%20%3E%20(property)%20id)

changes_requested : optional object { group_name }

The payload used to update the group.

group_name : optional string

The updated group name.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20group_name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20group.updated)

"invite.accepted" : optional object { id }

The details for events with this `type`.

id : optional string

The ID of the invite.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.accepted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.accepted)

"invite.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The ID of the invite.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.deleted)

"invite.sent" : optional object { id , data }

The details for events with this `type`.

id : optional string

The ID of the invite.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.sent%20%3E%20(property)%20id)

data : optional object { email , role }

The payload used to create the invite.

email : optional string

The email invited to the organization.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.sent%20%3E%20(property)%20data%20%3E%20(property)%20email)

role : optional string

The role the email was invited to be. Is either `owner` or `member`.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.sent%20%3E%20(property)%20data%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.sent%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20invite.sent)

"ip_allowlist.config.activated" : optional object { configs }

The details for events with this `type`.

configs : optional array of object { id , name }

The configurations that were activated.

id : optional string

The ID of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.activated%20%3E%20(property)%20configs%20%3E%20(items)%20%3E%20(property)%20id)

name : optional string

The name of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.activated%20%3E%20(property)%20configs%20%3E%20(items)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.activated%20%3E%20(property)%20configs)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.activated)

"ip_allowlist.config.deactivated" : optional object { configs }

The details for events with this `type`.

configs : optional array of object { id , name }

The configurations that were deactivated.

id : optional string

The ID of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.deactivated%20%3E%20(property)%20configs%20%3E%20(items)%20%3E%20(property)%20id)

name : optional string

The name of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.deactivated%20%3E%20(property)%20configs%20%3E%20(items)%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.deactivated%20%3E%20(property)%20configs)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.config.deactivated)

"ip_allowlist.created" : optional object { id , allowed_ips , name }

The details for events with this `type`.

id : optional string

The ID of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.created%20%3E%20(property)%20id)

allowed_ips : optional array of string

The IP addresses or CIDR ranges included in the configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.created%20%3E%20(property)%20allowed_ips)

name : optional string

The name of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.created%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.created)

"ip_allowlist.deleted" : optional object { id , allowed_ips , name }

The details for events with this `type`.

id : optional string

The ID of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.deleted%20%3E%20(property)%20id)

allowed_ips : optional array of string

The IP addresses or CIDR ranges that were in the configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.deleted%20%3E%20(property)%20allowed_ips)

name : optional string

The name of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.deleted%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.deleted)

"ip_allowlist.updated" : optional object { id , allowed_ips }

The details for events with this `type`.

id : optional string

The ID of the IP allowlist configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.updated%20%3E%20(property)%20id)

allowed_ips : optional array of string

The updated set of IP addresses or CIDR ranges in the configuration.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.updated%20%3E%20(property)%20allowed_ips)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20ip_allowlist.updated)

"login.failed" : optional object { error_code , error_message }

The details for events with this `type`.

error_code : optional string

The error code of the failure.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20login.failed%20%3E%20(property)%20error_code)

error_message : optional string

The error message of the failure.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20login.failed%20%3E%20(property)%20error_message)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20login.failed)

"login.succeeded" : optional unknown

This event has no additional fields beyond the standard audit log attributes.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20login.succeeded)

"logout.failed" : optional object { error_code , error_message }

The details for events with this `type`.

error_code : optional string

The error code of the failure.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20logout.failed%20%3E%20(property)%20error_code)

error_message : optional string

The error message of the failure.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20logout.failed%20%3E%20(property)%20error_message)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20logout.failed)

"logout.succeeded" : optional unknown

This event has no additional fields beyond the standard audit log attributes.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20logout.succeeded)

"organization.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The organization ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20id)

changes_requested : optional object { api_call_logging , api_call_logging_project_ids , description , 4 more }

The payload used to update the organization settings.

api_call_logging : optional string

How your organization logs data from supported API calls. One of `disabled`, `enabled_per_call`, `enabled_for_all_projects`, or `enabled_for_selected_projects`

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20api_call_logging)

api_call_logging_project_ids : optional string

The list of project ids if api_call_logging is set to `enabled_for_selected_projects`

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20api_call_logging_project_ids)

description : optional string

The organization description.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20description)

name : optional string

The organization name.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20name)

threads_ui_visibility : optional string

Visibility of the threads page which shows messages created with the Assistants API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20threads_ui_visibility)

title : optional string

The organization title.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20title)

usage_dashboard_visibility : optional string

Visibility of the usage dashboard which shows activity and costs for your organization. One of `ANY_ROLE` or `OWNERS`.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20usage_dashboard_visibility)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20organization.updated)

project : optional object { id , name }

The project that the action was scoped to. Absent for actions not scoped to projects. Note that any admin actions taken via Admin API keys are associated with the default project.

id : optional string

The project ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project%20%3E%20(property)%20id)

name : optional string

The project title.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project)

"project.archived" : optional object { id }

The details for events with this `type`.

id : optional string

The project ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.archived%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.archived)

"project.created" : optional object { id , data }

The details for events with this `type`.

id : optional string

The project ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.created%20%3E%20(property)%20id)

data : optional object { name , title }

The payload used to create the project.

name : optional string

The project name.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.created%20%3E%20(property)%20data%20%3E%20(property)%20name)

title : optional string

The title of the project as seen on the dashboard.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.created%20%3E%20(property)%20data%20%3E%20(property)%20title)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.created%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.created)

"project.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The project ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.deleted)

"project.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The project ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.updated%20%3E%20(property)%20id)

changes_requested : optional object { title }

The payload used to update the project.

title : optional string

The title of the project as seen on the dashboard.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20title)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20project.updated)

"rate_limit.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The rate limit ID

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.deleted)

"rate_limit.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The rate limit ID

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20id)

changes_requested : optional object { batch_1_day_max_input_tokens , max_audio_megabytes_per_1_minute , max_images_per_1_minute , 3 more }

The payload used to update the rate limits.

batch_1_day_max_input_tokens : optional number

The maximum batch input tokens per day. Only relevant for certain models.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20batch_1_day_max_input_tokens)

max_audio_megabytes_per_1_minute : optional number

The maximum audio megabytes per minute. Only relevant for certain models.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20max_audio_megabytes_per_1_minute)

max_images_per_1_minute : optional number

The maximum images per minute. Only relevant for certain models.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20max_images_per_1_minute)

max_requests_per_1_day : optional number

The maximum requests per day. Only relevant for certain models.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20max_requests_per_1_day)

max_requests_per_1_minute : optional number

The maximum requests per minute.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20max_requests_per_1_minute)

max_tokens_per_1_minute : optional number

The maximum tokens per minute.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20max_tokens_per_1_minute)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit.updated)

"role.assignment.created" : optional object { id , principal_id , principal_type , 2 more }

The details for events with this `type`.

id : optional string

The identifier of the role assignment.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.created%20%3E%20(property)%20id)

principal_id : optional string

The principal (user or group) that received the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.created%20%3E%20(property)%20principal_id)

principal_type : optional string

The type of principal (user or group) that received the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.created%20%3E%20(property)%20principal_type)

resource_id : optional string

The resource the role assignment is scoped to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.created%20%3E%20(property)%20resource_id)

resource_type : optional string

The type of resource the role assignment is scoped to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.created%20%3E%20(property)%20resource_type)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.created)

"role.assignment.deleted" : optional object { id , principal_id , principal_type , 2 more }

The details for events with this `type`.

id : optional string

The identifier of the role assignment.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.deleted%20%3E%20(property)%20id)

principal_id : optional string

The principal (user or group) that had the role removed.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.deleted%20%3E%20(property)%20principal_id)

principal_type : optional string

The type of principal (user or group) that had the role removed.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.deleted%20%3E%20(property)%20principal_type)

resource_id : optional string

The resource the role assignment was scoped to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.deleted%20%3E%20(property)%20resource_id)

resource_type : optional string

The type of resource the role assignment was scoped to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.deleted%20%3E%20(property)%20resource_type)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.assignment.deleted)

"role.bound_to_resource" : optional object { id , connector_id , connector_name , 7 more }

The details for events with this `type`.

id : optional string

The ID of the resource the role was bound to. ChatGPT workspace connector resources use ` __ `.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20id)

connector_id : optional string

The connector ID for a ChatGPT workspace connector resource.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20connector_id)

connector_name : optional string

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20connector_name)

enabled : optional boolean

Whether the connector is enabled for the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20enabled)

permissions : optional array of string

The permissions granted to the role for the resource.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20permissions)

resource_id : optional string

The ID of the resource the role was bound to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20resource_id)

resource_type : optional string

The type of resource the role was bound to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20resource_type)

role_id : optional string

The ID of the role that was bound to the resource.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20role_id)

source : optional "role_toggle" or "role_connector_update" or "role_delete" or 2 more

The connector role mutation path that produced the event.

One of the following:

"role_toggle"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20source%20%3E%20(member)%200)

"role_connector_update"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20source%20%3E%20(member)%201)

"role_delete"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20source%20%3E%20(member)%202)

"workspace_permissions"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20source%20%3E%20(member)%203)

"connector_publish"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20source%20%3E%20(member)%204)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20source)

workspace_id : optional string

The workspace ID for a ChatGPT workspace connector resource.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource%20%3E%20(property)%20workspace_id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.bound_to_resource)

"role.created" : optional object { id , permissions , resource_id , 2 more }

The details for events with this `type`.

id : optional string

The role ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.created%20%3E%20(property)%20id)

permissions : optional array of string

The permissions granted by the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.created%20%3E%20(property)%20permissions)

resource_id : optional string

The resource the role is scoped to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.created%20%3E%20(property)%20resource_id)

resource_type : optional string

The type of resource the role belongs to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.created%20%3E%20(property)%20resource_type)

role_name : optional string

The name of the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.created%20%3E%20(property)%20role_name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.created)

"role.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The role ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.deleted)

"role.unbound_from_resource" : optional object { id , connector_id , connector_name , 7 more }

The details for events with this `type`.

id : optional string

The ID of the resource the role was unbound from. ChatGPT workspace connector resources use ` __ `.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20id)

connector_id : optional string

The connector ID for a ChatGPT workspace connector resource.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20connector_id)

connector_name : optional string

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20connector_name)

enabled : optional boolean

Whether the connector is enabled for the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20enabled)

permissions : optional array of string

The permissions remaining for the role after the change.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20permissions)

resource_id : optional string

The ID of the resource the role was unbound from.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20resource_id)

resource_type : optional string

The type of resource the role was unbound from.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20resource_type)

role_id : optional string

The ID of the role that was unbound from the resource.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20role_id)

source : optional "role_toggle" or "role_connector_update" or "role_delete" or 2 more

The connector role mutation path that produced the event.

One of the following:

"role_toggle"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20source%20%3E%20(member)%200)

"role_connector_update"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20source%20%3E%20(member)%201)

"role_delete"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20source%20%3E%20(member)%202)

"workspace_permissions"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20source%20%3E%20(member)%203)

"connector_publish"

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20source%20%3E%20(member)%204)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20source)

workspace_id : optional string

The workspace ID for a ChatGPT workspace connector resource.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource%20%3E%20(property)%20workspace_id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.unbound_from_resource)

"role.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The role ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20id)

changes_requested : optional object { description , metadata , permissions_added , 4 more }

The payload used to update the role.

description : optional string

The updated role description, when provided.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20description)

metadata : optional unknown

Additional metadata stored on the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20metadata)

permissions_added : optional array of string

The permissions added to the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20permissions_added)

permissions_removed : optional array of string

The permissions removed from the role.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20permissions_removed)

resource_id : optional string

The resource the role is scoped to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20resource_id)

resource_type : optional string

The type of resource the role belongs to.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20resource_type)

role_name : optional string

The updated role name, when provided.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20role_name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20role.updated)

"scim.disabled" : optional object { id }

The details for events with this `type`.

id : optional string

The ID of the SCIM was disabled for.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20scim.disabled%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20scim.disabled)

"scim.enabled" : optional object { id }

The details for events with this `type`.

id : optional string

The ID of the SCIM was enabled for.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20scim.enabled%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20scim.enabled)

"service_account.created" : optional object { id , data }

The details for events with this `type`.

id : optional string

The service account ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.created%20%3E%20(property)%20id)

data : optional object { role }

The payload used to create the service account.

role : optional string

The role of the service account. Is either `owner` or `member`.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.created%20%3E%20(property)%20data%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.created%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.created)

"service_account.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The service account ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.deleted)

"service_account.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The service account ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.updated%20%3E%20(property)%20id)

changes_requested : optional object { role }

The payload used to updated the service account.

role : optional string

The role of the service account. Is either `owner` or `member`.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20service_account.updated)

"user.added" : optional object { id , data }

The details for events with this `type`.

id : optional string

The user ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.added%20%3E%20(property)%20id)

data : optional object { role }

The payload used to add the user to the project.

role : optional string

The role of the user. Is either `owner` or `member`.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.added%20%3E%20(property)%20data%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.added%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.added)

"user.deleted" : optional object { id }

The details for events with this `type`.

id : optional string

The user ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.deleted%20%3E%20(property)%20id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.deleted)

"user.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The project ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.updated%20%3E%20(property)%20id)

changes_requested : optional object { role }

The payload used to update the user.

role : optional string

The role of the user. Is either `owner` or `member`.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.updated%20%3E%20(property)%20changes_requested%20%3E%20(property)%20role)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20user.updated)

"workload_identity_provider_mapping.created" : optional object { id , data , identity_provider_id }

The details for events with this `type`.

id : optional string

The workload identity provider mapping ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.created%20%3E%20(property)%20id)

data : optional unknown

The payload used to create the workload identity provider mapping.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.created%20%3E%20(property)%20data)

identity_provider_id : optional string

The workload identity provider ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.created%20%3E%20(property)%20identity_provider_id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.created)

"workload_identity_provider_mapping.deleted" : optional object { id , identity_provider_id , project_id , service_account_id }

The details for events with this `type`.

id : optional string

The workload identity provider mapping ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.deleted%20%3E%20(property)%20id)

identity_provider_id : optional string

The workload identity provider ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.deleted%20%3E%20(property)%20identity_provider_id)

project_id : optional string

The project ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.deleted%20%3E%20(property)%20project_id)

service_account_id : optional string

The mapped service account ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.deleted%20%3E%20(property)%20service_account_id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.deleted)

"workload_identity_provider_mapping.updated" : optional object { id , changes_requested , identity_provider_id }

The details for events with this `type`.

id : optional string

The workload identity provider mapping ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.updated%20%3E%20(property)%20id)

changes_requested : optional unknown

The payload used to update the workload identity provider mapping.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.updated%20%3E%20(property)%20changes_requested)

identity_provider_id : optional string

The workload identity provider ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.updated%20%3E%20(property)%20identity_provider_id)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider_mapping.updated)

"workload_identity_provider.created" : optional object { id , data }

The details for events with this `type`.

id : optional string

The workload identity provider ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.created%20%3E%20(property)%20id)

data : optional unknown

The payload used to create the workload identity provider.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.created%20%3E%20(property)%20data)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.created)

"workload_identity_provider.deleted" : optional object { id , name }

The details for events with this `type`.

id : optional string

The workload identity provider ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.deleted%20%3E%20(property)%20id)

name : optional string

The workload identity provider name.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.deleted%20%3E%20(property)%20name)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.deleted)

"workload_identity_provider.updated" : optional object { id , changes_requested }

The details for events with this `type`.

id : optional string

The workload identity provider ID.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.updated%20%3E%20(property)%20id)

changes_requested : optional unknown

The payload used to update the workload identity provider.

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.updated%20%3E%20(property)%20changes_requested)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)%20%3E%20(property)%20workload_identity_provider.updated)

[](#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs
