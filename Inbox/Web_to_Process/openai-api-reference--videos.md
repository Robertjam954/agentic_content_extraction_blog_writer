---
source_url: https://developers.openai.com/api/reference/resources/videos
title: "Videos"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Videos

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Videos

##### [Create video](/api/reference/resources/videos/methods/create)

POST /videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/resources/videos/methods/edit)

POST /videos/edits

##### [Create an extension of a completed video.](/api/reference/resources/videos/methods/extend)

POST /videos/extensions

##### [Create a character from an uploaded video.](/api/reference/resources/videos/methods/create_character)

POST /videos/characters

##### [Fetch a character.](/api/reference/resources/videos/methods/get_character)

GET /videos/characters/{character_id}

##### [List videos](/api/reference/resources/videos/methods/list)

GET /videos

##### [Retrieve video](/api/reference/resources/videos/methods/retrieve)

GET /videos/{video_id}

##### [Delete video](/api/reference/resources/videos/methods/delete)

DELETE /videos/{video_id}

##### [Remix video](/api/reference/resources/videos/methods/remix)

POST /videos/{video_id}/remix

##### [Retrieve video content](/api/reference/resources/videos/methods/download_content)

GET /videos/{video_id}/content

##### Models Expand Collapse

ImageInputReferenceParam object { file_id , image_url }

file_id : optional string

[](#(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema)%20%3E%20(property)%20file_id)

image_url : optional string

A fully qualified URL or base64-encoded data URL.

maxLength 20971520

format uri

[](#(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema)%20%3E%20(property)%20image_url)

[](#(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema))

Video object { id , completed_at , created_at , 10 more }

Structured information describing a generated video job.

id : string

Unique identifier for the video job.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20id)

completed_at : number

Unix timestamp (seconds) for when the job completed, if finished.

format unixtime

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20completed_at)

created_at : number

Unix timestamp (seconds) for when the job was created.

format unixtime

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20created_at)

error : [VideoCreateError](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)) { code , message }

Error payload that explains why generation failed, if applicable.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20error)

expires_at : number

Unix timestamp (seconds) for when the downloadable assets expire, if set.

format unixtime

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20expires_at)

model : [VideoModel](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model)

object : "video"

The object type, which is always `video`.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20object)

progress : number

Approximate completion percentage for the generation task.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20progress)

prompt : string

The prompt that was used to generate the video.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20prompt)

remixed_from_video_id : string

Identifier of the source video if this video is a remix.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20remixed_from_video_id)

seconds : string

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20seconds)

size : [VideoSize](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

The resolution of the generated video.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20size)

status : "queued" or "in_progress" or "completed" or "failed"

Current lifecycle status of the video job.

One of the following:

"queued"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"in_progress"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"completed"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"failed"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20status)

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

VideoCreateError object { code , message }

An error that occurred while generating the response.

code : string

A machine-readable error code that was returned.

[](#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

A human-readable description of the error that was returned.

[](#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)%20%3E%20(property)%20message)

[](#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema))

VideoModel = string or "sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

string

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%200)

"sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

"sora-2"

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%200)

"sora-2-pro"

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%201)

"sora-2-2025-10-06"

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%202)

"sora-2-pro-2025-10-06"

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%203)

"sora-2-2025-12-08"

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%204)

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

VideoSeconds = "4" or "8" or "12"

One of the following:

"4"

[](#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)%20%3E%20(member)%200)

"8"

[](#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)%20%3E%20(member)%201)

"12"

[](#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)%20%3E%20(member)%202)

[](#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))

VideoSize = "720x1280" or "1280x720" or "1024x1792" or "1792x1024"

One of the following:

"720x1280"

[](#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%200)

"1280x720"

[](#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%201)

"1024x1792"

[](#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%202)

"1792x1024"

[](#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%203)

[](#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

VideoCreateCharacterResponse object { id , created_at , name }

id : string

Identifier for the character creation cameo.

[](#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the character was created.

format unixtime

[](#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Display name for the character.

[](#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema))

VideoGetCharacterResponse object { id , created_at , name }

id : string

Identifier for the character creation cameo.

[](#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the character was created.

format unixtime

[](#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

name : string

Display name for the character.

[](#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema))

VideoDeleteResponse object { id , deleted , object }

Confirmation payload returned after deleting a video.

id : string

Identifier of the deleted video.

[](#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Indicates that the video resource was deleted.

[](#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "video.deleted"

The object type that signals the deletion response.

[](#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/videos
