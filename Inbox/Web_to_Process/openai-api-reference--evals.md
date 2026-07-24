---
source_url: https://developers.openai.com/api/reference/resources/evals
title: "Evals"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Evals

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Evals

Manage and run evals in the OpenAI platform.

##### [List evals](/api/reference/resources/evals/methods/list)

GET /evals

##### [Create eval](/api/reference/resources/evals/methods/create)

POST /evals

##### [Get an eval](/api/reference/resources/evals/methods/retrieve)

GET /evals/{eval_id}

##### [Update an eval](/api/reference/resources/evals/methods/update)

POST /evals/{eval_id}

##### [Delete an eval](/api/reference/resources/evals/methods/delete)

DELETE /evals/{eval_id}

##### Models Expand Collapse

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

EvalListResponse object { id , created_at , data_source_config , 4 more }

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

- Improve the quality of my chatbot

- See how well my chatbot handles customer support

- Check if o4-mini is better at my usecase than gpt-4o

id : string

Unique identifier for the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the eval was created.

format unixtime

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20schema)

type : "logs"

The type of data source. Always `logs`.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20type)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20metadata)

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

The name of the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "eval"

The object type.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202)

PythonGrader = [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203)

ScoreModelGrader = [ScoreModelGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)) { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204)

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria)

[](#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema))

EvalCreateResponse object { id , created_at , data_source_config , 4 more }

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

- Improve the quality of my chatbot

- See how well my chatbot handles customer support

- Check if o4-mini is better at my usecase than gpt-4o

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

[](#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema))

EvalRetrieveResponse object { id , created_at , data_source_config , 4 more }

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

- Improve the quality of my chatbot

- See how well my chatbot handles customer support

- Check if o4-mini is better at my usecase than gpt-4o

id : string

Unique identifier for the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the eval was created.

format unixtime

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20schema)

type : "logs"

The type of data source. Always `logs`.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20type)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20metadata)

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

The name of the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "eval"

The object type.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20object)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202)

PythonGrader = [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203)

ScoreModelGrader = [ScoreModelGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)) { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204)

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria)

[](#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema))

EvalUpdateResponse object { id , created_at , data_source_config , 4 more }

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

- Improve the quality of my chatbot

- See how well my chatbot handles customer support

- Check if o4-mini is better at my usecase than gpt-4o

id : string

Unique identifier for the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the eval was created.

format unixtime

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20schema)

type : "logs"

The type of data source. Always `logs`.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20type)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201%20%3E%20(property)%20metadata)

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config%20%3E%20(variant)%201)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20data_source_config)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

name : string

The name of the evaluation.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20name)

object : "eval"

The object type.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20object)

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

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%202)

PythonGrader = [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%203)

ScoreModelGrader = [ScoreModelGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)) { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

pass_threshold : optional number

The threshold for the score.

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20pass_threshold)

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria%20%3E%20(items)%20%3E%20(variant)%204)

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema)%20%3E%20(property)%20testing_criteria)

[](#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema))

EvalDeleteResponse object { deleted , eval_id , object }

deleted : boolean

[](#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

eval_id : string

[](#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)%20%3E%20(property)%20eval_id)

object : string

[](#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema))

#### Evals Runs

Manage and run evals in the OpenAI platform.

##### [Get eval runs](/api/reference/resources/evals/subresources/runs/methods/list)

GET /evals/{eval_id}/runs

##### [Create eval run](/api/reference/resources/evals/subresources/runs/methods/create)

POST /evals/{eval_id}/runs

##### [Get an eval run](/api/reference/resources/evals/subresources/runs/methods/retrieve)

GET /evals/{eval_id}/runs/{run_id}

##### [Cancel eval run](/api/reference/resources/evals/subresources/runs/methods/cancel)

POST /evals/{eval_id}/runs/{run_id}

##### [Delete eval run](/api/reference/resources/evals/subresources/runs/methods/delete)

DELETE /evals/{eval_id}/runs/{run_id}

##### Models Expand Collapse

CreateEvalCompletionsRunDataSource object { source , type , input_messages , 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source : object { content , type } or object { id , type } or object { type , created_after , created_before , 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201)

StoredCompletionsRunDataSource object { type , created_after , created_before , 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type : "stored_completions"

The type of source. Always `stored_completions`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type)

created_after : optional number

An optional Unix timestamp to filter items created after this time.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_after)

created_before : optional number

An optional Unix timestamp to filter items created before this time.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_before)

limit : optional number

An optional maximum number of items to return.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20limit)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20metadata)

model : optional string

An optional model to filter by (e.g., ‘gpt-4o’).

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20model)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source)

type : "completions"

The type of run data source. Always `completions`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20type)

input_messages : optional object { template , type } or object { item_reference , type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

TemplateInputMessages object { template , type }

template : array of [EasyInputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content , role , phase , type } or object { content , role , type }

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage object { content , role , phase , type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content : string or [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , , }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputMessageContentList = array of [ResponseInputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

One of the following:

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

ResponseInputImage object { detail , type , file_id , 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

detail : "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"high"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"auto"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

"original"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%203)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail)

type : "input_image"

The type of the input item. Always `input_image`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20type)

file_id : optional string

The ID of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20file_id)

image_url : optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

format uri

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema))

ResponseInputFile object { type , detail , file_data , 4 more }

A file input to the model.

type : "input_file"

The type of the input item. Always `input_file`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20type)

detail : optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

One of the following:

"auto"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail)

file_data : optional string

The content of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_data)

file_id : optional string

The ID of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_id)

file_url : optional string

The URL of the file to be sent to the model.

format uri

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_url)

filename : optional string

The name of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20filename)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role)

phase : optional "commentary" or "final_answer"

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase%20%3E%20(member)%200)

"final_answer"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema))

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

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%200)

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

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203)

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

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template)

type : "template"

The type of input messages. Always `template`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200)

ItemReferenceInputMessages object { item_reference , type }

item_reference : string

A reference to a variable in the `item` namespace. Ie, “item.input_trajectory”

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20item_reference)

type : "item_reference"

The type of input messages. Always `item_reference`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages)

model : optional string

The name of the model to use for generating completions (e.g. “o3-mini”).

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20model)

sampling_params : optional object { max_completion_tokens , reasoning_effort , response_format , 4 more }

max_completion_tokens : optional number

The maximum number of tokens in the generated output.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completion_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

response_format : optional [ResponseFormatText](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type } or [ResponseFormatJSONSchema](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json_schema , type } or [ResponseFormatJSONObject](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONSchema object { json_schema , type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json_schema : object { name , description , schema , strict }

Structured Outputs configuration options, including a JSON Schema.

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20name)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20description)

schema : optional map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20schema)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20strict)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20response_format)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

tools : optional array of [ChatCompletionFunctionTool](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function , type }

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function : [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name , description , parameters , strict }

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema))

CreateEvalJSONLRunDataSource object { source , type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source : object { content , type } or object { id , type }

Determines what populates the `item` namespace in the data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source)

type : "jsonl"

The type of data source. Always `jsonl`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema))

EvalAPIError object { code , message }

An object representing an error response from the Eval API.

code : string

The error code.

[](#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)%20%3E%20(property)%20code)

message : string

The error message.

[](#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)%20%3E%20(property)%20message)

[](#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

RunListResponse object { id , created_at , data_source , 11 more }

A schema representing an evaluation run.

id : string

Unique identifier for the evaluation run.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

Unix timestamp (in seconds) when the evaluation run was created.

format unixtime

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

data_source : [CreateEvalJSONLRunDataSource](/api/reference/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source , type } or [CreateEvalCompletionsRunDataSource](/api/reference/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source , type , input_messages , 2 more } or object { source , type , input_messages , 2 more }

Information about the run’s data source.

One of the following:

CreateEvalJSONLRunDataSource object { source , type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source : object { content , type } or object { id , type }

Determines what populates the `item` namespace in the data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source)

type : "jsonl"

The type of data source. Always `jsonl`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema))

CreateEvalCompletionsRunDataSource object { source , type , input_messages , 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source : object { content , type } or object { id , type } or object { type , created_after , created_before , 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201)

StoredCompletionsRunDataSource object { type , created_after , created_before , 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type : "stored_completions"

The type of source. Always `stored_completions`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type)

created_after : optional number

An optional Unix timestamp to filter items created after this time.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_after)

created_before : optional number

An optional Unix timestamp to filter items created before this time.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_before)

limit : optional number

An optional maximum number of items to return.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20limit)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20metadata)

model : optional string

An optional model to filter by (e.g., ‘gpt-4o’).

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20model)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20source)

type : "completions"

The type of run data source. Always `completions`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20type)

input_messages : optional object { template , type } or object { item_reference , type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

TemplateInputMessages object { template , type }

template : array of [EasyInputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content , role , phase , type } or object { content , role , type }

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage object { content , role , phase , type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content : string or [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , , }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputMessageContentList = array of [ResponseInputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

One of the following:

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

ResponseInputImage object { detail , type , file_id , 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

detail : "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"high"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"auto"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

"original"

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%203)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20detail)

type : "input_image"

The type of the input item. Always `input_image`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20type)

file_id : optional string

The ID of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20file_id)

image_url : optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

format uri

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20image_url)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema))

ResponseInputFile object { type , detail , file_data , 4 more }

A file input to the model.

type : "input_file"

The type of the input item. Always `input_file`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20type)

detail : optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

One of the following:

"auto"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%200)

"low"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%201)

"high"

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail%20%3E%20(member)%202)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20detail)

file_data : optional string

The content of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_data)

file_id : optional string

The ID of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_id)

file_url : optional string

The URL of the file to be sent to the model.

format uri

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20file_url)

filename : optional string

The name of the file to be sent to the model.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20filename)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20role)

phase : optional "commentary" or "final_answer"

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase%20%3E%20(member)%200)

"final_answer"

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase%20%3E%20(member)%201)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20phase)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema))

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

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%200)

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

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203)

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

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template)

type : "template"

The type of input messages. Always `template`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%200)

ItemReferenceInputMessages object { item_reference , type }

item_reference : string

A reference to a variable in the `item` namespace. Ie, “item.input_trajectory”

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20item_reference)

type : "item_reference"

The type of input messages. Always `item_reference`.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages%20%3E%20(variant)%201)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20input_messages)

model : optional string

The name of the model to use for generating completions (e.g. “o3-mini”).

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20model)

sampling_params : optional object { max_completion_tokens , reasoning_effort , response_format , 4 more }

max_completion_tokens : optional number

The maximum number of tokens in the generated output.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completion_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

response_format : optional [ResponseFormatText](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type } or [ResponseFormatJSONSchema](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json_schema , type } or [ResponseFormatJSONObject](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type : "text"

The type of response format being defined. Always `text`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema))

ResponseFormatJSONSchema object { json_schema , type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json_schema : object { name , description , schema , strict }

Structured Outputs configuration options, including a JSON Schema.

name : string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20name)

description : optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20description)

schema : optional map [ unknown ]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20schema)

strict : optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema%20%3E%20(property)%20strict)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20json_schema)

type : "json_schema"

The type of response format being defined. Always `json_schema`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema))

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type : "json_object"

The type of response format being defined. Always `json_object`.

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema))

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20response_format)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

tools : optional array of [ChatCompletionFunctionTool](/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function , type }

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function : [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name , description , parameters , strict }

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of the tool. Currently, only `function` is supported.

[](#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20tools)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)%20%3E%20(property)%20sampling_params)

[](#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema))

ResponsesRunDataSource object { source , type , input_messages , 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source : object { content , type } or object { id , type } or object { type , created_after , created_before , 8 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

EvalJSONLFileContentSource object { content , type }

content : array of object { item , sample }

The content of the jsonl file.

item : map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20item)

sample : optional map [ unknown ]

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20sample)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20content)

type : "file_content"

The type of jsonl source. Always `file_content`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%200)

EvalJSONLFileIDSource object { id , type }

id : string

The identifier of the file.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20id)

type : "file_id"

The type of jsonl source. Always `file_id`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%201)

EvalResponsesSource object { type , created_after , created_before , 8 more }

A EvalResponsesSource object describing a run data source configuration.

type : "responses"

The type of run data source. Always `responses`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type)

created_after : optional number

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum 0

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_after)

created_before : optional number

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum 0

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20created_before)

instructions_search : optional string

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20instructions_search)

metadata : optional unknown

Metadata filter for the responses. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20metadata)

model : optional string

The name of the model to find responses for. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20model)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20reasoning_effort)

temperature : optional number

Sampling temperature. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20temperature)

tools : optional array of string

List of tool names. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20tools)

top_p : optional number

Nucleus sampling parameter. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20top_p)

users : optional array of string

List of user identifiers. This is a query parameter used to select responses.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20users)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source%20%3E%20(variant)%202)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20source)

type : "responses"

The type of run data source. Always `responses`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20type)

input_messages : optional object { template , type } or object { item_reference , type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

InputMessagesTemplate object { template , type }

template : array of object { content , role } or object { content , role , type }

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

ChatMessage object { content , role }

content : string

The content of the message.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20content)

role : string

The role of the message (e.g. “system”, “assistant”, “user”).

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20role)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%200)

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

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%200)

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

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)%20%3E%20(property)%20data_source%20%3E%20(variant)%202%20%3E%20(property)%20input_messages%20%3E%20(variant)%200%20%3E%20(property)%20template%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20content%20%3E%20(variant)%203)

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

[](#(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/evals
