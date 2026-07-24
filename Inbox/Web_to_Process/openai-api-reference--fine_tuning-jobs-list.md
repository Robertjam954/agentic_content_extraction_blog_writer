---
source_url: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/jobs/methods/list
title: "List fine-tuning jobs"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List fine-tuning jobs

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

[Jobs](/api/reference/resources/fine_tuning/subresources/jobs)

# List fine-tuning jobs

GET /fine_tuning/jobs

List your organization’s fine-tuning jobs

##### Q uery Parameters Expand Collapse

after : optional string

Identifier for the last job from the previous pagination request.

[](#(resource)%20fine_tuning.jobs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

Number of fine-tuning jobs to retrieve.

[](#(resource)%20fine_tuning.jobs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

metadata : optional map [ string ]

Optional metadata filter. To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to indicate no metadata.

[](#(resource)%20fine_tuning.jobs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20metadata%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [FineTuningJob](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) { id , created_at , error , 16 more }

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

project : string

The name of the project that the new run will be created under.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20wandb%20%2B%20(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20project)

entity : optional string

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20wandb%20%2B%20(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20entity)

name : optional string

A display name to set for the run. If not set, we will use the Job ID as the name.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20wandb%20%2B%20(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20name)

tags : optional array of string

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)%20%3E%20(property)%20wandb%20%2B%20(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)%20%3E%20(property)%20tags)

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

hyperparameters : optional [DpoHyperparameters](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)) { batch_size , beta , learning_rate_multiplier , n_epochs }

The hyperparameters used for the DPO fine-tuning job.

batch_size : optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size)

beta : optional "auto" or number

The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20beta%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20beta%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20beta)

learning_rate_multiplier : optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier)

n_epochs : optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20dpo%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20dpo)

reinforcement : optional [ReinforcementMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)) { grader , hyperparameters }

Configuration for the reinforcement fine-tuning method.

grader : [StringCheckGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input , name , operation , 2 more } or [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more } or [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag } or 2 more

The grader used for the fine-tuning job.

One of the following:

StringCheckGrader object { input , name , operation , 2 more }

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input : string

The input text. This may include template strings.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20name)

operation : "eq" or "ne" or "like" or "ilike"

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%200)

"ne"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%201)

"like"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%202)

"ilike"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%203)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation)

reference : string

The reference text. This may include template strings.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "string_check"

The object type, which is always `string_check`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema))

TextSimilarityGrader object { evaluation_metric , input , name , 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation_metric : "cosine" or "fuzzy_match" or "bleu" or 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

"cosine"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%200)

"fuzzy_match"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%201)

"bleu"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%202)

"gleu"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%203)

"meteor"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%204)

"rouge_1"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%205)

"rouge_2"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%206)

"rouge_3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%207)

"rouge_4"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%208)

"rouge_5"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%209)

"rouge_l"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%2010)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric)

input : string

The text being graded.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20name)

reference : string

The text being graded against.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "text_similarity"

The type of grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema))

PythonGrader object { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20name)

source : string

The source code of the python script.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20source)

type : "python"

The object type, which is always `python`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20type)

image_tag : optional string

The image tag to use for the python script.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20image_tag)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema))

ScoreModelGrader object { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input : array of object { content , role , type }

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input)

model : string

The model to use for the evaluation.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20name)

type : "score_model"

The object type, which is always `score_model`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20type)

range : optional array of number

The range of the score. Defaults to `[0, 1]`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20range)

sampling_params : optional object { max_completions_tokens , reasoning_effort , seed , 2 more }

The sampling parameters for the model.

max_completions_tokens : optional number

The maximum number of tokens the grader model may generate in its response.

minimum 1

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completions_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

One of the following:

"none"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"minimal"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"low"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"medium"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"high"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

"xhigh"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%205)

"max"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%206)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema))

MultiGrader object { calculate_output , graders , name , type }

A MultiGrader object combines the output of multiple graders to produce a single score.

calculate_output : string

A formula to calculate the output based on grader results.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20calculate_output)

graders : [StringCheckGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input , name , operation , 2 more } or [TextSimilarityGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation_metric , input , name , 2 more } or [PythonGrader](/api/reference/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name , source , type , image_tag } or 2 more

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

One of the following:

StringCheckGrader object { input , name , operation , 2 more }

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input : string

The input text. This may include template strings.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20name)

operation : "eq" or "ne" or "like" or "ilike"

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%200)

"ne"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%201)

"like"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%202)

"ilike"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation%20%3E%20(member)%203)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20operation)

reference : string

The reference text. This may include template strings.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "string_check"

The object type, which is always `string_check`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema))

TextSimilarityGrader object { evaluation_metric , input , name , 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation_metric : "cosine" or "fuzzy_match" or "bleu" or 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

"cosine"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%200)

"fuzzy_match"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%201)

"bleu"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%202)

"gleu"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%203)

"meteor"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%204)

"rouge_1"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%205)

"rouge_2"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%206)

"rouge_3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%207)

"rouge_4"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%208)

"rouge_5"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%209)

"rouge_l"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric%20%3E%20(member)%2010)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20evaluation_metric)

input : string

The text being graded.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20input)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20name)

reference : string

The text being graded against.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20reference)

type : "text_similarity"

The type of grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema))

PythonGrader object { name , source , type , image_tag }

A PythonGrader object that runs a python script on the input.

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20name)

source : string

The source code of the python script.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20source)

type : "python"

The object type, which is always `python`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20type)

image_tag : optional string

The image tag to use for the python script.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)%20%3E%20(property)%20image_tag)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema))

ScoreModelGrader object { input , model , name , 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input : array of object { content , role , type }

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20input)

model : string

The model to use for the evaluation.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20name)

type : "score_model"

The object type, which is always `score_model`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20type)

range : optional array of number

The range of the score. Defaults to `[0, 1]`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20range)

sampling_params : optional object { max_completions_tokens , reasoning_effort , seed , 2 more }

The sampling parameters for the model.

max_completions_tokens : optional number

The maximum number of tokens the grader model may generate in its response.

minimum 1

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20max_completions_tokens)

reasoning_effort : optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

One of the following:

"none"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%200)

"minimal"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%201)

"low"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%202)

"medium"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%203)

"high"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%204)

"xhigh"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%205)

"max"

[](#(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort%20%2B%20(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)%20%3E%20(member)%206)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20reasoning_effort)

seed : optional number

A seed value to initialize the randomness, during sampling.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20seed)

temperature : optional number

A higher temperature increases randomness in the outputs.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20temperature)

top_p : optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params%20%3E%20(property)%20top_p)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema)%20%3E%20(property)%20sampling_params)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20score_model_grader%20%3E%20(schema))

LabelModelGrader object { input , labels , model , 3 more }

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input : array of object { content , role , type }

content : string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

GraderInputs = array of string or [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text , type , prompt_cache_breakpoint } or object { text , type } or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

TextInput = string

A text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200)

ResponseInputText object { text , type , prompt_cache_breakpoint }

A text input to the model.

text : string

The text input to the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20text)

type : "input_text"

The type of the input item. Always `input_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20type)

prompt_cache_breakpoint : optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode : "explicit"

The breakpoint mode. Always `explicit`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint%20%3E%20(property)%20mode)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)%20%3E%20(property)%20prompt_cache_breakpoint)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema))

OutputText object { text , type }

A text output from the model.

text : string

The text output from the model.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20text)

type : "output_text"

The type of the output text. Always `output_text`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%202)

InputImage object { image_url , type , detail }

An image input block used within EvalItem content arrays.

image_url : string

The URL of the image input.

format uri

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20image_url)

type : "input_image"

The type of the image input. Always `input_image`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type)

detail : optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20detail)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%203)

ResponseInputAudio object { input_audio , type }

An audio input to the model.

input_audio : object { data , format }

data : string

Base64-encoded audio data.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20data)

format : "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%200)

"wav"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format%20%3E%20(member)%201)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio%20%3E%20(property)%20format)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20input_audio)

type : "input_audio"

The type of the input item. Always `input_audio`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20responses%20%3E%20(model)%20response_input_audio%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20grader_inputs%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20content)

role : "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%200)

"assistant"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%201)

"system"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%202)

"developer"

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role%20%3E%20(member)%203)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20role)

type : optional "message"

The type of the message input. Always `message`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20input)

labels : array of string

The labels to assign to each item in the evaluation.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20labels)

model : string

The model to use for the evaluation. Must support structured outputs.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20model)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20name)

passing_labels : array of string

The labels that indicate a passing result. Must be a subset of labels.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20passing_labels)

type : "label_model"

The object type, which is always `label_model`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20graders)

name : string

The name of the grader.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20name)

type : "multi"

The object type, which is always `multi`.

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20graders.grader_models%20%3E%20(model)%20multi_grader%20%3E%20(schema))

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20grader)

hyperparameters : optional [ReinforcementHyperparameters](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)) { batch_size , compute_multiplier , eval_interval , 4 more }

The hyperparameters used for the reinforcement fine-tuning job.

batch_size : optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size)

compute_multiplier : optional "auto" or number

Multiplier on amount of compute used for exploring search space during training.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20compute_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20compute_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20compute_multiplier)

eval_interval : optional "auto" or number

The number of training steps between evaluation runs.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_interval%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_interval%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_interval)

eval_samples : optional "auto" or number

Number of evaluation samples to generate per training step.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_samples%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_samples%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20eval_samples)

learning_rate_multiplier : optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier)

n_epochs : optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs)

reasoning_effort : optional "default" or "low" or "medium" or "high"

Level of reasoning effort.

One of the following:

"default"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%200)

"low"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%201)

"medium"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%202)

"high"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort%20%3E%20(member)%203)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20reasoning_effort)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20reinforcement)

supervised : optional [SupervisedMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)) { hyperparameters }

Configuration for the supervised fine-tuning method.

hyperparameters : optional [SupervisedHyperparameters](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)) { batch_size , learning_rate_multiplier , n_epochs }

The hyperparameters used for the fine-tuning job.

batch_size : optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20batch_size)

learning_rate_multiplier : optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20learning_rate_multiplier)

n_epochs : optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

"auto"

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%200)

number

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs%20%3E%20(variant)%201)

[](#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)%20%3E%20(property)%20n_epochs)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20supervised%20%2B%20(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)%20%3E%20(property)%20hyperparameters)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(property)%20supervised)

[](#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)%20%3E%20(property)%20method)

[](#(resource)%20fine_tuning.jobs%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20fine_tuning.jobs%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20fine_tuning.jobs%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

### List fine-tuning jobs

```
curl https://api.openai.com/v1/fine_tuning/jobs?limit=2&metadata[key]=value \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"object": "list",
"data": [
{
"object": "fine_tuning.job",
"id": "ftjob-abc123",
"model": "gpt-4o-mini-2024-07-18",
"created_at": 1721764800,
"fine_tuned_model": null,
"organization_id": "org-123",
"result_files": [],
"status": "queued",
"validation_file": null,
"training_file": "file-abc123",
"metadata": {
"key": "value"
}
},
{ ... },
{ ... }
], "has_more": true
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "fine_tuning.job",
"id": "ftjob-abc123",
"model": "gpt-4o-mini-2024-07-18",
"created_at": 1721764800,
"fine_tuned_model": null,
"organization_id": "org-123",
"result_files": [],
"status": "queued",
"validation_file": null,
"training_file": "file-abc123",
"metadata": {
"key": "value"
}
},
{ ... },
{ ... }
], "has_more": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/jobs/methods/list
