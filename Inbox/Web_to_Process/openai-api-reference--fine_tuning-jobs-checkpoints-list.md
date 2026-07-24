---
source_url: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list
title: "List fine-tuning checkpoints"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# List fine-tuning checkpoints

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

[Jobs](/api/reference/resources/fine_tuning/subresources/jobs)

[Checkpoints](/api/reference/resources/fine_tuning/subresources/jobs/subresources/checkpoints)

# List fine-tuning checkpoints

GET /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints

List checkpoints for a fine-tuning job.

##### P ath Parameters Expand Collapse

fine_tuning_job_id : string

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20fine_tuning_job_id%20%3E%20(schema))

##### Q uery Parameters Expand Collapse

after : optional string

Identifier for the last checkpoint ID from the previous pagination request.

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20after%20%3E%20(schema))

limit : optional number

Number of checkpoints to retrieve.

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20limit%20%3E%20(schema))

##### Returns Expand Collapse

data : array of [FineTuningJobCheckpoint](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)) { id , created_at , fine_tuned_model_checkpoint , 4 more }

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

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20data)

has_more : boolean

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20has_more)

object : "list"

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20object)

first_id : optional string

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20first_id)

last_id : optional string

[](#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(method)%20list%20%3E%20(network%20schema)%20%3E%20(property)%20last_id)

### List fine-tuning checkpoints

```
curl https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/checkpoints \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
"object": "list",
"data": [
{
"object": "fine_tuning.job.checkpoint",
"id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
"created_at": 1721764867,
"fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:96olL566:ckpt-step-2000",
"metrics": {
"full_valid_loss": 0.134,
"full_valid_mean_token_accuracy": 0.874
},
"fine_tuning_job_id": "ftjob-abc123",
"step_number": 2000
},
{
"object": "fine_tuning.job.checkpoint",
"id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
"created_at": 1721764800,
"fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:7q8mpxmy:ckpt-step-1000",
"metrics": {
"full_valid_loss": 0.167,
"full_valid_mean_token_accuracy": 0.781
},
"fine_tuning_job_id": "ftjob-abc123",
"step_number": 1000
}
],
"first_id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
"last_id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
"has_more": true
}
```

##### Returns Examples

```
{
"object": "list",
"data": [
{
"object": "fine_tuning.job.checkpoint",
"id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
"created_at": 1721764867,
"fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:96olL566:ckpt-step-2000",
"metrics": {
"full_valid_loss": 0.134,
"full_valid_mean_token_accuracy": 0.874
},
"fine_tuning_job_id": "ftjob-abc123",
"step_number": 2000
},
{
"object": "fine_tuning.job.checkpoint",
"id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
"created_at": 1721764800,
"fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:7q8mpxmy:ckpt-step-1000",
"metrics": {
"full_valid_loss": 0.167,
"full_valid_mean_token_accuracy": 0.781
},
"fine_tuning_job_id": "ftjob-abc123",
"step_number": 1000
}
],
"first_id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
"last_id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
"has_more": true
}
```

---
Source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list
