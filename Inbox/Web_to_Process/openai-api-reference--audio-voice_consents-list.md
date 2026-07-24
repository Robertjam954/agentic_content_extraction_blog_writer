---
source_url: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/list
title: "List voice consents"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List voice consents

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Voice Consents](/api/reference/resources/audio/subresources/voice_consents)

# List voice consents

GET /audio/voice_consents

Returns a list of voice consent recordings.

##### Q uery Parameters Expand Collapse

after : optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of object { id , created_at , language , 2 more }

id : string

The consent recording identifier.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the consent recording was created.

format unixtime

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

language : string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_list_response%20%3E%20(schema)%20%3E%20(property)%20language)

name : string

The label provided when the consent recording was uploaded.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "audio.voice_consent"

The object type, which is always `audio.voice_consent`.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List voice consents

```
curl https://api.openai.com/v1/audio/voice_consents?limit=20 \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"data": [
{
"id": "cons_1234",
"created_at": 0,
"language": "language",
"name": "name",
"object": "audio.voice_consent"
}
],
"has_more": true,
"object": "list",
"first_id": "first_id",
"last_id": "last_id"
}
```

##### Returns Examples

```
{
"data": [
{
"id": "cons_1234",
"created_at": 0,
"language": "language",
"name": "name",
"object": "audio.voice_consent"
}
],
"has_more": true,
"object": "list",
"first_id": "first_id",
"last_id": "last_id"
}
```

---
Source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/list
