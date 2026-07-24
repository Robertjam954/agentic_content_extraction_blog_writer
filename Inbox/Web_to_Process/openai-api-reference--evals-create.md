---
source_url: https://developers.openai.com/api/reference/resources/evals/methods/create
title: "Create eval"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create eval

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Evals](/api/reference/resources/evals)

# Create eval

POST /evals

Create the structure of an evaluation that can be used to test a model’s performance.
An evaluation is a set of testing criteria and the config for a data source, which dictates the schema of the data used in the evaluation. After creating an evaluation, you can run it on different models and model parameters. We support several types of graders and datasources.
For more information, see the [Evals guide](/docs/guides/evals).

##### Body Parameters JSON Expand Collapse

data_source_config : object { item_schema , type , include_sample_schema } or object { type , metadata } or object { type , metadata }

The configuration for the data source used for the evaluation runs. Dictates the schema of the data used in the evaluation.

One of the following:

CustomDataSourceConfig object { item_schema , type , include_sample_schema }

A CustomDataSourceConfig object that defines the schema for the data source used for the evaluation runs.
This schema is used to define the shape of the data that will be:

- Used to define your testing criteria and

- What data is required when creating a run

item_schema : map [ unknown ]

The json schema for each row in the data source.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20item_schema)

type : "custom"

The type of data source. Always `custom`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type)

include_sample_schema : optional boolean

Whether the eval should expect you to populate the sample namespace (ie, by generating responses off of your data source)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20include_sample_schema)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%200)

LogsDataSourceConfig object { type , metadata }

A data source config which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.

type : "logs"

The type of data source. Always `logs`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type)

metadata : optional map [ unknown ]

Metadata filters for the logs data source.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20metadata)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%201)

StoredCompletionsDataSourceConfig object { type , metadata }

Deprecated in favor of LogsDataSourceConfig.

type : "stored_completions"

The type of data source. Always `stored_completions`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20type)

metadata : optional map [ unknown ]

Metadata filters for the stored completions data source.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20metadata)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema)%20%3E%20(variant)%202)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20data_source_config%20%3E%20(schema))

testing_criteria : array of object { input , labels , model , 3 more } or [StringCheckGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input , name , operation , 2 more } or [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more } or 2 more

A list of graders for all eval runs in this group. Graders can reference variables in the data source using double curly braces notation, like `{{item.variable_name}}`. To reference the model’s output, use the `sample` namespace (ie, `{{sample.output_text}}`).

One of the following:

LabelModelGrader object { input , labels , model , 3 more }

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input : array of object { content , role } or object { content , role , type }

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

SimpleInputMessage object { content , role }

content : string

The content of the message.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20content)

role : string

The role of the message (e.g. “system”, “assistant”, “user”).

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20role)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%200)

EvalMessageObject object { content , role , type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%200)

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

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203)

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

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20input)

labels : array of string

The labels to classify to each item in the evaluation.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20labels)

model : string

The model to use for the evaluation. Must support structured outputs.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name)

passing_labels : array of string

The labels that indicate a passing result. Must be a subset of labels.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20passing_labels)

type : "label_model"

The object type, which is always `label_model`.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

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

TextSimilarityGrader = [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

pass_threshold : number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

PythonGrader = [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ScoreModelGrader = [ScoreModelGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)) { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%204)

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20testing_criteria%20%3E%20(schema))

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20metadata%20%3E%20(schema))

name : optional string

The name of the evaluation.

[](#(resource)%20evals%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20name%20%3E%20(schema))

##### Returns Expand Collapse

id : string

Unique identifier for the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the eval was created.

format unixtime

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

data_source_config : [EvalCustomDataSourceConfig](/api/reference/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_custom_data_source_config%20%3E%20(schema)) { schema , type } or object { schema , type , metadata } or [EvalStoredCompletionsDataSourceConfig](/api/reference/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_stored_completions_data_source_config%20%3E%20(schema)) { schema , type , metadata }

Configuration of data sources used in runs of the evaluation.

One of the following:

EvalCustomDataSourceConfig object { schema , type }

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

- Used to define your testing criteria and

- What data is required when creating a run

schema : map [ unknown ]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20evals%20%3E%20(model)%20eval_custom_data_source_config%20%3E%20(schema)%20%3E%20(property)%20schema)

type : "custom"

The type of data source. Always `custom`.

[](#(resource)%20evals%20%3E%20(model)%20eval_custom_data_source_config%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals%20%3E%20(model)%20eval_custom_data_source_config%20%3E%20(schema))

LogsDataSourceConfig object { schema , type , metadata }

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

schema : map [ unknown ]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20schema)

type : "logs"

The type of data source. Always `logs`.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20type)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20metadata)

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201)

EvalStoredCompletionsDataSourceConfig object { schema , type , metadata }

Deprecated in favor of LogsDataSourceConfig.

schema : map [ unknown ]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20evals%20%3E%20(model)%20eval_stored_completions_data_source_config%20%3E%20(schema)%20%3E%20(property)%20schema)

type : "stored_completions"

The type of data source. Always `stored_completions`.

[](#(resource)%20evals%20%3E%20(model)%20eval_stored_completions_data_source_config%20%3E%20(schema)%20%3E%20(property)%20type)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_stored_completions_data_source_config%20%3E%20(schema)%20%3E%20(property)%20metadata)

[](#(resource)%20evals%20%3E%20(model)%20eval_stored_completions_data_source_config%20%3E%20(schema))

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

The name of the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "eval"

The object type.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

testing_criteria : array of [LabelModelGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)) { input , labels , model , 3 more } or [StringCheckGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input , name , operation , 2 more } or [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more } or 2 more

A list of testing criteria.

One of the following:

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

TextSimilarityGrader = [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

pass_threshold : number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202)

PythonGrader = [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203)

ScoreModelGrader = [ScoreModelGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)) { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204)

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria)

### Create eval

```
curl https://api.openai.com/v1/evals \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
"name": "Sentiment",
"data_source_config": {
"type": "stored_completions",
"metadata": {
"usecase": "chatbot"
}
},
"testing_criteria": [
{
"type": "label_model",
"model": "o3-mini",
"input": [
{
"role": "developer",
"content": "Classify the sentiment of the following statement as one of 'positive', 'neutral', or 'negative'"
},
{
"role": "user",
"content": "Statement: {{item.input}}"
}
],
"passing_labels": [
"positive"
],
"labels": [
"positive",
"neutral",
"negative"
],
"name": "Example label grader"
}
]
}'
```

```
{
"object": "eval",
"id": "eval_67b7fa9a81a88190ab4aa417e397ea21",
"data_source_config": {
"type": "stored_completions",
"metadata": {
"usecase": "chatbot"
},
"schema": {
"type": "object",
"properties": {
"item": {
"type": "object"
},
"sample": {
"type": "object"
}
},
"required": [
"item",
"sample"
]
},
"testing_criteria": [
{
"name": "Example label grader",
"type": "label_model",
"model": "o3-mini",
"input": [
{
"type": "message",
"role": "developer",
"content": {
"type": "input_text",
"text": "Classify the sentiment of the following statement as one of positive, neutral, or negative"
}
},
{
"type": "message",
"role": "user",
"content": {
"type": "input_text",
"text": "Statement: {{item.input}}"
}
}
],
"passing_labels": [
"positive"
],
"labels": [
"positive",
"neutral",
"negative"
]
}
],
"name": "Sentiment",
"created_at": 1740110490,
"metadata": {
"description": "An eval for sentiment analysis"
}
}
```

##### Returns Examples

```
{
"object": "eval",
"id": "eval_67b7fa9a81a88190ab4aa417e397ea21",
"data_source_config": {
"type": "stored_completions",
"metadata": {
"usecase": "chatbot"
},
"schema": {
"type": "object",
"properties": {
"item": {
"type": "object"
},
"sample": {
"type": "object"
}
},
"required": [
"item",
"sample"
]
},
"testing_criteria": [
{
"name": "Example label grader",
"type": "label_model",
"model": "o3-mini",
"input": [
{
"type": "message",
"role": "developer",
"content": {
"type": "input_text",
"text": "Classify the sentiment of the following statement as one of positive, neutral, or negative"
}
},
{
"type": "message",
"role": "user",
"content": {
"type": "input_text",
"text": "Statement: {{item.input}}"
}
}
],
"passing_labels": [
"positive"
],
"labels": [
"positive",
"neutral",
"negative"
]
}
],
"name": "Sentiment",
"created_at": 1740110490,
"metadata": {
"description": "An eval for sentiment analysis"
}
}
```

---
Source: https://developers.openai.com/api/reference/resources/evals/methods/create
