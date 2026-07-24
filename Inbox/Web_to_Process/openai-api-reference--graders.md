---
source_url: https://developers.openai.com/api/reference/resources/graders
title: "Graders"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Graders

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Graders

#### Graders Grader Models

##### Models Expand Collapse

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

LabelModelGrader object { input , labels , model , 3 more }

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input : array of object { content , role , type }

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input)

labels : array of string

The labels to assign to each item in the evaluation.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20labels)

model : string

The model to use for the evaluation. Must support structured outputs.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20name)

passing_labels : array of string

The labels that indicate a passing result. Must be a subset of labels.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20passing_labels)

type : "label_model"

The object type, which is always `label_model`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema))

MultiGrader object { calculate_output , graders , name , type }

A MultiGrader object combines the output of multiple graders to produce a single score.

calculate_output : string

A formula to calculate the output based on grader results.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20calculate_output)

graders : [StringCheckGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input , name , operation , 2 more } or [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more } or [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag } or 2 more

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

One of the following:

StringCheckGrader object { input , name , operation , 2 more }

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input : string

The input text. This may include template strings.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20name)

operation : "eq" or "ne" or "like" or "ilike"

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%200)

"ne"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%201)

"like"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%202)

"ilike"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%203)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation)

reference : string

The reference text. This may include template strings.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "string_check"

The object type, which is always `string_check`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema))

TextSimilarityGrader object { evaluation_metric , input , name , 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation_metric : "cosine" or "fuzzy_match" or "bleu" or 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

"cosine"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%200)

"fuzzy_match"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%201)

"bleu"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%202)

"gleu"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%203)

"meteor"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%204)

"rouge_1"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%205)

"rouge_2"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%206)

"rouge_3"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%207)

"rouge_4"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%208)

"rouge_5"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%209)

"rouge_l"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%2010)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric)

input : string

The text being graded.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20name)

reference : string

The text being graded against.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "text_similarity"

The type of grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema))

PythonGrader object { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20name)

source : string

The source code of the python script.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20source)

type : "python"

The object type, which is always `python`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20type)

image_tag : optional string

The image tag to use for the python script.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20image_tag)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema))

ScoreModelGrader object { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input : array of object { content , role , type }

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input)

model : string

The model to use for the evaluation.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20name)

type : "score_model"

The object type, which is always `score_model`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20type)

range : optional array of number

The range of the score. Defaults to `[0, 1]`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20range)

sampling_params : optional object { max_completions_tokens , reasoning_effort , seed , 2 more }

The sampling parameters for the model.

max_completions_tokens : optional number

The maximum number of tokens the grader model may generate in its response.

minimum 1

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completions_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema))

LabelModelGrader object { input , labels , model , 3 more }

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input : array of object { content , role , type }

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input)

labels : array of string

The labels to assign to each item in the evaluation.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20labels)

model : string

The model to use for the evaluation. Must support structured outputs.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20name)

passing_labels : array of string

The labels that indicate a passing result. Must be a subset of labels.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20passing_labels)

type : "label_model"

The object type, which is always `label_model`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20graders)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20name)

type : "multi"

The object type, which is always `multi`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema))

PythonGrader object { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20name)

source : string

The source code of the python script.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20source)

type : "python"

The object type, which is always `python`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20type)

image_tag : optional string

The image tag to use for the python script.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20image_tag)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema))

ScoreModelGrader object { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input : array of object { content , role , type }

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input)

model : string

The model to use for the evaluation.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20name)

type : "score_model"

The object type, which is always `score_model`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20type)

range : optional array of number

The range of the score. Defaults to `[0, 1]`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20range)

sampling_params : optional object { max_completions_tokens , reasoning_effort , seed , 2 more }

The sampling parameters for the model.

max_completions_tokens : optional number

The maximum number of tokens the grader model may generate in its response.

minimum 1

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completions_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema))

StringCheckGrader object { input , name , operation , 2 more }

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input : string

The input text. This may include template strings.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20name)

operation : "eq" or "ne" or "like" or "ilike"

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%200)

"ne"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%201)

"like"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%202)

"ilike"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%203)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation)

reference : string

The reference text. This may include template strings.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "string_check"

The object type, which is always `string_check`.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema))

TextSimilarityGrader object { evaluation_metric , input , name , 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation_metric : "cosine" or "fuzzy_match" or "bleu" or 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

"cosine"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%200)

"fuzzy_match"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%201)

"bleu"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%202)

"gleu"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%203)

"meteor"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%204)

"rouge_1"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%205)

"rouge_2"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%206)

"rouge_3"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%207)

"rouge_4"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%208)

"rouge_5"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%209)

"rouge_l"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%2010)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric)

input : string

The text being graded.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20name)

reference : string

The text being graded against.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "text_similarity"

The type of grader.

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/graders
