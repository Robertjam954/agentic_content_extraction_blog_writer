---
source_url: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/retrieve
title: "Retrieve voice consent"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve voice consent

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Voice Consents](/api/reference/resources/audio/subresources/voice_consents)

# Retrieve voice consent

GET /audio/voice_consents/{consent_id}

Retrieves a voice consent recording.

##### P ath Parameters Expand Collapse

consent_id : string

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20consent_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

The consent recording identifier.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the consent recording was created.

format unixtime

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

language : string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20language)

name : string

The label provided when the consent recording was uploaded.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "audio.voice_consent"

The object type, which is always `audio.voice_consent`.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Retrieve voice consent

```
curl https://api.openai.com/v1/audio/voice_consents/cons_1234 \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "cons_1234",
"created_at": 0,
"language": "language",
"name": "name",
"object": "audio.voice_consent"
}
```

##### Returns Examples

```
{
"id": "cons_1234",
"created_at": 0,
"language": "language",
"name": "name",
"object": "audio.voice_consent"
}
```

---
Source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/retrieve
