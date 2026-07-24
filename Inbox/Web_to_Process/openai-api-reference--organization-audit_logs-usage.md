---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/usage
title: "Usage"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Usage

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# Usage

##### [Audio speeches](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

GET /organization/usage/audio_speeches

##### [Audio transcriptions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

GET /organization/usage/audio_transcriptions

##### [Code interpreter sessions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

GET /organization/usage/code_interpreter_sessions

##### [Completions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/completions)

GET /organization/usage/completions

##### [Embeddings](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

GET /organization/usage/embeddings

##### [Images](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/images)

GET /organization/usage/images

##### [Moderations](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/moderations)

GET /organization/usage/moderations

##### [Vector stores](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

GET /organization/usage/vector_stores

##### [File search calls](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

GET /organization/usage/file_search_calls

##### [Web search calls](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

GET /organization/usage/web_search_calls

##### [Costs](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/costs)

GET /organization/costs

##### Models Expand Collapse

UsageAudioSpeechesResponse object { data , has_more , next_page , object }

data : array of object { end_time , object , results , start_time }

end_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20end_time)

object : "bucket"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20object)

results : array of object { input_tokens , num_model_requests , object , 19 more } or object { input_tokens , num_model_requests , object , 4 more } or object { input_tokens , num_model_requests , object , 4 more } or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input_tokens , num_model_requests , object , 19 more }

The aggregated completions usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20num_model_requests)

object : "organization.usage.completions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20object)

output_tokens : number

The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20api_key_id)

batch : optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20batch)

input_audio_tokens : optional number

The aggregated number of uncached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_audio_tokens)

input_cache_write_tokens : optional number

The aggregated number of input tokens written to the cache.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cache_write_tokens)

input_cached_audio_tokens : optional number

The aggregated number of cached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_audio_tokens)

input_cached_image_tokens : optional number

The aggregated number of cached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_image_tokens)

input_cached_text_tokens : optional number

The aggregated number of cached text input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_text_tokens)

input_cached_tokens : optional number

The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_tokens)

input_image_tokens : optional number

The aggregated number of uncached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_image_tokens)

input_text_tokens : optional number

The aggregated number of uncached text input tokens used, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_text_tokens)

input_uncached_tokens : optional number

The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_uncached_tokens)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20model)

output_audio_tokens : optional number

The aggregated number of audio output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_audio_tokens)

output_image_tokens : optional number

The aggregated number of image output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_image_tokens)

output_text_tokens : optional number

The aggregated number of text output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_text_tokens)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20project_id)

service_tier : optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20service_tier)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200)

OrganizationUsageEmbeddingsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated embeddings usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20num_model_requests)

object : "organization.usage.embeddings.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201)

OrganizationUsageModerationsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated moderations usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20num_model_requests)

object : "organization.usage.moderations.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202)

OrganizationUsageImagesResult object { images , num_model_requests , object , 6 more }

The aggregated images usage details of the specific time bucket.

images : number

The number of images processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20images)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20num_model_requests)

object : "organization.usage.images.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20project_id)

size : optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20size)

source : optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20source)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203)

OrganizationUsageAudioSpeechesResult object { characters , num_model_requests , object , 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters : number

The number of characters processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20characters)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_speeches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204)

OrganizationUsageAudioTranscriptionsResult object { num_model_requests , object , seconds , 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_transcriptions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20object)

seconds : number

The number of seconds processed.

format int64

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20seconds)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205)

OrganizationUsageVectorStoresResult object { object , usage_bytes , project_id }

The aggregated vector stores usage details of the specific time bucket.

object : "organization.usage.vector_stores.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20object)

usage_bytes : number

The vector stores usage in bytes.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20usage_bytes)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206)

OrganizationUsageCodeInterpreterSessionsResult object { num_sessions , object , project_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num_sessions : number

The number of code interpreter sessions.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20num_sessions)

object : "organization.usage.code_interpreter_sessions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20object)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207)

OrganizationUsageFileSearchesResult object { num_requests , object , api_key_id , 3 more }

The aggregated file search calls usage details of the specific time bucket.

num_requests : number

The count of file search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20num_requests)

object : "organization.usage.file_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20api_key_id)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20user_id)

vector_store_id : optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20vector_store_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208)

OrganizationUsageWebSearchesResult object { num_model_requests , num_requests , object , 5 more }

The aggregated web search calls usage details of the specific time bucket.

num_model_requests : number

The count of model requests.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_model_requests)

num_requests : number

The count of web search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_requests)

object : "organization.usage.web_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20api_key_id)

context_level : optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20context_level)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209)

OrganizationCostsResult object { object , amount , api_key_id , 3 more }

The aggregated costs details of the specific time bucket.

object : "organization.costs.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20object)

amount : optional object { currency , value }

The monetary value in its associated currency.

currency : optional string

Lowercase ISO-4217 currency e.g. “usd”

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20currency)

value : optional number

The numeric value of the cost.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20api_key_id)

line_item : optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20line_item)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20project_id)

quantity : optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20quantity)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results)

start_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20start_time)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20has_more)

next_page : string

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20next_page)

object : "page"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema))

UsageAudioTranscriptionsResponse object { data , has_more , next_page , object }

data : array of object { end_time , object , results , start_time }

end_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20end_time)

object : "bucket"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20object)

results : array of object { input_tokens , num_model_requests , object , 19 more } or object { input_tokens , num_model_requests , object , 4 more } or object { input_tokens , num_model_requests , object , 4 more } or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input_tokens , num_model_requests , object , 19 more }

The aggregated completions usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20num_model_requests)

object : "organization.usage.completions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20object)

output_tokens : number

The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20api_key_id)

batch : optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20batch)

input_audio_tokens : optional number

The aggregated number of uncached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_audio_tokens)

input_cache_write_tokens : optional number

The aggregated number of input tokens written to the cache.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cache_write_tokens)

input_cached_audio_tokens : optional number

The aggregated number of cached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_audio_tokens)

input_cached_image_tokens : optional number

The aggregated number of cached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_image_tokens)

input_cached_text_tokens : optional number

The aggregated number of cached text input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_text_tokens)

input_cached_tokens : optional number

The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_tokens)

input_image_tokens : optional number

The aggregated number of uncached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_image_tokens)

input_text_tokens : optional number

The aggregated number of uncached text input tokens used, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_text_tokens)

input_uncached_tokens : optional number

The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_uncached_tokens)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20model)

output_audio_tokens : optional number

The aggregated number of audio output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_audio_tokens)

output_image_tokens : optional number

The aggregated number of image output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_image_tokens)

output_text_tokens : optional number

The aggregated number of text output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_text_tokens)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20project_id)

service_tier : optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20service_tier)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200)

OrganizationUsageEmbeddingsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated embeddings usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20num_model_requests)

object : "organization.usage.embeddings.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201)

OrganizationUsageModerationsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated moderations usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20num_model_requests)

object : "organization.usage.moderations.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202)

OrganizationUsageImagesResult object { images , num_model_requests , object , 6 more }

The aggregated images usage details of the specific time bucket.

images : number

The number of images processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20images)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20num_model_requests)

object : "organization.usage.images.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20project_id)

size : optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20size)

source : optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20source)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203)

OrganizationUsageAudioSpeechesResult object { characters , num_model_requests , object , 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters : number

The number of characters processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20characters)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_speeches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204)

OrganizationUsageAudioTranscriptionsResult object { num_model_requests , object , seconds , 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_transcriptions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20object)

seconds : number

The number of seconds processed.

format int64

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20seconds)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205)

OrganizationUsageVectorStoresResult object { object , usage_bytes , project_id }

The aggregated vector stores usage details of the specific time bucket.

object : "organization.usage.vector_stores.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20object)

usage_bytes : number

The vector stores usage in bytes.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20usage_bytes)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206)

OrganizationUsageCodeInterpreterSessionsResult object { num_sessions , object , project_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num_sessions : number

The number of code interpreter sessions.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20num_sessions)

object : "organization.usage.code_interpreter_sessions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20object)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207)

OrganizationUsageFileSearchesResult object { num_requests , object , api_key_id , 3 more }

The aggregated file search calls usage details of the specific time bucket.

num_requests : number

The count of file search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20num_requests)

object : "organization.usage.file_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20api_key_id)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20user_id)

vector_store_id : optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20vector_store_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208)

OrganizationUsageWebSearchesResult object { num_model_requests , num_requests , object , 5 more }

The aggregated web search calls usage details of the specific time bucket.

num_model_requests : number

The count of model requests.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_model_requests)

num_requests : number

The count of web search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_requests)

object : "organization.usage.web_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20api_key_id)

context_level : optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20context_level)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209)

OrganizationCostsResult object { object , amount , api_key_id , 3 more }

The aggregated costs details of the specific time bucket.

object : "organization.costs.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20object)

amount : optional object { currency , value }

The monetary value in its associated currency.

currency : optional string

Lowercase ISO-4217 currency e.g. “usd”

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20currency)

value : optional number

The numeric value of the cost.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20api_key_id)

line_item : optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20line_item)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20project_id)

quantity : optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20quantity)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results)

start_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20start_time)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20has_more)

next_page : string

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20next_page)

object : "page"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema))

UsageCodeInterpreterSessionsResponse object { data , has_more , next_page , object }

data : array of object { end_time , object , results , start_time }

end_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20end_time)

object : "bucket"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20object)

results : array of object { input_tokens , num_model_requests , object , 19 more } or object { input_tokens , num_model_requests , object , 4 more } or object { input_tokens , num_model_requests , object , 4 more } or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input_tokens , num_model_requests , object , 19 more }

The aggregated completions usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20num_model_requests)

object : "organization.usage.completions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20object)

output_tokens : number

The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20api_key_id)

batch : optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20batch)

input_audio_tokens : optional number

The aggregated number of uncached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_audio_tokens)

input_cache_write_tokens : optional number

The aggregated number of input tokens written to the cache.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cache_write_tokens)

input_cached_audio_tokens : optional number

The aggregated number of cached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_audio_tokens)

input_cached_image_tokens : optional number

The aggregated number of cached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_image_tokens)

input_cached_text_tokens : optional number

The aggregated number of cached text input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_text_tokens)

input_cached_tokens : optional number

The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_tokens)

input_image_tokens : optional number

The aggregated number of uncached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_image_tokens)

input_text_tokens : optional number

The aggregated number of uncached text input tokens used, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_text_tokens)

input_uncached_tokens : optional number

The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_uncached_tokens)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20model)

output_audio_tokens : optional number

The aggregated number of audio output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_audio_tokens)

output_image_tokens : optional number

The aggregated number of image output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_image_tokens)

output_text_tokens : optional number

The aggregated number of text output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_text_tokens)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20project_id)

service_tier : optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20service_tier)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200)

OrganizationUsageEmbeddingsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated embeddings usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20num_model_requests)

object : "organization.usage.embeddings.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201)

OrganizationUsageModerationsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated moderations usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20num_model_requests)

object : "organization.usage.moderations.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202)

OrganizationUsageImagesResult object { images , num_model_requests , object , 6 more }

The aggregated images usage details of the specific time bucket.

images : number

The number of images processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20images)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20num_model_requests)

object : "organization.usage.images.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20project_id)

size : optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20size)

source : optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20source)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203)

OrganizationUsageAudioSpeechesResult object { characters , num_model_requests , object , 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters : number

The number of characters processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20characters)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_speeches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204)

OrganizationUsageAudioTranscriptionsResult object { num_model_requests , object , seconds , 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_transcriptions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20object)

seconds : number

The number of seconds processed.

format int64

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20seconds)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205)

OrganizationUsageVectorStoresResult object { object , usage_bytes , project_id }

The aggregated vector stores usage details of the specific time bucket.

object : "organization.usage.vector_stores.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20object)

usage_bytes : number

The vector stores usage in bytes.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20usage_bytes)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206)

OrganizationUsageCodeInterpreterSessionsResult object { num_sessions , object , project_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num_sessions : number

The number of code interpreter sessions.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20num_sessions)

object : "organization.usage.code_interpreter_sessions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20object)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207)

OrganizationUsageFileSearchesResult object { num_requests , object , api_key_id , 3 more }

The aggregated file search calls usage details of the specific time bucket.

num_requests : number

The count of file search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20num_requests)

object : "organization.usage.file_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20api_key_id)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20user_id)

vector_store_id : optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20vector_store_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208)

OrganizationUsageWebSearchesResult object { num_model_requests , num_requests , object , 5 more }

The aggregated web search calls usage details of the specific time bucket.

num_model_requests : number

The count of model requests.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_model_requests)

num_requests : number

The count of web search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_requests)

object : "organization.usage.web_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20api_key_id)

context_level : optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20context_level)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209)

OrganizationCostsResult object { object , amount , api_key_id , 3 more }

The aggregated costs details of the specific time bucket.

object : "organization.costs.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20object)

amount : optional object { currency , value }

The monetary value in its associated currency.

currency : optional string

Lowercase ISO-4217 currency e.g. “usd”

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20currency)

value : optional number

The numeric value of the cost.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20api_key_id)

line_item : optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20line_item)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20project_id)

quantity : optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20quantity)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results)

start_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20start_time)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20has_more)

next_page : string

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20next_page)

object : "page"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema))

UsageCompletionsResponse object { data , has_more , next_page , object }

data : array of object { end_time , object , results , start_time }

end_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20end_time)

object : "bucket"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20object)

results : array of object { input_tokens , num_model_requests , object , 19 more } or object { input_tokens , num_model_requests , object , 4 more } or object { input_tokens , num_model_requests , object , 4 more } or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input_tokens , num_model_requests , object , 19 more }

The aggregated completions usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20num_model_requests)

object : "organization.usage.completions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20object)

output_tokens : number

The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20api_key_id)

batch : optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20batch)

input_audio_tokens : optional number

The aggregated number of uncached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_audio_tokens)

input_cache_write_tokens : optional number

The aggregated number of input tokens written to the cache.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cache_write_tokens)

input_cached_audio_tokens : optional number

The aggregated number of cached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_audio_tokens)

input_cached_image_tokens : optional number

The aggregated number of cached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_image_tokens)

input_cached_text_tokens : optional number

The aggregated number of cached text input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_text_tokens)

input_cached_tokens : optional number

The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_tokens)

input_image_tokens : optional number

The aggregated number of uncached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_image_tokens)

input_text_tokens : optional number

The aggregated number of uncached text input tokens used, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_text_tokens)

input_uncached_tokens : optional number

The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_uncached_tokens)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20model)

output_audio_tokens : optional number

The aggregated number of audio output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_audio_tokens)

output_image_tokens : optional number

The aggregated number of image output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_image_tokens)

output_text_tokens : optional number

The aggregated number of text output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_text_tokens)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20project_id)

service_tier : optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20service_tier)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200)

OrganizationUsageEmbeddingsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated embeddings usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20num_model_requests)

object : "organization.usage.embeddings.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201)

OrganizationUsageModerationsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated moderations usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20num_model_requests)

object : "organization.usage.moderations.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202)

OrganizationUsageImagesResult object { images , num_model_requests , object , 6 more }

The aggregated images usage details of the specific time bucket.

images : number

The number of images processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20images)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20num_model_requests)

object : "organization.usage.images.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20project_id)

size : optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20size)

source : optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20source)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203)

OrganizationUsageAudioSpeechesResult object { characters , num_model_requests , object , 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters : number

The number of characters processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20characters)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_speeches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204)

OrganizationUsageAudioTranscriptionsResult object { num_model_requests , object , seconds , 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_transcriptions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20object)

seconds : number

The number of seconds processed.

format int64

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20seconds)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205)

OrganizationUsageVectorStoresResult object { object , usage_bytes , project_id }

The aggregated vector stores usage details of the specific time bucket.

object : "organization.usage.vector_stores.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20object)

usage_bytes : number

The vector stores usage in bytes.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20usage_bytes)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206)

OrganizationUsageCodeInterpreterSessionsResult object { num_sessions , object , project_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num_sessions : number

The number of code interpreter sessions.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20num_sessions)

object : "organization.usage.code_interpreter_sessions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20object)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207)

OrganizationUsageFileSearchesResult object { num_requests , object , api_key_id , 3 more }

The aggregated file search calls usage details of the specific time bucket.

num_requests : number

The count of file search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20num_requests)

object : "organization.usage.file_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20api_key_id)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20user_id)

vector_store_id : optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20vector_store_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208)

OrganizationUsageWebSearchesResult object { num_model_requests , num_requests , object , 5 more }

The aggregated web search calls usage details of the specific time bucket.

num_model_requests : number

The count of model requests.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_model_requests)

num_requests : number

The count of web search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_requests)

object : "organization.usage.web_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20api_key_id)

context_level : optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20context_level)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209)

OrganizationCostsResult object { object , amount , api_key_id , 3 more }

The aggregated costs details of the specific time bucket.

object : "organization.costs.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20object)

amount : optional object { currency , value }

The monetary value in its associated currency.

currency : optional string

Lowercase ISO-4217 currency e.g. “usd”

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20currency)

value : optional number

The numeric value of the cost.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20api_key_id)

line_item : optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20line_item)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20project_id)

quantity : optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20quantity)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results)

start_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20start_time)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20has_more)

next_page : string

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20next_page)

object : "page"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema))

UsageEmbeddingsResponse object { data , has_more , next_page , object }

data : array of object { end_time , object , results , start_time }

end_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20end_time)

object : "bucket"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20object)

results : array of object { input_tokens , num_model_requests , object , 19 more } or object { input_tokens , num_model_requests , object , 4 more } or object { input_tokens , num_model_requests , object , 4 more } or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input_tokens , num_model_requests , object , 19 more }

The aggregated completions usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20num_model_requests)

object : "organization.usage.completions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20object)

output_tokens : number

The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20api_key_id)

batch : optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20batch)

input_audio_tokens : optional number

The aggregated number of uncached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_audio_tokens)

input_cache_write_tokens : optional number

The aggregated number of input tokens written to the cache.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cache_write_tokens)

input_cached_audio_tokens : optional number

The aggregated number of cached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_audio_tokens)

input_cached_image_tokens : optional number

The aggregated number of cached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_image_tokens)

input_cached_text_tokens : optional number

The aggregated number of cached text input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_text_tokens)

input_cached_tokens : optional number

The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_tokens)

input_image_tokens : optional number

The aggregated number of uncached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_image_tokens)

input_text_tokens : optional number

The aggregated number of uncached text input tokens used, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_text_tokens)

input_uncached_tokens : optional number

The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_uncached_tokens)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20model)

output_audio_tokens : optional number

The aggregated number of audio output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_audio_tokens)

output_image_tokens : optional number

The aggregated number of image output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_image_tokens)

output_text_tokens : optional number

The aggregated number of text output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_text_tokens)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20project_id)

service_tier : optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20service_tier)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200)

OrganizationUsageEmbeddingsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated embeddings usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20num_model_requests)

object : "organization.usage.embeddings.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201)

OrganizationUsageModerationsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated moderations usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20num_model_requests)

object : "organization.usage.moderations.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202)

OrganizationUsageImagesResult object { images , num_model_requests , object , 6 more }

The aggregated images usage details of the specific time bucket.

images : number

The number of images processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20images)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20num_model_requests)

object : "organization.usage.images.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20project_id)

size : optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20size)

source : optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20source)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%203)

OrganizationUsageAudioSpeechesResult object { characters , num_model_requests , object , 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters : number

The number of characters processed.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20characters)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_speeches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%204)

OrganizationUsageAudioTranscriptionsResult object { num_model_requests , object , seconds , 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20num_model_requests)

object : "organization.usage.audio_transcriptions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20object)

seconds : number

The number of seconds processed.

format int64

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20seconds)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%205)

OrganizationUsageVectorStoresResult object { object , usage_bytes , project_id }

The aggregated vector stores usage details of the specific time bucket.

object : "organization.usage.vector_stores.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20object)

usage_bytes : number

The vector stores usage in bytes.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20usage_bytes)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%206)

OrganizationUsageCodeInterpreterSessionsResult object { num_sessions , object , project_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num_sessions : number

The number of code interpreter sessions.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20num_sessions)

object : "organization.usage.code_interpreter_sessions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20object)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20project_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%207)

OrganizationUsageFileSearchesResult object { num_requests , object , api_key_id , 3 more }

The aggregated file search calls usage details of the specific time bucket.

num_requests : number

The count of file search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20num_requests)

object : "organization.usage.file_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20api_key_id)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20user_id)

vector_store_id : optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20vector_store_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%208)

OrganizationUsageWebSearchesResult object { num_model_requests , num_requests , object , 5 more }

The aggregated web search calls usage details of the specific time bucket.

num_model_requests : number

The count of model requests.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_model_requests)

num_requests : number

The count of web search calls.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20num_requests)

object : "organization.usage.web_searches.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20api_key_id)

context_level : optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20context_level)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%209)

OrganizationCostsResult object { object , amount , api_key_id , 3 more }

The aggregated costs details of the specific time bucket.

object : "organization.costs.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20object)

amount : optional object { currency , value }

The monetary value in its associated currency.

currency : optional string

Lowercase ISO-4217 currency e.g. “usd”

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20currency)

value : optional number

The numeric value of the cost.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount%20%3E%20(property)%20value)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20amount)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20api_key_id)

line_item : optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20line_item)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20project_id)

quantity : optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20quantity)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%2010)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results)

start_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20start_time)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20has_more)

next_page : string

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20next_page)

object : "page"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema))

UsageImagesResponse object { data , has_more , next_page , object }

data : array of object { end_time , object , results , start_time }

end_time : number

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20end_time)

object : "bucket"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20object)

results : array of object { input_tokens , num_model_requests , object , 19 more } or object { input_tokens , num_model_requests , object , 4 more } or object { input_tokens , num_model_requests , object , 4 more } or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input_tokens , num_model_requests , object , 19 more }

The aggregated completions usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20num_model_requests)

object : "organization.usage.completions.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20object)

output_tokens : number

The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_tokens)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20api_key_id)

batch : optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20batch)

input_audio_tokens : optional number

The aggregated number of uncached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_audio_tokens)

input_cache_write_tokens : optional number

The aggregated number of input tokens written to the cache.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cache_write_tokens)

input_cached_audio_tokens : optional number

The aggregated number of cached audio input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_audio_tokens)

input_cached_image_tokens : optional number

The aggregated number of cached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_image_tokens)

input_cached_text_tokens : optional number

The aggregated number of cached text input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_text_tokens)

input_cached_tokens : optional number

The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_cached_tokens)

input_image_tokens : optional number

The aggregated number of uncached image input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_image_tokens)

input_text_tokens : optional number

The aggregated number of uncached text input tokens used, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_text_tokens)

input_uncached_tokens : optional number

The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input_uncached_tokens)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20model)

output_audio_tokens : optional number

The aggregated number of audio output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_audio_tokens)

output_image_tokens : optional number

The aggregated number of image output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_image_tokens)

output_text_tokens : optional number

The aggregated number of text output tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output_text_tokens)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20project_id)

service_tier : optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20service_tier)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%200)

OrganizationUsageEmbeddingsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated embeddings usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20num_model_requests)

object : "organization.usage.embeddings.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20object)

api_key_id : optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20api_key_id)

model : optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20model)

project_id : optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20project_id)

user_id : optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20user_id)

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%201)

OrganizationUsageModerationsResult object { input_tokens , num_model_requests , object , 4 more }

The aggregated moderations usage details of the specific time bucket.

input_tokens : number

The aggregated number of input tokens used.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20input_tokens)

num_model_requests : number

The count of requests made to the model.

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20num_model_requests)

object : "organization.usage.moderations.result"

[](#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)%20%3

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/audit_logs/subresources/usage
