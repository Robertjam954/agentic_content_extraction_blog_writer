---
source_url: https://developers.openai.com/api/reference/resources/containers/subresources/files/methods/list
title: "List container files"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List container files

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Containers](/api/reference/resources/containers)

[Files](/api/reference/resources/containers/subresources/files)

# List container files

GET /containers/{container_id}/files

List Container files

##### P ath Parameters Expand Collapse

container_id : string

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20container_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

order : optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%200)

"desc"

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))

##### Returns Expand Collapse

data : array of object { id , bytes , container_id , 4 more }

A list of container files.

id : string

Unique identifier for the file.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

bytes : number

Size of the file in bytes.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20bytes)

container_id : string

The container this file belongs to.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20container_id)

created_at : number

Unix timestamp (in seconds) when the file was created.

format unixtime

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : string

The type of this object (`container.file`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

path : string

Path of the file in the container.

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20path)

source : string

Source of the file (e.g., `user`, `assistant`).

[](#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)%20%3E%20(property)%20source)

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

first_id : string

The ID of the first file in the list.

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

has_more : boolean

Whether there are more files available.

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

last_id : string

The ID of the last file in the list.

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

object : "list"

The type of object returned, must be ‘list’.

[](#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List container files

```
curl https://api.openai.com/v1/containers/cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04/files \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"object": "list",
"data": [
{
"id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"object": "container.file",
"created_at": 1747848842,
"bytes": 880,
"container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
"path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
"source": "user"
}
],
"first_id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"has_more": false,
"last_id": "cfile_682e0e8a43c88191a7978f477a09bdf5"
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"object": "container.file",
"created_at": 1747848842,
"bytes": 880,
"container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
"path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
"source": "user"
}
],
"first_id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
"has_more": false,
"last_id": "cfile_682e0e8a43c88191a7978f477a09bdf5"
}
```

---
Source: https://developers.openai.com/api/reference/resources/containers/subresources/files/methods/list
