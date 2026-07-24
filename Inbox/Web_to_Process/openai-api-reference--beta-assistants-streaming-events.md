---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/streaming-events.md
title: "Assistants streaming events"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Assistants streaming events

> OpenAI API streaming event reference.
Stream the result of executing a Run or resuming a Run after submitting tool outputs.
You can stream events from the [Create Thread and Run](https://developers.openai.com/docs/api-reference/runs/createThreadAndRun),
[Create Run](https://developers.openai.com/docs/api-reference/runs/createRun), and [Submit Tool Outputs](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs)
endpoints by passing `"stream": true`. The response will be a [Server-Sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) stream.
Our Node and Python SDKs provide helpful utilities to make streaming easy. Reference the
[Assistants API quickstart](https://developers.openai.com/docs/assistants/overview) to learn more.

## event

Occurs when a new [thread](https://developers.openai.com/docs/api-reference/threads/object) is created.

### Schema

Schema name: `(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0`

```json
{
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ThreadStreamEvent/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "data"
        },
        {
          "ident": "event"
        },
        {
          "ident": "enabled"
        }
      ]
    },
    "docstring": "Occurs when a new [thread](/docs/api-reference/threads/object) is created.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) data",
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) event",
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) enabled"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) data": {
    "kind": "HttpDeclProperty",
    "title": "Thread",
    "docstring": "Represents a thread that contains [messages](/docs/api-reference/messages).",
    "key": "data",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Thread",
      "$ref": "(resource) beta.threads > (model) thread > (schema)"
    },
    "oasRef": "#/components/schemas/ThreadStreamEvent/oneOf/0/properties/data",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads > (model) thread",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) thread > (schema) > (property) id",
      "(resource) beta.threads > (model) thread > (schema) > (property) created_at",
      "(resource) beta.threads > (model) thread > (schema) > (property) metadata",
      "(resource) beta.threads > (model) thread > (schema) > (property) object",
      "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) event": {
    "kind": "HttpDeclProperty",
    "key": "event",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "thread.created"
        }
      ],
      "oasRef": "#/components/schemas/ThreadStreamEvent/oneOf/0/properties/event"
    },
    "oasRef": "#/components/schemas/ThreadStreamEvent/oneOf/0/properties/event",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) event > (member) 0"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) enabled": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable input audio transcription.",
    "key": "enabled",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/ThreadStreamEvent/oneOf/0/properties/enabled",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The identifier, which can be referenced in API endpoints.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) created_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the thread was created.",
    "key": "created_at",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/created_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) metadata": {
    "kind": "HttpDeclProperty",
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard.\n\nKeys are strings with a maximum length of 64 characters. Values are strings\nwith a maximum length of 512 characters.\n",
    "key": "metadata",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Metadata",
      "$ref": "(resource) $shared > (model) metadata > (schema)"
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/metadata",
    "deprecated": false,
    "schemaType": "map",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) metadata",
    "children": []
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "The object type, which is always `thread`.",
    "key": "object",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "thread"
        }
      ],
      "oasRef": "#/components/schemas/ThreadObject/properties/object"
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads > (model) thread > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources": {
    "kind": "HttpDeclProperty",
    "docstring": "A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.\n",
    "key": "tool_resources",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code_interpreter"
        },
        {
          "ident": "file_search"
        }
      ]
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/tool_resources",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) code_interpreter",
      "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) file_search"
    ]
  },
  "(resource) beta.threads > (model) thread > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ThreadObject",
    "ident": "Thread",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "created_at"
        },
        {
          "ident": "metadata"
        },
        {
          "ident": "object"
        },
        {
          "ident": "tool_resources"
        }
      ]
    },
    "docstring": "Represents a thread that contains [messages](/docs/api-reference/messages).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) thread > (schema) > (property) id",
      "(resource) beta.threads > (model) thread > (schema) > (property) created_at",
      "(resource) beta.threads > (model) thread > (schema) > (property) metadata",
      "(resource) beta.threads > (model) thread > (schema) > (property) object",
      "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 0 > (property) event > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "thread.created"
    }
  },
  "(resource) $shared > (model) metadata > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Metadata",
    "ident": "Metadata",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeString"
        }
      ],
      "oasRef": "#/components/schemas/Metadata"
    },
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard.\n\nKeys are strings with a maximum length of 64 characters. Values are strings\nwith a maximum length of 512 characters.\n",
    "children": []
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "thread"
    }
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) code_interpreter": {
    "kind": "HttpDeclProperty",
    "key": "code_interpreter",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "file_ids"
        }
      ]
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/tool_resources/anyOf/0/properties/code_interpreter",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) code_interpreter > (property) file_ids"
    ]
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) file_search": {
    "kind": "HttpDeclProperty",
    "key": "file_search",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "vector_store_ids"
        }
      ]
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/tool_resources/anyOf/0/properties/file_search",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) file_search > (property) vector_store_ids"
    ]
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) code_interpreter > (property) file_ids": {
    "kind": "HttpDeclProperty",
    "docstring": "A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.\n",
    "key": "file_ids",
    "optional": true,
    "nullable": false,
    "default": [],
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeString"
      },
      "oasRef": "#/components/schemas/ThreadObject/properties/tool_resources/anyOf/0/properties/code_interpreter/properties/file_ids"
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/tool_resources/anyOf/0/properties/code_interpreter/properties/file_ids",
    "deprecated": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) beta.threads > (model) thread > (schema) > (property) tool_resources > (property) file_search > (property) vector_store_ids": {
    "kind": "HttpDeclProperty",
    "docstring": "The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.\n",
    "key": "vector_store_ids",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeString"
      },
      "oasRef": "#/components/schemas/ThreadObject/properties/tool_resources/anyOf/0/properties/file_search/properties/vector_store_ids"
    },
    "oasRef": "#/components/schemas/ThreadObject/properties/tool_resources/anyOf/0/properties/file_search/properties/vector_store_ids",
    "deprecated": false,
    "schemaType": "array",
    "children": []
  }
}
```

### Example

```json
{}
```

## event

Occurs when a new [run](https://developers.openai.com/docs/api-reference/runs/object) is created.

### Schema

Schema name: `(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1`

```json
{
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/0",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "data"
        },
        {
          "ident": "event"
        }
      ]
    },
    "docstring": "Occurs when a new [run](/docs/api-reference/runs/object) is created.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1 > (property) data",
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1 > (property) event"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1 > (property) data": {
    "kind": "HttpDeclProperty",
    "title": "A run on a thread",
    "docstring": "Represents an execution run on a [thread](/docs/api-reference/threads).",
    "key": "data",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Run",
      "$ref": "(resource) beta.threads.runs > (model) run > (schema)"
    },
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/0/properties/data",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads.runs > (model) run",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) assistant_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) cancelled_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) completed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) created_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) expires_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) failed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) instructions",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_completion_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_prompt_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) metadata",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) model",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) object",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) parallel_tool_calls",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) response_format",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) started_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) thread_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tool_choice",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) temperature",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) top_p"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1 > (property) event": {
    "kind": "HttpDeclProperty",
    "key": "event",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "thread.run.created"
        }
      ],
      "oasRef": "#/components/schemas/RunStreamEvent/oneOf/0/properties/event"
    },
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/0/properties/event",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1 > (property) event > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The identifier, which can be referenced in API endpoints.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) assistant_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.",
    "key": "assistant_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/assistant_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) cancelled_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was cancelled.",
    "key": "cancelled_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/cancelled_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) completed_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was completed.",
    "key": "completed_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/completed_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) created_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was created.",
    "key": "created_at",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/created_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) expires_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run will expire.",
    "key": "expires_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/expires_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) failed_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run failed.",
    "key": "failed_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/failed_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details": {
    "kind": "HttpDeclProperty",
    "docstring": "Details on why the run is incomplete. Will be `null` if the run is not incomplete.",
    "key": "incomplete_details",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "reason"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/incomplete_details",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "docstring": "The instructions that the [assistant](/docs/api-reference/assistants) used for this run.",
    "key": "instructions",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/instructions",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error": {
    "kind": "HttpDeclProperty",
    "docstring": "The last error associated with this run. Will be `null` if there are no errors.",
    "key": "last_error",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "message"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/last_error",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) message"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) max_completion_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of completion tokens specified to have been used over the course of the run.\n",
    "key": "max_completion_tokens",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 256
    },
    "oasRef": "#/components/schemas/RunObject/properties/max_completion_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) max_prompt_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of prompt tokens specified to have been used over the course of the run.\n",
    "key": "max_prompt_tokens",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 256
    },
    "oasRef": "#/components/schemas/RunObject/properties/max_prompt_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) metadata": {
    "kind": "HttpDeclProperty",
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard.\n\nKeys are strings with a maximum length of 64 characters. Values are strings\nwith a maximum length of 512 characters.\n",
    "key": "metadata",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Metadata",
      "$ref": "(resource) $shared > (model) metadata > (schema)"
    },
    "oasRef": "#/components/schemas/RunObject/properties/metadata",
    "deprecated": false,
    "schemaType": "map",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) metadata",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "docstring": "The model that the [assistant](/docs/api-reference/assistants) used for this run.",
    "key": "model",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/model",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "The object type, which is always `thread.run`.",
    "key": "object",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "thread.run"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/object"
    },
    "oasRef": "#/components/schemas/RunObject/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.",
    "key": "parallel_tool_calls",
    "optional": false,
    "nullable": false,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RunObject/properties/parallel_tool_calls",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action": {
    "kind": "HttpDeclProperty",
    "docstring": "Details on the action required to continue the run. Will be `null` if no action is required.",
    "key": "required_action",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "submit_tool_outputs"
        },
        {
          "ident": "type"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) response_format": {
    "kind": "HttpDeclProperty",
    "docstring": "Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.\n\nSetting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).\n\nSetting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.\n\n**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if `finish_reason=\"length\"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.\n",
    "key": "response_format",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantResponseFormatOption",
      "$ref": "(resource) beta.threads > (model) assistant_response_format_option > (schema)"
    },
    "oasRef": "#/components/schemas/RunObject/properties/response_format",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads > (model) assistant_response_format_option",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 1",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 2",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 3"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) started_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was started.",
    "key": "started_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/started_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.",
    "key": "status",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "queued"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "requires_action"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "cancelling"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "cancelled"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "expired"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/status"
    },
    "oasRef": "#/components/schemas/RunObject/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 1",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 2",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 3",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 4",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 5",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 6",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 7",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 8"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) thread_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.",
    "key": "thread_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/thread_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "docstring": "Controls which (if any) tool is called by the model.\n`none` means the model will not call any tools and instead generates a message.\n`auto` is the default value and means the model can pick between generating a message or calling one or more tools.\n`required` means the model must call one or more tools before responding to the user.\nSpecifying a particular tool like `{\"type\": \"file_search\"}` or `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}` forces the model to call that tool.\n",
    "key": "tool_choice",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantToolChoiceOption",
      "$ref": "(resource) beta.threads > (model) assistant_tool_choice_option > (schema)"
    },
    "oasRef": "#/components/schemas/RunObject/properties/tool_choice",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads > (model) assistant_tool_choice_option",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "docstring": "The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.",
    "key": "tools",
    "optional": false,
    "nullable": false,
    "default": [],
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "CodeInterpreterTool",
            "$ref": "(resource) beta.assistants > (model) code_interpreter_tool > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "FileSearchTool",
            "$ref": "(resource) beta.assistants > (model) file_search_tool > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "FunctionTool",
            "$ref": "(resource) beta.assistants > (model) function_tool > (schema)"
          }
        ],
        "oasRef": "#/components/schemas/RunObject/properties/tools/items"
      },
      "oasRef": "#/components/schemas/RunObject/properties/tools"
    },
    "oasRef": "#/components/schemas/RunObject/properties/tools",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 1",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 2"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy": {
    "kind": "HttpDeclProperty",
    "title": "Thread Truncation Controls",
    "docstring": "Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.",
    "key": "truncation_strategy",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "last_messages"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/truncation_strategy",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) last_messages"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage": {
    "kind": "HttpDeclProperty",
    "docstring": "Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).",
    "key": "usage",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "completion_tokens"
        },
        {
          "ident": "prompt_tokens"
        },
        {
          "ident": "total_tokens"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/usage",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) completion_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) prompt_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) total_tokens"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) temperature": {
    "kind": "HttpDeclProperty",
    "docstring": "The sampling temperature used for this run. If not set, defaults to 1.",
    "key": "temperature",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunObject/properties/temperature",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) top_p": {
    "kind": "HttpDeclProperty",
    "docstring": "The nucleus sampling value used for this run. If not set, defaults to 1.",
    "key": "top_p",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunObject/properties/top_p",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RunObject",
    "ident": "Run",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "assistant_id"
        },
        {
          "ident": "cancelled_at"
        },
        {
          "ident": "completed_at"
        },
        {
          "ident": "created_at"
        },
        {
          "ident": "expires_at"
        },
        {
          "ident": "failed_at"
        },
        {
          "ident": "incomplete_details"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "last_error"
        },
        {
          "ident": "max_completion_tokens"
        },
        {
          "ident": "max_prompt_tokens"
        },
        {
          "ident": "metadata"
        },
        {
          "ident": "model"
        },
        {
          "ident": "object"
        },
        {
          "ident": "parallel_tool_calls"
        },
        {
          "ident": "required_action"
        },
        {
          "ident": "response_format"
        },
        {
          "ident": "started_at"
        },
        {
          "ident": "status"
        },
        {
          "ident": "thread_id"
        },
        {
          "ident": "tool_choice"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "truncation_strategy"
        },
        {
          "ident": "usage"
        },
        {
          "ident": "temperature"
        },
        {
          "ident": "top_p"
        }
      ]
    },
    "docstring": "Represents an execution run on a [thread](/docs/api-reference/threads).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) assistant_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) cancelled_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) completed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) created_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) expires_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) failed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) instructions",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_completion_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_prompt_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) metadata",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) model",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) object",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) parallel_tool_calls",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) response_format",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) started_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) thread_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tool_choice",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) temperature",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) top_p"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 1 > (property) event > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "thread.run.created"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason": {
    "kind": "HttpDeclProperty",
    "docstring": "The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.",
    "key": "reason",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "max_completion_tokens"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "max_prompt_tokens"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/incomplete_details/properties/reason"
    },
    "oasRef": "#/components/schemas/RunObject/properties/incomplete_details/properties/reason",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code": {
    "kind": "HttpDeclProperty",
    "docstring": "One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.",
    "key": "code",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "server_error"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "rate_limit_exceeded"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "invalid_prompt"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/last_error/properties/code"
    },
    "oasRef": "#/components/schemas/RunObject/properties/last_error/properties/code",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 1",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 2"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) message": {
    "kind": "HttpDeclProperty",
    "docstring": "A human-readable description of the error.",
    "key": "message",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/last_error/properties/message",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) metadata > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Metadata",
    "ident": "Metadata",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeString"
        }
      ],
      "oasRef": "#/components/schemas/Metadata"
    },
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard.\n\nKeys are strings with a maximum length of 64 characters. Values are strings\nwith a maximum length of 512 characters.\n",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "thread.run"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs": {
    "kind": "HttpDeclProperty",
    "docstring": "Details on the tool outputs needed for this run to continue.",
    "key": "submit_tool_outputs",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "tool_calls"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/submit_tool_outputs",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs > (property) tool_calls"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "For now, this is always `submit_tool_outputs`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "submit_tool_outputs"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/type"
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type > (member) 0"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption/oneOf/0"
    },
    "docstring": "`auto` is the default value\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0 > (member) 0"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseFormatText",
      "$ref": "(resource) $shared > (model) response_format_text > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_text > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseFormatJSONObject",
      "$ref": "(resource) $shared > (model) response_format_json_object > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_object > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseFormatJSONSchema",
      "$ref": "(resource) $shared > (model) response_format_json_schema > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption",
    "ident": "AssistantResponseFormatOption",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            }
          ],
          "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption/oneOf/0"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseFormatText",
          "$ref": "(resource) $shared > (model) response_format_text > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseFormatJSONObject",
          "$ref": "(resource) $shared > (model) response_format_json_object > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseFormatJSONSchema",
          "$ref": "(resource) $shared > (model) response_format_json_schema > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption"
    },
    "docstring": "Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.\n\nSetting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).\n\nSetting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.\n\n**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if `finish_reason=\"length\"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 1",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 2",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 3"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "queued"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "requires_action"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "cancelling"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "cancelled"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "expired"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "none"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "required"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption/oneOf/0"
    },
    "docstring": "`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 0",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 1",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 2"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantToolChoice",
      "$ref": "(resource) beta.threads > (model) assistant_tool_choice > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) function"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption",
    "ident": "AssistantToolChoiceOption",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "none"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "required"
            }
          ],
          "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption/oneOf/0"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "AssistantToolChoice",
          "$ref": "(resource) beta.threads > (model) assistant_tool_choice > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption"
    },
    "docstring": "Controls which (if any) tool is called by the model.\n`none` means the model will not call any tools and instead generates a message.\n`auto` is the default value and means the model can pick between generating a message or calling one or more tools.\n`required` means the model must call one or more tools before responding to the user.\nSpecifying a particular tool like `{\"type\": \"file_search\"}` or `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}` forces the model to call that tool.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "CodeInterpreterTool",
      "$ref": "(resource) beta.assistants > (model) code_interpreter_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FileSearchTool",
      "$ref": "(resource) beta.assistants > (model) file_search_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionTool",
      "$ref": "(resource) beta.assistants > (model) function_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) function",
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.assistants > (model) code_interpreter_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantToolsCode",
    "ident": "CodeInterpreterTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantToolsFileSearch",
    "ident": "FileSearchTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "file_search"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantToolsFunction",
    "ident": "FunctionTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "function"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) function",
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "last_messages"
        }
      ],
      "oasRef": "#/components/schemas/TruncationObject/properties/type"
    },
    "oasRef": "#/components/schemas/TruncationObject/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) last_messages": {
    "kind": "HttpDeclProperty",
    "docstring": "The number of most recent messages from the thread when constructing the context for the run.",
    "key": "last_messages",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 1
    },
    "oasRef": "#/components/schemas/TruncationObject/properties/last_messages",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) completion_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of completion tokens used over the course of the run.",
    "key": "completion_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunCompletionUsage/anyOf/0/properties/completion_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) prompt_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of prompt tokens used over the course of the run.",
    "key": "prompt_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunCompletionUsage/anyOf/0/properties/prompt_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) total_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Total number of tokens used (prompt + completion).",
    "key": "total_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunCompletionUsage/anyOf/0/properties/total_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "max_completion_tokens"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "max_prompt_tokens"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "server_error"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "rate_limit_exceeded"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "invalid_prompt"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs > (property) tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "A list of the relevant tool calls.",
    "key": "tool_calls",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "RequiredActionFunctionToolCall",
        "$ref": "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema)"
      },
      "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/submit_tool_outputs/properties/tool_calls"
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/submit_tool_outputs/properties/tool_calls",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "submit_tool_outputs"
    }
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) $shared > (model) response_format_text > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of response format being defined. Always `text`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "text"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatText/properties/type"
    },
    "oasRef": "#/components/schemas/ResponseFormatText/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) response_format_text > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) $shared > (model) response_format_text > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseFormatText",
    "ident": "ResponseFormatText",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Default response format. Used to generate text responses.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_text > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) response_format_json_object > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of response format being defined. Always `json_object`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "json_object"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatJsonObject/properties/type"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonObject/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) response_format_json_object > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) $shared > (model) response_format_json_object > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseFormatJsonObject",
    "ident": "ResponseFormatJSONObject",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "JSON object response format. An older method of generating JSON responses.\nUsing `json_schema` is recommended for models that support it. Note that the\nmodel will not generate JSON without a system or user message instructing it\nto do so.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_object > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema": {
    "kind": "HttpDeclProperty",
    "title": "JSON schema",
    "docstring": "Structured Outputs configuration options, including a JSON Schema.\n",
    "key": "json_schema",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "description"
        },
        {
          "ident": "schema"
        },
        {
          "ident": "strict"
        }
      ]
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) name",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) description",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) schema",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) strict"
    ]
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of response format being defined. Always `json_schema`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "json_schema"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/type"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) $shared > (model) response_format_json_schema > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema",
    "ident": "ResponseFormatJSONSchema",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "json_schema"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "JSON Schema response format. Used to generate structured JSON responses.\nLearn more about [Structured Outputs](/docs/guides/structured-outputs).\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "required"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the tool. If type is `function`, the function name must be set",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 0",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 1",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 2"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) function": {
    "kind": "HttpDeclProperty",
    "key": "function",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantToolChoiceFunction",
      "$ref": "(resource) beta.threads > (model) assistant_tool_choice_function > (schema)"
    },
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/function",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads > (model) assistant_tool_choice_function",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_function > (schema) > (property) name"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice",
    "ident": "AssistantToolChoice",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "function"
        }
      ]
    },
    "docstring": "Specifies a tool the model should use. Use to force the model to call a specific tool.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) function"
    ]
  },
  "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool being defined: `code_interpreter`",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter"
        }
      ],
      "oasRef": "#/components/schemas/AssistantToolsCode/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantToolsCode/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool being defined: `file_search`",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search"
        }
      ],
      "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search": {
    "kind": "HttpDeclProperty",
    "docstring": "Overrides for the file search tool.",
    "key": "file_search",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "max_num_results"
        },
        {
          "ident": "ranking_options"
        }
      ]
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/file_search",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) max_num_results",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema) > (property) function": {
    "kind": "HttpDeclProperty",
    "key": "function",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionDefinition",
      "$ref": "(resource) $shared > (model) function_definition > (schema)"
    },
    "oasRef": "#/components/schemas/AssistantToolsFunction/properties/function",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) function_definition",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) function_definition > (schema) > (property) name",
      "(resource) $shared > (model) function_definition > (schema) > (property) description",
      "(resource) $shared > (model) function_definition > (schema) > (property) parameters",
      "(resource) $shared > (model) function_definition > (schema) > (property) strict"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool being defined: `function`",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ],
      "oasRef": "#/components/schemas/AssistantToolsFunction/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantToolsFunction/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "last_messages"
    }
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](/docs/api-reference/runs/submitToolOutputs) endpoint.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function": {
    "kind": "HttpDeclProperty",
    "docstring": "The function definition.",
    "key": "function",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "arguments"
        },
        {
          "ident": "name"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/function",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) arguments",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) name"
    ]
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool call the output is required for. For now, this is always `function`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ],
      "oasRef": "#/components/schemas/RunToolCallObject/properties/type"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RunToolCallObject",
    "ident": "RequiredActionFunctionToolCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "function"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Tool call objects",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) response_format_text > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "text"
    }
  },
  "(resource) $shared > (model) response_format_json_object > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "json_object"
    }
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the response format. Must be a-z, A-Z, 0-9, or contain\nunderscores and dashes, with a maximum length of 64.\n",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) description": {
    "kind": "HttpDeclProperty",
    "docstring": "A description of what the response format is for, used by the model to\ndetermine how to respond in the format.\n",
    "key": "description",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/description",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) schema": {
    "kind": "HttpDeclProperty",
    "title": "JSON schema",
    "docstring": "The schema for the response format, described as a JSON Schema object.\nLearn how to build JSON schemas [here](https://json-schema.org/).\n",
    "key": "schema",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/schema"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/schema",
    "deprecated": false,
    "schemaType": "map",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) strict": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable strict schema adherence when generating the output.\nIf set to true, the model will always follow the exact schema defined\nin the `schema` field. Only a subset of JSON Schema is supported when\n`strict` is `true`. To learn more, read the [Structured Outputs\nguide](/docs/guides/structured-outputs).\n",
    "key": "strict",
    "optional": true,
    "nullable": true,
    "default": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/strict",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "json_schema"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_function > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function to call.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/function/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads > (model) assistant_tool_choice_function > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/function",
    "ident": "AssistantToolChoiceFunction",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_function > (schema) > (property) name"
    ]
  },
  "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) max_num_results": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.\n\nNote that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.\n",
    "key": "max_num_results",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 1,
      "maximum": 50
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/file_search/properties/max_num_results",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options": {
    "kind": "HttpDeclProperty",
    "title": "File search tool call ranking options",
    "docstring": "The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.\n\nSee the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.\n",
    "key": "ranking_options",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "score_threshold"
        },
        {
          "ident": "ranker"
        }
      ]
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/file_search/properties/ranking_options",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) score_threshold",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker"
    ]
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) description": {
    "kind": "HttpDeclProperty",
    "docstring": "A description of what the function does, used by the model to choose when and how to call the function.",
    "key": "description",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/description",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) parameters": {
    "kind": "HttpDeclProperty",
    "docstring": "The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. \n\nOmitting `parameters` defines a function with an empty parameter list.",
    "key": "parameters",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionParameters",
      "$ref": "(resource) $shared > (model) function_parameters > (schema)"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/parameters",
    "deprecated": false,
    "schemaType": "map",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) function_parameters",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) strict": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](/docs/guides/function-calling).",
    "key": "strict",
    "optional": true,
    "nullable": true,
    "default": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/strict",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/FunctionObject",
    "ident": "FunctionDefinition",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "description"
        },
        {
          "ident": "parameters"
        },
        {
          "ident": "strict"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) function_definition > (schema) > (property) name",
      "(resource) $shared > (model) function_definition > (schema) > (property) description",
      "(resource) $shared > (model) function_definition > (schema) > (property) parameters",
      "(resource) $shared > (model) function_definition > (schema) > (property) strict"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) arguments": {
    "kind": "HttpDeclProperty",
    "docstring": "The arguments that the model expects you to pass to the function.",
    "key": "arguments",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/function/properties/arguments",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/function/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) score_threshold": {
    "kind": "HttpDeclProperty",
    "docstring": "The score threshold for the file search. All values must be a floating point number between 0 and 1.",
    "key": "score_threshold",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 1
    },
    "oasRef": "#/components/schemas/FileSearchRankingOptions/properties/score_threshold",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker": {
    "kind": "HttpDeclProperty",
    "docstring": "The ranker to use for the file search. If not specified will use the `auto` ranker.",
    "key": "ranker",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "default_2024_08_21"
        }
      ],
      "oasRef": "#/components/schemas/FileSearchRankingOptions/properties/ranker"
    },
    "oasRef": "#/components/schemas/FileSearchRankingOptions/properties/ranker",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 0",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 1"
    ]
  },
  "(resource) $shared > (model) function_parameters > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/FunctionParameters",
    "ident": "FunctionParameters",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ],
      "oasRef": "#/components/schemas/FunctionParameters"
    },
    "docstring": "The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. \n\nOmitting `parameters` defines a function with an empty parameter list.",
    "children": []
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default_2024_08_21"
    }
  }
}
```

### Example

```json
{}
```

## event

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

### Schema

Schema name: `(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2`

```json
{
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/1",
    "ident": "UnionMember2",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "data"
        },
        {
          "ident": "event"
        }
      ]
    },
    "docstring": "Occurs when a [run](/docs/api-reference/runs/object) moves to a `queued` status.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2 > (property) data",
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2 > (property) event"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2 > (property) data": {
    "kind": "HttpDeclProperty",
    "title": "A run on a thread",
    "docstring": "Represents an execution run on a [thread](/docs/api-reference/threads).",
    "key": "data",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Run",
      "$ref": "(resource) beta.threads.runs > (model) run > (schema)"
    },
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/1/properties/data",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads.runs > (model) run",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) assistant_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) cancelled_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) completed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) created_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) expires_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) failed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) instructions",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_completion_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_prompt_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) metadata",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) model",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) object",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) parallel_tool_calls",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) response_format",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) started_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) thread_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tool_choice",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) temperature",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) top_p"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2 > (property) event": {
    "kind": "HttpDeclProperty",
    "key": "event",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "thread.run.queued"
        }
      ],
      "oasRef": "#/components/schemas/RunStreamEvent/oneOf/1/properties/event"
    },
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/1/properties/event",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2 > (property) event > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The identifier, which can be referenced in API endpoints.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) assistant_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.",
    "key": "assistant_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/assistant_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) cancelled_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was cancelled.",
    "key": "cancelled_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/cancelled_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) completed_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was completed.",
    "key": "completed_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/completed_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) created_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was created.",
    "key": "created_at",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/created_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) expires_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run will expire.",
    "key": "expires_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/expires_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) failed_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run failed.",
    "key": "failed_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/failed_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details": {
    "kind": "HttpDeclProperty",
    "docstring": "Details on why the run is incomplete. Will be `null` if the run is not incomplete.",
    "key": "incomplete_details",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "reason"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/incomplete_details",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "docstring": "The instructions that the [assistant](/docs/api-reference/assistants) used for this run.",
    "key": "instructions",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/instructions",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error": {
    "kind": "HttpDeclProperty",
    "docstring": "The last error associated with this run. Will be `null` if there are no errors.",
    "key": "last_error",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "message"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/last_error",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) message"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) max_completion_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of completion tokens specified to have been used over the course of the run.\n",
    "key": "max_completion_tokens",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 256
    },
    "oasRef": "#/components/schemas/RunObject/properties/max_completion_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) max_prompt_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of prompt tokens specified to have been used over the course of the run.\n",
    "key": "max_prompt_tokens",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 256
    },
    "oasRef": "#/components/schemas/RunObject/properties/max_prompt_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) metadata": {
    "kind": "HttpDeclProperty",
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard.\n\nKeys are strings with a maximum length of 64 characters. Values are strings\nwith a maximum length of 512 characters.\n",
    "key": "metadata",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Metadata",
      "$ref": "(resource) $shared > (model) metadata > (schema)"
    },
    "oasRef": "#/components/schemas/RunObject/properties/metadata",
    "deprecated": false,
    "schemaType": "map",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) metadata",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "docstring": "The model that the [assistant](/docs/api-reference/assistants) used for this run.",
    "key": "model",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/model",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "The object type, which is always `thread.run`.",
    "key": "object",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "thread.run"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/object"
    },
    "oasRef": "#/components/schemas/RunObject/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.",
    "key": "parallel_tool_calls",
    "optional": false,
    "nullable": false,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RunObject/properties/parallel_tool_calls",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action": {
    "kind": "HttpDeclProperty",
    "docstring": "Details on the action required to continue the run. Will be `null` if no action is required.",
    "key": "required_action",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "submit_tool_outputs"
        },
        {
          "ident": "type"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) response_format": {
    "kind": "HttpDeclProperty",
    "docstring": "Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.\n\nSetting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).\n\nSetting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.\n\n**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if `finish_reason=\"length\"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.\n",
    "key": "response_format",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantResponseFormatOption",
      "$ref": "(resource) beta.threads > (model) assistant_response_format_option > (schema)"
    },
    "oasRef": "#/components/schemas/RunObject/properties/response_format",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads > (model) assistant_response_format_option",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 1",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 2",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 3"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) started_at": {
    "kind": "HttpDeclProperty",
    "docstring": "The Unix timestamp (in seconds) for when the run was started.",
    "key": "started_at",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/RunObject/properties/started_at",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.",
    "key": "status",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "queued"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "requires_action"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "cancelling"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "cancelled"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "expired"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/status"
    },
    "oasRef": "#/components/schemas/RunObject/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 1",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 2",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 3",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 4",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 5",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 6",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 7",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 8"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) thread_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.",
    "key": "thread_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/thread_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "docstring": "Controls which (if any) tool is called by the model.\n`none` means the model will not call any tools and instead generates a message.\n`auto` is the default value and means the model can pick between generating a message or calling one or more tools.\n`required` means the model must call one or more tools before responding to the user.\nSpecifying a particular tool like `{\"type\": \"file_search\"}` or `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}` forces the model to call that tool.\n",
    "key": "tool_choice",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantToolChoiceOption",
      "$ref": "(resource) beta.threads > (model) assistant_tool_choice_option > (schema)"
    },
    "oasRef": "#/components/schemas/RunObject/properties/tool_choice",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads > (model) assistant_tool_choice_option",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "docstring": "The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.",
    "key": "tools",
    "optional": false,
    "nullable": false,
    "default": [],
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "CodeInterpreterTool",
            "$ref": "(resource) beta.assistants > (model) code_interpreter_tool > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "FileSearchTool",
            "$ref": "(resource) beta.assistants > (model) file_search_tool > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "FunctionTool",
            "$ref": "(resource) beta.assistants > (model) function_tool > (schema)"
          }
        ],
        "oasRef": "#/components/schemas/RunObject/properties/tools/items"
      },
      "oasRef": "#/components/schemas/RunObject/properties/tools"
    },
    "oasRef": "#/components/schemas/RunObject/properties/tools",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 1",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 2"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy": {
    "kind": "HttpDeclProperty",
    "title": "Thread Truncation Controls",
    "docstring": "Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.",
    "key": "truncation_strategy",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "last_messages"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/truncation_strategy",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) last_messages"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage": {
    "kind": "HttpDeclProperty",
    "docstring": "Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).",
    "key": "usage",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "completion_tokens"
        },
        {
          "ident": "prompt_tokens"
        },
        {
          "ident": "total_tokens"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/usage",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) completion_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) prompt_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) total_tokens"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) temperature": {
    "kind": "HttpDeclProperty",
    "docstring": "The sampling temperature used for this run. If not set, defaults to 1.",
    "key": "temperature",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunObject/properties/temperature",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) top_p": {
    "kind": "HttpDeclProperty",
    "docstring": "The nucleus sampling value used for this run. If not set, defaults to 1.",
    "key": "top_p",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunObject/properties/top_p",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RunObject",
    "ident": "Run",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "assistant_id"
        },
        {
          "ident": "cancelled_at"
        },
        {
          "ident": "completed_at"
        },
        {
          "ident": "created_at"
        },
        {
          "ident": "expires_at"
        },
        {
          "ident": "failed_at"
        },
        {
          "ident": "incomplete_details"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "last_error"
        },
        {
          "ident": "max_completion_tokens"
        },
        {
          "ident": "max_prompt_tokens"
        },
        {
          "ident": "metadata"
        },
        {
          "ident": "model"
        },
        {
          "ident": "object"
        },
        {
          "ident": "parallel_tool_calls"
        },
        {
          "ident": "required_action"
        },
        {
          "ident": "response_format"
        },
        {
          "ident": "started_at"
        },
        {
          "ident": "status"
        },
        {
          "ident": "thread_id"
        },
        {
          "ident": "tool_choice"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "truncation_strategy"
        },
        {
          "ident": "usage"
        },
        {
          "ident": "temperature"
        },
        {
          "ident": "top_p"
        }
      ]
    },
    "docstring": "Represents an execution run on a [thread](/docs/api-reference/threads).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) assistant_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) cancelled_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) completed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) created_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) expires_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) failed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) instructions",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_completion_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) max_prompt_tokens",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) metadata",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) model",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) object",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) parallel_tool_calls",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) response_format",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) started_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) status",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) thread_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tool_choice",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) tools",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) usage",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) temperature",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) top_p"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 2 > (property) event > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "thread.run.queued"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason": {
    "kind": "HttpDeclProperty",
    "docstring": "The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.",
    "key": "reason",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "max_completion_tokens"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "max_prompt_tokens"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/incomplete_details/properties/reason"
    },
    "oasRef": "#/components/schemas/RunObject/properties/incomplete_details/properties/reason",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code": {
    "kind": "HttpDeclProperty",
    "docstring": "One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.",
    "key": "code",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "server_error"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "rate_limit_exceeded"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "invalid_prompt"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/last_error/properties/code"
    },
    "oasRef": "#/components/schemas/RunObject/properties/last_error/properties/code",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 1",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 2"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) message": {
    "kind": "HttpDeclProperty",
    "docstring": "A human-readable description of the error.",
    "key": "message",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunObject/properties/last_error/properties/message",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) metadata > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Metadata",
    "ident": "Metadata",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeString"
        }
      ],
      "oasRef": "#/components/schemas/Metadata"
    },
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard.\n\nKeys are strings with a maximum length of 64 characters. Values are strings\nwith a maximum length of 512 characters.\n",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "thread.run"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs": {
    "kind": "HttpDeclProperty",
    "docstring": "Details on the tool outputs needed for this run to continue.",
    "key": "submit_tool_outputs",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "tool_calls"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/submit_tool_outputs",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs > (property) tool_calls"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "For now, this is always `submit_tool_outputs`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "submit_tool_outputs"
        }
      ],
      "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/type"
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type > (member) 0"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption/oneOf/0"
    },
    "docstring": "`auto` is the default value\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0 > (member) 0"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseFormatText",
      "$ref": "(resource) $shared > (model) response_format_text > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_text > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseFormatJSONObject",
      "$ref": "(resource) $shared > (model) response_format_json_object > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_object > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseFormatJSONSchema",
      "$ref": "(resource) $shared > (model) response_format_json_schema > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption",
    "ident": "AssistantResponseFormatOption",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            }
          ],
          "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption/oneOf/0"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseFormatText",
          "$ref": "(resource) $shared > (model) response_format_text > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseFormatJSONObject",
          "$ref": "(resource) $shared > (model) response_format_json_object > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseFormatJSONSchema",
          "$ref": "(resource) $shared > (model) response_format_json_schema > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiResponseFormatOption"
    },
    "docstring": "Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.\n\nSetting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).\n\nSetting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.\n\n**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if `finish_reason=\"length\"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 1",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 2",
      "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 3"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "queued"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "requires_action"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "cancelling"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "cancelled"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) status > (member) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "expired"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "none"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "required"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption/oneOf/0"
    },
    "docstring": "`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 0",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 1",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 2"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantToolChoice",
      "$ref": "(resource) beta.threads > (model) assistant_tool_choice > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) function"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption",
    "ident": "AssistantToolChoiceOption",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "none"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "required"
            }
          ],
          "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption/oneOf/0"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "AssistantToolChoice",
          "$ref": "(resource) beta.threads > (model) assistant_tool_choice > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsApiToolChoiceOption"
    },
    "docstring": "Controls which (if any) tool is called by the model.\n`none` means the model will not call any tools and instead generates a message.\n`auto` is the default value and means the model can pick between generating a message or calling one or more tools.\n`required` means the model must call one or more tools before responding to the user.\nSpecifying a particular tool like `{\"type\": \"file_search\"}` or `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}` forces the model to call that tool.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0",
      "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "CodeInterpreterTool",
      "$ref": "(resource) beta.assistants > (model) code_interpreter_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FileSearchTool",
      "$ref": "(resource) beta.assistants > (model) file_search_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) tools > (items) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionTool",
      "$ref": "(resource) beta.assistants > (model) function_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) function",
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.assistants > (model) code_interpreter_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantToolsCode",
    "ident": "CodeInterpreterTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantToolsFileSearch",
    "ident": "FileSearchTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "file_search"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantToolsFunction",
    "ident": "FunctionTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "function"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) function",
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "last_messages"
        }
      ],
      "oasRef": "#/components/schemas/TruncationObject/properties/type"
    },
    "oasRef": "#/components/schemas/TruncationObject/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 0",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 1"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) last_messages": {
    "kind": "HttpDeclProperty",
    "docstring": "The number of most recent messages from the thread when constructing the context for the run.",
    "key": "last_messages",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 1
    },
    "oasRef": "#/components/schemas/TruncationObject/properties/last_messages",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) completion_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of completion tokens used over the course of the run.",
    "key": "completion_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunCompletionUsage/anyOf/0/properties/completion_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) prompt_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of prompt tokens used over the course of the run.",
    "key": "prompt_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunCompletionUsage/anyOf/0/properties/prompt_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) usage > (property) total_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Total number of tokens used (prompt + completion).",
    "key": "total_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RunCompletionUsage/anyOf/0/properties/total_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "max_completion_tokens"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details > (property) reason > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "max_prompt_tokens"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "server_error"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "rate_limit_exceeded"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error > (property) code > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "invalid_prompt"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) submit_tool_outputs > (property) tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "A list of the relevant tool calls.",
    "key": "tool_calls",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "RequiredActionFunctionToolCall",
        "$ref": "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema)"
      },
      "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/submit_tool_outputs/properties/tool_calls"
    },
    "oasRef": "#/components/schemas/RunObject/properties/required_action/properties/submit_tool_outputs/properties/tool_calls",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) required_action > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "submit_tool_outputs"
    }
  },
  "(resource) beta.threads > (model) assistant_response_format_option > (schema) > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) $shared > (model) response_format_text > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of response format being defined. Always `text`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "text"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatText/properties/type"
    },
    "oasRef": "#/components/schemas/ResponseFormatText/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) response_format_text > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) $shared > (model) response_format_text > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseFormatText",
    "ident": "ResponseFormatText",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Default response format. Used to generate text responses.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_text > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) response_format_json_object > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of response format being defined. Always `json_object`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "json_object"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatJsonObject/properties/type"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonObject/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) response_format_json_object > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) $shared > (model) response_format_json_object > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseFormatJsonObject",
    "ident": "ResponseFormatJSONObject",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "JSON object response format. An older method of generating JSON responses.\nUsing `json_schema` is recommended for models that support it. Note that the\nmodel will not generate JSON without a system or user message instructing it\nto do so.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_object > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema": {
    "kind": "HttpDeclProperty",
    "title": "JSON schema",
    "docstring": "Structured Outputs configuration options, including a JSON Schema.\n",
    "key": "json_schema",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "description"
        },
        {
          "ident": "schema"
        },
        {
          "ident": "strict"
        }
      ]
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) name",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) description",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) schema",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) strict"
    ]
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of response format being defined. Always `json_schema`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "json_schema"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/type"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) $shared > (model) response_format_json_schema > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema",
    "ident": "ResponseFormatJSONSchema",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "json_schema"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "JSON Schema response format. Used to generate structured JSON responses.\nLearn more about [Structured Outputs](/docs/guides/structured-outputs).\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema",
      "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_option > (schema) > (variant) 0 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "required"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the tool. If type is `function`, the function name must be set",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search"
        }
      ],
      "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 0",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 1",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 2"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) function": {
    "kind": "HttpDeclProperty",
    "key": "function",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AssistantToolChoiceFunction",
      "$ref": "(resource) beta.threads > (model) assistant_tool_choice_function > (schema)"
    },
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/function",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads > (model) assistant_tool_choice_function",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_function > (schema) > (property) name"
    ]
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice",
    "ident": "AssistantToolChoice",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "function"
        }
      ]
    },
    "docstring": "Specifies a tool the model should use. Use to force the model to call a specific tool.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type",
      "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) function"
    ]
  },
  "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool being defined: `code_interpreter`",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter"
        }
      ],
      "oasRef": "#/components/schemas/AssistantToolsCode/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantToolsCode/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool being defined: `file_search`",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search"
        }
      ],
      "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search": {
    "kind": "HttpDeclProperty",
    "docstring": "Overrides for the file search tool.",
    "key": "file_search",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "max_num_results"
        },
        {
          "ident": "ranking_options"
        }
      ]
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/file_search",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) max_num_results",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema) > (property) function": {
    "kind": "HttpDeclProperty",
    "key": "function",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionDefinition",
      "$ref": "(resource) $shared > (model) function_definition > (schema)"
    },
    "oasRef": "#/components/schemas/AssistantToolsFunction/properties/function",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) function_definition",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) function_definition > (schema) > (property) name",
      "(resource) $shared > (model) function_definition > (schema) > (property) description",
      "(resource) $shared > (model) function_definition > (schema) > (property) parameters",
      "(resource) $shared > (model) function_definition > (schema) > (property) strict"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool being defined: `function`",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ],
      "oasRef": "#/components/schemas/AssistantToolsFunction/properties/type"
    },
    "oasRef": "#/components/schemas/AssistantToolsFunction/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) function_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) beta.threads.runs > (model) run > (schema) > (property) truncation_strategy > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "last_messages"
    }
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](/docs/api-reference/runs/submitToolOutputs) endpoint.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function": {
    "kind": "HttpDeclProperty",
    "docstring": "The function definition.",
    "key": "function",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "arguments"
        },
        {
          "ident": "name"
        }
      ]
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/function",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) arguments",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) name"
    ]
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of tool call the output is required for. For now, this is always `function`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ],
      "oasRef": "#/components/schemas/RunToolCallObject/properties/type"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RunToolCallObject",
    "ident": "RequiredActionFunctionToolCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "function"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Tool call objects",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function",
      "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) response_format_text > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "text"
    }
  },
  "(resource) $shared > (model) response_format_json_object > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "json_object"
    }
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the response format. Must be a-z, A-Z, 0-9, or contain\nunderscores and dashes, with a maximum length of 64.\n",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) description": {
    "kind": "HttpDeclProperty",
    "docstring": "A description of what the response format is for, used by the model to\ndetermine how to respond in the format.\n",
    "key": "description",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/description",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) schema": {
    "kind": "HttpDeclProperty",
    "title": "JSON schema",
    "docstring": "The schema for the response format, described as a JSON Schema object.\nLearn how to build JSON schemas [here](https://json-schema.org/).\n",
    "key": "schema",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ],
      "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/schema"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/schema",
    "deprecated": false,
    "schemaType": "map",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) json_schema > (property) strict": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable strict schema adherence when generating the output.\nIf set to true, the model will always follow the exact schema defined\nin the `schema` field. Only a subset of JSON Schema is supported when\n`strict` is `true`. To learn more, read the [Structured Outputs\nguide](/docs/guides/structured-outputs).\n",
    "key": "strict",
    "optional": true,
    "nullable": true,
    "default": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/ResponseFormatJsonSchema/properties/json_schema/properties/strict",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) $shared > (model) response_format_json_schema > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "json_schema"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice > (schema) > (property) type > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search"
    }
  },
  "(resource) beta.threads > (model) assistant_tool_choice_function > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function to call.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/function/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads > (model) assistant_tool_choice_function > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AssistantsNamedToolChoice/properties/function",
    "ident": "AssistantToolChoiceFunction",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads > (model) assistant_tool_choice_function > (schema) > (property) name"
    ]
  },
  "(resource) beta.assistants > (model) code_interpreter_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) max_num_results": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.\n\nNote that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.\n",
    "key": "max_num_results",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 1,
      "maximum": 50
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/file_search/properties/max_num_results",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options": {
    "kind": "HttpDeclProperty",
    "title": "File search tool call ranking options",
    "docstring": "The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.\n\nSee the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.\n",
    "key": "ranking_options",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "score_threshold"
        },
        {
          "ident": "ranker"
        }
      ]
    },
    "oasRef": "#/components/schemas/AssistantToolsFileSearch/properties/file_search/properties/ranking_options",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) score_threshold",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker"
    ]
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) description": {
    "kind": "HttpDeclProperty",
    "docstring": "A description of what the function does, used by the model to choose when and how to call the function.",
    "key": "description",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/description",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) parameters": {
    "kind": "HttpDeclProperty",
    "docstring": "The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. \n\nOmitting `parameters` defines a function with an empty parameter list.",
    "key": "parameters",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionParameters",
      "$ref": "(resource) $shared > (model) function_parameters > (schema)"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/parameters",
    "deprecated": false,
    "schemaType": "map",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) function_parameters",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema) > (property) strict": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](/docs/guides/function-calling).",
    "key": "strict",
    "optional": true,
    "nullable": true,
    "default": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/FunctionObject/properties/strict",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) $shared > (model) function_definition > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/FunctionObject",
    "ident": "FunctionDefinition",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "description"
        },
        {
          "ident": "parameters"
        },
        {
          "ident": "strict"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) function_definition > (schema) > (property) name",
      "(resource) $shared > (model) function_definition > (schema) > (property) description",
      "(resource) $shared > (model) function_definition > (schema) > (property) parameters",
      "(resource) $shared > (model) function_definition > (schema) > (property) strict"
    ]
  },
  "(resource) beta.assistants > (model) function_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) arguments": {
    "kind": "HttpDeclProperty",
    "docstring": "The arguments that the model expects you to pass to the function.",
    "key": "arguments",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/function/properties/arguments",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) function > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RunToolCallObject/properties/function/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.threads.runs > (model) required_action_function_tool_call > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) score_threshold": {
    "kind": "HttpDeclProperty",
    "docstring": "The score threshold for the file search. All values must be a floating point number between 0 and 1.",
    "key": "score_threshold",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 1
    },
    "oasRef": "#/components/schemas/FileSearchRankingOptions/properties/score_threshold",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker": {
    "kind": "HttpDeclProperty",
    "docstring": "The ranker to use for the file search. If not specified will use the `auto` ranker.",
    "key": "ranker",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "default_2024_08_21"
        }
      ],
      "oasRef": "#/components/schemas/FileSearchRankingOptions/properties/ranker"
    },
    "oasRef": "#/components/schemas/FileSearchRankingOptions/properties/ranker",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 0",
      "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 1"
    ]
  },
  "(resource) $shared > (model) function_parameters > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/FunctionParameters",
    "ident": "FunctionParameters",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ],
      "oasRef": "#/components/schemas/FunctionParameters"
    },
    "docstring": "The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. \n\nOmitting `parameters` defines a function with an empty parameter list.",
    "children": []
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) beta.assistants > (model) file_search_tool > (schema) > (property) file_search > (property) ranking_options > (property) ranker > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default_2024_08_21"
    }
  }
}
```

### Example

```json
{}
```

## event

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

### Schema

Schema name: `(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 3`

```json
{
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/2",
    "ident": "UnionMember3",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "data"
        },
        {
          "ident": "event"
        }
      ]
    },
    "docstring": "Occurs when a [run](/docs/api-reference/runs/object) moves to an `in_progress` status.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 3 > (property) data",
      "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 3 > (property) event"
    ]
  },
  "(resource) beta.assistants > (model) assistant_stream_event > (schema) > (variant) 3 > (property) data": {
    "kind": "HttpDeclProperty",
    "title": "A run on a thread",
    "docstring": "Represents an execution run on a [thread](/docs/api-reference/threads).",
    "key": "data",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Run",
      "$ref": "(resource) beta.threads.runs > (model) run > (schema)"
    },
    "oasRef": "#/components/schemas/RunStreamEvent/oneOf/2/properties/data",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.threads.runs > (model) run",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.threads.runs > (model) run > (schema) > (property) id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) assistant_id",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) cancelled_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) completed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) created_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) expires_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) failed_at",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) incomplete_details",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) instructions",
      "(resource) beta.threads.runs > (model) run > (schema) > (property) last_error",
      "(resource) beta.threads.runs > (model) run > (sche

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/streaming-events.md
