---
source_url: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/delete
title: "Delete voice consent"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Delete voice consent

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Voice Consents](/api/reference/resources/audio/subresources/voice_consents)

# Delete voice consent

DELETE /audio/voice_consents/{consent_id}

Deletes a voice consent recording.

##### P ath Parameters Expand Collapse

consent_id : string

[](#(resource)%20audio.voice_consents%20%3E%20(method)%20delete%20%3E%20(params)%20default%20%3E%20(param)%20consent_id%20%3E%20(schema))

##### Returns Expand Collapse

id : string

The consent recording identifier.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "audio.voice_consent"

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

### Delete voice consent

```
curl https://api.openai.com/v1/audio/voice_consents/cons_1234 \
-X DELETE \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "cons_1234",
"deleted": true,
"object": "audio.voice_consent"
}
```

##### Returns Examples

```
{
"id": "cons_1234",
"deleted": true,
"object": "audio.voice_consent"
}
```

---
Source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/delete
