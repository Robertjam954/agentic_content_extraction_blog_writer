---
source_url: https://developers.openai.com/api/reference/resources/vector_stores/methods/search
title: "Search vector store"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Search vector store

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

# Search vector store

POST /vector_stores/{vector_store_id}/search

Search a vector store for relevant chunks based on a query and file attributes filter.

##### P ath Parameters Expand Collapse

vector_store_id : string

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%20default%20%3E%20(param)%20vector_store_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

query : string or array of string

A query string for a search

One of the following:

string

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20query%20%3E%20(schema)%20%3E%20(variant)%200)

array of string

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20query%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20query%20%3E%20(schema))

filters : optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key , type , value } or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters , type }

A filter to apply based on file attributes.

One of the following:

ComparisonFilter object { key , type , value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key : string

The key to compare against the value.

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20key)

type : "eq" or "ne" or "gt" or 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

- `eq`: equals

- `ne`: not equal

- `gt`: greater than

- `gte`: greater than or equal

- `lt`: less than

- `lte`: less than or equal

- `in`: in

- `nin`: not in

One of the following:

"eq"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"ne"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"gt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

"gte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203)

"lt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204)

"lte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205)

"in"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206)

"nin"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type)

value : string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%201)

boolean

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%202)

array of string or number

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

CompoundFilter object { filters , type }

Combine multiple filters using `and` or `or`.

filters : array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key , type , value } or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

ComparisonFilter object { key , type , value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key : string

The key to compare against the value.

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20key)

type : "eq" or "ne" or "gt" or 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

- `eq`: equals

- `ne`: not equal

- `gt`: greater than

- `gte`: greater than or equal

- `lt`: less than

- `lte`: less than or equal

- `in`: in

- `nin`: not in

One of the following:

"eq"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"ne"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"gt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

"gte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203)

"lt"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204)

"lte"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205)

"in"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206)

"nin"

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20type)

value : string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%201)

boolean

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%202)

array of string or number

One of the following:

string

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)%20%3E%20(property)%20value)

[](#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

unknown

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20filters)

type : "and" or "or"

Type of operation: `and` or `or`.

One of the following:

"and"

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"or"

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema))

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20filters%20%3E%20(schema))

max_num_results : optional number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

minimum 1

maximum 50

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20max_num_results%20%3E%20(schema))

ranking_options : optional object { ranker , score_threshold }

Ranking options for search.

ranker : optional "none" or "auto" or "default-2024-11-15"

Enable re-ranking; set to `none` to disable, which can help reduce latency.

One of the following:

"none"

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20ranking_options%20%3E%20(schema)%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"auto"

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20ranking_options%20%3E%20(schema)%20%3E%20(property)%20ranker%20%3E%20(member)%201)

"default-2024-11-15"

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20ranking_options%20%3E%20(schema)%20%3E%20(property)%20ranker%20%3E%20(member)%202)

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20ranking_options%20%3E%20(schema)%20%3E%20(property)%20ranker)

score_threshold : optional number

minimum 0

maximum 1

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20ranking_options%20%3E%20(schema)%20%3E%20(property)%20score_threshold)

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20ranking_options%20%3E%20(schema))

rewrite_query : optional boolean

Whether to rewrite the natural language query for vector search.

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%200%20%3E%20(param)%20rewrite_query%20%3E%20(schema))

##### Returns Expand Collapse

data : array of object { attributes , content , file_id , 2 more }

The list of search result items.

attributes : map [ string or number or boolean ]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%200)

number

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%201)

boolean

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes%20%3E%20(items)%20%3E%20(variant)%202)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20attributes)

content : array of object { text , type }

Content chunks from the file.

text : string

The text content returned from search.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : "text"

The type of content.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20content)

file_id : string

The ID of the vector store file.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20file_id)

filename : string

The name of the vector store file.

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20filename)

score : number

The similarity score for the result.

minimum 0

maximum 1

[](#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)%20%3E%20(property)%20score)

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

Indicates if there are more results to fetch.

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

next_page : string

The token for the next page, if any.

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(network%20schema)%20%3E%20(property)%20next_page)

object : "vector_store.search_results.page"

The object type, which is always `vector_store.search_results.page`

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(network%20schema)%20%3E%20(property)%20object)

search_query : array of string

[](#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(network%20schema)%20%3E%20(property)%20search_query)

### Search vector store

```
curl -X POST \
https://api.openai.com/v1/vector_stores/vs_abc123/search \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{"query": "What is the return policy?", "filters": {...}}'
```

```
{
"object": "vector_store.search_results.page",
"search_query": "What is the return policy?",
"data": [
{
"file_id": "file_123",
"filename": "document.pdf",
"score": 0.95,
"attributes": {
"author": "John Doe",
"date": "2023-01-01"
},
"content": [
{
"type": "text",
"text": "Relevant chunk"
}
]
},
{
"file_id": "file_456",
"filename": "notes.txt",
"score": 0.89,
"attributes": {
"author": "Jane Smith",
"date": "2023-01-02"
},
"content": [
{
"type": "text",
"text": "Sample text content from the vector store."
}
]
}
],
"has_more": false,
"next_page": null
}
```

##### Returns Examples

```
{
"object": "vector_store.search_results.page",
"search_query": "What is the return policy?",
"data": [
{
"file_id": "file_123",
"filename": "document.pdf",
"score": 0.95,
"attributes": {
"author": "John Doe",
"date": "2023-01-01"
},
"content": [
{
"type": "text",
"text": "Relevant chunk"
}
]
},
{
"file_id": "file_456",
"filename": "notes.txt",
"score": 0.89,
"attributes": {
"author": "Jane Smith",
"date": "2023-01-02"
},
"content": [
{
"type": "text",
"text": "Sample text content from the vector store."
}
]
}
],
"has_more": false,
"next_page": null
}
```

---
Source: https://developers.openai.com/api/reference/resources/vector_stores/methods/search
