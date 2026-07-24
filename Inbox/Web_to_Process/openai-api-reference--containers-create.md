---
source_url: https://developers.openai.com/api/reference/resources/containers/methods/create
title: "Create container"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create container

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

# Create container

POST /containers

Create Container

##### Body Parameters JSON Expand Collapse

name : string

Name of the container to create.

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

expires_after : optional object { anchor , minutes }

Container expiration time in seconds relative to the ‘anchor’ time.

anchor : "last_active_at"

Time anchor for the expiration time. Currently only ‘last_active_at’ is supported.

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20anchor)

minutes : number

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema)%20%3E%20(property)%20minutes)

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20expires_after%20%3E%20(schema))

file_ids : optional array of string

IDs of files to copy to the container.

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20file_ids%20%3E%20(schema))

memory_limit : optional "1g" or "4g" or "16g" or "64g"

Optional memory limit for the container. Defaults to “1g”.

One of the following:

"1g"

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20memory_limit%20%3E%20(schema)%20%3E%20(member)%200)

"4g"

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20memory_limit%20%3E%20(schema)%20%3E%20(member)%201)

"16g"

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20memory_limit%20%3E%20(schema)%20%3E%20(member)%202)

"64g"

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20memory_limit%20%3E%20(schema)%20%3E%20(member)%203)

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20memory_limit%20%3E%20(schema))

network_policy : optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type } or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed_domains , type , domain_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled object { type }

type : "disabled"

Disable outbound network access. Always `disabled`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema))

ContainerNetworkPolicyAllowlist object { allowed_domains , type , domain_secrets }

allowed_domains : array of string

A list of allowed domains when type is `allowlist`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20allowed_domains)

type : "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20type)

domain_secrets : optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain , name , value }

Optional domain-scoped secrets for allowlisted domains.

domain : string

The domain associated with the secret.

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20domain)

name : string

The name of the secret to inject for the domain.

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20name)

value : string

The secret value to inject for the domain.

maxLength 10485760

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)%20%3E%20(property)%20domain_secrets)

[](#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema))

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20network_policy%20%3E%20(schema))

skills : optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill_id , type , version } or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description , name , source , type }

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference object { skill_id , type , version }

skill_id : string

The ID of the referenced skill.

maxLength 64

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)%20%3E%20(property)%20skill_id)

type : "skill_reference"

References a skill created with the /v1/skills endpoint.

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)%20%3E%20(property)%20type)

version : optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)%20%3E%20(property)%20version)

[](#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema))

InlineSkill object { description , name , source , type }

description : string

The description of the skill.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20description)

name : string

The name of the skill.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20name)

source : [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data , media_type , type }

Inline skill payload

data : string

Base64-encoded skill zip bundle.

maxLength 70254592

minLength 1

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source%20%2B%20(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)%20%3E%20(property)%20data)

media_type : "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source%20%2B%20(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)%20%3E%20(property)%20media_type)

type : "base64"

The type of the inline skill source. Must be `base64`.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source%20%2B%20(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20source)

type : "inline"

Defines an inline skill for this request.

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema))

[](#(resource)%20containers%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20skills%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Unique identifier for the container.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the container was created.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Name of the container.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : string

The type of this object.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

status : string

Status of the container (e.g., active, deleted).

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20status)

expires_after : optional object { anchor , minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor : optional "last_active_at"

The reference point for the expiration.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

minutes : optional number

The number of minutes after the anchor before the container expires.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20minutes)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_after)

last_active_at : optional number

Unix timestamp (in seconds) when the container was last active.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit)

network_policy : optional object { type , allowed_domains }

Network access policy for the container.

type : "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%200)

"disabled"

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type)

allowed_domains : optional array of string

Allowed outbound domains when `type` is `allowlist`.

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20allowed_domains)

[](#(resource)%20containers%20%3E%20(model)%20container_create_response%20%3E%20(schema)%20%3E%20(property)%20network_policy)

### Create container

```
curl https://api.openai.com/v1/containers \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "My Container",
"memory_limit": "4g",
"skills": [
{
"type": "skill_reference",
"skill_id": "skill_4db6f1a2c9e73508b41f9da06e2c7b5f"
},
{
"type": "skill_reference",
"skill_id": "openai-spreadsheets",
"version": "latest"
}
],
"network_policy": {
"type": "allowlist",
"allowed_domains": ["api.buildkite.com"]
}
}'
```

```
{
"id": "cntr_682e30645a488191b6363a0cbefc0f0a025ec61b66250591",
"object": "container",
"created_at": 1747857508,
"status": "running",
"expires_after": {
"anchor": "last_active_at",
"minutes": 20
},
"last_active_at": 1747857508,
"network_policy": {
"type": "allowlist",
"allowed_domains": ["api.buildkite.com"]
},
"memory_limit": "4g",
"name": "My Container"
}
```

##### Returns Examples

```
{
"id": "cntr_682e30645a488191b6363a0cbefc0f0a025ec61b66250591",
"object": "container",
"created_at": 1747857508,
"status": "running",
"expires_after": {
"anchor": "last_active_at",
"minutes": 20
},
"last_active_at": 1747857508,
"network_policy": {
"type": "allowlist",
"allowed_domains": ["api.buildkite.com"]
},
"memory_limit": "4g",
"name": "My Container"
}
```

---
Source: https://developers.openai.com/api/reference/resources/containers/methods/create
