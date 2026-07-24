---
source_url: https://developers.openai.com/api/reference/resources/audio
title: "Audio"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Audio

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Audio

##### Models Expand Collapse

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

AudioResponseFormat = "json" or "text" or "srt" or 3 more

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

One of the following:

"json"

[](#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema)%20%3E%20(member)%200)

"text"

[](#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema)%20%3E%20(member)%201)

"srt"

[](#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema)%20%3E%20(member)%202)

"verbose_json"

[](#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema)%20%3E%20(member)%203)

"vtt"

[](#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema)%20%3E%20(member)%204)

"diarized_json"

[](#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema)%20%3E%20(member)%205)

[](#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema))

#### Audio Transcriptions

Turn audio into text or text into audio.

##### [Create transcription](/api/reference/resources/audio/subresources/transcriptions/methods/create)

POST /audio/transcriptions

##### Models Expand Collapse

Transcription object { text , logprobs , usage }

Represents a transcription response returned by model, based on the provided input.

text : string

The transcribed text.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20text)

logprobs : optional array of object { token , bytes , logprob }

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

token : optional string

The token in the transcription.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : optional array of number

The bytes of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : optional number

The log probability of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs)

usage : optional object { input_tokens , output_tokens , total_tokens , 2 more } or object { seconds , type }

Token usage statistics for the request.

One of the following:

TokenUsage object { input_tokens , output_tokens , total_tokens , 2 more }

Usage statistics for models billed by token usage.

input_tokens : number

Number of input tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

output_tokens : number

Number of output tokens generated.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

total_tokens : number

Total number of tokens used (input + output).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20total_tokens)

type : "tokens"

The type of the usage object. Always `tokens` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20type)

input_token_details : optional object { audio_tokens , text_tokens }

Details about the input tokens billed for this request.

audio_tokens : optional number

Number of audio tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20audio_tokens)

text_tokens : optional number

Number of text tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200)

DurationUsage object { seconds , type }

Usage statistics for models billed by audio input duration.

seconds : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20seconds)

type : "duration"

The type of the usage object. Always `duration` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema))

TranscriptionDiarized object { duration , segments , task , 2 more }

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

duration : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20duration)

segments : array of [TranscriptionDiarizedSegment](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)) { id , end , speaker , 3 more }

Segments of the transcript annotated with timestamps and speaker labels.

id : string

Unique identifier for the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20id)

end : number

End timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20end)

speaker : string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20speaker)

start : number

Start timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20start)

text : string

Transcript text for this segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20text)

type : "transcript.text.segment"

The type of the segment. Always `transcript.text.segment`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20segments)

task : "transcribe"

The type of task that was run. Always `transcribe`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20task)

text : string

The concatenated transcript text for the entire audio input.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20text)

usage : optional object { input_tokens , output_tokens , total_tokens , 2 more } or object { seconds , type }

Token or duration usage statistics for the request.

One of the following:

Tokens object { input_tokens , output_tokens , total_tokens , 2 more }

Usage statistics for models billed by token usage.

input_tokens : number

Number of input tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

output_tokens : number

Number of output tokens generated.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

total_tokens : number

Total number of tokens used (input + output).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20total_tokens)

type : "tokens"

The type of the usage object. Always `tokens` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20type)

input_token_details : optional object { audio_tokens , text_tokens }

Details about the input tokens billed for this request.

audio_tokens : optional number

Number of audio tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20audio_tokens)

text_tokens : optional number

Number of text tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200)

Duration object { seconds , type }

Usage statistics for models billed by audio input duration.

seconds : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20seconds)

type : "duration"

The type of the usage object. Always `duration` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema))

TranscriptionDiarizedSegment object { id , end , speaker , 3 more }

A segment of diarized transcript text with speaker metadata.

id : string

Unique identifier for the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20id)

end : number

End timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20end)

speaker : string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20speaker)

start : number

Start timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20start)

text : string

Transcript text for this segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20text)

type : "transcript.text.segment"

The type of the segment. Always `transcript.text.segment`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema))

TranscriptionInclude = "logprobs"

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_include%20%3E%20(schema))

TranscriptionSegment object { id , avg_logprob , compression_ratio , 7 more }

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

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))

TranscriptionStreamEvent = [TranscriptionTextSegmentEvent](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)) { id , end , speaker , 3 more } or [TranscriptionTextDeltaEvent](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)) { delta , type , logprobs , segment_id } or [TranscriptionTextDoneEvent](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)) { text , type , logprobs , usage }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

One of the following:

TranscriptionTextSegmentEvent object { id , end , speaker , 3 more }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

id : string

Unique identifier for the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20id)

end : number

End timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20end)

speaker : string

Speaker label for this segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20speaker)

start : number

Start timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20start)

text : string

Transcript text for this segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20text)

type : "transcript.text.segment"

The type of the event. Always `transcript.text.segment`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema))

TranscriptionTextDeltaEvent object { delta , type , logprobs , segment_id }

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

delta : string

The text delta that was additionally transcribed.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta)

type : "transcript.text.delta"

The type of the event. Always `transcript.text.delta`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20type)

logprobs : optional array of object { token , bytes , logprob }

The log probabilities of the delta. Only included if you [create a transcription](/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token : optional string

The token that was used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : optional array of number

The bytes that were used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : optional number

The log probability of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs)

segment_id : optional string

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20segment_id)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema))

TranscriptionTextDoneEvent object { text , type , logprobs , usage }

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

text : string

The text that was transcribed.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20text)

type : "transcript.text.done"

The type of the event. Always `transcript.text.done`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20type)

logprobs : optional array of object { token , bytes , logprob }

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token : optional string

The token that was used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : optional array of number

The bytes that were used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : optional number

The log probability of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs)

usage : optional object { input_tokens , output_tokens , total_tokens , 2 more }

Usage statistics for models billed by token usage.

input_tokens : number

Number of input tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_tokens)

output_tokens : number

Number of output tokens generated.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20output_tokens)

total_tokens : number

Total number of tokens used (input + output).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20total_tokens)

type : "tokens"

The type of the usage object. Always `tokens` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20type)

input_token_details : optional object { audio_tokens , text_tokens }

Details about the input tokens billed for this request.

audio_tokens : optional number

Number of audio tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_token_details%20%3E%20(property)%20audio_tokens)

text_tokens : optional number

Number of text tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_token_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_token_details)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema))

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_stream_event%20%3E%20(schema))

TranscriptionTextDeltaEvent object { delta , type , logprobs , segment_id }

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

delta : string

The text delta that was additionally transcribed.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta)

type : "transcript.text.delta"

The type of the event. Always `transcript.text.delta`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20type)

logprobs : optional array of object { token , bytes , logprob }

The log probabilities of the delta. Only included if you [create a transcription](/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token : optional string

The token that was used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : optional array of number

The bytes that were used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : optional number

The log probability of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs)

segment_id : optional string

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)%20%3E%20(property)%20segment_id)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema))

TranscriptionTextDoneEvent object { text , type , logprobs , usage }

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

text : string

The text that was transcribed.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20text)

type : "transcript.text.done"

The type of the event. Always `transcript.text.done`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20type)

logprobs : optional array of object { token , bytes , logprob }

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token : optional string

The token that was used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : optional array of number

The bytes that were used to generate the log probability.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : optional number

The log probability of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20logprobs)

usage : optional object { input_tokens , output_tokens , total_tokens , 2 more }

Usage statistics for models billed by token usage.

input_tokens : number

Number of input tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_tokens)

output_tokens : number

Number of output tokens generated.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20output_tokens)

total_tokens : number

Total number of tokens used (input + output).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20total_tokens)

type : "tokens"

The type of the usage object. Always `tokens` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20type)

input_token_details : optional object { audio_tokens , text_tokens }

Details about the input tokens billed for this request.

audio_tokens : optional number

Number of audio tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_token_details%20%3E%20(property)%20audio_tokens)

text_tokens : optional number

Number of text tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_token_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_token_details)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema))

TranscriptionTextSegmentEvent object { id , end , speaker , 3 more }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

id : string

Unique identifier for the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20id)

end : number

End timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20end)

speaker : string

Speaker label for this segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20speaker)

start : number

Start timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20start)

text : string

Transcript text for this segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20text)

type : "transcript.text.segment"

The type of the event. Always `transcript.text.segment`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema))

TranscriptionVerbose object { duration , language , text , 3 more }

Represents a verbose json transcription response returned by model, based on the provided input.

duration : number

The duration of the input audio.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20duration)

language : string

The language of the input audio.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20language)

text : string

The transcribed text.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20text)

segments : optional array of [TranscriptionSegment](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id , avg_logprob , compression_ratio , 7 more }

Segments of the transcribed text and their corresponding details.

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

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20segments)

usage : optional object { seconds , type }

Usage statistics for models billed by audio input duration.

seconds : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20seconds)

type : "duration"

The type of the usage object. Always `duration` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20usage)

words : optional array of [TranscriptionWord](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)) { end , start , word }

Extracted words and their corresponding timestamps.

end : number

End time of the word in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20end)

start : number

Start time of the word in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20start)

word : string

The text content of the word.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20word)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20words)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema))

TranscriptionWord object { end , start , word }

end : number

End time of the word in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20end)

start : number

Start time of the word in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20start)

word : string

The text content of the word.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20word)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema))

TranscriptionCreateResponse = [Transcription](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)) { text , logprobs , usage } or [TranscriptionDiarized](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)) { duration , segments , task , 2 more } or [TranscriptionVerbose](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)) { duration , language , text , 3 more }

Represents a transcription response returned by model, based on the provided input.

One of the following:

Transcription object { text , logprobs , usage }

Represents a transcription response returned by model, based on the provided input.

text : string

The transcribed text.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20text)

logprobs : optional array of object { token , bytes , logprob }

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

token : optional string

The token in the transcription.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : optional array of number

The bytes of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : optional number

The log probability of the token.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20logprobs)

usage : optional object { input_tokens , output_tokens , total_tokens , 2 more } or object { seconds , type }

Token usage statistics for the request.

One of the following:

TokenUsage object { input_tokens , output_tokens , total_tokens , 2 more }

Usage statistics for models billed by token usage.

input_tokens : number

Number of input tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

output_tokens : number

Number of output tokens generated.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

total_tokens : number

Total number of tokens used (input + output).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20total_tokens)

type : "tokens"

The type of the usage object. Always `tokens` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20type)

input_token_details : optional object { audio_tokens , text_tokens }

Details about the input tokens billed for this request.

audio_tokens : optional number

Number of audio tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20audio_tokens)

text_tokens : optional number

Number of text tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200)

DurationUsage object { seconds , type }

Usage statistics for models billed by audio input duration.

seconds : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20seconds)

type : "duration"

The type of the usage object. Always `duration` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema))

TranscriptionDiarized object { duration , segments , task , 2 more }

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

duration : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20duration)

segments : array of [TranscriptionDiarizedSegment](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)) { id , end , speaker , 3 more }

Segments of the transcript annotated with timestamps and speaker labels.

id : string

Unique identifier for the segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20id)

end : number

End timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20end)

speaker : string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20speaker)

start : number

Start timestamp of the segment in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20start)

text : string

Transcript text for this segment.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20text)

type : "transcript.text.segment"

The type of the segment. Always `transcript.text.segment`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20segments)

task : "transcribe"

The type of task that was run. Always `transcribe`.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20task)

text : string

The concatenated transcript text for the entire audio input.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20text)

usage : optional object { input_tokens , output_tokens , total_tokens , 2 more } or object { seconds , type }

Token or duration usage statistics for the request.

One of the following:

Tokens object { input_tokens , output_tokens , total_tokens , 2 more }

Usage statistics for models billed by token usage.

input_tokens : number

Number of input tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

output_tokens : number

Number of output tokens generated.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

total_tokens : number

Total number of tokens used (input + output).

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20total_tokens)

type : "tokens"

The type of the usage object. Always `tokens` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20type)

input_token_details : optional object { audio_tokens , text_tokens }

Details about the input tokens billed for this request.

audio_tokens : optional number

Number of audio tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20audio_tokens)

text_tokens : optional number

Number of text tokens billed for this request.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200)

Duration object { seconds , type }

Usage statistics for models billed by audio input duration.

seconds : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20seconds)

type : "duration"

The type of the usage object. Always `duration` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema))

TranscriptionVerbose object { duration , language , text , 3 more }

Represents a verbose json transcription response returned by model, based on the provided input.

duration : number

The duration of the input audio.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20duration)

language : string

The language of the input audio.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20language)

text : string

The transcribed text.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20text)

segments : optional array of [TranscriptionSegment](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id , avg_logprob , compression_ratio , 7 more }

Segments of the transcribed text and their corresponding details.

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

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20segments)

usage : optional object { seconds , type }

Usage statistics for models billed by audio input duration.

seconds : number

Duration of the input audio in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20seconds)

type : "duration"

The type of the usage object. Always `duration` for this variant.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20type)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20usage)

words : optional array of [TranscriptionWord](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)) { end , start , word }

Extracted words and their corresponding timestamps.

end : number

End time of the word in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20end)

start : number

Start time of the word in seconds.

format double

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20start)

word : string

The text content of the word.

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)%20%3E%20(property)%20word)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)%20%3E%20(property)%20words)

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema))

[](#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_create_response%20%3E%20(schema))

#### Audio Translations

Turn audio into text or text into audio.

##### [Create translation](/api/reference/resources/audio/subresources/translations/methods/create)

POST /audio/translations

##### Models Expand Collapse

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

TranslationCreateResponse = [Translation](/api/reference/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)) { text } or [TranslationVerbose](/api/reference/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)) { duration , language , text , segments }

One of the following:

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

[](#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

#### Audio Speech

Turn audio into text or text into audio.

##### [Create speech](/api/reference/resources/audio/subresources/speech/methods/create)

POST /audio/speech

##### Models Expand Collapse

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

#### Audio Voices

Turn audio into text or text into audio.

##### [Create voice](/api/reference/resources/audio/subresources/voices/methods/create)

POST /audio/voices

##### Models Expand Collapse

VoiceCreateResponse object { id , created_at , name , object }

A custom voice that can be used for audio output.

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

[](#(resource)%20audio.voices%20%3E%20(model)%20voice_create_response%20%3E%20(schema))

#### Audio Voice Consents

Turn audio into text or text into audio.

##### [List voice consents](/api/reference/resources/audio/subresources/voice_consents/methods/list)

GET /audio/voice_consents

##### [Create voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/create)

POST /audio/voice_consents

##### [Retrieve voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/retrieve)

GET /audio/voice_consents/{consent_id}

##### [Update voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/update)

POST /audio/voice_consents/{consent_id}

##### [Delete voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/delete)

DELETE /audio/voice_consents/{consent_id}

##### Models Expand Collapse

VoiceConsentListResponse object { id , created_at , language , 2 more }

A consent recording used to authorize creation of a custom voice.

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

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_list_response%20%3E%20(schema))

VoiceConsentCreateResponse object { id , created_at , language , 2 more }

A consent recording used to authorize creation of a custom voice.

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

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_create_response%20%3E%20(schema))

VoiceConsentRetrieveResponse object { id , created_at , language , 2 more }

A consent recording used to authorize creation of a custom voice.

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

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_retrieve_response%20%3E%20(schema))

VoiceConsentUpdateResponse object { id , created_at , language , 2 more }

A consent recording used to authorize creation of a custom voice.

id : string

The consent recording identifier.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_update_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the consent recording was created.

format unixtime

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

language : string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_update_response%20%3E%20(schema)%20%3E%20(property)%20language)

name : string

The label provided when the consent recording was uploaded.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_update_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "audio.voice_consent"

The object type, which is always `audio.voice_consent`.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_update_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_update_response%20%3E%20(schema))

VoiceConsentDeleteResponse object { id , deleted , object }

id : string

The consent recording identifier.

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "audio.voice_consent"

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20audio.voice_consents%20%3E%20(model)%20voice_consent_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/audio
