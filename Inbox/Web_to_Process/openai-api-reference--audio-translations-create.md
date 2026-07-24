---
source_url: https://developers.openai.com/api/reference/resources/audio/subresources/translations/methods/create
title: "Create translation"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create translation

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Translations](/api/reference/resources/audio/subresources/translations)

# Create translation

POST /audio/translations

Translates audio into English.

##### Body Parameters Form Data Expand Collapse

file : file

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20file%20%3E%20(schema))

model : string or [AudioModel](/api/reference/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

One of the following:

string

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%200)

AudioModel = "whisper-1" or "gpt-4o-transcribe" or "gpt-4o-mini-transcribe" or 2 more

One of the following:

"whisper-1"

[](#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)%20%3E%20(member)%200)

"gpt-4o-transcribe"

[](#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)%20%3E%20(member)%201)

"gpt-4o-mini-transcribe"

[](#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)%20%3E%20(member)%202)

"gpt-4o-mini-transcribe-2025-12-15"

[](#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)%20%3E%20(member)%203)

"gpt-4o-transcribe-diarize"

[](#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)%20%3E%20(member)%204)

[](#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema))

prompt : optional string

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text#prompting) should be in English.

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20prompt%20%3E%20(schema))

response_format : optional "json" or "text" or "srt" or 2 more

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

One of the following:

"json"

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%200)

"text"

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%201)

"srt"

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%202)

"verbose_json"

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%203)

"vtt"

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%204)

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema))

temperature : optional number

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

[](#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20temperature%20%3E%20(schema))

##### Returns Expand Collapse

Translation object { text }

text : string

[](#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema))

TranslationVerbose object { duration , language , text , segments }

duration : number

The duration of the input audio.

format double

[](#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)%20%3E%20(property)%20duration)

language : string

The language of the output translation (always `english`).

[](#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)%20%3E%20(property)%20language)

text : string

The translated text.

[](#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)%20%3E%20(property)%20text)

segments : optional array of [TranscriptionSegment](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id , avg_logprob , compression_ratio , 7 more }

Segments of the translated text and their corresponding details.

id : number

Unique identifier of the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20id)

avg_logprob : number

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

format float

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20avg_logprob)

compression_ratio : number

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

format float

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20compression_ratio)

end : number

End time of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20end)

no_speech_prob : number

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

format float

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20no_speech_prob)

seek : number

Seek offset of the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20seek)

start : number

Start time of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20start)

temperature : number

Temperature parameter used for generating the segment.

format float

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20temperature)

text : string

Text content of the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20text)

tokens : array of number

Array of token IDs for the text content.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)%20%3E%20(property)%20tokens)

[](#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)%20%3E%20(property)%20segments)

[](#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema))

### Create translation

```
curl https://api.openai.com/v1/audio/translations \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: multipart/form-data" \
-F file="@/path/to/file/german.m4a" \
-F model="whisper-1"
```

```
{
"text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
}
```

##### Returns Examples

```
{
"text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
}
```

---
Source: https://developers.openai.com/api/reference/resources/audio/subresources/translations/methods/create
