---
source_url: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/rate_limits
title: "Rate Limits"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Rate Limits

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Rate Limits

##### [List project rate limits](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

GET /organization/projects/{project_id}/rate_limits

##### [Modify project rate limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

POST /organization/projects/{project_id}/rate_limits/{rate_limit_id}

##### Models Expand Collapse

ProjectRateLimit object { id , max_requests_per_1_minute , max_tokens_per_1_minute , 6 more }

Represents a project rate limit config.

id : string

The identifier, which can be referenced in API endpoints.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20id)

max_requests_per_1_minute : number

The maximum requests per minute.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_minute)

max_tokens_per_1_minute : number

The maximum tokens per minute.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_tokens_per_1_minute)

model : string

The model this rate limit applies to.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20model)

object : "project.rate_limit"

The object type, which is always `project.rate_limit`

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20object)

batch_1_day_max_input_tokens : optional number

The maximum batch input tokens per day. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20batch_1_day_max_input_tokens)

max_audio_megabytes_per_1_minute : optional number

The maximum audio megabytes per minute. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_audio_megabytes_per_1_minute)

max_images_per_1_minute : optional number

The maximum images per minute. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_images_per_1_minute)

max_requests_per_1_day : optional number

The maximum requests per day. Only present for relevant models.

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)%20%3E%20(property)%20max_requests_per_1_day)

[](#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/organization/subresources/projects/subresources/rate_limits
