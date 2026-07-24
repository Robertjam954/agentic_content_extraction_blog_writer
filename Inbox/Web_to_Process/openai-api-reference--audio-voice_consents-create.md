---
source_url: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/create
title: "Create voice consent"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create voice consent

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Voice Consents](/api/reference/resources/audio/subresources/voice_consents)

# Create voice consent

POST /audio/voice_consents

Upload a voice consent recording.

##### Body Parameters Form Data Expand Collapse

language : string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20language%20%3E%20(schema))

name : string

The label to use for this consent recording.

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

recording : file

The consent audio recording file. Maximum size is 10 MiB.

Supported MIME types:
`audio/mpeg`, `audio/wav`, `audio/x-wav`, `audio/ogg`, `audio/aac`, `audio/flac`, `audio/webm`, `audio/mp4`.

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20recording%20%3E%20(schema))

##### Returns Expand Collapse

id : string

The consent recording identifier.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the consent recording was created.

format unixtime

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

language : string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_create_response%20%3E%20(schema)%20%3E%20(property)%20language)

name : string

The label provided when the consent recording was uploaded.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "audio.voice_consent"

The object type, which is always `audio.voice_consent`.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Create voice consent

```
curl https://api.openai.com/v1/audio/voice_consents \
-X POST \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-F "name=John Doe" \
-F "language=en-US" \
-F "recording=@$HOME/consent_recording.wav;type=audio/x-wav"
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
Source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/create
