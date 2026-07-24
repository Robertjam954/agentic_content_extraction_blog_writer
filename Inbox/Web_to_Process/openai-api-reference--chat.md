---
source_url: https://developers.openai.com/api/reference/resources/chat
title: "Chat"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Chat

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Chat

#### Chat Completions

Given a list of messages comprising a conversation, the model will return a response.

##### [Create chat completion](/api/reference/resources/chat/subresources/completions/methods/create)

POST /chat/completions

##### [List Chat Completions](/api/reference/resources/chat/subresources/completions/methods/list)

GET /chat/completions

##### [Get chat completion](/api/reference/resources/chat/subresources/completions/methods/retrieve)

GET /chat/completions/{completion_id}

##### [Update chat completion](/api/reference/resources/chat/subresources/completions/methods/update)

POST /chat/completions/{completion_id}

##### [Delete chat completion](/api/reference/resources/chat/subresources/completions/methods/delete)

DELETE /chat/completions/{completion_id}

##### Models Expand Collapse

ChatCompletion object { id , choices , created , 6 more }

Represents a chat completion response returned by model, based on the provided input.

id : string

A unique identifier for the chat completion.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20id)

choices : array of object { finish_reason , index , logprobs , message }

A list of chat completion choices. Can be more than one if `n` is greater than 1.

finish_reason : "stop" or "length" or "tool_calls" or 2 more

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
Read the [Model Spec](https://model-spec.openai.com/2025-12-18.html) for more.

One of the following:

"stop"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%200)

"length"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%201)

"tool_calls"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%202)

"content_filter"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%203)

"function_call"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%204)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason)

index : number

The index of the choice in the list of choices.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20index)

logprobs : object { content , refusal }

Log probability information for the choice.

content : array of [ChatCompletionTokenLogprob](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token , bytes , logprob , top_logprobs }

A list of message content tokens with log probability information.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20logprob)

top_logprobs : array of object { token , bytes , logprob }

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20logprobs%20%3E%20(property)%20content)

refusal : array of [ChatCompletionTokenLogprob](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token , bytes , logprob , top_logprobs }

A list of message refusal tokens with log probability information.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20logprob)

top_logprobs : array of object { token , bytes , logprob }

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20logprobs%20%3E%20(property)%20refusal)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20logprobs)

message : [ChatCompletionMessage](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)) { content , refusal , role , 4 more }

A chat completion message generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices)

created : number

The Unix timestamp (in seconds) of when the chat completion was created.

format unixtime

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20created)

model : string

The model used for the chat completion.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20model)

object : "chat.completion"

The object type, which is always `chat.completion`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20object)

moderation : optional object { input , output }

Moderation results for the request input and generated output, if moderated
completions were requested.

input : object { model , results , type } or object { code , message , type }

Moderation for the request input.

One of the following:

ModerationResults object { model , results , type }

Successful moderation results for the request input or generated output.

model : string

The moderation model used to generate the results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20model)

results : array of object { categories , category_applied_input_types , category_scores , 3 more }

A list of moderation results.

categories : map [ boolean ]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20categories)

category_applied_input_types : map [ array of "text" or "image" ]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types)

category_scores : map [ number ]

A dictionary of moderation categories to scores.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_scores)

flagged : boolean

A boolean indicating whether the content was flagged by any category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20flagged)

model : string

The moderation model that produced this result.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20model)

type : "moderation_result"

The object type, which was always `moderation_result` for successful moderation results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results)

type : "moderation_results"

The object type, which is always `moderation_results`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200)

Error object { code , message , type }

An error produced while attempting moderation.

code : string

The error code.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201%20%3E%20(property)%20code)

message : string

The error message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201%20%3E%20(property)%20message)

type : "error"

The object type, which is always `error`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input)

output : object { model , results , type } or object { code , message , type }

Moderation for the generated output.

One of the following:

ModerationResults object { model , results , type }

Successful moderation results for the request input or generated output.

model : string

The moderation model used to generate the results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20model)

results : array of object { categories , category_applied_input_types , category_scores , 3 more }

A list of moderation results.

categories : map [ boolean ]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20categories)

category_applied_input_types : map [ array of "text" or "image" ]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types)

category_scores : map [ number ]

A dictionary of moderation categories to scores.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_scores)

flagged : boolean

A boolean indicating whether the content was flagged by any category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20flagged)

model : string

The moderation model that produced this result.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20model)

type : "moderation_result"

The object type, which was always `moderation_result` for successful moderation results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results)

type : "moderation_results"

The object type, which is always `moderation_results`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200)

Error object { code , message , type }

An error produced while attempting moderation.

code : string

The error code.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201%20%3E%20(property)%20code)

message : string

The error message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201%20%3E%20(property)%20message)

type : "error"

The object type, which is always `error`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20moderation)

service_tier : optional "auto" or "default" or "flex" or 2 more

Specifies the processing type used for serving the request.

- If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.

- If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.

- If set to ‘[flex](/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.

- When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%200)

"default"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%201)

"flex"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%202)

"scale"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%203)

"priority"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%204)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20service_tier)

Deprecated system_fingerprint : optional string

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20system_fingerprint)

usage : optional [CompletionUsage](/api/reference/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)) { completion_tokens , prompt_tokens , total_tokens , 2 more }

Usage statistics for the completion request.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))

ChatCompletionAllowedToolChoice object { allowed_tools , type }

Constrains the tools available to the model to a pre-defined set.

allowed_tools : [ChatCompletionAllowedTools](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)) { mode , tools }

Constrains the tools available to the model to a pre-defined set.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema)%20%3E%20(property)%20allowed_tools)

type : "allowed_tools"

Allowed tool configuration type. Always `allowed_tools`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema))

ChatCompletionAssistantMessageParam object { role , audio , content , 4 more }

Messages sent by the model in response to user messages.

role : "assistant"

The role of the messages author, in this case `assistant`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

audio : optional object { id }

Data about a previous audio response from the model.
[Learn more](/docs/guides/audio).

id : string

Unique identifier for a previous audio response from the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20id)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20audio)

content : optional string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or [ChatCompletionContentPartRefusal](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal , type }

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

TextContent = string

The contents of the assistant message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or [ChatCompletionContentPartRefusal](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal , type }

An array of content parts with a defined type. Can be one or more of type `text`, or exactly one of type `refusal`.

One of the following:

ChatCompletionContentPartText object { text , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

ChatCompletionContentPartRefusal object { refusal , type }

refusal : string

The refusal message generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)%20%3E%20(property)%20refusal)

type : "refusal"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

Deprecated function_call : optional object { arguments , name }

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20function_call)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

refusal : optional string

The refusal message by the assistant.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20refusal)

tool_calls : optional array of [ChatCompletionMessageToolCall](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))

The tool calls generated by the model, such as function calls.

One of the following:

ChatCompletionMessageFunctionToolCall object { id , function , type }

A call to a function tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function that the model called.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema))

ChatCompletionMessageCustomToolCall object { id , custom , type }

A call to a custom tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

custom : object { input , name }

The custom tool that the model called.

input : string

The input for the custom tool call generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20input)

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema))

ChatCompletionAudio object { id , data , expires_at , transcript }

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](/docs/guides/audio).

id : string

Unique identifier for this audio response.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20id)

data : string

Base64 encoded audio bytes generated by the model, in the format
specified in the request.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20data)

expires_at : number

The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

format unixtime

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20expires_at)

transcript : string

Transcript of the audio generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20transcript)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema))

ChatCompletionAudioParam object { format , voice }

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](/docs/guides/audio).

format : "wav" or "aac" or "mp3" or 3 more

Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,
`opus`, or `pcm16`.

One of the following:

"wav"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20format%20%3E%20(member)%200)

"aac"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20format%20%3E%20(member)%201)

"mp3"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20format%20%3E%20(member)%202)

"flac"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20format%20%3E%20(member)%203)

"opus"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20format%20%3E%20(member)%204)

"pcm16"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20format%20%3E%20(member)%205)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20format)

voice : string or "alloy" or "ash" or "ballad" or 7 more or object { id }

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`, `onyx`,
`sage`, `shimmer`, `marin`, and `cedar`. You may also provide a
custom voice object with an `id`, for example `{ "id": "voice_1234" }`.

One of the following:

string

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%200)

"alloy" or "ash" or "ballad" or 7 more

One of the following:

"alloy"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%200)

"ash"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%201)

"ballad"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%202)

"coral"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%203)

"echo"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%204)

"sage"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%205)

"shimmer"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%206)

"verse"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%207)

"marin"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%208)

"cedar"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201%20%3E%20(member)%209)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%201)

ID object { id }

Custom voice reference.

id : string

The custom voice ID, e.g. `voice_1234`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%202%20%3E%20(property)%20id)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice%20%3E%20(variant)%202)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema)%20%3E%20(property)%20voice)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema))

ChatCompletionChunk object { id , choices , created , 6 more }

Represents a streamed chunk of a chat completion response returned
by the model, based on the provided input.
[Learn more](/docs/guides/streaming-responses).

id : string

A unique identifier for the chat completion. Each chunk has the same ID.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20id)

choices : array of object { delta , finish_reason , index , logprobs }

A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the
last chunk if you set `stream_options: {"include_usage": true}`.

delta : object { content , function_call , refusal , 2 more }

A chat completion delta generated by streamed model responses.

content : optional string

The contents of the chunk message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20content)

Deprecated function_call : optional object { arguments , name }

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments : optional string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20function_call%20%3E%20(property)%20arguments)

name : optional string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20function_call%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20function_call)

refusal : optional string

The refusal message generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20refusal)

role : optional "developer" or "system" or "user" or 2 more

The role of the author of this message.

One of the following:

"developer"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20role%20%3E%20(member)%200)

"system"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20role%20%3E%20(member)%201)

"user"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20role%20%3E%20(member)%202)

"assistant"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20role%20%3E%20(member)%203)

"tool"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20role%20%3E%20(member)%204)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20role)

tool_calls : optional array of object { index , id , function , type }

index : number

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20tool_calls%20%3E%20(items)%20%3E%20(property)%20index)

id : optional string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20tool_calls%20%3E%20(items)%20%3E%20(property)%20id)

function : optional object { arguments , name }

arguments : optional string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20tool_calls%20%3E%20(items)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : optional string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20tool_calls%20%3E%20(items)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20tool_calls%20%3E%20(items)%20%3E%20(property)%20function)

type : optional "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20tool_calls%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta%20%3E%20(property)%20tool_calls)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20delta)

finish_reason : "stop" or "length" or "tool_calls" or 2 more

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

One of the following:

"stop"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%200)

"length"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%201)

"tool_calls"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%202)

"content_filter"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%203)

"function_call"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason%20%3E%20(member)%204)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20finish_reason)

index : number

The index of the choice in the list of choices.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20index)

logprobs : optional object { content , refusal }

Log probability information for the choice.

content : array of [ChatCompletionTokenLogprob](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token , bytes , logprob , top_logprobs }

A list of message content tokens with log probability information.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20logprob)

top_logprobs : array of object { token , bytes , logprob }

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20logprobs%20%3E%20(property)%20content)

refusal : array of [ChatCompletionTokenLogprob](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token , bytes , logprob , top_logprobs }

A list of message refusal tokens with log probability information.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20logprob)

top_logprobs : array of object { token , bytes , logprob }

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20logprobs%20%3E%20(property)%20refusal)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20logprobs)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20choices)

created : number

The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

format unixtime

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20created)

model : string

The model to generate the completion.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20model)

object : "chat.completion.chunk"

The object type, which is always `chat.completion.chunk`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20object)

moderation : optional object { input , output }

Moderation results for the request input and generated output. Present
on the moderation chunk when moderated completions are requested.

input : object { model , results , type } or object { code , message , type }

Moderation for the request input.

One of the following:

ModerationResults object { model , results , type }

Successful moderation results for the request input or generated output.

model : string

The moderation model used to generate the results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20model)

results : array of object { categories , category_applied_input_types , category_scores , 3 more }

A list of moderation results.

categories : map [ boolean ]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20categories)

category_applied_input_types : map [ array of "text" or "image" ]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types)

category_scores : map [ number ]

A dictionary of moderation categories to scores.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_scores)

flagged : boolean

A boolean indicating whether the content was flagged by any category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20flagged)

model : string

The moderation model that produced this result.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20model)

type : "moderation_result"

The object type, which was always `moderation_result` for successful moderation results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20results)

type : "moderation_results"

The object type, which is always `moderation_results`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%200)

Error object { code , message , type }

An error produced while attempting moderation.

code : string

The error code.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201%20%3E%20(property)%20code)

message : string

The error message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201%20%3E%20(property)%20message)

type : "error"

The object type, which is always `error`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20input)

output : object { model , results , type } or object { code , message , type }

Moderation for the generated output.

One of the following:

ModerationResults object { model , results , type }

Successful moderation results for the request input or generated output.

model : string

The moderation model used to generate the results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20model)

results : array of object { categories , category_applied_input_types , category_scores , 3 more }

A list of moderation results.

categories : map [ boolean ]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20categories)

category_applied_input_types : map [ array of "text" or "image" ]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types%20%3E%20(items)%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_applied_input_types)

category_scores : map [ number ]

A dictionary of moderation categories to scores.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20category_scores)

flagged : boolean

A boolean indicating whether the content was flagged by any category.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20flagged)

model : string

The moderation model that produced this result.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20model)

type : "moderation_result"

The object type, which was always `moderation_result` for successful moderation results.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20results)

type : "moderation_results"

The object type, which is always `moderation_results`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%200)

Error object { code , message , type }

An error produced while attempting moderation.

code : string

The error code.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201%20%3E%20(property)%20code)

message : string

The error message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201%20%3E%20(property)%20message)

type : "error"

The object type, which is always `error`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation%20%3E%20(property)%20output)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20moderation)

service_tier : optional "auto" or "default" or "flex" or 2 more

Specifies the processing type used for serving the request.

- If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.

- If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.

- If set to ‘[flex](/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.

- When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%200)

"default"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%201)

"flex"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%202)

"scale"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%203)

"priority"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20service_tier%20%3E%20(member)%204)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20service_tier)

Deprecated system_fingerprint : optional string

This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20system_fingerprint)

usage : optional [CompletionUsage](/api/reference/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)) { completion_tokens , prompt_tokens , total_tokens , 2 more }

An optional field that will only be present when you set
`stream_options: {"include_usage": true}` in your request. When present, it
contains a null value **except for the last chunk** which contains the
token usage statistics for the entire request.

**NOTE:** If the stream is interrupted or cancelled, you may not
receive the final usage chunk which contains the total token usage for
the request.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_chunk%20%3E%20(schema))

ChatCompletionContentPart = [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or [ChatCompletionContentPartImage](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)) { image_url , type , prompt_cache_breakpoint } or [ChatCompletionContentPartInputAudio](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)) { input_audio , type , prompt_cache_breakpoint } or object { file , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

One of the following:

ChatCompletionContentPartText object { text , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

ChatCompletionContentPartImage object { image_url , type , prompt_cache_breakpoint }

Learn about [image inputs](/docs/guides/vision).

image_url : object { url , detail }

url : string

Either a URL of the image or the base64 encoded image data.

format uri

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20url)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema))

ChatCompletionContentPartInputAudio object { input_audio , type , prompt_cache_breakpoint }

Learn about [audio inputs](/docs/guides/audio).

input_audio : object { data , format }

data : string

Base64 encoded audio data.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "wav" or "mp3"

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

"wav"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"mp3"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the content part. Always `input_audio`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema))

FileContentPart object { file , type , prompt_cache_breakpoint }

Learn about [file inputs](/docs/guides/text) for text generation.

file : object { file_data , file_id , filename }

file_data : optional string

The base64 encoded file data, used when passing the file to the model
as a string.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20file_data)

file_id : optional string

The ID of an uploaded file to use as input.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20file_id)

filename : optional string

The name of the file, used when passing the file to the model as a
string.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20filename)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file)

type : "file"

The type of the content part. Always `file`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))

ChatCompletionContentPartImage object { image_url , type , prompt_cache_breakpoint }

Learn about [image inputs](/docs/guides/vision).

image_url : object { url , detail }

url : string

Either a URL of the image or the base64 encoded image data.

format uri

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20url)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema))

ChatCompletionContentPartInputAudio object { input_audio , type , prompt_cache_breakpoint }

Learn about [audio inputs](/docs/guides/audio).

input_audio : object { data , format }

data : string

Base64 encoded audio data.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "wav" or "mp3"

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

"wav"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"mp3"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the content part. Always `input_audio`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema))

ChatCompletionContentPartRefusal object { refusal , type }

refusal : string

The refusal message generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)%20%3E%20(property)%20refusal)

type : "refusal"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema))

ChatCompletionContentPartText object { text , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

ChatCompletionCustomTool object { custom , type }

A custom tool that processes input using a specified format.

custom : object { name , description , format }

Properties of the custom tool.

name : string

The name of the custom tool, used to identify it in tool calls.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

description : optional string

Optional description of the custom tool, used to provide more context.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20description)

format : optional object { type } or object { grammar , type }

The input format for the custom tool. Default is unconstrained text.

One of the following:

TextFormat object { type }

Unconstrained free-form text.

type : "text"

Unconstrained text format. Always `text`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%200)

GrammarFormat object { grammar , type }

A grammar defined by the user.

grammar : object { definition , syntax }

Your chosen grammar.

definition : string

The grammar definition.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20definition)

syntax : "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20syntax%20%3E%20(member)%200)

"regex"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20syntax%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20syntax)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar)

type : "grammar"

Grammar format. Always `grammar`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the custom tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema))

ChatCompletionDeleted object { id , deleted , object }

id : string

The ID of the chat completion that was deleted.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the chat completion was deleted.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "chat.completion.deleted"

The type of object being deleted.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema))

ChatCompletionDeveloperMessageParam object { content , role , name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

content : string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

The contents of the developer message.

One of the following:

TextContent = string

The contents of the developer message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

An array of content parts with a defined type. For developer messages, only type `text` is supported.

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "developer"

The role of the messages author, in this case `developer`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema))

ChatCompletionFunctionCallOption object { name }

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_call_option%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_call_option%20%3E%20(schema))

ChatCompletionFunctionMessageParam object { content , name , role }

content : string

The contents of the function message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

role : "function"

The role of the messages author, in this case `function`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema))

ChatCompletionFunctionTool object { function , type }

A function tool that can be used to generate a response.

function : [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name , description , parameters , strict }

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))

ChatCompletionMessage object { content , refusal , role , 4 more }

A chat completion message generated by the model.

content : string

The contents of the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20content)

refusal : string

The refusal message generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20refusal)

role : "assistant"

The role of the author of this message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20role)

annotations : optional array of object { type , url_citation }

Annotations for the message, when applicable, as when using the
[web search tool](/docs/guides/tools-web-search?api-mode=chat).

type : "url_citation"

The type of the URL citation. Always `url_citation`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20type)

url_citation : object { end_index , start_index , title , url }

A URL citation when using web search.

end_index : number

The index of the last character of the URL citation in the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20end_index)

start_index : number

The index of the first character of the URL citation in the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20start_index)

title : string

The title of the web resource.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20title)

url : string

The URL of the web resource.

format uri

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20url)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations)

audio : optional [ChatCompletionAudio](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)) { id , data , expires_at , transcript }

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](/docs/guides/audio).

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20audio)

Deprecated function_call : optional object { arguments , name }

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20function_call)

tool_calls : optional array of [ChatCompletionMessageToolCall](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))

The tool calls generated by the model, such as function calls.

One of the following:

ChatCompletionMessageFunctionToolCall object { id , function , type }

A call to a function tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function that the model called.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema))

ChatCompletionMessageCustomToolCall object { id , custom , type }

A call to a custom tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

custom : object { input , name }

The custom tool that the model called.

input : string

The input for the custom tool call generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20input)

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema))

ChatCompletionMessageCustomToolCall object { id , custom , type }

A call to a custom tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

custom : object { input , name }

The custom tool that the model called.

input : string

The input for the custom tool call generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20input)

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema))

ChatCompletionMessageFunctionToolCall object { id , function , type }

A call to a function tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function that the model called.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema))

ChatCompletionMessageParam = [ChatCompletionDeveloperMessageParam](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)) { content , role , name } or [ChatCompletionSystemMessageParam](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)) { content , role , name } or [ChatCompletionUserMessageParam](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)) { content , role , name } or 3 more

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

One of the following:

ChatCompletionDeveloperMessageParam object { content , role , name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

content : string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

The contents of the developer message.

One of the following:

TextContent = string

The contents of the developer message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

An array of content parts with a defined type. For developer messages, only type `text` is supported.

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "developer"

The role of the messages author, in this case `developer`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema))

ChatCompletionSystemMessageParam object { content , role , name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

content : string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

The contents of the system message.

One of the following:

TextContent = string

The contents of the system message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

An array of content parts with a defined type. For system messages, only type `text` is supported.

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "system"

The role of the messages author, in this case `system`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema))

ChatCompletionUserMessageParam object { content , role , name }

Messages sent by an end user, containing prompts or additional context
information.

content : string or array of [ChatCompletionContentPart](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))

The contents of the user message.

One of the following:

TextContent = string

The text contents of the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPart](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))

An array of content parts with a defined type. Supported options differ based on the [model](/docs/models) being used to generate the response. Can contain text, image, or audio inputs.

One of the following:

ChatCompletionContentPartText object { text , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

ChatCompletionContentPartImage object { image_url , type , prompt_cache_breakpoint }

Learn about [image inputs](/docs/guides/vision).

image_url : object { url , detail }

url : string

Either a URL of the image or the base64 encoded image data.

format uri

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20url)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema))

ChatCompletionContentPartInputAudio object { input_audio , type , prompt_cache_breakpoint }

Learn about [audio inputs](/docs/guides/audio).

input_audio : object { data , format }

data : string

Base64 encoded audio data.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "wav" or "mp3"

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

"wav"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"mp3"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the content part. Always `input_audio`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema))

FileContentPart object { file , type , prompt_cache_breakpoint }

Learn about [file inputs](/docs/guides/text) for text generation.

file : object { file_data , file_id , filename }

file_data : optional string

The base64 encoded file data, used when passing the file to the model
as a string.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20file_data)

file_id : optional string

The ID of an uploaded file to use as input.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20file_id)

filename : optional string

The name of the file, used when passing the file to the model as a
string.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20filename)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file)

type : "file"

The type of the content part. Always `file`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user"

The role of the messages author, in this case `user`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema))

ChatCompletionAssistantMessageParam object { role , audio , content , 4 more }

Messages sent by the model in response to user messages.

role : "assistant"

The role of the messages author, in this case `assistant`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

audio : optional object { id }

Data about a previous audio response from the model.
[Learn more](/docs/guides/audio).

id : string

Unique identifier for a previous audio response from the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20audio%20%3E%20(property)%20id)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20audio)

content : optional string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or [ChatCompletionContentPartRefusal](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal , type }

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

TextContent = string

The contents of the assistant message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or [ChatCompletionContentPartRefusal](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal , type }

An array of content parts with a defined type. Can be one or more of type `text`, or exactly one of type `refusal`.

One of the following:

ChatCompletionContentPartText object { text , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

ChatCompletionContentPartRefusal object { refusal , type }

refusal : string

The refusal message generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)%20%3E%20(property)%20refusal)

type : "refusal"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

Deprecated function_call : optional object { arguments , name }

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20function_call)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

refusal : optional string

The refusal message by the assistant.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20refusal)

tool_calls : optional array of [ChatCompletionMessageToolCall](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))

The tool calls generated by the model, such as function calls.

One of the following:

ChatCompletionMessageFunctionToolCall object { id , function , type }

A call to a function tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function that the model called.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema))

ChatCompletionMessageCustomToolCall object { id , custom , type }

A call to a custom tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

custom : object { input , name }

The custom tool that the model called.

input : string

The input for the custom tool call generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20input)

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_assistant_message_param%20%3E%20(schema))

ChatCompletionToolMessageParam object { content , role , tool_call_id }

content : string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

The contents of the tool message.

One of the following:

TextContent = string

The contents of the tool message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

An array of content parts with a defined type. For tool messages, only type `text` is supported.

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "tool"

The role of the messages author, in this case `tool`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

tool_call_id : string

Tool call that this message is responding to.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20tool_call_id)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema))

ChatCompletionFunctionMessageParam object { content , name , role }

content : string

The contents of the function message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

role : "function"

The role of the messages author, in this case `function`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_message_param%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_param%20%3E%20(schema))

ChatCompletionMessageToolCall = [ChatCompletionMessageFunctionToolCall](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)) { id , function , type } or [ChatCompletionMessageCustomToolCall](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)) { id , custom , type }

A call to a function tool created by the model.

One of the following:

ChatCompletionMessageFunctionToolCall object { id , function , type }

A call to a function tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function that the model called.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema))

ChatCompletionMessageCustomToolCall object { id , custom , type }

A call to a custom tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

custom : object { input , name }

The custom tool that the model called.

input : string

The input for the custom tool call generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20input)

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))

ChatCompletionModality = "text" or "audio"

One of the following:

"text"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_modality%20%3E%20(schema)%20%3E%20(member)%200)

"audio"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_modality%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_modality%20%3E%20(schema))

ChatCompletionNamedToolChoice object { function , type }

Specifies a tool the model should use. Use to force the model to call a specific function.

function : object { name }

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

For function calling, the type is always `function`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema))

ChatCompletionNamedToolChoiceCustom object { custom , type }

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

custom : object { name }

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

For custom tool calling, the type is always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema))

ChatCompletionPredictionContent object { content , type }

Static predicted output content, such as the content of a text file that is
being regenerated.

content : string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

The content that should be matched when generating a model response.
If generated tokens would match this content, the entire model response
can be returned much more quickly.

One of the following:

TextContent = string

The content used for a Predicted Output. This is often the
text of a file you are regenerating with minor changes.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_prediction_content%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

An array of content parts with a defined type. Supported options differ based on the [model](/docs/models) being used to generate the response. Can contain text inputs.

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_prediction_content%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_prediction_content%20%3E%20(schema)%20%3E%20(property)%20content)

type : "content"

The type of the predicted content you want to provide. This type is
currently always `content`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_prediction_content%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_prediction_content%20%3E%20(schema))

ChatCompletionRole = "developer" or "system" or "user" or 3 more

The role of the author of a message

One of the following:

"developer"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)%20%3E%20(member)%200)

"system"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)%20%3E%20(member)%201)

"user"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)%20%3E%20(member)%202)

"assistant"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)%20%3E%20(member)%203)

"tool"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)%20%3E%20(member)%204)

"function"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)%20%3E%20(member)%205)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema))

ChatCompletionStoreMessage = [ChatCompletionMessage](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)) { content , refusal , role , 4 more }

A chat completion message generated by the model.

id : string

The identifier of the chat message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20id)

content_parts : optional array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or [ChatCompletionContentPartImage](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)) { image_url , type , prompt_cache_breakpoint }

If a content parts array was provided, this is an array of `text` and `image_url` parts.
Otherwise, null.

One of the following:

ChatCompletionContentPartText object { text , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

ChatCompletionContentPartImage object { image_url , type , prompt_cache_breakpoint }

Learn about [image inputs](/docs/guides/vision).

image_url : object { url , detail }

url : string

Either a URL of the image or the base64 encoded image data.

format uri

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20url)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20content_parts)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema))

ChatCompletionStreamOptions object { include_obfuscation , include_usage }

Options for streaming response. Only set this when you set `stream: true`.

include_obfuscation : optional boolean

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema)%20%3E%20(property)%20include_obfuscation)

include_usage : optional boolean

If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema)%20%3E%20(property)%20include_usage)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema))

ChatCompletionSystemMessageParam object { content , role , name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

content : string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

The contents of the system message.

One of the following:

TextContent = string

The contents of the system message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

An array of content parts with a defined type. For system messages, only type `text` is supported.

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "system"

The role of the messages author, in this case `system`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema))

ChatCompletionTokenLogprob object { token , bytes , logprob , top_logprobs }

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20logprob)

top_logprobs : array of object { token , bytes , logprob }

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token : string

The token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20token)

bytes : array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20bytes)

logprob : number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs%20%3E%20(items)%20%3E%20(property)%20logprob)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)%20%3E%20(property)%20top_logprobs)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))

ChatCompletionTool = [ChatCompletionFunctionTool](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function , type } or [ChatCompletionCustomTool](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)) { custom , type }

A function tool that can be used to generate a response.

One of the following:

ChatCompletionFunctionTool object { function , type }

A function tool that can be used to generate a response.

function : [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name , description , parameters , strict }

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))

ChatCompletionCustomTool object { custom , type }

A custom tool that processes input using a specified format.

custom : object { name , description , format }

Properties of the custom tool.

name : string

The name of the custom tool, used to identify it in tool calls.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

description : optional string

Optional description of the custom tool, used to provide more context.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20description)

format : optional object { type } or object { grammar , type }

The input format for the custom tool. Default is unconstrained text.

One of the following:

TextFormat object { type }

Unconstrained free-form text.

type : "text"

Unconstrained text format. Always `text`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%200)

GrammarFormat object { grammar , type }

A grammar defined by the user.

grammar : object { definition , syntax }

Your chosen grammar.

definition : string

The grammar definition.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20definition)

syntax : "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20syntax%20%3E%20(member)%200)

"regex"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20syntax%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar%20%3E%20(property)%20syntax)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20grammar)

type : "grammar"

Grammar format. Always `grammar`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20format)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the custom tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool%20%3E%20(schema))

ChatCompletionToolChoiceOption = "none" or "auto" or "required" or [ChatCompletionAllowedToolChoice](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema)) { allowed_tools , type } or [ChatCompletionNamedToolChoice](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)) { function , type } or [ChatCompletionNamedToolChoiceCustom](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)) { custom , type }

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

One of the following:

ToolChoiceMode = "none" or "auto" or "required"

`none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools.

One of the following:

"none"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%200)

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%201)

"required"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(member)%202)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema)%20%3E%20(variant)%200)

ChatCompletionAllowedToolChoice object { allowed_tools , type }

Constrains the tools available to the model to a pre-defined set.

allowed_tools : [ChatCompletionAllowedTools](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)) { mode , tools }

Constrains the tools available to the model to a pre-defined set.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema)%20%3E%20(property)%20allowed_tools)

type : "allowed_tools"

Allowed tool configuration type. Always `allowed_tools`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema))

ChatCompletionNamedToolChoice object { function , type }

Specifies a tool the model should use. Use to force the model to call a specific function.

function : object { name }

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

For function calling, the type is always `function`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema))

ChatCompletionNamedToolChoiceCustom object { custom , type }

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

custom : object { name }

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

For custom tool calling, the type is always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema))

ChatCompletionToolMessageParam object { content , role , tool_call_id }

content : string or array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

The contents of the tool message.

One of the following:

TextContent = string

The contents of the tool message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPartText](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint }

An array of content parts with a defined type. For tool messages, only type `text` is supported.

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "tool"

The role of the messages author, in this case `tool`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

tool_call_id : string

Tool call that this message is responding to.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema)%20%3E%20(property)%20tool_call_id)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_message_param%20%3E%20(schema))

ChatCompletionUserMessageParam object { content , role , name }

Messages sent by an end user, containing prompts or additional context
information.

content : string or array of [ChatCompletionContentPart](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))

The contents of the user message.

One of the following:

TextContent = string

The text contents of the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ArrayOfContentParts = array of [ChatCompletionContentPart](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))

An array of content parts with a defined type. Supported options differ based on the [model](/docs/models) being used to generate the response. Can contain text, image, or audio inputs.

One of the following:

ChatCompletionContentPartText object { text , type , prompt_cache_breakpoint }

Learn about [text inputs](/docs/guides/text-generation).

text : string

The text content.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "text"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

ChatCompletionContentPartImage object { image_url , type , prompt_cache_breakpoint }

Learn about [image inputs](/docs/guides/vision).

image_url : object { url , detail }

url : string

Either a URL of the image or the base64 encoded image data.

format uri

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20url)

detail : optional "auto" or "low" or "high"

Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url%20%3E%20(property)%20detail)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

type : "image_url"

The type of the content part.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema))

ChatCompletionContentPartInputAudio object { input_audio , type , prompt_cache_breakpoint }

Learn about [audio inputs](/docs/guides/audio).

input_audio : object { data , format }

data : string

Base64 encoded audio data.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "wav" or "mp3"

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

"wav"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"mp3"

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the content part. Always `input_audio`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema))

FileContentPart object { file , type , prompt_cache_breakpoint }

Learn about [file inputs](/docs/guides/text) for text generation.

file : object { file_data , file_id , filename }

file_data : optional string

The base64 encoded file data, used when passing the file to the model
as a string.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20file_data)

file_id : optional string

The ID of an uploaded file to use as input.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20file_id)

filename : optional string

The name of the file, used when passing the file to the model as a
string.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file%20%3E%20(property)%20filename)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20file)

type : "file"

The type of the content part. Always `file`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema)%20%3E%20(variant)%203)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user"

The role of the messages author, in this case `user`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20role)

name : optional string

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema))

ChatCompletionAllowedTools object { mode , tools }

Constrains the tools available to the model to a pre-defined set.

mode : "auto" or "required"

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

One of the following:

"auto"

[](#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200)

"required"

[](#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201)

[](#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)%20%3E%20(property)%20mode)

tools : array of map [ unknown ]

A list of tool definitions that the model should be allowed to call.

For the Chat Completions API, the list of tool definitions might look like:

```
[
{ "type": "function", "function": { "name": "get_weather" } },
{ "type": "function", "function": { "name": "get_time" } }
]
```

[](#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)%20%3E%20(property)%20tools)

[](#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema))

#### Chat Completions Messages

Given a list of messages comprising a conversation, the model will return a response.

##### [Get chat messages](/api/reference/resources/chat/subresources/completions/subresources/messages/methods/list)

GET /chat/completions/{completion_id}/messages

---
Source: https://developers.openai.com/api/reference/resources/chat
