---
source_url: https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/retrieve
title: "Get chat completion"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Get chat completion

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Chat](/api/reference/resources/chat)

[Completions](/api/reference/resources/chat/subresources/completions)

# Get chat completion

GET /chat/completions/{completion_id}

Get a stored chat completion. Only Chat Completions that have been created
with the `store` parameter set to `true` will be returned.

##### P ath Parameters Expand Collapse

completion_id : string

[](#(resource)%20chat.completions%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20completion_id%20%3E%20(schema))

##### Returns Expand Collapse

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

content : string

The contents of the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20content)

refusal : string

The refusal message generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20refusal)

role : "assistant"

The role of the author of this message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20role)

annotations : optional array of object { type , url_citation }

Annotations for the message, when applicable, as when using the
[web search tool](/docs/guides/tools-web-search?api-mode=chat).

type : "url_citation"

The type of the URL citation. Always `url_citation`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20type)

url_citation : object { end_index , start_index , title , url }

A URL citation when using web search.

end_index : number

The index of the last character of the URL citation in the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20end_index)

start_index : number

The index of the first character of the URL citation in the message.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20start_index)

title : string

The title of the web resource.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20title)

url : string

The URL of the web resource.

format uri

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation%20%3E%20(property)%20url)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20url_citation)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20annotations)

audio : optional [ChatCompletionAudio](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)) { id , data , expires_at , transcript }

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](/docs/guides/audio).

id : string

Unique identifier for this audio response.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20audio%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20id)

data : string

Base64 encoded audio bytes generated by the model, in the format
specified in the request.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20audio%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20data)

expires_at : number

The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

format unixtime

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20audio%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20expires_at)

transcript : string

Transcript of the audio generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20audio%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)%20%3E%20(property)%20transcript)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20audio)

Deprecated function_call : optional object { arguments , name }

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20function_call%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20function_call)

tool_calls : optional array of [ChatCompletionMessageToolCall](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))

The tool calls generated by the model, such as function calls.

One of the following:

ChatCompletionMessageFunctionToolCall object { id , function , type }

A call to a function tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name }

The function that the model called.

arguments : string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema))

ChatCompletionMessageCustomToolCall object { id , custom , type }

A call to a custom tool created by the model.

id : string

The ID of the tool call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

custom : object { input , name }

The custom tool that the model called.

input : string

The input for the custom tool call generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20input)

name : string

The name of the custom tool to call.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom%20%3E%20(property)%20name)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20custom)

type : "custom"

The type of the tool. Always `custom`.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema))

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20choices%20%3E%20(items)%20%3E%20(property)%20message%20%2B%20(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

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

completion_tokens : number

Number of tokens in the generated completion.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens)

prompt_tokens : number

Number of tokens in the prompt.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens)

total_tokens : number

Total number of tokens used in the request (prompt + completion).

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20total_tokens)

completion_tokens_details : optional object { accepted_prediction_tokens , audio_tokens , reasoning_tokens , rejected_prediction_tokens }

Breakdown of tokens used in a completion.

accepted_prediction_tokens : optional number

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20accepted_prediction_tokens)

audio_tokens : optional number

Audio input tokens generated by the model.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20audio_tokens)

reasoning_tokens : optional number

Tokens generated by the model for reasoning.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20reasoning_tokens)

rejected_prediction_tokens : optional number

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details%20%3E%20(property)%20rejected_prediction_tokens)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20completion_tokens_details)

prompt_tokens_details : optional object { audio_tokens , cache_write_tokens , cached_tokens }

Breakdown of tokens used in the prompt.

audio_tokens : optional number

Audio input tokens present in the prompt.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20audio_tokens)

cache_write_tokens : optional number

The unadjusted number of prompt tokens written to cache.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20cache_write_tokens)

cached_tokens : optional number

Cached tokens present in the prompt.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details%20%3E%20(property)%20cached_tokens)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage%20%2B%20(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)%20%3E%20(property)%20prompt_tokens_details)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))

### Get chat completion

```
curl https://api.openai.com/v1/chat/completions/chatcmpl-abc123 \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json"
```

```
{
"object": "chat.completion",
"id": "chatcmpl-abc123",
"model": "gpt-4o-2024-08-06",
"created": 1738960610,
"request_id": "req_ded8ab984ec4bf840f37566c1011c417",
"tool_choice": null,
"usage": {
"total_tokens": 31,
"completion_tokens": 18,
"prompt_tokens": 13
},
"seed": 4944116822809979520,
"top_p": 1.0,
"temperature": 1.0,
"presence_penalty": 0.0,
"frequency_penalty": 0.0,
"system_fingerprint": "fp_50cad350e4",
"input_user": null,
"service_tier": "default",
"tools": null,
"metadata": {},
"choices": [
{
"index": 0,
"message": {
"content": "Mind of circuits hum, \nLearning patterns in silence— \nFuture's quiet spark.",
"role": "assistant",
"tool_calls": null,
"function_call": null
},
"finish_reason": "stop",
"logprobs": null
}
],
"response_format": null
}
```

##### Returns Examples

```
{
"object": "chat.completion",
"id": "chatcmpl-abc123",
"model": "gpt-4o-2024-08-06",
"created": 1738960610,
"request_id": "req_ded8ab984ec4bf840f37566c1011c417",
"tool_choice": null,
"usage": {
"total_tokens": 31,
"completion_tokens": 18,
"prompt_tokens": 13
},
"seed": 4944116822809979520,
"top_p": 1.0,
"temperature": 1.0,
"presence_penalty": 0.0,
"frequency_penalty": 0.0,
"system_fingerprint": "fp_50cad350e4",
"input_user": null,
"service_tier": "default",
"tools": null,
"metadata": {},
"choices": [
{
"index": 0,
"message": {
"content": "Mind of circuits hum, \nLearning patterns in silence— \nFuture's quiet spark.",
"role": "assistant",
"tool_calls": null,
"function_call": null
},
"finish_reason": "stop",
"logprobs": null
}
],
"response_format": null
}
```

---
Source: https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/retrieve
