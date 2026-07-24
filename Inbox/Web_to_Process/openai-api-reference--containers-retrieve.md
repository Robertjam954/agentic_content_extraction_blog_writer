---
source_url: https://developers.openai.com/api/reference/resources/containers/methods/retrieve
title: "Retrieve container"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve container

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

# Retrieve container

GET /containers/{container_id}

Retrieve Container

##### P ath Parameters Expand Collapse

container_id : string

[](#(resource)%20containers%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20container_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Unique identifier for the container.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the container was created.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Name of the container.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : string

The type of this object.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20object)

status : string

Status of the container (e.g., active, deleted).

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20status)

expires_after : optional object { anchor , minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor : optional "last_active_at"

The reference point for the expiration.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

minutes : optional number

The number of minutes after the anchor before the container expires.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20minutes)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20expires_after)

last_active_at : optional number

Unix timestamp (in seconds) when the container was last active.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit)

network_policy : optional object { type , allowed_domains }

Network access policy for the container.

type : "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%200)

"disabled"

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type)

allowed_domains : optional array of string

Allowed outbound domains when `type` is `allowlist`.

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20allowed_domains)

[](#(resource)%20containers%20%3E%20(model)%20container_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20network_policy)

### Retrieve container

```
curl https://api.openai.com/v1/containers/cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863 \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
"object": "container",
"created_at": 1747844794,
"status": "running",
"expires_after": {
"anchor": "last_active_at",
"minutes": 20
},
"last_active_at": 1747844794,
"memory_limit": "4g",
"name": "My Container"
}
```

##### Returns Examples

```
{
"id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
"object": "container",
"created_at": 1747844794,
"status": "running",
"expires_after": {
"anchor": "last_active_at",
"minutes": 20
},
"last_active_at": 1747844794,
"memory_limit": "4g",
"name": "My Container"
}
```

---
Source: https://developers.openai.com/api/reference/resources/containers/methods/retrieve
