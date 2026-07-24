---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/methods/list
title: "List vector stores"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List vector stores

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

# List vector stores

GET /vector_stores

Returns a list of vector stores.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

before : optional string

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20before%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [VectorStore](/api/reference/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)) { id , created_at , file_counts , 8 more }

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the vector store was created.

format unixtime

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20created_at)

file_counts : object { cancelled , completed , failed , 2 more }

cancelled : number

The number of files that were cancelled.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20cancelled)

completed : number

The number of files that have been successfully processed.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20completed)

failed : number

The number of files that have failed to process.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20failed)

in_progress : number

The number of files that are currently being processed.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20in_progress)

total : number

The total number of files.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts%20%3E%20(property)%20total)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20file_counts)

last_active_at : number

The Unix timestamp (in seconds) for when the vector store was last active.

format unixtime

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20last_active_at)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

The name of the vector store.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20name)

object : "vector_store"

The object type, which is always `vector_store`.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20object)

status : "expired" or "in_progress" or "completed"

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

One of the following:

"expired"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"in_progress"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"completed"

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20status)

usage_bytes : number

The total number of bytes used by the files in the vector store.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20usage_bytes)

expires_after : optional object { anchor , days }

The expiration policy for a vector store.

anchor : "last_active_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20anchor)

days : number

The number of days after the anchor time that the vector store will expire.

minimum 1

maximum 365

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_after%20%3E%20(property)%20days)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_after)

expires_at : optional number

The Unix timestamp (in seconds) for when the vector store will expire.

format unixtime

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store%20%3E%20(schema)%20%3E%20(property)%20expires_at)

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

first_id : string

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

has_more : boolean

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

last_id : string

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

object : string

[](#(resource)%20vector_stores%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List vector stores

```
curl https://api.openai.com/v1/vector_stores \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-H "OpenAI-Beta: assistants=v2"
```

```
{
"object": "list",
"data": [
{
"id": "vs_abc123",
"object": "vector_store",
"created_at": 1699061776,
"name": "Support FAQ",
"description": "Contains commonly asked questions and answers, organized by topic.",
"bytes": 139920,
"file_counts": {
"in_progress": 0,
"completed": 3,
"failed": 0,
"cancelled": 0,
"total": 3
}
},
{
"id": "vs_abc456",
"object": "vector_store",
"created_at": 1699061776,
"name": "Support FAQ v2",
"description": null,
"bytes": 139920,
"file_counts": {
"in_progress": 0,
"completed": 3,
"failed": 0,
"cancelled": 0,
"total": 3
}
}
],
"first_id": "vs_abc123",
"last_id": "vs_abc456",
"has_more": false
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "vs_abc123",
"object": "vector_store",
"created_at": 1699061776,
"name": "Support FAQ",
"description": "Contains commonly asked questions and answers, organized by topic.",
"bytes": 139920,
"file_counts": {
"in_progress": 0,
"completed": 3,
"failed": 0,
"cancelled": 0,
"total": 3
}
},
{
"id": "vs_abc456",
"object": "vector_store",
"created_at": 1699061776,
"name": "Support FAQ v2",
"description": null,
"bytes": 139920,
"file_counts": {
"in_progress": 0,
"completed": 3,
"failed": 0,
"cancelled": 0,
"total": 3
}
}
],
"first_id": "vs_abc123",
"last_id": "vs_abc456",
"has_more": false
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/methods/list
