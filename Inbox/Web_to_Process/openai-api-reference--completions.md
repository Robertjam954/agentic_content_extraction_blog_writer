---
source_url: https://developers.openai.com/api/reference/resources/completions
title: "Completions"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Completions

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Completions

Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.

##### [Create completion](/api/reference/resources/completions/methods/create)

POST /completions

##### Models Expand Collapse

Completion object { id , choices , created , 4 more }

Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint).

id : string

A unique identifier for the completion.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20id)

choices : array of [CompletionChoice](/api/reference/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)) { finish_reason , index , logprobs , text }

The list of completion choices the model generated for the input prompt.

finish_reason : "stop" or "length" or "content_filter"

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
or `content_filter` if content was omitted due to a flag from our content filters.

One of the following:

"stop"

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason%20%3E%20(member)%200)

"length"

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason%20%3E%20(member)%201)

"content_filter"

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason%20%3E%20(member)%202)

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason)

index : number

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20index)

logprobs : object { text_offset , token_logprobs , tokens , top_logprobs }

text_offset : optional array of number

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20text_offset)

token_logprobs : optional array of number

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20token_logprobs)

tokens : optional array of string

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20tokens)

top_logprobs : optional array of map [ number ]

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20top_logprobs)

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs)

text : string

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20choices)

created : number

The Unix timestamp (in seconds) of when the completion was created.

format unixtime

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20created)

model : string

The model used for completion.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20model)

object : "text_completion"

The object type, which is always “text_completion”

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20object)

system_fingerprint : optional string

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20system_fingerprint)

usage : optional [CompletionUsage](/api/reference/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)) { completion_tokens , prompt_tokens , total_tokens , 2 more }

Usage statistics for the completion request.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema))

CompletionChoice object { finish_reason , index , logprobs , text }

finish_reason : "stop" or "length" or "content_filter"

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
or `content_filter` if content was omitted due to a flag from our content filters.

One of the following:

"stop"

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason%20%3E%20(member)%200)

"length"

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason%20%3E%20(member)%201)

"content_filter"

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason%20%3E%20(member)%202)

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20finish_reason)

index : number

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20index)

logprobs : object { text_offset , token_logprobs , tokens , top_logprobs }

text_offset : optional array of number

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20text_offset)

token_logprobs : optional array of number

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20token_logprobs)

tokens : optional array of string

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20tokens)

top_logprobs : optional array of map [ number ]

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs%20%3E%20(property)%20top_logprobs)

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20logprobs)

text : string

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema)%20%3E%20(property)%20text)

[](#(resource)%20completions%20%3E%20(model)%20completion_choice%20%3E%20(schema))

CompletionUsage object { completion_tokens , prompt_tokens , total_tokens , 2 more }

Usage statistics for the completion request.

completion_tokens : number

Number of tokens in the generated completion.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens)

prompt_tokens : number

Number of tokens in the prompt.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens)

total_tokens : number

Total number of tokens used in the request (prompt + completion).

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20total_tokens)

completion_tokens_details : optional object { accepted_prediction_tokens , audio_tokens , reasoning_tokens , rejected_prediction_tokens }

Breakdown of tokens used in a completion.

accepted_prediction_tokens : optional number

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20accepted_prediction_tokens)

audio_tokens : optional number

Audio input tokens generated by the model.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20audio_tokens)

reasoning_tokens : optional number

Tokens generated by the model for reasoning.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20reasoning_tokens)

rejected_prediction_tokens : optional number

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20rejected_prediction_tokens)

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details)

prompt_tokens_details : optional object { audio_tokens , cache_write_tokens , cached_tokens }

Breakdown of tokens used in the prompt.

audio_tokens : optional number

Audio input tokens present in the prompt.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20audio_tokens)

cache_write_tokens : optional number

The unadjusted number of prompt tokens written to cache.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20cache_write_tokens)

cached_tokens : optional number

Cached tokens present in the prompt.

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20cached_tokens)

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details)

[](#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/completions
