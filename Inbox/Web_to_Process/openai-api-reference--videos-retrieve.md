---
source_url: https://developers.openai.com/api/reference/resources/videos/methods/retrieve
title: "Retrieve video"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Retrieve video

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Videos](/api/reference/resources/videos)

# Retrieve video

GET /videos/{video_id}

Fetch the latest metadata for a generated video.

##### P ath Parameters Expand Collapse

video_id : string

[](#(resource)%20videos%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20video_id%20%3E%20(schema))

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

### Retrieve video

```
curl https://api.openai.com/v1/videos/$VIDEO_ID \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"id": "id",
"completed_at": 0,
"created_at": 0,
"error": {
"code": "code",
"message": "message"
},
"expires_at": 0,
"model": "sora-2",
"object": "video",
"progress": 0,
"prompt": "prompt",
"remixed_from_video_id": "remixed_from_video_id",
"seconds": "seconds",
"size": "720x1280",
"status": "queued"
}
```

##### Returns Examples

```
{
"id": "id",
"completed_at": 0,
"created_at": 0,
"error": {
"code": "code",
"message": "message"
},
"expires_at": 0,
"model": "sora-2",
"object": "video",
"progress": 0,
"prompt": "prompt",
"remixed_from_video_id": "remixed_from_video_id",
"seconds": "seconds",
"size": "720x1280",
"status": "queued"
}
```

---
Source: https://developers.openai.com/api/reference/resources/videos/methods/retrieve
