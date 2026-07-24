---
source_url: https://developers.openai.com/api/reference/resources/realtime
title: "Realtime"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Realtime

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Realtime

##### Models Expand Collapse

AudioTranscription object { delay , language , model , prompt }

delay : optional "minimal" or "low" or "medium" or 2 more

Controls how long the model waits before emitting transcription text.
Higher values can improve transcription accuracy at the cost of latency.
Only supported with `gpt-realtime-whisper` in GA Realtime sessions.

One of the following:

"minimal"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20delay%20%3E%20(member)%200)

"low"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20delay%20%3E%20(member)%201)

"medium"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20delay%20%3E%20(member)%202)

"high"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20delay%20%3E%20(member)%203)

"xhigh"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20delay%20%3E%20(member)%204)

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20delay)

language : optional string

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20language)

model : optional string or "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 3 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

string

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%200)

"whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 3 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

"whisper-1"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%200)

"gpt-4o-mini-transcribe"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%201)

"gpt-4o-mini-transcribe-2025-12-15"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%202)

"gpt-4o-transcribe"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%203)

"gpt-4o-transcribe-diarize"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%204)

"gpt-realtime-whisper"

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%205)

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201)

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20model)

prompt : optional string

An optional text to guide the model’s style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example “expect words related to technology”.
Prompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)%20%3E%20(property)%20prompt)

[](#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema))

ConversationCreatedEvent object { conversation , event_id , type }

Returned when a conversation is created. Emitted right after session creation.

conversation : object { id , object }

The conversation resource.

id : optional string

The unique ID of the conversation.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_created_event%20%3E%20(schema)%20%3E%20(property)%20conversation%20%3E%20(property)%20id)

object : optional string

The object type, must be `realtime.conversation`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_created_event%20%3E%20(schema)%20%3E%20(property)%20conversation%20%3E%20(property)%20object)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_created_event%20%3E%20(schema)%20%3E%20(property)%20conversation)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_created_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

type : "conversation.created"

The event type, must be `conversation.created`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_created_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_created_event%20%3E%20(schema))

ConversationItem = [RealtimeConversationItemSystemMessage](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)) { content , role , type , 3 more } or [RealtimeConversationItemUserMessage](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)) { content , role , type , 3 more } or [RealtimeConversationItemAssistantMessage](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)) { content , role , type , 3 more } or 6 more

A single item within a Realtime conversation.

One of the following:

RealtimeConversationItemSystemMessage object { content , role , type , 3 more }

A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation’s behavior, use instructions, but for smaller updates (e.g. “the user is now asking about a different topic”), use system messages.

content : array of object { text , type }

The content of the message.

text : optional string

The text content.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "input_text"

The content type. Always `input_text` for system messages.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "system"

The role of the message sender. Always `system`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema))

RealtimeConversationItemUserMessage object { content , role , type , 3 more }

A user message item in a Realtime conversation.

content : array of object { audio , detail , image_url , 3 more }

The content of the message.

audio : optional string

Base64-encoded audio bytes (for `input_audio`), these will be parsed as the format specified in the session input audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20audio)

detail : optional "auto" or "low" or "high"

The detail level of the image (for `input_image`). `auto` will default to `high`.

One of the following:

"auto"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail)

image_url : optional string

Base64-encoded image bytes (for `input_image`) as a data URI. For example `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...`. Supported formats are PNG and JPEG.

format uri

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20image_url)

text : optional string

The text content (for `input_text`).

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

transcript : optional string

Transcript of the audio (for `input_audio`). This is not sent to the model, but will be attached to the message item for reference.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20transcript)

type : optional "input_text" or "input_audio" or "input_image"

The content type (`input_text`, `input_audio`, or `input_image`).

One of the following:

"input_text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"input_audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

"input_image"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user"

The role of the message sender. Always `user`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema))

RealtimeConversationItemAssistantMessage object { content , role , type , 3 more }

An assistant message item in a Realtime conversation.

content : array of object { audio , text , transcript , type }

The content of the message.

audio : optional string

Base64-encoded audio bytes, these will be parsed as the format specified in the session output audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20audio)

text : optional string

The text content.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

transcript : optional string

The transcript of the audio content, this will always be present if the output type is `audio`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20transcript)

type : optional "output_text" or "output_audio"

The content type, `output_text` or `output_audio` depending on the session `output_modalities` configuration.

One of the following:

"output_text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"output_audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "assistant"

The role of the message sender. Always `assistant`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema))

RealtimeConversationItemFunctionCall object { arguments , name , type , 4 more }

A function call item in a Realtime conversation.

arguments : string

The arguments of the function call. This is a JSON-encoded string representing the arguments passed to the function, for example `{"arg1": "value1", "arg2": 42}`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the function being called.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20name)

type : "function_call"

The type of the item. Always `function_call`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20id)

call_id : optional string

The ID of the function call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20call_id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema))

RealtimeConversationItemFunctionCallOutput object { call_id , output , type , 3 more }

A function call output item in a Realtime conversation.

call_id : string

The ID of the function call this output is for.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20call_id)

output : string

The output of the function call, this is free text and can contain any information or simply be empty.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20output)

type : "function_call_output"

The type of the item. Always `function_call_output`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema))

RealtimeMcpApprovalResponse object { id , approval_request_id , approve , 2 more }

A Realtime item responding to an MCP approval request.

id : string

The unique ID of the approval response.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20id)

approval_request_id : string

The ID of the approval request being answered.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20approval_request_id)

approve : boolean

Whether the request was approved.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20approve)

type : "mcp_approval_response"

The type of the item. Always `mcp_approval_response`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20type)

reason : optional string

Optional reason for the decision.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20reason)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema))

RealtimeMcpListTools object { server_label , tools , type , id }

A Realtime item listing tools available on an MCP server.

server_label : string

The label of the MCP server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20server_label)

tools : array of object { input_schema , name , annotations , description }

The tools available on the server.

input_schema : unknown

The JSON schema describing the tool’s input.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20input_schema)

name : string

The name of the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20name)

annotations : optional unknown

Additional annotations about the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20annotations)

description : optional string

The description of the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20description)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools)

type : "mcp_list_tools"

The type of the item. Always `mcp_list_tools`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the list.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema))

RealtimeMcpToolCall object { id , arguments , name , 5 more }

A Realtime item representing an invocation of a tool on an MCP server.

id : string

The unique ID of the tool call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

arguments : string

A JSON string of the arguments passed to the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the tool that was run.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20name)

server_label : string

The label of the MCP server running the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20server_label)

type : "mcp_call"

The type of the item. Always `mcp_call`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

approval_request_id : optional string

The ID of an associated approval request, if any.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20approval_request_id)

error : optional [RealtimeMcpProtocolError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)) { code , message , type } or [RealtimeMcpToolExecutionError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)) { message , type } or [RealtimeMcphttpError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)) { code , message , type }

The error from the tool call, if any.

One of the following:

RealtimeMcpProtocolError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "protocol_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema))

RealtimeMcpToolExecutionError object { message , type }

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "tool_execution_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema))

RealtimeMcphttpError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "http_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema))

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20error)

output : optional string

The output from the tool call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20output)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema))

RealtimeMcpApprovalRequest object { id , arguments , name , 2 more }

A Realtime item requesting human approval of a tool invocation.

id : string

The unique ID of the approval request.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20id)

arguments : string

A JSON string of arguments for the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the tool to run.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20name)

server_label : string

The label of the MCP server making the request.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20server_label)

type : "mcp_approval_request"

The type of the item. Always `mcp_approval_request`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema))

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

ConversationItemAdded object { event_id , item , type , previous_item_id }

Sent by the server when an Item is added to the default Conversation. This can happen in several cases:

- When the client sends a `conversation.item.create` event.

- When the input audio buffer is committed. In this case the item will be a user message containing the audio from the buffer.

- When the model is generating a Response. In this case the `conversation.item.added` event will be sent when the model starts generating a specific Item, and thus it will not yet have any content (and `status` will be `in_progress`).

The event will include the full content of the Item (except when model is generating a Response) except for audio data, which can be retrieved separately with a `conversation.item.retrieve` event if necessary.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_added%20%3E%20(schema)%20%3E%20(property)%20event_id)

item : [ConversationItem](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

A single item within a Realtime conversation.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_added%20%3E%20(schema)%20%3E%20(property)%20item)

type : "conversation.item.added"

The event type, must be `conversation.item.added`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_added%20%3E%20(schema)%20%3E%20(property)%20type)

previous_item_id : optional string

The ID of the item that precedes this one, if any. This is used to
maintain ordering when items are inserted.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_added%20%3E%20(schema)%20%3E%20(property)%20previous_item_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_added%20%3E%20(schema))

ConversationItemCreateEvent object { item , type , event_id , previous_item_id }

Add a new Item to the Conversation’s context, including messages, function
calls, and function call responses. This event can be used both to populate a
“history” of the conversation and to add new items mid-stream, but has the
current limitation that it cannot populate assistant audio messages.

If successful, the server will respond with a `conversation.item.created`
event, otherwise an `error` event will be sent.

item : [ConversationItem](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

A single item within a Realtime conversation.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20item)

type : "conversation.item.create"

The event type, must be `conversation.item.create`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

previous_item_id : optional string

The ID of the preceding item after which the new item will be inserted. If not set, the new item will be appended to the end of the conversation.

If set to `root`, the new item will be added to the beginning of the conversation.

If set to an existing ID, it allows an item to be inserted mid-conversation. If the ID cannot be found, an error will be returned and the item will not be added.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20previous_item_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema))

ConversationItemCreatedEvent object { event_id , item , type , previous_item_id }

Returned when a conversation item is created. There are several scenarios that produce this event:

- The server is generating a Response, which if successful will produce
either one or two Items, which will be of type `message`
(role `assistant`) or type `function_call`.

- The input audio buffer has been committed, either by the client or the
server (in `server_vad` mode). The server will take the content of the
input audio buffer and add it to a new user message Item.

- The client has sent a `conversation.item.create` event to add a new Item
to the Conversation.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_created_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item : [ConversationItem](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

A single item within a Realtime conversation.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_created_event%20%3E%20(schema)%20%3E%20(property)%20item)

type : "conversation.item.created"

The event type, must be `conversation.item.created`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_created_event%20%3E%20(schema)%20%3E%20(property)%20type)

previous_item_id : optional string

The ID of the preceding item in the Conversation context, allows the
client to understand the order of the conversation. Can be `null` if the
item has no predecessor.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_created_event%20%3E%20(schema)%20%3E%20(property)%20previous_item_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_created_event%20%3E%20(schema))

ConversationItemDeleteEvent object { item_id , type , event_id }

Send this event when you want to remove any item from the conversation
history. The server will respond with a `conversation.item.deleted` event,
unless the item does not exist in the conversation history, in which case the
server will respond with an error.

item_id : string

The ID of the item to delete.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.delete"

The event type, must be `conversation.item.delete`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema))

ConversationItemDeletedEvent object { event_id , item_id , type }

Returned when an item in the conversation is deleted by the client with a
`conversation.item.delete` event. This event is used to synchronize the
server’s understanding of the conversation history with the client’s view.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_deleted_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the item that was deleted.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_deleted_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.deleted"

The event type, must be `conversation.item.deleted`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_deleted_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_deleted_event%20%3E%20(schema))

ConversationItemDone object { event_id , item , type , previous_item_id }

Returned when a conversation item is finalized.

The event will include the full content of the Item except for audio data, which can be retrieved separately with a `conversation.item.retrieve` event if needed.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_done%20%3E%20(schema)%20%3E%20(property)%20event_id)

item : [ConversationItem](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

A single item within a Realtime conversation.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_done%20%3E%20(schema)%20%3E%20(property)%20item)

type : "conversation.item.done"

The event type, must be `conversation.item.done`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_done%20%3E%20(schema)%20%3E%20(property)%20type)

previous_item_id : optional string

The ID of the item that precedes this one, if any. This is used to
maintain ordering when items are inserted.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_done%20%3E%20(schema)%20%3E%20(property)%20previous_item_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_done%20%3E%20(schema))

ConversationItemInputAudioTranscriptionCompletedEvent object { content_index , event_id , item_id , 4 more }

This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (when VAD is enabled). Transcription runs
asynchronously with Response creation, so this event may come before or after
the Response events.

Realtime API models accept audio natively, and thus input transcription is a
separate process run on a separate ASR (Automatic Speech Recognition) model.
The transcript may diverge somewhat from the model’s interpretation, and
should be treated as a rough guide.

content_index : number

The index of the content part containing the audio.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20content_index)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the item containing the audio that is being transcribed.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

transcript : string

The transcribed text.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20transcript)

type : "conversation.item.input_audio_transcription.completed"

The event type, must be
`conversation.item.input_audio_transcription.completed`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20type)

usage : object { input_tokens , output_tokens , total_tokens , 2 more } or object { seconds , type }

Usage statistics for the transcription, this is billed according to the ASR model’s pricing rather than the realtime model’s pricing.

One of the following:

TokenUsage object { input_tokens , output_tokens , total_tokens , 2 more }

Usage statistics for models billed by token usage.

input_tokens : number

Number of input tokens billed for this request.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

output_tokens : number

Number of output tokens generated.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

total_tokens : number

Total number of tokens used (input + output).

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20total_tokens)

type : "tokens"

The type of the usage object. Always `tokens` for this variant.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20type)

input_token_details : optional object { audio_tokens , text_tokens }

Details about the input tokens billed for this request.

audio_tokens : optional number

Number of audio tokens billed for this request.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20audio_tokens)

text_tokens : optional number

Number of text tokens billed for this request.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200%20%3E%20(property)%20input_token_details)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%200)

DurationUsage object { seconds , type }

Usage statistics for models billed by audio input duration.

seconds : number

Duration of the input audio in seconds.

format double

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20seconds)

type : "duration"

The type of the usage object. Always `duration` for this variant.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(variant)%201)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20usage)

logprobs : optional array of [LogProbProperties](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)) { token , bytes , logprob }

The log probabilities of the transcription.

token : string

The token that was used to generate the log probability.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

The bytes that were used to generate the log probability.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of the token.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20logprob)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema)%20%3E%20(property)%20logprobs)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_completed_event%20%3E%20(schema))

ConversationItemInputAudioTranscriptionDeltaEvent object { event_id , item_id , type , 3 more }

Returned when the text value of an input audio transcription content part is updated with incremental transcription results.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_delta_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the item containing the audio that is being transcribed.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_delta_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.input_audio_transcription.delta"

The event type, must be `conversation.item.input_audio_transcription.delta`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_delta_event%20%3E%20(schema)%20%3E%20(property)%20type)

content_index : optional number

The index of the content part in the item’s content array.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_delta_event%20%3E%20(schema)%20%3E%20(property)%20content_index)

delta : optional string

The text delta.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta)

logprobs : optional array of [LogProbProperties](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)) { token , bytes , logprob }

The log probabilities of the transcription. These can be enabled by configurating the session with `"include": ["item.input_audio_transcription.logprobs"]`. Each entry in the array corresponds a log probability of which token would be selected for this chunk of transcription. This can help to identify if it was possible there were multiple valid options for a given chunk of transcription.

token : string

The token that was used to generate the log probability.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

The bytes that were used to generate the log probability.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of the token.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20logprob)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_delta_event%20%3E%20(schema)%20%3E%20(property)%20logprobs)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_delta_event%20%3E%20(schema))

ConversationItemInputAudioTranscriptionFailedEvent object { content_index , error , event_id , 2 more }

Returned when input audio transcription is configured, and a transcription
request for a user message failed. These events are separate from other
`error` events so that the client can identify the related Item.

content_index : number

The index of the content part containing the audio.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20content_index)

error : object { code , message , param , type }

Details of the transcription error.

code : optional string

Error code, if any.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20code)

message : optional string

A human-readable error message.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20message)

param : optional string

Parameter related to the error, if any.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20param)

type : optional string

The type of error.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20error)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the user message item.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.input_audio_transcription.failed"

The event type, must be
`conversation.item.input_audio_transcription.failed`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_failed_event%20%3E%20(schema))

ConversationItemInputAudioTranscriptionSegment object { id , content_index , end , 6 more }

Returned when an input audio transcription segment is identified for an item.

id : string

The segment identifier.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20id)

content_index : number

The index of the input audio content part within the item.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20content_index)

end : number

End time of the segment in seconds.

format double

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20end)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the item containing the input audio content.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20item_id)

speaker : string

The detected speaker label for this segment.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20speaker)

start : number

Start time of the segment in seconds.

format double

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20start)

text : string

The text for this segment.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20text)

type : "conversation.item.input_audio_transcription.segment"

The event type, must be `conversation.item.input_audio_transcription.segment`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_input_audio_transcription_segment%20%3E%20(schema))

ConversationItemRetrieveEvent object { item_id , type , event_id }

Send this event when you want to retrieve the server’s representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VAD.
The server will respond with a `conversation.item.retrieved` event,
unless the item does not exist in the conversation history, in which case the
server will respond with an error.

item_id : string

The ID of the item to retrieve.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.retrieve"

The event type, must be `conversation.item.retrieve`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema))

ConversationItemTruncateEvent object { audio_end_ms , content_index , item_id , 2 more }

Send this event to truncate a previous assistant message’s audio. The server
will produce audio faster than realtime, so this event is useful when the user
interrupts to truncate audio that has already been sent to the client but not
yet played. This will synchronize the server’s understanding of the audio with
the client’s playback.

Truncating audio will delete the server-side text transcript to ensure there
is not text in the context that hasn’t been heard by the user.

If successful, the server will respond with a `conversation.item.truncated`
event.

audio_end_ms : number

Inclusive duration up to which audio is truncated, in milliseconds. If
the audio_end_ms is greater than the actual audio duration, the server
will respond with an error.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20audio_end_ms)

content_index : number

The index of the content part to truncate. Set this to `0`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20content_index)

item_id : string

The ID of the assistant message item to truncate. Only assistant message
items can be truncated.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.truncate"

The event type, must be `conversation.item.truncate`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema))

ConversationItemTruncatedEvent object { audio_end_ms , content_index , event_id , 2 more }

Returned when an earlier assistant audio message item is truncated by the
client with a `conversation.item.truncate` event. This event is used to
synchronize the server’s understanding of the audio with the client’s playback.

This action will truncate the audio and remove the server-side text transcript
to ensure there is no text in the context that hasn’t been heard by the user.

audio_end_ms : number

The duration up to which the audio was truncated, in milliseconds.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncated_event%20%3E%20(schema)%20%3E%20(property)%20audio_end_ms)

content_index : number

The index of the content part that was truncated.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncated_event%20%3E%20(schema)%20%3E%20(property)%20content_index)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncated_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the assistant message item that was truncated.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncated_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.truncated"

The event type, must be `conversation.item.truncated`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncated_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncated_event%20%3E%20(schema))

ConversationItemWithReference object { id , arguments , call_id , 7 more }

The item to add to the conversation.

id : optional string

For an item of type (`message` | `function_call` | `function_call_output`)
this field allows the client to assign the unique ID of the item. It is
not required because the server will generate one if not provided.

For an item of type `item_reference`, this field is required and is a
reference to any item that has previously existed in the conversation.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20id)

arguments : optional string

The arguments of the function call (for `function_call` items).

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20arguments)

call_id : optional string

The ID of the function call (for `function_call` and
`function_call_output` items). If passed on a `function_call_output`
item, the server will check that a `function_call` item with the same
ID exists in the conversation history.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20call_id)

content : optional array of object { id , audio , text , 2 more }

The content of the message, applicable for `message` items.

- Message items of role `system` support only `input_text` content

- Message items of role `user` support `input_text` and `input_audio`
content

- Message items of role `assistant` support `text` content.

id : optional string

ID of a previous conversation item to reference (for `item_reference`
content types in `response.create` events). These can reference both
client and server created items.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20id)

audio : optional string

Base64-encoded audio bytes, used for `input_audio` content type.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20audio)

text : optional string

The text content, used for `input_text` and `text` content types.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

transcript : optional string

The transcript of the audio, used for `input_audio` content type.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20transcript)

type : optional "input_audio" or "input_text" or "item_reference" or "text"

The content type (`input_text`, `input_audio`, `item_reference`, `text`).

One of the following:

"input_audio"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"input_text"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

"item_reference"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202)

"text"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%203)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20content)

name : optional string

The name of the function being called (for `function_call` items).

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20name)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20object)

output : optional string

The output of the function call (for `function_call_output` items).

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20output)

role : optional "user" or "assistant" or "system"

The role of the message sender (`user`, `assistant`, `system`), only
applicable for `message` items.

One of the following:

"user"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20role)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item (`completed`, `incomplete`, `in_progress`). These have no effect
on the conversation, but are accepted for consistency with the
`conversation.item.created` event.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20status)

type : optional "message" or "function_call" or "function_call_output"

The type of the item (`message`, `function_call`, `function_call_output`, `item_reference`).

One of the following:

"message"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"function_call"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

"function_call_output"

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_with_reference%20%3E%20(schema))

InputAudioBufferAppendEvent object { audio , type , event_id }

Send this event to append audio bytes to the input audio buffer. The audio
buffer is temporary storage you can write to and later commit. A “commit” will create a new
user message item in the conversation history from the buffer content and clear the buffer.
Input audio transcription (if enabled) will be generated when the buffer is committed.

If VAD is enabled the audio buffer is used to detect speech and the server will decide
when to commit. When Server VAD is disabled, you must commit the audio buffer
manually. Input audio noise reduction operates on writes to the audio buffer.

The client may choose how much audio to place in each event up to a maximum
of 15 MiB, for example streaming smaller chunks from the client may allow the
VAD to be more responsive. Unlike most other client events, the server will
not send a confirmation response to this event.

audio : string

Base64-encoded audio bytes. This must be in the format specified by the
`input_audio_format` field in the session configuration.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema)%20%3E%20(property)%20audio)

type : "input_audio_buffer.append"

The event type, must be `input_audio_buffer.append`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema))

InputAudioBufferClearEvent object { type , event_id }

Send this event to clear the audio bytes in the buffer. The server will
respond with an `input_audio_buffer.cleared` event.

type : "input_audio_buffer.clear"

The event type, must be `input_audio_buffer.clear`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_clear_event%20%3E%20(schema))

InputAudioBufferClearedEvent object { event_id , type }

Returned when the input audio buffer is cleared by the client with a
`input_audio_buffer.clear` event.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_cleared_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

type : "input_audio_buffer.cleared"

The event type, must be `input_audio_buffer.cleared`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_cleared_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_cleared_event%20%3E%20(schema))

InputAudioBufferCommitEvent object { type , event_id }

Send this event to commit the user input audio buffer, which will create a new user message item in the conversation. This event will produce an error if the input audio buffer is empty. When in Server VAD mode, the client does not need to send this event, the server will commit the audio buffer automatically.

Committing the input audio buffer will trigger input audio transcription (if enabled in session configuration), but it will not create a response from the model. The server will respond with an `input_audio_buffer.committed` event.

type : "input_audio_buffer.commit"

The event type, must be `input_audio_buffer.commit`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_commit_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_commit_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_commit_event%20%3E%20(schema))

InputAudioBufferCommittedEvent object { event_id , item_id , type , previous_item_id }

Returned when an input audio buffer is committed, either by the client or
automatically in server VAD mode. The `item_id` property is the ID of the user
message item that will be created, thus a `conversation.item.created` event
will also be sent to the client.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_committed_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the user message item that will be created.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_committed_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "input_audio_buffer.committed"

The event type, must be `input_audio_buffer.committed`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_committed_event%20%3E%20(schema)%20%3E%20(property)%20type)

previous_item_id : optional string

The ID of the preceding item after which the new item will be inserted.
Can be `null` if the item has no predecessor.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_committed_event%20%3E%20(schema)%20%3E%20(property)%20previous_item_id)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_committed_event%20%3E%20(schema))

InputAudioBufferDtmfEventReceivedEvent object { event , received_at , type }

**SIP Only:** Returned when an DTMF event is received. A DTMF event is a message that
represents a telephone keypad press (0–9, *, #, A–D). The `event` property
is the keypad that the user press. The `received_at` is the UTC Unix Timestamp
that the server received the event.

event : string

The telephone keypad that was pressed by the user.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_dtmf_event_received_event%20%3E%20(schema)%20%3E%20(property)%20event)

received_at : number

UTC Unix Timestamp when DTMF Event was received by server.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_dtmf_event_received_event%20%3E%20(schema)%20%3E%20(property)%20received_at)

type : "input_audio_buffer.dtmf_event_received"

The event type, must be `input_audio_buffer.dtmf_event_received`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_dtmf_event_received_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_dtmf_event_received_event%20%3E%20(schema))

InputAudioBufferSpeechStartedEvent object { audio_start_ms , event_id , item_id , type }

Sent by the server when in `server_vad` mode to indicate that speech has been
detected in the audio buffer. This can happen any time audio is added to the
buffer (unless speech is already detected). The client may want to use this
event to interrupt audio playback or provide visual feedback to the user.

The client should expect to receive a `input_audio_buffer.speech_stopped` event
when speech stops. The `item_id` property is the ID of the user message item
that will be created when speech stops and will also be included in the
`input_audio_buffer.speech_stopped` event (unless the client manually commits
the audio buffer during VAD activation).

audio_start_ms : number

Milliseconds from the start of all audio written to the buffer during the
session when speech was first detected. This will correspond to the
beginning of audio sent to the model, and thus includes the
`prefix_padding_ms` configured in the Session.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_started_event%20%3E%20(schema)%20%3E%20(property)%20audio_start_ms)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_started_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the user message item that will be created when speech stops.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_started_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "input_audio_buffer.speech_started"

The event type, must be `input_audio_buffer.speech_started`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_started_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_started_event%20%3E%20(schema))

InputAudioBufferSpeechStoppedEvent object { audio_end_ms , event_id , item_id , type }

Returned in `server_vad` mode when the server detects the end of speech in
the audio buffer. The server will also send an `conversation.item.created`
event with the user message item that is created from the audio buffer.

audio_end_ms : number

Milliseconds since the session started when speech stopped. This will
correspond to the end of audio sent to the model, and thus includes the
`min_silence_duration_ms` configured in the Session.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_stopped_event%20%3E%20(schema)%20%3E%20(property)%20audio_end_ms)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_stopped_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the user message item that will be created.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_stopped_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "input_audio_buffer.speech_stopped"

The event type, must be `input_audio_buffer.speech_stopped`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_stopped_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_speech_stopped_event%20%3E%20(schema))

InputAudioBufferTimeoutTriggered object { audio_end_ms , audio_start_ms , event_id , 2 more }

Returned when the Server VAD timeout is triggered for the input audio buffer. This is configured
with `idle_timeout_ms` in the `turn_detection` settings of the session, and it indicates that
there hasn’t been any speech detected for the configured duration.

The `audio_start_ms` and `audio_end_ms` fields indicate the segment of audio after the last
model response up to the triggering time, as an offset from the beginning of audio written
to the input audio buffer. This means it demarcates the segment of audio that was silent and
the difference between the start and end values will roughly match the configured timeout.

The empty audio will be committed to the conversation as an `input_audio` item (there will be a
`input_audio_buffer.committed` event) and a model response will be generated. There may be speech
that didn’t trigger VAD but is still detected by the model, so the model may respond with
something relevant to the conversation or a prompt to continue speaking.

audio_end_ms : number

Millisecond offset of audio written to the input audio buffer at the time the timeout was triggered.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_timeout_triggered%20%3E%20(schema)%20%3E%20(property)%20audio_end_ms)

audio_start_ms : number

Millisecond offset of audio written to the input audio buffer that was after the playback time of the last model response.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_timeout_triggered%20%3E%20(schema)%20%3E%20(property)%20audio_start_ms)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_timeout_triggered%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the item associated with this segment.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_timeout_triggered%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "input_audio_buffer.timeout_triggered"

The event type, must be `input_audio_buffer.timeout_triggered`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_timeout_triggered%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_timeout_triggered%20%3E%20(schema))

LogProbProperties object { token , bytes , logprob }

A log probability object.

token : string

The token that was used to generate the log probability.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

The bytes that were used to generate the log probability.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of the token.

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema)%20%3E%20(property)%20logprob)

[](#(resource)%20realtime%20%3E%20(model)%20log_prob_properties%20%3E%20(schema))

McpListToolsCompleted object { event_id , item_id , type }

Returned when listing MCP tools has completed for an item.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_completed%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the MCP list tools item.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_completed%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "mcp_list_tools.completed"

The event type, must be `mcp_list_tools.completed`.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_completed%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_completed%20%3E%20(schema))

McpListToolsFailed object { event_id , item_id , type }

Returned when listing MCP tools has failed for an item.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_failed%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the MCP list tools item.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_failed%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "mcp_list_tools.failed"

The event type, must be `mcp_list_tools.failed`.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_failed%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_failed%20%3E%20(schema))

McpListToolsInProgress object { event_id , item_id , type }

Returned when listing MCP tools is in progress for an item.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_in_progress%20%3E%20(schema)%20%3E%20(property)%20event_id)

item_id : string

The ID of the MCP list tools item.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_in_progress%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "mcp_list_tools.in_progress"

The event type, must be `mcp_list_tools.in_progress`.

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_in_progress%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20mcp_list_tools_in_progress%20%3E%20(schema))

NoiseReductionType = "near_field" or "far_field"

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

One of the following:

"near_field"

[](#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)%20%3E%20(member)%200)

"far_field"

[](#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

OutputAudioBufferClearEvent object { type , event_id }

**WebRTC/SIP Only:** Emit to cut off the current audio response. This will trigger the server to
stop generating audio and emit a `output_audio_buffer.cleared` event. This
event should be preceded by a `response.cancel` client event to stop the
generation of the current response.
[Learn more](/docs/guides/realtime-conversations#client-and-server-events-for-audio-in-webrtc).

type : "output_audio_buffer.clear"

The event type, must be `output_audio_buffer.clear`.

[](#(resource)%20realtime%20%3E%20(model)%20output_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

The unique ID of the client event used for error handling.

[](#(resource)%20realtime%20%3E%20(model)%20output_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20output_audio_buffer_clear_event%20%3E%20(schema))

RateLimitsUpdatedEvent object { event_id , rate_limits , type }

Emitted at the beginning of a Response to indicate the updated rate limits.
When a Response is created some tokens will be “reserved” for the output
tokens, the rate limits shown here reflect that reservation, which is then
adjusted accordingly once the Response is completed.

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

rate_limits : array of object { limit , name , remaining , reset_seconds }

List of rate limit information.

limit : optional number

The maximum allowed value for the rate limit.

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20rate_limits%20%3E%20(items)%20%3E%20(property)%20limit)

name : optional "requests" or "tokens"

The name of the rate limit (`requests`, `tokens`).

One of the following:

"requests"

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20rate_limits%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%200)

"tokens"

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20rate_limits%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%201)

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20rate_limits%20%3E%20(items)%20%3E%20(property)%20name)

remaining : optional number

The remaining value before the limit is reached.

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20rate_limits%20%3E%20(items)%20%3E%20(property)%20remaining)

reset_seconds : optional number

Seconds until the rate limit resets.

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20rate_limits%20%3E%20(items)%20%3E%20(property)%20reset_seconds)

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20rate_limits)

type : "rate_limits.updated"

The event type, must be `rate_limits.updated`.

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20rate_limits_updated_event%20%3E%20(schema))

RealtimeAudioConfig object { input , output }

Configuration for input and output audio.

input : optional [RealtimeAudioConfigInput](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema)) { format , noise_reduction , transcription , turn_detection }

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config%20%3E%20(schema)%20%3E%20(property)%20input)

output : optional [RealtimeAudioConfigOutput](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)) { format , speed , voice }

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config%20%3E%20(schema)%20%3E%20(property)%20output)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config%20%3E%20(schema))

RealtimeAudioConfigInput object { format , noise_reduction , transcription , turn_detection }

format : optional [RealtimeAudioFormats](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the input audio.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema)%20%3E%20(property)%20format)

noise_reduction : optional object { type }

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

type : optional [NoiseReductionType](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema)%20%3E%20(property)%20noise_reduction%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema)%20%3E%20(property)%20noise_reduction)

transcription : optional [AudioTranscription](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)) { delay , language , model , prompt }

Configuration for input audio transcription, defaults to off and can be set to `null` to turn off once on. Input audio transcription is not native to the model, since the model consumes audio directly. Transcription runs asynchronously through [the /audio/transcriptions endpoint](/docs/api-reference/audio/createTranscription) and should be treated as guidance of input audio content rather than precisely what the model heard. The client can optionally set the language and prompt for transcription, these offer additional guidance to the transcription service.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema)%20%3E%20(property)%20transcription)

turn_detection : optional [RealtimeAudioInputTurnDetection](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema))

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema)%20%3E%20(property)%20turn_detection)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema))

RealtimeAudioConfigOutput object { format , speed , voice }

format : optional [RealtimeAudioFormats](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the output audio.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20format)

speed : optional number

The speed of the model’s spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it’s
also possible to prompt the model to speak faster or slower.

maximum 1.5

minimum 0.25

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20speed)

voice : optional string or "alloy" or "ash" or "ballad" or 7 more or object { id }

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`,
`marin`, and `cedar`. You may also provide a custom voice object with
an `id`, for example `{ "id": "voice_1234" }`. Voice cannot be changed
during the session once the model has responded with audio at least once.
We recommend `marin` and `cedar` for best quality.

One of the following:

string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%200)

"alloy" or "ash" or "ballad" or 7 more

One of the following:

"alloy"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%200)

"ash"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%201)

"ballad"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%202)

"coral"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%203)

"echo"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%204)

"sage"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%205)

"shimmer"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%206)

"verse"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%207)

"marin"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%208)

"cedar"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%209)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201)

ID object { id }

Custom voice reference.

id : string

The custom voice ID, e.g. `voice_1234`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%202%20%3E%20(property)%20id)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)%20%3E%20(property)%20voice)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema))

RealtimeAudioFormats = object { rate , type } or object { type } or object { type }

The PCM audio format. Only a 24kHz sample rate is supported.

One of the following:

PCMAudioFormat object { rate , type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate : optional 24000

The sample rate of the audio. Always `24000`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rate)

type : optional "audio/pcm"

The audio format. Always `audio/pcm`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema)%20%3E%20(variant)%200)

PCMUAudioFormat object { type }

The G.711 μ-law format.

type : optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema)%20%3E%20(variant)%201)

PCMAAudioFormat object { type }

The G.711 A-law format.

type : optional "audio/pcma"

The audio format. Always `audio/pcma`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema)%20%3E%20(variant)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

RealtimeAudioInputTurnDetection = object { type , create_response , idle_timeout_ms , 4 more } or object { type , create_response , eagerness , interrupt_response }

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

One of the following:

ServerVad object { type , create_response , idle_timeout_ms , 4 more }

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

type : "server_vad"

Type of turn detection, `server_vad` to turn on simple Server VAD.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type)

create_response : optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20create_response)

idle_timeout_ms : optional number

Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response’s audio has finished playing,
i.e. it’s set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

minimum 5000

maximum 30000

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20idle_timeout_ms)

interrupt_response : optional boolean

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20interrupt_response)

prefix_padding_ms : optional number

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20prefix_padding_ms)

silence_duration_ms : optional number

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20silence_duration_ms)

threshold : optional number

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20threshold)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%200)

SemanticVad object { type , create_response , eagerness , interrupt_response }

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

type : "semantic_vad"

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type)

create_response : optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20create_response)

eagerness : optional "low" or "medium" or "high" or "auto"

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

One of the following:

"low"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20eagerness%20%3E%20(member)%200)

"medium"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20eagerness%20%3E%20(member)%201)

"high"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20eagerness%20%3E%20(member)%202)

"auto"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20eagerness%20%3E%20(member)%203)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20eagerness)

interrupt_response : optional boolean

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20interrupt_response)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema))

RealtimeClientEvent = [ConversationItemCreateEvent](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)) { item , type , event_id , previous_item_id } or [ConversationItemDeleteEvent](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema)) { item_id , type , event_id } or [ConversationItemRetrieveEvent](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema)) { item_id , type , event_id } or 8 more

A realtime client event.

One of the following:

ConversationItemCreateEvent object { item , type , event_id , previous_item_id }

Add a new Item to the Conversation’s context, including messages, function
calls, and function call responses. This event can be used both to populate a
“history” of the conversation and to add new items mid-stream, but has the
current limitation that it cannot populate assistant audio messages.

If successful, the server will respond with a `conversation.item.created`
event, otherwise an `error` event will be sent.

item : [ConversationItem](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

A single item within a Realtime conversation.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20item)

type : "conversation.item.create"

The event type, must be `conversation.item.create`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

previous_item_id : optional string

The ID of the preceding item after which the new item will be inserted. If not set, the new item will be appended to the end of the conversation.

If set to `root`, the new item will be added to the beginning of the conversation.

If set to an existing ID, it allows an item to be inserted mid-conversation. If the ID cannot be found, an error will be returned and the item will not be added.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema)%20%3E%20(property)%20previous_item_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_create_event%20%3E%20(schema))

ConversationItemDeleteEvent object { item_id , type , event_id }

Send this event when you want to remove any item from the conversation
history. The server will respond with a `conversation.item.deleted` event,
unless the item does not exist in the conversation history, in which case the
server will respond with an error.

item_id : string

The ID of the item to delete.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.delete"

The event type, must be `conversation.item.delete`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_delete_event%20%3E%20(schema))

ConversationItemRetrieveEvent object { item_id , type , event_id }

Send this event when you want to retrieve the server’s representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VAD.
The server will respond with a `conversation.item.retrieved` event,
unless the item does not exist in the conversation history, in which case the
server will respond with an error.

item_id : string

The ID of the item to retrieve.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.retrieve"

The event type, must be `conversation.item.retrieve`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_retrieve_event%20%3E%20(schema))

ConversationItemTruncateEvent object { audio_end_ms , content_index , item_id , 2 more }

Send this event to truncate a previous assistant message’s audio. The server
will produce audio faster than realtime, so this event is useful when the user
interrupts to truncate audio that has already been sent to the client but not
yet played. This will synchronize the server’s understanding of the audio with
the client’s playback.

Truncating audio will delete the server-side text transcript to ensure there
is not text in the context that hasn’t been heard by the user.

If successful, the server will respond with a `conversation.item.truncated`
event.

audio_end_ms : number

Inclusive duration up to which audio is truncated, in milliseconds. If
the audio_end_ms is greater than the actual audio duration, the server
will respond with an error.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20audio_end_ms)

content_index : number

The index of the content part to truncate. Set this to `0`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20content_index)

item_id : string

The ID of the assistant message item to truncate. Only assistant message
items can be truncated.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20item_id)

type : "conversation.item.truncate"

The event type, must be `conversation.item.truncate`.

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20conversation_item_truncate_event%20%3E%20(schema))

InputAudioBufferAppendEvent object { audio , type , event_id }

Send this event to append audio bytes to the input audio buffer. The audio
buffer is temporary storage you can write to and later commit. A “commit” will create a new
user message item in the conversation history from the buffer content and clear the buffer.
Input audio transcription (if enabled) will be generated when the buffer is committed.

If VAD is enabled the audio buffer is used to detect speech and the server will decide
when to commit. When Server VAD is disabled, you must commit the audio buffer
manually. Input audio noise reduction operates on writes to the audio buffer.

The client may choose how much audio to place in each event up to a maximum
of 15 MiB, for example streaming smaller chunks from the client may allow the
VAD to be more responsive. Unlike most other client events, the server will
not send a confirmation response to this event.

audio : string

Base64-encoded audio bytes. This must be in the format specified by the
`input_audio_format` field in the session configuration.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema)%20%3E%20(property)%20audio)

type : "input_audio_buffer.append"

The event type, must be `input_audio_buffer.append`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_append_event%20%3E%20(schema))

InputAudioBufferClearEvent object { type , event_id }

Send this event to clear the audio bytes in the buffer. The server will
respond with an `input_audio_buffer.cleared` event.

type : "input_audio_buffer.clear"

The event type, must be `input_audio_buffer.clear`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_clear_event%20%3E%20(schema))

OutputAudioBufferClearEvent object { type , event_id }

**WebRTC/SIP Only:** Emit to cut off the current audio response. This will trigger the server to
stop generating audio and emit a `output_audio_buffer.cleared` event. This
event should be preceded by a `response.cancel` client event to stop the
generation of the current response.
[Learn more](/docs/guides/realtime-conversations#client-and-server-events-for-audio-in-webrtc).

type : "output_audio_buffer.clear"

The event type, must be `output_audio_buffer.clear`.

[](#(resource)%20realtime%20%3E%20(model)%20output_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

The unique ID of the client event used for error handling.

[](#(resource)%20realtime%20%3E%20(model)%20output_audio_buffer_clear_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20output_audio_buffer_clear_event%20%3E%20(schema))

InputAudioBufferCommitEvent object { type , event_id }

Send this event to commit the user input audio buffer, which will create a new user message item in the conversation. This event will produce an error if the input audio buffer is empty. When in Server VAD mode, the client does not need to send this event, the server will commit the audio buffer automatically.

Committing the input audio buffer will trigger input audio transcription (if enabled in session configuration), but it will not create a response from the model. The server will respond with an `input_audio_buffer.committed` event.

type : "input_audio_buffer.commit"

The event type, must be `input_audio_buffer.commit`.

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_commit_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_commit_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20input_audio_buffer_commit_event%20%3E%20(schema))

ResponseCancelEvent object { type , event_id , response_id }

Send this event to cancel an in-progress response. The server will respond
with a `response.done` event with a status of `response.status=cancelled`. If
there is no response to cancel, the server will respond with an error. It’s safe
to call `response.cancel` even if no response is in progress, an error will be
returned the session will remain unaffected.

type : "response.cancel"

The event type, must be `response.cancel`.

[](#(resource)%20realtime%20%3E%20(model)%20response_cancel_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20response_cancel_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

response_id : optional string

A specific response ID to cancel - if not provided, will cancel an
in-progress response in the default conversation.

[](#(resource)%20realtime%20%3E%20(model)%20response_cancel_event%20%3E%20(schema)%20%3E%20(property)%20response_id)

[](#(resource)%20realtime%20%3E%20(model)%20response_cancel_event%20%3E%20(schema))

ResponseCreateEvent object { type , event_id , response }

This event instructs the server to create a Response, which means triggering
model inference. When in Server VAD mode, the server will create Responses
automatically.

A Response will include at least one Item, and may have two, in which case
the second will be a function call. These Items will be appended to the
conversation history by default.

The server will respond with a `response.created` event, events for Items
and content created, and finally a `response.done` event to indicate the
Response is complete.

The `response.create` event includes inference configuration like
`instructions` and `tools`. If these are set, they will override the Session’s
configuration for this Response only.

Responses can be created out-of-band of the default Conversation, meaning that they can
have arbitrary input, and it’s possible to disable writing the output to the Conversation.
Only one Response can write to the default Conversation at a time, but otherwise multiple
Responses can be created in parallel. The `metadata` field is a good way to disambiguate
multiple simultaneous Responses.

Clients can set `conversation` to `none` to create a Response that does not write to the default
Conversation. Arbitrary input can be provided with the `input` field, which is an array accepting
raw Items and references to existing Items.

type : "response.create"

The event type, must be `response.create`.

[](#(resource)%20realtime%20%3E%20(model)%20response_create_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20response_create_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

response : optional [RealtimeResponseCreateParams](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_params%20%3E%20(schema)) { audio , conversation , input , 9 more }

Create a new Realtime response with these parameters

[](#(resource)%20realtime%20%3E%20(model)%20response_create_event%20%3E%20(schema)%20%3E%20(property)%20response)

[](#(resource)%20realtime%20%3E%20(model)%20response_create_event%20%3E%20(schema))

SessionUpdateEvent object { session , type , event_id }

Send this event to update the session’s configuration.
The client may send this event at any time to update any field
except for `voice` and `model`. `voice` can be updated only if there have been no other audio outputs yet.

When the server receives a `session.update`, it will respond
with a `session.updated` event showing the full, effective configuration.
Only the fields that are present in the `session.update` are updated. To clear a field like
`instructions`, pass an empty string. To clear a field like `tools`, pass an empty array.
To clear a field like `turn_detection`, pass `null`.

session : [RealtimeSessionCreateRequest](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)) { type , audio , include , 11 more } or [RealtimeTranscriptionSessionCreateRequest](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_create_request%20%3E%20(schema)) { type , audio , include }

Update the Realtime session. Choose either a realtime
session or a transcription session.

One of the following:

RealtimeSessionCreateRequest object { type , audio , include , 11 more }

Realtime session object configuration.

type : "realtime"

The type of session to create. Always `realtime` for the Realtime API.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20type)

audio : optional [RealtimeAudioConfig](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config%20%3E%20(schema)) { input , output }

Configuration for input and output audio.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20audio)

include : optional array of "item.input_audio_transcription.logprobs"

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20include)

instructions : optional string

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20instructions)

max_output_tokens : optional number or "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

One of the following:

number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20max_output_tokens%20%3E%20(variant)%200)

"inf"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20max_output_tokens%20%3E%20(variant)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20max_output_tokens)

model : optional string or "gpt-realtime" or "gpt-realtime-1.5" or "gpt-realtime-2" or 16 more

The Realtime model used for this session.

One of the following:

string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%200)

"gpt-realtime" or "gpt-realtime-1.5" or "gpt-realtime-2" or 16 more

The Realtime model used for this session.

One of the following:

"gpt-realtime"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%200)

"gpt-realtime-1.5"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%201)

"gpt-realtime-2"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%202)

"gpt-realtime-2.1"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%203)

"gpt-realtime-2.1-mini"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%204)

"gpt-realtime-2025-08-28"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%205)

"gpt-4o-realtime-preview"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%206)

"gpt-4o-realtime-preview-2024-10-01"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%207)

"gpt-4o-realtime-preview-2024-12-17"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%208)

"gpt-4o-realtime-preview-2025-06-03"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%209)

"gpt-4o-mini-realtime-preview"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2010)

"gpt-4o-mini-realtime-preview-2024-12-17"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2011)

"gpt-realtime-mini"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2012)

"gpt-realtime-mini-2025-10-06"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2013)

"gpt-realtime-mini-2025-12-15"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2014)

"gpt-audio-1.5"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2015)

"gpt-audio-mini"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2016)

"gpt-audio-mini-2025-10-06"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2017)

"gpt-audio-mini-2025-12-15"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201%20%3E%20(member)%2018)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model%20%3E%20(variant)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20model)

output_modalities : optional array of "text" or "audio"

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

One of the following:

"text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20output_modalities%20%3E%20(items)%20%3E%20(member)%200)

"audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20output_modalities%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20output_modalities)

parallel_tool_calls : optional boolean

Whether the model may call multiple tools in parallel. Only supported by
reasoning Realtime models such as `gpt-realtime-2`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20parallel_tool_calls)

prompt : optional [ResponsePrompt](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema)) { id , variables , version }

Reference to a prompt template and its variables.
[Learn more](/docs/guides/text?api-mode=responses#reusable-prompts).

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20prompt)

reasoning : optional [RealtimeReasoning](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema)) { effort }

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20reasoning)

tool_choice : optional [RealtimeToolChoiceConfig](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_tool_choice_config%20%3E%20(schema))

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20tool_choice)

tools : optional [RealtimeToolsConfig](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_tools_config%20%3E%20(schema)) { , McpTool }

Tools available to the model.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20tools)

tracing : optional [RealtimeTracingConfig](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_tracing_config%20%3E%20(schema))

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20tracing)

truncation : optional [RealtimeTruncation](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation%20%3E%20(schema))

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)%20%3E%20(property)%20truncation)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema))

RealtimeTranscriptionSessionCreateRequest object { type , audio , include }

Realtime transcription session object configuration.

type : "transcription"

The type of session to create. Always `transcription` for transcription sessions.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_create_request%20%3E%20(schema)%20%3E%20(property)%20type)

audio : optional [RealtimeTranscriptionSessionAudio](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_audio%20%3E%20(schema)) { input }

Configuration for input and output audio.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_create_request%20%3E%20(schema)%20%3E%20(property)%20audio)

include : optional array of "item.input_audio_transcription.logprobs"

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_create_request%20%3E%20(schema)%20%3E%20(property)%20include)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_create_request%20%3E%20(schema))

[](#(resource)%20realtime%20%3E%20(model)%20session_update_event%20%3E%20(schema)%20%3E%20(property)%20session)

type : "session.update"

The event type, must be `session.update`.

[](#(resource)%20realtime%20%3E%20(model)%20session_update_event%20%3E%20(schema)%20%3E%20(property)%20type)

event_id : optional string

Optional client-generated ID used to identify this event. This is an arbitrary string that a client may assign. It will be passed back if there is an error with the event, but the corresponding `session.updated` event will not include it.

maxLength 512

[](#(resource)%20realtime%20%3E%20(model)%20session_update_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

[](#(resource)%20realtime%20%3E%20(model)%20session_update_event%20%3E%20(schema))

[](#(resource)%20realtime%20%3E%20(model)%20realtime_client_event%20%3E%20(schema))

RealtimeConversationItemAssistantMessage object { content , role , type , 3 more }

An assistant message item in a Realtime conversation.

content : array of object { audio , text , transcript , type }

The content of the message.

audio : optional string

Base64-encoded audio bytes, these will be parsed as the format specified in the session output audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20audio)

text : optional string

The text content.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

transcript : optional string

The transcript of the audio content, this will always be present if the output type is `audio`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20transcript)

type : optional "output_text" or "output_audio"

The content type, `output_text` or `output_audio` depending on the session `output_modalities` configuration.

One of the following:

"output_text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"output_audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "assistant"

The role of the message sender. Always `assistant`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema))

RealtimeConversationItemFunctionCall object { arguments , name , type , 4 more }

A function call item in a Realtime conversation.

arguments : string

The arguments of the function call. This is a JSON-encoded string representing the arguments passed to the function, for example `{"arg1": "value1", "arg2": 42}`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the function being called.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20name)

type : "function_call"

The type of the item. Always `function_call`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20id)

call_id : optional string

The ID of the function call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20call_id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema))

RealtimeConversationItemFunctionCallOutput object { call_id , output , type , 3 more }

A function call output item in a Realtime conversation.

call_id : string

The ID of the function call this output is for.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20call_id)

output : string

The output of the function call, this is free text and can contain any information or simply be empty.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20output)

type : "function_call_output"

The type of the item. Always `function_call_output`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema))

RealtimeConversationItemSystemMessage object { content , role , type , 3 more }

A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation’s behavior, use instructions, but for smaller updates (e.g. “the user is now asking about a different topic”), use system messages.

content : array of object { text , type }

The content of the message.

text : optional string

The text content.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "input_text"

The content type. Always `input_text` for system messages.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "system"

The role of the message sender. Always `system`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema))

RealtimeConversationItemUserMessage object { content , role , type , 3 more }

A user message item in a Realtime conversation.

content : array of object { audio , detail , image_url , 3 more }

The content of the message.

audio : optional string

Base64-encoded audio bytes (for `input_audio`), these will be parsed as the format specified in the session input audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20audio)

detail : optional "auto" or "low" or "high"

The detail level of the image (for `input_image`). `auto` will default to `high`.

One of the following:

"auto"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail)

image_url : optional string

Base64-encoded image bytes (for `input_image`) as a data URI. For example `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...`. Supported formats are PNG and JPEG.

format uri

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20image_url)

text : optional string

The text content (for `input_text`).

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

transcript : optional string

Transcript of the audio (for `input_audio`). This is not sent to the model, but will be attached to the message item for reference.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20transcript)

type : optional "input_text" or "input_audio" or "input_image"

The content type (`input_text`, `input_audio`, or `input_image`).

One of the following:

"input_text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"input_audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

"input_image"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user"

The role of the message sender. Always `user`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema))

RealtimeError object { message , type , code , 2 more }

Details of the error.

message : string

A human-readable error message.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : string

The type of error (e.g., “invalid_request_error”, “server_error”).

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema)%20%3E%20(property)%20type)

code : optional string

Error code, if any.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema)%20%3E%20(property)%20code)

event_id : optional string

The event_id of the client event that caused the error, if applicable.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema)%20%3E%20(property)%20event_id)

param : optional string

Parameter related to the error, if any.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema)%20%3E%20(property)%20param)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema))

RealtimeErrorEvent object { error , event_id , type }

Returned when an error occurs, which could be a client problem or a server
problem. Most errors are recoverable and the session will stay open, we
recommend to implementors to monitor and log error messages by default.

error : [RealtimeError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema)) { message , type , code , 2 more }

Details of the error.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error_event%20%3E%20(schema)%20%3E%20(property)%20error)

event_id : string

The unique ID of the server event.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error_event%20%3E%20(schema)%20%3E%20(property)%20event_id)

type : "error"

The event type, must be `error`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_error_event%20%3E%20(schema))

RealtimeFunctionTool object { description , name , parameters , type }

description : optional string

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

[](#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)%20%3E%20(property)%20description)

name : optional string

The name of the function.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)%20%3E%20(property)%20name)

parameters : optional unknown

Parameters of the function in JSON Schema.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)%20%3E%20(property)%20parameters)

type : optional "function"

The type of the tool, i.e. `function`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema))

RealtimeMcpApprovalRequest object { id , arguments , name , 2 more }

A Realtime item requesting human approval of a tool invocation.

id : string

The unique ID of the approval request.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20id)

arguments : string

A JSON string of arguments for the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the tool to run.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20name)

server_label : string

The label of the MCP server making the request.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20server_label)

type : "mcp_approval_request"

The type of the item. Always `mcp_approval_request`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema))

RealtimeMcpApprovalResponse object { id , approval_request_id , approve , 2 more }

A Realtime item responding to an MCP approval request.

id : string

The unique ID of the approval response.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20id)

approval_request_id : string

The ID of the approval request being answered.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20approval_request_id)

approve : boolean

Whether the request was approved.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20approve)

type : "mcp_approval_response"

The type of the item. Always `mcp_approval_response`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20type)

reason : optional string

Optional reason for the decision.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20reason)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema))

RealtimeMcpListTools object { server_label , tools , type , id }

A Realtime item listing tools available on an MCP server.

server_label : string

The label of the MCP server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20server_label)

tools : array of object { input_schema , name , annotations , description }

The tools available on the server.

input_schema : unknown

The JSON schema describing the tool’s input.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20input_schema)

name : string

The name of the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20name)

annotations : optional unknown

Additional annotations about the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20annotations)

description : optional string

The description of the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20description)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools)

type : "mcp_list_tools"

The type of the item. Always `mcp_list_tools`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the list.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema))

RealtimeMcpProtocolError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "protocol_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema))

RealtimeMcpToolCall object { id , arguments , name , 5 more }

A Realtime item representing an invocation of a tool on an MCP server.

id : string

The unique ID of the tool call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

arguments : string

A JSON string of the arguments passed to the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the tool that was run.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20name)

server_label : string

The label of the MCP server running the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20server_label)

type : "mcp_call"

The type of the item. Always `mcp_call`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

approval_request_id : optional string

The ID of an associated approval request, if any.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20approval_request_id)

error : optional [RealtimeMcpProtocolError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)) { code , message , type } or [RealtimeMcpToolExecutionError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)) { message , type } or [RealtimeMcphttpError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)) { code , message , type }

The error from the tool call, if any.

One of the following:

RealtimeMcpProtocolError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "protocol_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema))

RealtimeMcpToolExecutionError object { message , type }

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "tool_execution_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema))

RealtimeMcphttpError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "http_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema))

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20error)

output : optional string

The output from the tool call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20output)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema))

RealtimeMcpToolExecutionError object { message , type }

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "tool_execution_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema))

RealtimeMcphttpError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "http_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema))

RealtimeReasoning object { effort }

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

effort : optional [RealtimeReasoningEffort](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning-capable Realtime models such as
`gpt-realtime-2`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema)%20%3E%20(property)%20effort)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema))

RealtimeReasoningEffort = "minimal" or "low" or "medium" or 2 more

Constrains effort on reasoning for reasoning-capable Realtime models such as
`gpt-realtime-2`.

One of the following:

"minimal"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"low"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"medium"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"high"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"xhigh"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema))

RealtimeResponse object { id , audio , conversation_id , 8 more }

The response resource.

id : optional string

The unique ID of the response, will look like `resp_1234`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20id)

audio : optional object { output }

Configuration for audio output.

output : optional object { format , voice }

format : optional [RealtimeAudioFormats](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the output audio.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20format)

voice : optional string or "alloy" or "ash" or "ballad" or 7 more

The voice the model uses to respond. Voice cannot be changed during the
session once the model has responded with audio at least once. Current
voice options are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`,
`shimmer`, `verse`, `marin`, and `cedar`. We recommend `marin` and `cedar` for
best quality.

One of the following:

string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%200)

"alloy" or "ash" or "ballad" or 7 more

The voice the model uses to respond. Voice cannot be changed during the
session once the model has responded with audio at least once. Current
voice options are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`,
`shimmer`, `verse`, `marin`, and `cedar`. We recommend `marin` and `cedar` for
best quality.

One of the following:

"alloy"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%200)

"ash"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%201)

"ballad"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%202)

"coral"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%203)

"echo"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%204)

"sage"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%205)

"shimmer"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%206)

"verse"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%207)

"marin"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%208)

"cedar"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%209)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output%20%3E%20(property)%20voice)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20output)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20audio)

conversation_id : optional string

Which conversation the response is added to, determined by the `conversation`
field in the `response.create` event. If `auto`, the response will be added to
the default conversation and the value of `conversation_id` will be an id like
`conv_1234`. If `none`, the response will not be added to any conversation and
the value of `conversation_id` will be `null`. If responses are being triggered
automatically by VAD the response will be added to the default conversation

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20conversation_id)

max_output_tokens : optional number or "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls, that was used in this response.

One of the following:

number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20max_output_tokens%20%3E%20(variant)%200)

"inf"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20max_output_tokens%20%3E%20(variant)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20max_output_tokens)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

object : optional "realtime.response"

The object type, must be `realtime.response`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20object)

output : optional array of [ConversationItem](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

The list of output items generated by the response.

One of the following:

RealtimeConversationItemSystemMessage object { content , role , type , 3 more }

A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation’s behavior, use instructions, but for smaller updates (e.g. “the user is now asking about a different topic”), use system messages.

content : array of object { text , type }

The content of the message.

text : optional string

The text content.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "input_text"

The content type. Always `input_text` for system messages.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "system"

The role of the message sender. Always `system`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_system_message%20%3E%20(schema))

RealtimeConversationItemUserMessage object { content , role , type , 3 more }

A user message item in a Realtime conversation.

content : array of object { audio , detail , image_url , 3 more }

The content of the message.

audio : optional string

Base64-encoded audio bytes (for `input_audio`), these will be parsed as the format specified in the session input audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20audio)

detail : optional "auto" or "low" or "high"

The detail level of the image (for `input_image`). `auto` will default to `high`.

One of the following:

"auto"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20detail)

image_url : optional string

Base64-encoded image bytes (for `input_image`) as a data URI. For example `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...`. Supported formats are PNG and JPEG.

format uri

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20image_url)

text : optional string

The text content (for `input_text`).

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

transcript : optional string

Transcript of the audio (for `input_audio`). This is not sent to the model, but will be attached to the message item for reference.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20transcript)

type : optional "input_text" or "input_audio" or "input_image"

The content type (`input_text`, `input_audio`, or `input_image`).

One of the following:

"input_text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"input_audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

"input_image"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user"

The role of the message sender. Always `user`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_user_message%20%3E%20(schema))

RealtimeConversationItemAssistantMessage object { content , role , type , 3 more }

An assistant message item in a Realtime conversation.

content : array of object { audio , text , transcript , type }

The content of the message.

audio : optional string

Base64-encoded audio bytes, these will be parsed as the format specified in the session output audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20audio)

text : optional string

The text content.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

transcript : optional string

The transcript of the audio content, this will always be present if the output type is `audio`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20transcript)

type : optional "output_text" or "output_audio"

The content type, `output_text` or `output_audio` depending on the session `output_modalities` configuration.

One of the following:

"output_text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200)

"output_audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "assistant"

The role of the message sender. Always `assistant`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20role)

type : "message"

The type of the item. Always `message`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_assistant_message%20%3E%20(schema))

RealtimeConversationItemFunctionCall object { arguments , name , type , 4 more }

A function call item in a Realtime conversation.

arguments : string

The arguments of the function call. This is a JSON-encoded string representing the arguments passed to the function, for example `{"arg1": "value1", "arg2": 42}`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the function being called.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20name)

type : "function_call"

The type of the item. Always `function_call`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20id)

call_id : optional string

The ID of the function call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20call_id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call%20%3E%20(schema))

RealtimeConversationItemFunctionCallOutput object { call_id , output , type , 3 more }

A function call output item in a Realtime conversation.

call_id : string

The ID of the function call this output is for.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20call_id)

output : string

The output of the function call, this is free text and can contain any information or simply be empty.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20output)

type : "function_call_output"

The type of the item. Always `function_call_output`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the item. This may be provided by the client or generated by the server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20id)

object : optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20object)

status : optional "completed" or "incomplete" or "in_progress"

The status of the item. Has no effect on the conversation.

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_conversation_item_function_call_output%20%3E%20(schema))

RealtimeMcpApprovalResponse object { id , approval_request_id , approve , 2 more }

A Realtime item responding to an MCP approval request.

id : string

The unique ID of the approval response.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20id)

approval_request_id : string

The ID of the approval request being answered.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20approval_request_id)

approve : boolean

Whether the request was approved.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20approve)

type : "mcp_approval_response"

The type of the item. Always `mcp_approval_response`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20type)

reason : optional string

Optional reason for the decision.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema)%20%3E%20(property)%20reason)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_response%20%3E%20(schema))

RealtimeMcpListTools object { server_label , tools , type , id }

A Realtime item listing tools available on an MCP server.

server_label : string

The label of the MCP server.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20server_label)

tools : array of object { input_schema , name , annotations , description }

The tools available on the server.

input_schema : unknown

The JSON schema describing the tool’s input.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20input_schema)

name : string

The name of the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20name)

annotations : optional unknown

Additional annotations about the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20annotations)

description : optional string

The description of the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools%20%3E%20(items)%20%3E%20(property)%20description)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20tools)

type : "mcp_list_tools"

The type of the item. Always `mcp_list_tools`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The unique ID of the list.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_list_tools%20%3E%20(schema))

RealtimeMcpToolCall object { id , arguments , name , 5 more }

A Realtime item representing an invocation of a tool on an MCP server.

id : string

The unique ID of the tool call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

arguments : string

A JSON string of the arguments passed to the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the tool that was run.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20name)

server_label : string

The label of the MCP server running the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20server_label)

type : "mcp_call"

The type of the item. Always `mcp_call`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

approval_request_id : optional string

The ID of an associated approval request, if any.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20approval_request_id)

error : optional [RealtimeMcpProtocolError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)) { code , message , type } or [RealtimeMcpToolExecutionError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)) { message , type } or [RealtimeMcphttpError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)) { code , message , type }

The error from the tool call, if any.

One of the following:

RealtimeMcpProtocolError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "protocol_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema))

RealtimeMcpToolExecutionError object { message , type }

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "tool_execution_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema))

RealtimeMcphttpError object { code , message , type }

code : number

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20message)

type : "http_error"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema))

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20error)

output : optional string

The output from the tool call.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema)%20%3E%20(property)%20output)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_call%20%3E%20(schema))

RealtimeMcpApprovalRequest object { id , arguments , name , 2 more }

A Realtime item requesting human approval of a tool invocation.

id : string

The unique ID of the approval request.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20id)

arguments : string

A JSON string of arguments for the tool.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20arguments)

name : string

The name of the tool to run.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20name)

server_label : string

The label of the MCP server making the request.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20server_label)

type : "mcp_approval_request"

The type of the item. Always `mcp_approval_request`.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_approval_request%20%3E%20(schema))

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20output)

output_modalities : optional array of "text" or "audio"

The set of modalities the model used to respond, currently the only possible values are
`[\"audio\"]`, `[\"text\"]`. Audio output always include a text transcript. Setting the
output to mode `text` will disable audio output from the model.

One of the following:

"text"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20output_modalities%20%3E%20(items)%20%3E%20(member)%200)

"audio"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20output_modalities%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20output_modalities)

status : optional "completed" or "cancelled" or "failed" or 2 more

The final status of the response (`completed`, `cancelled`, `failed`, or
`incomplete`, `in_progress`).

One of the following:

"completed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"cancelled"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"failed"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"incomplete"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

"in_progress"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20status)

status_details : optional [RealtimeResponseStatus](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_response_status%20%3E%20(schema)) { error , reason , type }

Additional details about the status.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20status_details)

usage : optional [RealtimeResponseUsage](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_response_usage%20%3E%20(schema)) { input_token_details , input_tokens , output_token_details , 2 more }

Usage statistics for the Response, this will correspond to billing. A
Realtime API session will maintain a conversation context and append new
Items to the Conversation, thus output from previous turns (text and
audio tokens) will become the input for later turns.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response%20%3E%20(schema))

RealtimeResponseCreateAudioOutput object { output }

Configuration for audio input and output.

output : optional object { format , voice }

format : optional [RealtimeAudioFormats](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the output audio.

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_audio_output%20%3E%20(schema)%20%3E%20(property)%20output%20%3E%20(property)%20format)

voice : optional string or "alloy" or "ash" or "ballad" or 7 more or object { id }

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`,
`marin`, and `cedar`. You may also provide a custom voice object with
an `id`, for example `{ "id": "voice_1234" }`. Voice cannot be changed
during the session once the model has responded with audio at least once.
We recommend `marin` and `cedar` for best quality.

One of the following:

string

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_audio_output%20%3E%20(schema)%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%200)

"alloy" or "ash" or "ballad" or 7 more

One of the following:

"alloy"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_audio_output%20%3E%20(schema)%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%200)

"ash"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_audio_output%20%3E%20(schema)%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%201)

"ballad"

[](#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_audio_output%20%3E%20(schema)%20%3E%20(property)%20output%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%202)

"coral"

[](#(resource)%20realtime%20%3E%20(model)%20realtime

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/realtime
