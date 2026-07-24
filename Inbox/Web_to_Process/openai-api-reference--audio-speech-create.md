---
source_url: https://developers.openai.com/api/reference/resources/audio/subresources/speech/methods/create
title: "Create speech"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create speech

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Speech](/api/reference/resources/audio/subresources/speech)

# Create speech

POST /audio/speech

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

##### Body Parameters JSON Expand Collapse

input : string

The text to generate audio for. The maximum length is 4096 characters.

maxLength 4096

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema))

model : string or [SpeechModel](/api/reference/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema))

One of the available [TTS models](/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

One of the following:

string

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%200)

SpeechModel = "tts-1" or "tts-1-hd" or "gpt-4o-mini-tts" or "gpt-4o-mini-tts-2025-12-15"

One of the following:

"tts-1"

[](#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)%20%3E%20(member)%200)

"tts-1-hd"

[](#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)%20%3E%20(member)%201)

"gpt-4o-mini-tts"

[](#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)%20%3E%20(member)%202)

"gpt-4o-mini-tts-2025-12-15"

[](#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)%20%3E%20(member)%203)

[](#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema))

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema))

voice : string or "alloy" or "ash" or "ballad" or 7 more or object { id }

The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](/docs/guides/text-to-speech#voice-options).

One of the following:

string

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%200)

"alloy" or "ash" or "ballad" or 7 more

One of the following:

"alloy"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%200)

"ash"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%201)

"ballad"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%202)

"coral"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%203)

"echo"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%204)

"sage"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%205)

"shimmer"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%206)

"verse"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%207)

"marin"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%208)

"cedar"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%209)

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%201)

ID object { id }

Custom voice reference.

id : string

The custom voice ID, e.g. `voice_1234`.

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20id)

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema)%20%3E%20(variant)%202)

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20voice%20%3E%20(schema))

instructions : optional string

Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

maxLength 4096

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20instructions%20%3E%20(schema))

response_format : optional "mp3" or "opus" or "aac" or 3 more

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

One of the following:

"mp3"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%200)

"opus"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%201)

"aac"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%202)

"flac"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%203)

"wav"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%204)

"pcm"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%205)

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema))

speed : optional number

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

minimum 0.25

maximum 4

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20speed%20%3E%20(schema))

stream_format : optional "sse" or "audio"

The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

One of the following:

"sse"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20stream_format%20%3E%20(schema)%20%3E%20(member)%200)

"audio"

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20stream_format%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20stream_format%20%3E%20(schema))

Default SSE Stream Format

### Create speech

```
curl https://api.openai.com/v1/audio/speech \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
"model": "gpt-4o-mini-tts",
"input": "The quick brown fox jumped over the lazy dog.",
"voice": "alloy"
}' \
--output speech.mp3
```

### Create speech

```
curl https://api.openai.com/v1/audio/speech \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
"model": "gpt-4o-mini-tts",
"input": "The quick brown fox jumped over the lazy dog.",
"voice": "alloy",
"stream_format": "sse"
}'
```

##### Returns Examples

---
Source: https://developers.openai.com/api/reference/resources/audio/subresources/speech/methods/create
