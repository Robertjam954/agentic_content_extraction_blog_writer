---
source_url: https://developers.openai.com/api/reference/resources/containers/methods/list
title: "List containers"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List containers

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

# List containers

GET /containers

List Containers

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

name : optional string

Filter results by container name.

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20name%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of object { id , created_at , name , 6 more }

A list of containers.

id : string

Unique identifier for the container.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the container was created.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Name of the container.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : string

The type of this object.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

status : string

Status of the container (e.g., active, deleted).

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20status)

expires_after : optional object { anchor , minutes }

The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

anchor : optional "last_active_at"

The reference point for the expiration.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

minutes : optional number

The number of minutes after the anchor before the container expires.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20minutes)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_after)

last_active_at : optional number

Unix timestamp (in seconds) when the container was last active.

format unixtime

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

memory_limit : optional "1g" or "4g" or "16g" or "64g"

The memory limit configured for the container.

One of the following:

"1g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%200)

"4g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%201)

"16g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%202)

"64g"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit%20%3E%20(member)%203)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20memory_limit)

network_policy : optional object { type , allowed_domains }

Network access policy for the container.

type : "allowlist" or "disabled"

The network policy mode.

One of the following:

"allowlist"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%200)

"disabled"

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20type)

allowed_domains : optional array of string

Allowed outbound domains when `type` is `allowlist`.

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy%20%3E%20(property)%20allowed_domains)

[](#(resource)%20containers%20%3E%20(model)%20container_list_response%20%3E%20(schema)%20%3E%20(property)%20network_policy)

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

first_id : string

The ID of the first container in the list.

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

has_more : boolean

Whether there are more containers available.

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

last_id : string

The ID of the last container in the list.

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

object : "list"

The type of object returned, must be ‘list’.

[](#(resource)%20containers%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List containers

```
curl https://api.openai.com/v1/containers \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"object": "list",
"data": [
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
],
"first_id": "container_123",
"last_id": "container_123",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
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
],
"first_id": "container_123",
"last_id": "container_123",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/containers/methods/list
