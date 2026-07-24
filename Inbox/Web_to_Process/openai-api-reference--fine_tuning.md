---
source_url: https://developers.openai.com/api/reference/resources/fine_tuning
title: "Fine Tuning"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Fine Tuning

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Fine Tuning

#### Fine Tuning Methods

##### Models Expand Collapse

DpoHyperparameters object { batch_size , beta , learning_rate_multiplier , n_epochs }

The hyperparameters used for the DPO fine-tuning job.

batch_size : optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size)

beta : optional "auto" or number

The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20beta%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20beta%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20beta)

learning_rate_multiplier : optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier)

n_epochs : optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema))

DpoMethod object { hyperparameters }

Configuration for the DPO fine-tuning method.

hyperparameters : optional [DpoHyperparameters](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)) { batch_size , beta , learning_rate_multiplier , n_epochs }

The hyperparameters used for the DPO fine-tuning job.

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema))

ReinforcementHyperparameters object { batch_size , compute_multiplier , eval_interval , 4 more }

The hyperparameters used for the reinforcement fine-tuning job.

batch_size : optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size)

compute_multiplier : optional "auto" or number

Multiplier on amount of compute used for exploring search space during training.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20compute_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20compute_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20compute_multiplier)

eval_interval : optional "auto" or number

The number of training steps between evaluation runs.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_interval%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_interval%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_interval)

eval_samples : optional "auto" or number

Number of evaluation samples to generate per training step.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_samples%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_samples%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_samples)

learning_rate_multiplier : optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier)

n_epochs : optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs)

reasoning_effort : optional "default" or "low" or "medium" or "high"

Level of reasoning effort.

One of the following:

"default"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%200)

"low"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%201)

"medium"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%202)

"high"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%203)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema))

ReinforcementMethod object { grader , hyperparameters }

Configuration for the reinforcement fine-tuning method.

grader : [StringCheckGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input , name , operation , 2 more } or [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more } or [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag } or 2 more

The grader used for the fine-tuning job.

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

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20grader)

hyperparameters : optional [ReinforcementHyperparameters](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)) { batch_size , compute_multiplier , eval_interval , 4 more }

The hyperparameters used for the reinforcement fine-tuning job.

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema))

SupervisedHyperparameters object { batch_size , learning_rate_multiplier , n_epochs }

The hyperparameters used for the fine-tuning job.

batch_size : optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size)

learning_rate_multiplier : optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier)

n_epochs : optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema))

SupervisedMethod object { hyperparameters }

Configuration for the supervised fine-tuning method.

hyperparameters : optional [SupervisedHyperparameters](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)) { batch_size , learning_rate_multiplier , n_epochs }

The hyperparameters used for the fine-tuning job.

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema))

#### Fine Tuning Jobs

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Create fine-tuning job](/api/reference/resources/fine_tuning/subresources/jobs/methods/create)

POST /fine_tuning/jobs

##### [List fine-tuning jobs](/api/reference/resources/fine_tuning/subresources/jobs/methods/list)

GET /fine_tuning/jobs

##### [Retrieve fine-tuning job](/api/reference/resources/fine_tuning/subresources/jobs/methods/retrieve)

GET /fine_tuning/jobs/{fine_tuning_job_id}

##### [List fine-tuning events](/api/reference/resources/fine_tuning/subresources/jobs/methods/list_events)

GET /fine_tuning/jobs/{fine_tuning_job_id}/events

##### [Cancel fine-tuning](/api/reference/resources/fine_tuning/subresources/jobs/methods/cancel)

POST /fine_tuning/jobs/{fine_tuning_job_id}/cancel

##### [Pause fine-tuning](/api/reference/resources/fine_tuning/subresources/jobs/methods/pause)

POST /fine_tuning/jobs/{fine_tuning_job_id}/pause

##### [Resume fine-tuning](/api/reference/resources/fine_tuning/subresources/jobs/methods/resume)

POST /fine_tuning/jobs/{fine_tuning_job_id}/resume

##### Models Expand Collapse

FineTuningJob object { id , created_at , error , 16 more }

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

id : string

The object identifier, which can be referenced in the API endpoints.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the fine-tuning job was created.

format unixtime

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20created_at)

error : object { code , message , param }

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

code : string

A machine-readable error code.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20code)

message : string

A human-readable error message.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20message)

param : string

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20param)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20error)

fine_tuned_model : string

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20fine_tuned_model)

finished_at : number

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

format unixtime

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20finished_at)

hyperparameters : object { batch_size , learning_rate_multiplier , n_epochs }

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

batch_size : optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

"auto"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20batch_size%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20batch_size%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20batch_size)

learning_rate_multiplier : optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

"auto"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20learning_rate_multiplier)

n_epochs : optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

"auto"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20n_epochs%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20n_epochs%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%3E%20(property)%20n_epochs)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20hyperparameters)

model : string

The base model that is being fine-tuned.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20model)

object : "fine_tuning.job"

The object type, which is always “fine_tuning.job”.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20object)

organization_id : string

The organization that owns the fine-tuning job.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20organization_id)

result_files : array of string

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents).

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20result_files)

seed : number

The seed used for the fine-tuning job.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20seed)

status : "validating_files" or "queued" or "running" or 3 more

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

"validating_files"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"queued"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"running"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"succeeded"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

"failed"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204)

"cancelled"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20status)

trained_tokens : number

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20trained_tokens)

training_file : string

The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents).

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20training_file)

validation_file : string

The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents).

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20validation_file)

estimated_finish : optional number

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

format unixtime

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20estimated_finish)

integrations : optional array of [FineTuningJobWandbIntegrationObject](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)) { type , wandb }

A list of integrations to enable for this fine-tuning job.

type : "wandb"

The type of the integration being enabled for the fine-tuning job

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20type)

wandb : [FineTuningJobWandbIntegration](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) { project , entity , name , tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20wandb)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20integrations)

metadata : optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20metadata)

method : optional object { type , dpo , reinforcement , supervised }

The method used for fine-tuning.

type : "supervised" or "dpo" or "reinforcement"

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

"supervised"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20type%20%3E%20(member)%200)

"dpo"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20type%20%3E%20(member)%201)

"reinforcement"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20type%20%3E%20(member)%202)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20type)

dpo : optional [DpoMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)) { hyperparameters }

Configuration for the DPO fine-tuning method.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20dpo)

reinforcement : optional [ReinforcementMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)) { grader , hyperparameters }

Configuration for the reinforcement fine-tuning method.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement)

supervised : optional [SupervisedMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)) { hyperparameters }

Configuration for the supervised fine-tuning method.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20supervised)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))

FineTuningJobEvent object { id , created_at , level , 4 more }

Fine-tuning job event object

id : string

The object identifier.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the fine-tuning job was created.

format unixtime

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20created_at)

level : "info" or "warn" or "error"

The log level of the event.

One of the following:

"info"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20level%20%3E%20(member)%200)

"warn"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20level%20%3E%20(member)%201)

"error"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20level%20%3E%20(member)%202)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20level)

message : string

The message of the event.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20message)

object : "fine_tuning.job.event"

The object type, which is always “fine_tuning.job.event”.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20object)

data : optional unknown

The data associated with the event.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20data)

type : optional "message" or "metrics"

The type of event.

One of the following:

"message"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"metrics"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema))

FineTuningJobWandbIntegration object { project , entity , name , tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

project : string

The name of the project that the new run will be created under.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20project)

entity : optional string

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20entity)

name : optional string

A display name to set for the run. If not set, we will use the Job ID as the name.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20name)

tags : optional array of string

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20tags)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema))

FineTuningJobWandbIntegrationObject object { type , wandb }

type : "wandb"

The type of the integration being enabled for the fine-tuning job

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20type)

wandb : [FineTuningJobWandbIntegration](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) { project , entity , name , tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20wandb)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema))

#### Fine Tuning Jobs Checkpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

GET /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints

##### Models Expand Collapse

FineTuningJobCheckpoint object { id , created_at , fine_tuned_model_checkpoint , 4 more }

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

id : string

The checkpoint identifier, which can be referenced in the API endpoints.

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the checkpoint was created.

format unixtime

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20created_at)

fine_tuned_model_checkpoint : string

The name of the fine-tuned checkpoint model that is created.

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20fine_tuned_model_checkpoint)

fine_tuning_job_id : string

The name of the fine-tuning job that this checkpoint was created from.

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20fine_tuning_job_id)

metrics : object { full_valid_loss , full_valid_mean_token_accuracy , step , 4 more }

Metrics at the step number during the fine-tuning job.

full_valid_loss : optional number

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics%20%3E%20(property)%20full_valid_loss)

full_valid_mean_token_accuracy : optional number

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics%20%3E%20(property)%20full_valid_mean_token_accuracy)

step : optional number

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics%20%3E%20(property)%20step)

train_loss : optional number

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics%20%3E%20(property)%20train_loss)

train_mean_token_accuracy : optional number

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics%20%3E%20(property)%20train_mean_token_accuracy)

valid_loss : optional number

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics%20%3E%20(property)%20valid_loss)

valid_mean_token_accuracy : optional number

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics%20%3E%20(property)%20valid_mean_token_accuracy)

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20metrics)

object : "fine_tuning.job.checkpoint"

The object type, which is always “fine_tuning.job.checkpoint”.

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20object)

step_number : number

The step number that the checkpoint was created at.

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)%20%3E%20(property)%20step_number)

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema))

#### Fine Tuning Checkpoints

#### Fine Tuning Checkpoints Permissions

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List checkpoint permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve)

Deprecated

GET /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions

##### [List checkpoint permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list)

GET /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions

##### [Create checkpoint permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create)

POST /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions

##### [Delete checkpoint permission](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete)

DELETE /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}

##### Models Expand Collapse

PermissionRetrieveResponse object { data , has_more , object , 2 more }

data : array of object { id , created_at , object , project_id }

id : string

The permission identifier, which can be referenced in the API endpoints.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the permission was created.

format unixtime

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20created_at)

object : "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20object)

project_id : string

The project identifier that the permission is for.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20project_id)

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)%20%3E%20(property)%20last_id)

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema))

PermissionListResponse object { id , created_at , object , project_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id : string

The permission identifier, which can be referenced in the API endpoints.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the permission was created.

format unixtime

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)%20%3E%20(property)%20object)

project_id : string

The project identifier that the permission is for.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)%20%3E%20(property)%20project_id)

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema))

PermissionCreateResponse object { id , created_at , object , project_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id : string

The permission identifier, which can be referenced in the API endpoints.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

created_at : number

The Unix timestamp (in seconds) for when the permission was created.

format unixtime

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at)

object : "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20object)

project_id : string

The project identifier that the permission is for.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)%20%3E%20(property)%20project_id)

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema))

PermissionDeleteResponse object { id , deleted , object }

id : string

The ID of the fine-tuned model checkpoint permission that was deleted.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)%20%3E%20(property)%20id)

deleted : boolean

Whether the fine-tuned model checkpoint permission was successfully deleted.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted)

object : "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema))

#### Fine Tuning Alpha

#### Fine Tuning Alpha Graders

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Run grader](/api/reference/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run)

POST /fine_tuning/alpha/graders/run

##### [Validate grader](/api/reference/resources/fine_tuning/subresources/alpha/subresources/graders/methods/validate)

POST /fine_tuning/alpha/graders/validate

##### Models Expand Collapse

GraderRunResponse object { metadata , model_grader_token_usage_per_model , reward , sub_rewards }

metadata : object { errors , execution_time , name , 4 more }

errors : object { formula_parse_error , invalid_variable_error , model_grader_parse_error , 11 more }

formula_parse_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20formula_parse_error)

invalid_variable_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20invalid_variable_error)

model_grader_parse_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20model_grader_parse_error)

model_grader_refusal_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20model_grader_refusal_error)

model_grader_server_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20model_grader_server_error)

model_grader_server_error_details : string

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20model_grader_server_error_details)

other_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20other_error)

python_grader_runtime_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20python_grader_runtime_error)

python_grader_runtime_error_details : string

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20python_grader_runtime_error_details)

python_grader_server_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20python_grader_server_error)

python_grader_server_error_type : string

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20python_grader_server_error_type)

sample_parse_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20sample_parse_error)

truncated_observation_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20truncated_observation_error)

unresponsive_reward_error : boolean

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors%20%3E%20(property)%20unresponsive_reward_error)

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20errors)

execution_time : number

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20execution_time)

name : string

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20name)

sampled_model_name : string

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20sampled_model_name)

scores : map [ unknown ]

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20scores)

token_usage : number

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20token_usage)

type : string

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20metadata)

model_grader_token_usage_per_model : map [ unknown ]

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20model_grader_token_usage_per_model)

reward : number

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20reward)

sub_rewards : map [ unknown ]

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)%20%3E%20(property)%20sub_rewards)

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema))

GraderValidateResponse object { grader }

grader : optional [StringCheckGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input , name , operation , 2 more } or [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more } or [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag } or 2 more

The grader used for the fine-tuning job.

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

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_validate_response%20%3E%20(schema)%20%3E%20(property)%20grader)

[](#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_validate_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/fine_tuning
