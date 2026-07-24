---
source_url: https://developers.openai.com/api/reference/resources/audio/subresources/voices/methods/create
title: "Create voice"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create voice

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Voices](/api/reference/resources/audio/subresources/voices)

# Create voice

POST /audio/voices

Creates a custom voice.

##### Body Parameters Form Data Expand Collapse

audio_sample : file

The sample audio recording file. Maximum size is 10 MiB.

Supported MIME types:
`audio/mpeg`, `audio/wav`, `audio/x-wav`, `audio/ogg`, `audio/aac`, `audio/flac`, `audio/webm`, `audio/mp4`.

[](#(resource)%20audio.voices%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20audio_sample%20%3E%20(schema))

consent : string

The consent recording ID (for example, `cons_1234`).

[](#(resource)%20audio.voices%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20consent%20%3E%20(schema))

name : string

The name of the new voice.

[](#(resource)%20audio.voices%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

##### Returns Expand Collapse

id : string

The voice identifier, which can be referenced in API endpoints.

[](#(resource)%20audio.voices%20%3E%20(model)%20voice_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the voice was created.

format unixtime

[](#(resource)%20audio.voices%20%3E%20(model)%20voice_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

The name of the voice.

[](#(resource)%20audio.voices%20%3E%20(model)%20voice_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "audio.voice"

The object type, which is always `audio.voice`.

[](#(resource)%20audio.voices%20%3E%20(model)%20voice_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Create voice

```
curl https://api.openai.com/v1/audio/voices \
-X POST \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-F "name=My new voice" \
-F "consent=cons_1234" \
-F "audio_sample=@$HOME/audio_sample.wav;type=audio/x-wav"
```

```
{
"id": "id",
"created_at": 0,
"name": "name",
"object": "audio.voice"
}
```

##### Returns Examples

```
{
"id": "id",
"created_at": 0,
"name": "name",
"object": "audio.voice"
}
```

---
Source: https://developers.openai.com/api/reference/resources/audio/subresources/voices/methods/create
