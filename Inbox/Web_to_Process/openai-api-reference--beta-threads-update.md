---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/update
title: "Modify thread"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Modify thread

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

# Modify thread

POST /threads/{thread_id}

Modifies a thread.

##### P ath Parameters Expand Collapse

thread_id : string

[](#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20thread_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20metadata%20%3E%20(schema))

tool_resources : optional object { code_interpreter , file_search }

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code_interpreter : optional object { file_ids }

file_ids : optional array of string

A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

[](#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20file_ids)

[](#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

file_search : optional object { vector_store_ids }

vector_store_ids : optional array of string

The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

[](#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_store_ids)

[](#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema)%20%3E%20(property)%20file_search)

[](#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%200%20%3E%20(param)%20tool_resources%20%3E%20(schema))

##### Returns Expand Collapse

Thread object { id , created_at , metadata , 2 more }

Represents a thread that contains [messages](/docs/api-reference/messages).

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the thread was created.

format unixtime

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20created_at)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20metadata)

object : "thread"

The object type, which is always `thread`.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20object)

tool_resources : object { code_interpreter , file_search }

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code_interpreter : optional object { file_ids }

file_ids : optional array of string

A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20file_ids)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20code_interpreter)

file_search : optional object { vector_store_ids }

vector_store_ids : optional array of string

The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20file_search%20%3E%20(property)%20vector_store_ids)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources%20%3E%20(property)%20file_search)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)%20%3E%20(property)%20tool_resources)

[](#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

### Modify thread

```
curl https://api.openai.com/v1/threads/thread_abc123 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "OpenAI-Beta: assistants=v2" \
-d '{
"metadata": {
"modified": "true",
"user": "abc123"
}
}'
```

```
{
"id": "thread_abc123",
"object": "thread",
"created_at": 1699014083,
"metadata": {
"modified": "true",
"user": "abc123"
},
"tool_resources": {}
}
```

##### Returns Examples

```
{
"id": "thread_abc123",
"object": "thread",
"created_at": 1699014083,
"metadata": {
"modified": "true",
"user": "abc123"
},
"tool_resources": {}
}
```

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/update
