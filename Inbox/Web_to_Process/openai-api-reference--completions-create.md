---
source_url: https://developers.openai.com/api/reference/resources/completions/methods/create
title: "Create completion"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create completion

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Completions](/api/reference/resources/completions)

# Create completion

POST /completions

Creates a completion for the provided prompt and parameters.

Returns a completion object, or a sequence of completion objects if the request is streamed.

##### Body Parameters JSON Expand Collapse

model : string or "gpt-3.5-turbo-instruct" or "davinci-002" or "babbage-002"

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models) for descriptions of them.

One of the following:

string

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%200)

"gpt-3.5-turbo-instruct" or "davinci-002" or "babbage-002"

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models) for descriptions of them.

One of the following:

"gpt-3.5-turbo-instruct"

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%200)

"davinci-002"

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%201)

"babbage-002"

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(member)%202)

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema))

prompt : string or array of string or array of number or array of array of number

The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.

Note that <|endoftext|> is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document.

One of the following:

string

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt%20%3E%20(schema)%20%3E%20(variant)%200)

array of string

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt%20%3E%20(schema)%20%3E%20(variant)%201)

array of number

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt%20%3E%20(schema)%20%3E%20(variant)%202)

array of array of number

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt%20%3E%20(schema)%20%3E%20(variant)%203)

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt%20%3E%20(schema))

best_of : optional number

Generates `best_of` completions server-side and returns the “best” (the one with the highest log probability per token). Results cannot be streamed.

When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return – `best_of` must be greater than `n`.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

minimum 0

maximum 20

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20best_of%20%3E%20(schema))

echo : optional boolean

Echo back the prompt in addition to the completion

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20echo%20%3E%20(schema))

frequency_penalty : optional number

Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim.

[See more information about frequency and presence penalties.](/docs/guides/text-generation)

minimum -2

maximum 2

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20frequency_penalty%20%3E%20(schema))

logit_bias : optional map [ number ]

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated.

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20logit_bias%20%3E%20(schema))

logprobs : optional number

Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.

The maximum value for `logprobs` is 5.

minimum 0

maximum 5

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20logprobs%20%3E%20(schema))

max_tokens : optional number

The maximum number of [tokens](/tokenizer) that can be generated in the completion.

The token count of your prompt plus `max_tokens` cannot exceed the model’s context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

minimum 0

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20max_tokens%20%3E%20(schema))

n : optional number

How many completions to generate for each prompt.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

minimum 1

maximum 128

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20n%20%3E%20(schema))

presence_penalty : optional number

Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics.

[See more information about frequency and presence penalties.](/docs/guides/text-generation)

minimum -2

maximum 2

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20presence_penalty%20%3E%20(schema))

seed : optional number

If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.

Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

format int64

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20seed%20%3E%20(schema))

stop : optional string or array of string

Not supported with latest reasoning models `o3` and `o4-mini`.

Up to 4 sequences where the API will stop generating further tokens. The
returned text will not contain the stop sequence.

One of the following:

string

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stop%20%3E%20(schema)%20%3E%20(variant)%200)

array of string

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stop%20%3E%20(schema)%20%3E%20(variant)%201)

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stop%20%3E%20(schema))

stream : optional boolean

Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream%20%3E%20(schema))

stream_options : optional [ChatCompletionStreamOptions](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema)) { include_obfuscation , include_usage }

Options for streaming response. Only set this when you set `stream: true`.

include_obfuscation : optional boolean

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream_options%20%3E%20(schema)%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema)%20%3E%20(property)%20include_obfuscation)

include_usage : optional boolean

If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream_options%20%3E%20(schema)%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema)%20%3E%20(property)%20include_usage)

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream_options%20%3E%20(schema))

suffix : optional string

The suffix that comes after a completion of inserted text.

This parameter is only supported for `gpt-3.5-turbo-instruct`.

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20suffix%20%3E%20(schema))

temperature : optional number

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

We generally recommend altering this or `top_p` but not both.

minimum 0

maximum 2

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20temperature%20%3E%20(schema))

top_p : optional number

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or `temperature` but not both.

minimum 0

maximum 1

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20top_p%20%3E%20(schema))

user : optional string

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).

[](#(resource)%20completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20user%20%3E%20(schema))

##### Returns Expand Collapse

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

completion_tokens : number

Number of tokens in the generated completion.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens)

prompt_tokens : number

Number of tokens in the prompt.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens)

total_tokens : number

Total number of tokens used in the request (prompt + completion).

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20total_tokens)

completion_tokens_details : optional object { accepted_prediction_tokens , audio_tokens , reasoning_tokens , rejected_prediction_tokens }

Breakdown of tokens used in a completion.

accepted_prediction_tokens : optional number

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20accepted_prediction_tokens)

audio_tokens : optional number

Audio input tokens generated by the model.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20audio_tokens)

reasoning_tokens : optional number

Tokens generated by the model for reasoning.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20reasoning_tokens)

rejected_prediction_tokens : optional number

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20rejected_prediction_tokens)

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details)

prompt_tokens_details : optional object { audio_tokens , cache_write_tokens , cached_tokens }

Breakdown of tokens used in the prompt.

audio_tokens : optional number

Audio input tokens present in the prompt.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20audio_tokens)

cache_write_tokens : optional number

The unadjusted number of prompt tokens written to cache.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20cache_write_tokens)

cached_tokens : optional number

Cached tokens present in the prompt.

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20cached_tokens)

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details)

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20completions%20%3E%20(model)%20completion%20%3E%20(schema))

No streaming Streaming

### Create completion

```
curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
"model": "VAR_completion_model_id",
"prompt": "Say this is a test",
"max_tokens": 7,
"temperature": 0
}'
```

```
{
"id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
"object": "text_completion",
"created": 1589478378,
"model": "VAR_completion_model_id",
"system_fingerprint": "fp_44709d6fcb",
"choices": [
{
"text": "\n\nThis is indeed a test",
"index": 0,
"logprobs": null,
"finish_reason": "length"
}
],
"usage": {
"prompt_tokens": 5,
"completion_tokens": 7,
"total_tokens": 12
}
}
```

### Create completion

```
curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
"model": "VAR_completion_model_id",
"prompt": "Say this is a test",
"max_tokens": 7,
"temperature": 0,
"stream": true
}'
```

```
{
"id": "cmpl-7iA7iJjj8V2zOkCGvWF2hAkDWBQZe",
"object": "text_completion",
"created": 1690759702,
"choices": [
{
"text": "This",
"index": 0,
"logprobs": null,
"finish_reason": null
}
],
"model": "gpt-3.5-turbo-instruct"
"system_fingerprint": "fp_44709d6fcb",
}
```

##### Returns Examples

```
{
"id": "id",
"choices": [
{
"finish_reason": "stop",
"index": 0,
"logprobs": {
"text_offset": [
0
],
"token_logprobs": [
0
],
"tokens": [
"string"
],
"top_logprobs": [
{
"foo": 0
}
]
},
"text": "text"
}
],
"created": 0,
"model": "model",
"object": "text_completion",
"system_fingerprint": "system_fingerprint",
"usage": {
"completion_tokens": 0,
"prompt_tokens": 0,
"total_tokens": 0,
"completion_tokens_details": {
"accepted_prediction_tokens": 0,
"audio_tokens": 0,
"reasoning_tokens": 0,
"rejected_prediction_tokens": 0
},
"prompt_tokens_details": {
"audio_tokens": 0,
"cache_write_tokens": 0,
"cached_tokens": 0
}
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/completions/methods/create
