---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/runs/subresources/steps
title: "Steps"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Steps

> OpenAI API endpoint reference.
[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

[Runs](/api/reference/resources/beta/subresources/threads/subresources/runs)

# Steps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

GET /threads/{thread_id}/runs/{run_id}/steps

##### [Retrieve run step](/api/reference/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

GET /threads/{thread_id}/runs/{run_id}/steps/{step_id}

##### Models Expand Collapse

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

CodeInterpreterToolCall object { id , code_interpreter , type }

Details of the Code Interpreter tool call the run step was involved in.

id : string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : object { input , outputs }

The Code Interpreter tool call definition.

input : string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : array of object { logs , type } or object { image , type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogOutput object { logs , type }

Text output from the Code Interpreter tool call as part of a run step.

logs : string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20logs)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200)

CodeInterpreterImageOutput object { image , type }

image : object { file_id }

file_id : string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema))

CodeInterpreterToolCallDelta object { index , type , id , code_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : optional object { input , outputs }

The Code Interpreter tool call definition.

input : optional string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : optional array of [CodeInterpreterLogs](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index , type , logs } or [CodeInterpreterOutputImage](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index , type , image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema))

FileSearchToolCall object { id , file_search , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

file_search : object { ranking_options , results }

For now, this is always going to be an empty object.

ranking_options : optional object { ranker , score_threshold }

The ranking options for the file search.

ranker : "auto" or "default_2024_08_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default_2024_08_21"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

score_threshold : number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options)

results : optional array of object { file_id , file_name , score , content }

The results of the file search.

file_id : string

The ID of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_id)

file_name : string

The name of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_name)

score : number

The score of the result. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score)

content : optional array of object { text , type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text : optional string

The text content of the file.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "text"

The type of the content.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema))

FileSearchToolCallDelta object { file_search , index , type , id }

file_search : unknown

For now, this is always going to be an empty object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20file_search)

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema))

FunctionToolCall object { id , function , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name , output }

The definition of the function that was called.

arguments : string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema))

FunctionToolCallDelta object { index , type , id , function }

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

function : optional object { arguments , name , output }

The definition of the function that was called.

arguments : optional string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : optional string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : optional string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema))

MessageCreationStepDetails object { message_creation , type }

Details of the message creation by the run step.

message_creation : object { message_id }

message_id : string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation)

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema))

RunStep object { id , assistant_id , cancelled_at , 13 more }

Represents a step in execution of a run.

id : string

The identifier of the run step, which can be referenced in API endpoints.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20id)

assistant_id : string

The ID of the [assistant](/docs/api-reference/assistants) associated with the run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20assistant_id)

cancelled_at : number

The Unix timestamp (in seconds) for when the run step was cancelled.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20cancelled_at)

completed_at : number

The Unix timestamp (in seconds) for when the run step completed.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20completed_at)

created_at : number

The Unix timestamp (in seconds) for when the run step was created.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20created_at)

expired_at : number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20expired_at)

failed_at : number

The Unix timestamp (in seconds) for when the run step failed.

format unixtime

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20failed_at)

last_error : object { code , message }

The last error associated with this run step. Will be `null` if there are no errors.

code : "server_error" or "rate_limit_exceeded"

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server_error"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%200)

"rate_limit_exceeded"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20code)

message : string

A human-readable description of the error.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error%20%3E%20(property)%20message)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20last_error)

metadata : [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20metadata)

object : "thread.run.step"

The object type, which is always `thread.run.step`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20object)

run_id : string

The ID of the [run](/docs/api-reference/runs) that this run step is a part of.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20run_id)

status : "in_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in_progress"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200)

"cancelled"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201)

"failed"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202)

"completed"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203)

"expired"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20status)

step_details : [MessageCreationStepDetails](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message_creation , type } or [ToolCallsStepDetails](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool_calls , type }

The details of the run step.

One of the following:

MessageCreationStepDetails object { message_creation , type }

Details of the message creation by the run step.

message_creation : object { message_id }

message_id : string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20message_creation)

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema))

ToolCallsStepDetails object { tool_calls , type }

Details of the tool call.

tool_calls : array of [CodeInterpreterToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id , code_interpreter , type } or [FileSearchToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id , file_search , type } or [FunctionToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id , function , type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall object { id , code_interpreter , type }

Details of the Code Interpreter tool call the run step was involved in.

id : string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : object { input , outputs }

The Code Interpreter tool call definition.

input : string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : array of object { logs , type } or object { image , type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogOutput object { logs , type }

Text output from the Code Interpreter tool call as part of a run step.

logs : string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20logs)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200)

CodeInterpreterImageOutput object { image , type }

image : object { file_id }

file_id : string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema))

FileSearchToolCall object { id , file_search , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

file_search : object { ranking_options , results }

For now, this is always going to be an empty object.

ranking_options : optional object { ranker , score_threshold }

The ranking options for the file search.

ranker : "auto" or "default_2024_08_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default_2024_08_21"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

score_threshold : number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options)

results : optional array of object { file_id , file_name , score , content }

The results of the file search.

file_id : string

The ID of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_id)

file_name : string

The name of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_name)

score : number

The score of the result. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score)

content : optional array of object { text , type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text : optional string

The text content of the file.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "text"

The type of the content.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema))

FunctionToolCall object { id , function , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name , output }

The definition of the function that was called.

arguments : string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20step_details)

thread_id : string

The ID of the [thread](/docs/api-reference/threads) that was run.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20thread_id)

type : "message_creation" or "tool_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message_creation"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200)

"tool_calls"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20type)

usage : object { completion_tokens , prompt_tokens , total_tokens }

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion_tokens : number

Number of completion tokens used over the course of the run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20completion_tokens)

prompt_tokens : number

Number of prompt tokens used over the course of the run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20prompt_tokens)

total_tokens : number

Total number of tokens used (prompt + completion).

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20total_tokens)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

RunStepDeltaEvent object { id , delta , object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

id : string

The identifier of the run step, which can be referenced in API endpoints.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20id)

delta : object { step_details }

The delta containing the fields that have changed on the run step.

step_details : optional [RunStepDeltaMessageDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type , message_creation } or [ToolCallDeltaObject](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type , tool_calls }

The details of the run step.

One of the following:

RunStepDeltaMessageDelta object { type , message_creation }

Details of the message creation by the run step.

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20type)

message_creation : optional object { message_id }

message_id : optional string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema))

ToolCallDeltaObject object { type , tool_calls }

Details of the tool call.

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20type)

tool_calls : optional array of [CodeInterpreterToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index , type , id , code_interpreter } or [FileSearchToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file_search , index , type , id } or [FunctionToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index , type , id , function }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta object { index , type , id , code_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : optional object { input , outputs }

The Code Interpreter tool call definition.

input : optional string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : optional array of [CodeInterpreterLogs](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index , type , logs } or [CodeInterpreterOutputImage](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index , type , image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema))

FileSearchToolCallDelta object { file_search , index , type , id }

file_search : unknown

For now, this is always going to be an empty object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20file_search)

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema))

FunctionToolCallDelta object { index , type , id , function }

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

function : optional object { arguments , name , output }

The definition of the function that was called.

arguments : optional string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : optional string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : optional string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta%20%3E%20(property)%20step_details)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20delta)

object : "thread.run.step.delta"

The object type, which is always `thread.run.step.delta`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)%20%3E%20(property)%20object)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

RunStepDeltaMessageDelta object { type , message_creation }

Details of the message creation by the run step.

type : "message_creation"

Always `message_creation`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20type)

message_creation : optional object { message_id }

message_id : optional string

The ID of the message that was created by this run step.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation%20%3E%20(property)%20message_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)%20%3E%20(property)%20message_creation)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema))

RunStepInclude = "step_details.tool_calls[*].file_search.results[*].content"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_include%20%3E%20(schema))

ToolCallDeltaObject object { type , tool_calls }

Details of the tool call.

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20type)

tool_calls : optional array of [CodeInterpreterToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index , type , id , code_interpreter } or [FileSearchToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file_search , index , type , id } or [FunctionToolCallDelta](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index , type , id , function }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta object { index , type , id , code_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : optional object { input , outputs }

The Code Interpreter tool call definition.

input : optional string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : optional array of [CodeInterpreterLogs](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index , type , logs } or [CodeInterpreterOutputImage](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index , type , image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs object { index , type , logs }

Text output from the Code Interpreter tool call as part of a run step.

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20index)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20type)

logs : optional string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)%20%3E%20(property)%20logs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema))

CodeInterpreterOutputImage object { index , type , image }

index : number

The index of the output in the outputs array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20index)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20type)

image : optional object { file_id }

file_id : optional string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)%20%3E%20(property)%20image)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema))

FileSearchToolCallDelta object { file_search , index , type , id }

file_search : unknown

For now, this is always going to be an empty object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20file_search)

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema))

FunctionToolCallDelta object { index , type , id , function }

index : number

The index of the tool call in the tool calls array.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20index)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20type)

id : optional string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20id)

function : optional object { arguments , name , output }

The definition of the function that was called.

arguments : optional string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : optional string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : optional string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)%20%3E%20(property)%20function)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema))

ToolCallsStepDetails object { tool_calls , type }

Details of the tool call.

tool_calls : array of [CodeInterpreterToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id , code_interpreter , type } or [FileSearchToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id , file_search , type } or [FunctionToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id , function , type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall object { id , code_interpreter , type }

Details of the Code Interpreter tool call the run step was involved in.

id : string

The ID of the tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

code_interpreter : object { input , outputs }

The Code Interpreter tool call definition.

input : string

The input to the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20input)

outputs : array of object { logs , type } or object { image , type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogOutput object { logs , type }

Text output from the Code Interpreter tool call as part of a run step.

logs : string

The text output from the Code Interpreter tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20logs)

type : "logs"

Always `logs`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%200)

CodeInterpreterImageOutput object { image , type }

image : object { file_id }

file_id : string

The [file](/docs/api-reference/files) ID of the image.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image%20%3E%20(property)%20file_id)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20image)

type : "image"

Always `image`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter%20%3E%20(property)%20outputs)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20code_interpreter)

type : "code_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema))

FileSearchToolCall object { id , file_search , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

file_search : object { ranking_options , results }

For now, this is always going to be an empty object.

ranking_options : optional object { ranker , score_threshold }

The ranking options for the file search.

ranker : "auto" or "default_2024_08_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%200)

"default_2024_08_21"

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker%20%3E%20(member)%201)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20ranker)

score_threshold : number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options%20%3E%20(property)%20score_threshold)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20ranking_options)

results : optional array of object { file_id , file_name , score , content }

The results of the file search.

file_id : string

The ID of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_id)

file_name : string

The name of the file that result was found in.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20file_name)

score : number

The score of the result. All values must be a floating point number between 0 and 1.

minimum 0

maximum 1

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score)

content : optional array of object { text , type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text : optional string

The text content of the file.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20text)

type : optional "text"

The type of the content.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20content)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search%20%3E%20(property)%20results)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20file_search)

type : "file_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema))

FunctionToolCall object { id , function , type }

id : string

The ID of the tool call object.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20id)

function : object { arguments , name , output }

The definition of the function that was called.

arguments : string

The arguments passed to the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20arguments)

name : string

The name of the function.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20name)

output : string

The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function%20%3E%20(property)%20output)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20function)

type : "function"

The type of tool call. This is always going to be `function` for this type of tool call.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema))

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20tool_calls)

type : "tool_calls"

Always `tool_calls`.

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)%20%3E%20(property)%20type)

[](#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/runs/subresources/steps
