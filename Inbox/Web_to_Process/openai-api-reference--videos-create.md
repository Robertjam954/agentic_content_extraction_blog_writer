---
source_url: https://developers.openai.com/api/reference/resources/videos/methods/create
title: "Create video"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create video

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Videos](/api/reference/resources/videos)

# Create video

POST /videos

Create a new video generation job from a prompt and optional reference assets.

##### Body Parameters JSON Expand Collapse

prompt : string

Text prompt that describes the video to generate.

maxLength 32000

minLength 1

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20prompt%20%3E%20(schema))

input_reference : optional [ImageInputReferenceParam](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema)) { file_id , image_url }

Optional reference object that guides generation. Provide exactly one of `image_url` or `file_id`.

file_id : optional string

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input_reference%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema)%20%3E%20(property)%20file_id)

image_url : optional string

A fully qualified URL or base64-encoded data URL.

maxLength 20971520

format uri

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input_reference%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema)%20%3E%20(property)%20image_url)

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input_reference%20%3E%20(schema))

model : optional [VideoModel](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model to use (allowed values: sora-2, sora-2-pro). Defaults to `sora-2`.

One of the following:

string

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%200)

"sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

"sora-2"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%200)

"sora-2-pro"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%201)

"sora-2-2025-10-06"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%202)

"sora-2-pro-2025-10-06"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%203)

"sora-2-2025-12-08"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%204)

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema))

seconds : optional [VideoSeconds](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))

Clip duration in seconds (allowed values: 4, 8, 12). Defaults to 4 seconds.

One of the following:

"4"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20seconds%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)%20%3E%20(member)%200)

"8"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20seconds%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)%20%3E%20(member)%201)

"12"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20seconds%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)%20%3E%20(member)%202)

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20seconds%20%3E%20(schema))

size : optional [VideoSize](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

Output resolution formatted as width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). Defaults to 720x1280.

One of the following:

"720x1280"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%200)

"1280x720"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%201)

"1024x1792"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%202)

"1792x1024"

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema)%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%203)

[](#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema))

##### Returns Expand Collapse

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

code : string

A machine-readable error code that was returned.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20error%20%2B%20(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

A human-readable description of the error that was returned.

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20error%20%2B%20(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)%20%3E%20(property)%20message)

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20error)

expires_at : number

Unix timestamp (seconds) for when the downloadable assets expire, if set.

format unixtime

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20expires_at)

model : [VideoModel](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

One of the following:

string

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%200)

"sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

"sora-2"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%200)

"sora-2-pro"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%201)

"sora-2-2025-10-06"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%202)

"sora-2-pro-2025-10-06"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%203)

"sora-2-2025-12-08"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%204)

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20model%20%2B%20(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema)%20%3E%20(variant)%201)

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

One of the following:

"720x1280"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20size%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%200)

"1280x720"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20size%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%201)

"1024x1792"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20size%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%202)

"1792x1024"

[](#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)%20%3E%20(property)%20size%20%2B%20(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)%20%3E%20(member)%203)

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

### Create video

```
curl https://api.openai.com/v1/videos \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-F "model=sora-2" \
-F "prompt=A calico cat playing a piano on stage"
```

```
{
"id": "video_123",
"object": "video",
"model": "sora-2",
"status": "queued",
"progress": 0,
"created_at": 1712697600,
"size": "1024x1792",
"seconds": "8",
"quality": "standard"
}
```

##### Returns Examples

```
{
"id": "video_123",
"object": "video",
"model": "sora-2",
"status": "queued",
"progress": 0,
"created_at": 1712697600,
"size": "1024x1792",
"seconds": "8",
"quality": "standard"
}
```

---
Source: https://developers.openai.com/api/reference/resources/videos/methods/create
