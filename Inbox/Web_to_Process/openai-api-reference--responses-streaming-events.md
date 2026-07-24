---
source_url: https://developers.openai.com/api/reference/resources/responses/streaming-events.md
title: "Responses streaming events"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Responses streaming events

> OpenAI API streaming event reference.
When you [create a Response](https://developers.openai.com/docs/api-reference/responses/create) with
`stream` set to `true`, the server will emit server-sent events to the
client as the Response is generated. This section contains the events that
are emitted by the server.

[Learn more about streaming responses](https://developers.openai.com/docs/guides/streaming-responses?api-mode=responses).

## response.created

An event that is emitted when a response is created.

### Schema

Schema name: `ResponseCreatedEvent`

```json
{
  "(resource) responses > (model) response_created_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseCreatedEvent",
    "ident": "ResponseCreatedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "response"
        },
        {
          "ident": "sequence_number"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "An event that is emitted when a response is created.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_created_event > (schema) > (property) response",
      "(resource) responses > (model) response_created_event > (schema) > (property) sequence_number",
      "(resource) responses > (model) response_created_event > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response_created_event > (schema) > (property) response": {
    "kind": "HttpDeclProperty",
    "title": "The response object",
    "docstring": "The response that was created.\n",
    "key": "response",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Response",
      "$ref": "(resource) responses > (model) response > (schema)"
    },
    "oasRef": "#/components/schemas/ResponseCreatedEvent/properties/response",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) responses > (model) response",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) id",
      "(resource) responses > (model) response > (schema) > (property) created_at",
      "(resource) responses > (model) response > (schema) > (property) error",
      "(resource) responses > (model) response > (schema) > (property) incomplete_details",
      "(resource) responses > (model) response > (schema) > (property) instructions",
      "(resource) responses > (model) response > (schema) > (property) metadata",
      "(resource) responses > (model) response > (schema) > (property) model",
      "(resource) responses > (model) response > (schema) > (property) object",
      "(resource) responses > (model) response > (schema) > (property) output",
      "(resource) responses > (model) response > (schema) > (property) parallel_tool_calls",
      "(resource) responses > (model) response > (schema) > (property) temperature",
      "(resource) responses > (model) response > (schema) > (property) tool_choice",
      "(resource) responses > (model) response > (schema) > (property) tools",
      "(resource) responses > (model) response > (schema) > (property) top_p",
      "(resource) responses > (model) response > (schema) > (property) background",
      "(resource) responses > (model) response > (schema) > (property) completed_at",
      "(resource) responses > (model) response > (schema) > (property) conversation",
      "(resource) responses > (model) response > (schema) > (property) max_output_tokens",
      "(resource) responses > (model) response > (schema) > (property) max_tool_calls",
      "(resource) responses > (model) response > (schema) > (property) moderation",
      "(resource) responses > (model) response > (schema) > (property) output_text",
      "(resource) responses > (model) response > (schema) > (property) previous_response_id",
      "(resource) responses > (model) response > (schema) > (property) prompt",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_key",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_options",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_retention",
      "(resource) responses > (model) response > (schema) > (property) reasoning",
      "(resource) responses > (model) response > (schema) > (property) safety_identifier",
      "(resource) responses > (model) response > (schema) > (property) service_tier",
      "(resource) responses > (model) response > (schema) > (property) status",
      "(resource) responses > (model) response > (schema) > (property) text",
      "(resource) responses > (model) response > (schema) > (property) top_logprobs",
      "(resource) responses > (model) response > (schema) > (property) truncation",
      "(resource) responses > (model) response > (schema) > (property) usage",
      "(resource) responses > (model) response > (schema) > (property) user"
    ]
  },
  "(resource) responses > (model) response_created_event > (schema) > (property) sequence_number": {
    "kind": "HttpDeclProperty",
    "docstring": "The sequence number for this event.",
    "key": "sequence_number",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/ResponseCreatedEvent/properties/sequence_number",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_created_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the event. Always `response.created`.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "response.created"
        }
      ],
      "oasRef": "#/components/schemas/ResponseCreatedEvent/properties/type"
    },
    "oasRef": "#/components/schemas/ResponseCreatedEvent/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_created_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "Unique identifier for this Response.\n",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) created_at": {
    "kind": "HttpDeclProperty",
    "docstring": "Unix timestamp (in seconds) of when this Response was created.\n",
    "key": "created_at",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/created_at",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) error": {
    "kind": "HttpDeclProperty",
    "docstring": "An error object returned when the model fails to generate a Response.\n",
    "key": "error",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseError",
      "$ref": "(resource) responses > (model) response_error > (schema)"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/error",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) responses > (model) response_error",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_error > (schema) > (property) code",
      "(resource) responses > (model) response_error > (schema) > (property) message"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) incomplete_details": {
    "kind": "HttpDeclProperty",
    "docstring": "Details about why the response is incomplete.\n",
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
    "oasRef": "#/components/schemas/Response/allOf/2/properties/incomplete_details",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) incomplete_details > (property) reason"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "docstring": "A system (or developer) message inserted into the model's context.\n\nWhen using along with `previous_response_id`, the instructions from a previous\nresponse will not be carried over to the next response. This makes it simple\nto swap out system (or developer) messages in new responses.\n",
    "key": "instructions",
    "optional": false,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeArray",
          "elementType": {
            "kind": "HttpTypeUnion",
            "types": [
              {
                "kind": "HttpTypeReference",
                "ident": "EasyInputMessage",
                "$ref": "(resource) responses > (model) easy_input_message > (schema)"
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "content"
                  },
                  {
                    "ident": "role"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeReference",
                "ident": "ResponseOutputMessage",
                "$ref": "(resource) responses > (model) response_output_message > (schema)"
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "queries"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "results"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "pending_safety_checks"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "action"
                  },
                  {
                    "ident": "actions"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "output"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "acknowledged_safety_checks"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "action"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "arguments"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "name"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  },
                  {
                    "ident": "namespace"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "output"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "arguments"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "execution"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "tools"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "execution"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "role"
                  },
                  {
                    "ident": "tools"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "summary"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "content"
                  },
                  {
                    "ident": "encrypted_content"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "encrypted_content"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "result"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "code"
                  },
                  {
                    "ident": "container_id"
                  },
                  {
                    "ident": "outputs"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "action"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "output"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "action"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  },
                  {
                    "ident": "environment"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "output"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  },
                  {
                    "ident": "max_output_length"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "operation"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  },
                  {
                    "ident": "output"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "server_label"
                  },
                  {
                    "ident": "tools"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "error"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "arguments"
                  },
                  {
                    "ident": "name"
                  },
                  {
                    "ident": "server_label"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "approval_request_id"
                  },
                  {
                    "ident": "approve"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "reason"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "arguments"
                  },
                  {
                    "ident": "name"
                  },
                  {
                    "ident": "server_label"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "approval_request_id"
                  },
                  {
                    "ident": "error"
                  },
                  {
                    "ident": "output"
                  },
                  {
                    "ident": "status"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "output"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "input"
                  },
                  {
                    "ident": "name"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "caller"
                  },
                  {
                    "ident": "namespace"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "code"
                  },
                  {
                    "ident": "fingerprint"
                  },
                  {
                    "ident": "type"
                  }
                ]
              },
              {
                "kind": "HttpTypeObject",
                "members": [
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "call_id"
                  },
                  {
                    "ident": "result"
                  },
                  {
                    "ident": "status"
                  },
                  {
                    "ident": "type"
                  }
                ]
              }
            ],
            "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions/anyOf/0/oneOf/1/items"
          },
          "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions/anyOf/0/oneOf/1"
        }
      ],
      "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 0",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) metadata": {
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
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/metadata",
    "deprecated": false,
    "schemaType": "map",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) metadata",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "docstring": "Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI\noffers a wide range of models with different capabilities, performance\ncharacteristics, and price points. Refer to the [model guide](/docs/models)\nto browse and compare available models.\n",
    "key": "model",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponsesModel",
      "$ref": "(resource) $shared > (model) responses_model > (schema)"
    },
    "examples": [
      "gpt-5.1"
    ],
    "oasRef": "#/components/schemas/ResponseProperties/properties/model",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) responses_model",
    "childrenParentSchema": "union",
    "children": [
      "(resource) $shared > (model) responses_model > (schema) > (variant) 0",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "The object type of this resource - always set to `response`.\n",
    "key": "object",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "response"
        }
      ],
      "oasRef": "#/components/schemas/Response/allOf/2/properties/object"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) output": {
    "kind": "HttpDeclProperty",
    "docstring": "An array of content items generated by the model.\n\n- The length and order of items in the `output` array is dependent\n  on the model's response.\n- Rather than accessing the first item in the `output` array and\n  assuming it's an `assistant` message with the content generated by\n  the model, you might consider using the `output_text` property where\n  supported in SDKs.\n",
    "key": "output",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "ResponseOutputItem",
        "$ref": "(resource) responses > (model) response_output_item > (schema)"
      },
      "oasRef": "#/components/schemas/Response/allOf/2/properties/output"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/output",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 0",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 1",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 4",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 8",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 9",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 12",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 13",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 14",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 16",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 17",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 23",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 24",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 25",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to allow the model to run tool calls in parallel.\n",
    "key": "parallel_tool_calls",
    "optional": false,
    "nullable": false,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/parallel_tool_calls",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) temperature": {
    "kind": "HttpDeclProperty",
    "docstring": "What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.\nWe generally recommend altering this or `top_p` but not both.\n",
    "key": "temperature",
    "optional": false,
    "nullable": true,
    "default": 1,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 2
    },
    "examples": [
      1
    ],
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/temperature",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "docstring": "How the model should select which tool (or tools) to use when generating\na response. See the `tools` parameter to see how to specify which tools\nthe model can call.\n",
    "key": "tool_choice",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceOptions",
          "$ref": "(resource) responses > (model) tool_choice_options > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceAllowed",
          "$ref": "(resource) responses > (model) tool_choice_allowed > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceTypes",
          "$ref": "(resource) responses > (model) tool_choice_types > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceFunction",
          "$ref": "(resource) responses > (model) tool_choice_function > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceMcp",
          "$ref": "(resource) responses > (model) tool_choice_mcp > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceCustom",
          "$ref": "(resource) responses > (model) tool_choice_custom > (schema)"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceApplyPatch",
          "$ref": "(resource) responses > (model) tool_choice_apply_patch > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceShell",
          "$ref": "(resource) responses > (model) tool_choice_shell > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/ResponseProperties/properties/tool_choice"
    },
    "oasRef": "#/components/schemas/ResponseProperties/properties/tool_choice",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 0",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 1",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 2",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 3",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 4",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 5",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 6",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 7",
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 8"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "docstring": "An array of tools the model may call while generating a response. You\ncan specify which tool to use by setting the `tool_choice` parameter.\n\nWe support the following categories of tools:\n- **Built-in tools**: Tools that are provided by OpenAI that extend the\n  model's capabilities, like [web search](/docs/guides/tools-web-search)\n  or [file search](/docs/guides/tools-file-search). Learn more about\n  [built-in tools](/docs/guides/tools).\n- **MCP Tools**: Integrations with third-party systems via custom MCP servers\n  or predefined connectors such as Google Drive and SharePoint. Learn more about\n  [MCP Tools](/docs/guides/tools-connectors-mcp).\n- **Function calls (custom tools)**: Functions that are defined by you,\n  enabling the model to call your own code with strongly typed arguments\n  and outputs. Learn more about\n  [function calling](/docs/guides/function-calling). You can also use\n  custom tools to call your own code.\n",
    "key": "tools",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "parameters"
              },
              {
                "ident": "strict"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "output_schema"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "vector_store_ids"
              },
              {
                "ident": "filters"
              },
              {
                "ident": "max_num_results"
              },
              {
                "ident": "ranking_options"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "display_height"
              },
              {
                "ident": "display_width"
              },
              {
                "ident": "environment"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "filters"
              },
              {
                "ident": "search_context_size"
              },
              {
                "ident": "user_location"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "server_label"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "allowed_tools"
              },
              {
                "ident": "authorization"
              },
              {
                "ident": "connector_id"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "headers"
              },
              {
                "ident": "require_approval"
              },
              {
                "ident": "server_description"
              },
              {
                "ident": "server_url"
              },
              {
                "ident": "tunnel_id"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "container"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "action"
              },
              {
                "ident": "background"
              },
              {
                "ident": "input_fidelity"
              },
              {
                "ident": "input_image_mask"
              },
              {
                "ident": "model"
              },
              {
                "ident": "moderation"
              },
              {
                "ident": "output_compression"
              },
              {
                "ident": "output_format"
              },
              {
                "ident": "partial_images"
              },
              {
                "ident": "quality"
              },
              {
                "ident": "size"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "environment"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "format"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "description"
              },
              {
                "ident": "name"
              },
              {
                "ident": "tools"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "description"
              },
              {
                "ident": "execution"
              },
              {
                "ident": "parameters"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "search_content_types"
              },
              {
                "ident": "search_context_size"
              },
              {
                "ident": "user_location"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              }
            ]
          }
        ],
        "oasRef": "#/components/schemas/Tool"
      },
      "oasRef": "#/components/schemas/ResponseProperties/properties/tools"
    },
    "oasRef": "#/components/schemas/ResponseProperties/properties/tools",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 0",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 1",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 2",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 3",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 4",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 5",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 6",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 7",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 8",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 9",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 10",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 11",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 12",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 13",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 14",
      "(resource) responses > (model) response > (schema) > (property) tools > (items) > (variant) 15"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) top_p": {
    "kind": "HttpDeclProperty",
    "docstring": "An alternative to sampling with temperature, called nucleus sampling,\nwhere the model considers the results of the tokens with top_p probability\nmass. So 0.1 means only the tokens comprising the top 10% probability mass\nare considered.\n\nWe generally recommend altering this or `temperature` but not both.\n",
    "key": "top_p",
    "optional": false,
    "nullable": true,
    "default": 1,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 1
    },
    "examples": [
      1
    ],
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/top_p",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) background": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to run the model response in the background.\n[Learn more](/docs/guides/background).\n",
    "key": "background",
    "optional": true,
    "nullable": true,
    "default": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/ResponseProperties/properties/background",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) completed_at": {
    "kind": "HttpDeclProperty",
    "docstring": "Unix timestamp (in seconds) of when this Response was completed.\nOnly present when the status is `completed`.\n",
    "key": "completed_at",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "unixtime"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/completed_at",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) conversation": {
    "kind": "HttpDeclProperty",
    "title": "Conversation",
    "docstring": "The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.",
    "key": "conversation",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        }
      ]
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/conversation",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) conversation > (property) id"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) max_output_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](/docs/guides/reasoning).\n",
    "key": "max_output_tokens",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/max_output_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) max_tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.\n",
    "key": "max_tool_calls",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/ResponseProperties/properties/max_tool_calls",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) moderation": {
    "kind": "HttpDeclProperty",
    "title": "Moderation",
    "docstring": "Moderation results for the response input and output, if moderated completions were requested.\n",
    "key": "moderation",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "input"
        },
        {
          "ident": "output"
        }
      ]
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/moderation",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) moderation > (property) input",
      "(resource) responses > (model) response > (schema) > (property) moderation > (property) output"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) output_text": {
    "kind": "HttpDeclProperty",
    "docstring": "SDK-only convenience property that contains the aggregated text output\nfrom all `output_text` items in the `output` array, if any are present.\nSupported in the Python and JavaScript SDKs.\n",
    "key": "output_text",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/output_text",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) previous_response_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the previous response to the model. Use this to\ncreate multi-turn conversations. Learn more about\n[conversation state](/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.\n",
    "key": "previous_response_id",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ResponseProperties/properties/previous_response_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) prompt": {
    "kind": "HttpDeclProperty",
    "docstring": "Reference to a prompt template and its variables.\n[Learn more](/docs/guides/text?api-mode=responses#reusable-prompts).\n",
    "key": "prompt",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponsePrompt",
      "$ref": "(resource) responses > (model) response_prompt > (schema)"
    },
    "oasRef": "#/components/schemas/ResponseProperties/properties/prompt",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) responses > (model) response_prompt",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_prompt > (schema) > (property) id",
      "(resource) responses > (model) response_prompt > (schema) > (property) variables",
      "(resource) responses > (model) response_prompt > (schema) > (property) version"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) prompt_cache_key": {
    "kind": "HttpDeclProperty",
    "docstring": "Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](/docs/guides/prompt-caching).\n",
    "key": "prompt_cache_key",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "prompt-cache-key-1234"
    ],
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/prompt_cache_key",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) prompt_cache_options": {
    "kind": "HttpDeclProperty",
    "title": "Prompt cache options",
    "docstring": "The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.",
    "key": "prompt_cache_options",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        },
        {
          "ident": "ttl"
        }
      ]
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/prompt_cache_options",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_options > (property) mode",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_options > (property) ttl"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) prompt_cache_retention": {
    "kind": "HttpDeclProperty",
    "docstring": "Deprecated. Use `prompt_cache_options.ttl` instead.\n\nThe retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](/docs/guides/prompt-caching#prompt-cache-retention).\nThis field expresses a maximum retention policy, while\n`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two\nfields are independent and do not interact.\nFor `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.\n\nFor older models that support both `in_memory` and `24h`, the default depends on your organization's data retention policy:\n  - Organizations without ZDR enabled default to `24h`.\n  - Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.\n",
    "key": "prompt_cache_retention",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_memory"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "24h"
        }
      ],
      "oasRef": "#/components/schemas/ModelResponseProperties/properties/prompt_cache_retention"
    },
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/prompt_cache_retention",
    "deprecated": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_retention > (member) 0",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_retention > (member) 1"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) reasoning": {
    "kind": "HttpDeclProperty",
    "title": "Reasoning",
    "docstring": "**gpt-5 and o-series models only**\n\nConfiguration options for\n[reasoning models](https://platform.openai.com/docs/guides/reasoning).\n",
    "key": "reasoning",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Reasoning",
      "$ref": "(resource) $shared > (model) reasoning > (schema)"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/reasoning",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) $shared > (model) reasoning",
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) reasoning > (schema) > (property) context",
      "(resource) $shared > (model) reasoning > (schema) > (property) effort",
      "(resource) $shared > (model) reasoning > (schema) > (property) generate_summary",
      "(resource) $shared > (model) reasoning > (schema) > (property) mode",
      "(resource) $shared > (model) reasoning > (schema) > (property) summary"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) safety_identifier": {
    "kind": "HttpDeclProperty",
    "docstring": "A stable identifier used to help detect users of your application that may be violating OpenAI's usage policies.\nThe IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](/docs/guides/safety-best-practices#safety-identifiers).\n",
    "key": "safety_identifier",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 64
    },
    "examples": [
      "safety-identifier-1234"
    ],
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/safety_identifier",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) service_tier": {
    "kind": "HttpDeclProperty",
    "docstring": "Specifies the processing type used for serving the request.\n  - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.\n  - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.\n  - If set to '[flex](/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.\n  - When not set, the default behavior is 'auto'.\n\n  When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.\n",
    "key": "service_tier",
    "optional": true,
    "nullable": true,
    "default": "auto",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "default"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "flex"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "scale"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "priority"
        }
      ],
      "oasRef": "#/components/schemas/ModelResponseProperties/properties/service_tier"
    },
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/service_tier",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) service_tier > (member) 0",
      "(resource) responses > (model) response > (schema) > (property) service_tier > (member) 1",
      "(resource) responses > (model) response > (schema) > (property) service_tier > (member) 2",
      "(resource) responses > (model) response > (schema) > (property) service_tier > (member) 3",
      "(resource) responses > (model) response > (schema) > (property) service_tier > (member) 4"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the response generation. One of `completed`, `failed`,\n`in_progress`, `cancelled`, `queued`, or `incomplete`.\n",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseStatus",
      "$ref": "(resource) responses > (model) response_status > (schema)"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "modelImplicit": false,
    "modelPath": "(resource) responses > (model) response_status",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_status > (schema) > (member) 0",
      "(resource) responses > (model) response_status > (schema) > (member) 1",
      "(resource) responses > (model) response_status > (schema) > (member) 2",
      "(resource) responses > (model) response_status > (schema) > (member) 3",
      "(resource) responses > (model) response_status > (schema) > (member) 4",
      "(resource) responses > (model) response_status > (schema) > (member) 5"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration options for a text response from the model. Can be plain\ntext or structured JSON data. Learn more:\n- [Text inputs and outputs](/docs/guides/text)\n- [Structured Outputs](/docs/guides/structured-outputs)\n",
    "key": "text",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseTextConfig",
      "$ref": "(resource) responses > (model) response_text_config > (schema)"
    },
    "oasRef": "#/components/schemas/ResponseProperties/properties/text",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) responses > (model) response_text_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_text_config > (schema) > (property) format",
      "(resource) responses > (model) response_text_config > (schema) > (property) verbosity"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) top_logprobs": {
    "kind": "HttpDeclProperty",
    "docstring": "An integer between 0 and 20 specifying the maximum number of most likely\ntokens to return at each token position, each with an associated log\nprobability. In some cases, the number of returned tokens may be fewer than\nrequested.\n",
    "key": "top_logprobs",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 20
    },
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/top_logprobs",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) truncation": {
    "kind": "HttpDeclProperty",
    "docstring": "The truncation strategy to use for the model response.\n- `auto`: If the input to this Response exceeds\n  the model's context window size, the model will truncate the\n  response to fit the context window by dropping items from the beginning of the conversation.\n- `disabled` (default): If the input size will exceed the context window\n  size for a model, the request will fail with a 400 error.\n",
    "key": "truncation",
    "optional": true,
    "nullable": true,
    "default": "disabled",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "disabled"
        }
      ],
      "oasRef": "#/components/schemas/Response/allOf/2/properties/truncation"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/truncation",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) truncation > (member) 0",
      "(resource) responses > (model) response > (schema) > (property) truncation > (member) 1"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) usage": {
    "kind": "HttpDeclProperty",
    "docstring": "Represents token usage details including input tokens, output tokens,\na breakdown of output tokens, and the total tokens used.\n",
    "key": "usage",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseUsage",
      "$ref": "(resource) responses > (model) response_usage > (schema)"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/usage",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) responses > (model) response_usage",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_usage > (schema) > (property) input_tokens",
      "(resource) responses > (model) response_usage > (schema) > (property) input_tokens_details",
      "(resource) responses > (model) response_usage > (schema) > (property) output_tokens",
      "(resource) responses > (model) response_usage > (schema) > (property) output_tokens_details",
      "(resource) responses > (model) response_usage > (schema) > (property) total_tokens"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) user": {
    "kind": "HttpDeclProperty",
    "docstring": "This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.\nA stable identifier for your end-users.\nUsed to boost cache hit rates by better bucketing similar requests and  to help OpenAI detect and prevent abuse. [Learn more](/docs/guides/safety-best-practices#safety-identifiers).\n",
    "key": "user",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "user-1234"
    ],
    "oasRef": "#/components/schemas/ModelResponseProperties/properties/user",
    "deprecated": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Response",
    "ident": "Response",
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
          "ident": "error"
        },
        {
          "ident": "incomplete_details"
        },
        {
          "ident": "instructions"
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
          "ident": "output"
        },
        {
          "ident": "parallel_tool_calls"
        },
        {
          "ident": "temperature"
        },
        {
          "ident": "tool_choice"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "top_p"
        },
        {
          "ident": "background"
        },
        {
          "ident": "completed_at"
        },
        {
          "ident": "conversation"
        },
        {
          "ident": "max_output_tokens"
        },
        {
          "ident": "max_tool_calls"
        },
        {
          "ident": "moderation"
        },
        {
          "ident": "output_text"
        },
        {
          "ident": "previous_response_id"
        },
        {
          "ident": "prompt"
        },
        {
          "ident": "prompt_cache_key"
        },
        {
          "ident": "prompt_cache_options"
        },
        {
          "ident": "prompt_cache_retention"
        },
        {
          "ident": "reasoning"
        },
        {
          "ident": "safety_identifier"
        },
        {
          "ident": "service_tier"
        },
        {
          "ident": "status"
        },
        {
          "ident": "text"
        },
        {
          "ident": "top_logprobs"
        },
        {
          "ident": "truncation"
        },
        {
          "ident": "usage"
        },
        {
          "ident": "user"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) id",
      "(resource) responses > (model) response > (schema) > (property) created_at",
      "(resource) responses > (model) response > (schema) > (property) error",
      "(resource) responses > (model) response > (schema) > (property) incomplete_details",
      "(resource) responses > (model) response > (schema) > (property) instructions",
      "(resource) responses > (model) response > (schema) > (property) metadata",
      "(resource) responses > (model) response > (schema) > (property) model",
      "(resource) responses > (model) response > (schema) > (property) object",
      "(resource) responses > (model) response > (schema) > (property) output",
      "(resource) responses > (model) response > (schema) > (property) parallel_tool_calls",
      "(resource) responses > (model) response > (schema) > (property) temperature",
      "(resource) responses > (model) response > (schema) > (property) tool_choice",
      "(resource) responses > (model) response > (schema) > (property) tools",
      "(resource) responses > (model) response > (schema) > (property) top_p",
      "(resource) responses > (model) response > (schema) > (property) background",
      "(resource) responses > (model) response > (schema) > (property) completed_at",
      "(resource) responses > (model) response > (schema) > (property) conversation",
      "(resource) responses > (model) response > (schema) > (property) max_output_tokens",
      "(resource) responses > (model) response > (schema) > (property) max_tool_calls",
      "(resource) responses > (model) response > (schema) > (property) moderation",
      "(resource) responses > (model) response > (schema) > (property) output_text",
      "(resource) responses > (model) response > (schema) > (property) previous_response_id",
      "(resource) responses > (model) response > (schema) > (property) prompt",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_key",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_options",
      "(resource) responses > (model) response > (schema) > (property) prompt_cache_retention",
      "(resource) responses > (model) response > (schema) > (property) reasoning",
      "(resource) responses > (model) response > (schema) > (property) safety_identifier",
      "(resource) responses > (model) response > (schema) > (property) service_tier",
      "(resource) responses > (model) response > (schema) > (property) status",
      "(resource) responses > (model) response > (schema) > (property) text",
      "(resource) responses > (model) response > (schema) > (property) top_logprobs",
      "(resource) responses > (model) response > (schema) > (property) truncation",
      "(resource) responses > (model) response > (schema) > (property) usage",
      "(resource) responses > (model) response > (schema) > (property) user"
    ]
  },
  "(resource) responses > (model) response_created_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "response.created"
    }
  },
  "(resource) responses > (model) response_error > (schema) > (property) code": {
    "kind": "HttpDeclProperty",
    "docstring": "The error code for the response.\n",
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
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "data_residency_mismatch"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "bio_policy"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "vector_store_timeout"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "invalid_image"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "invalid_image_format"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "invalid_base64_image"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "invalid_image_url"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_too_large"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_too_small"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_parse_error"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_content_policy_violation"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "invalid_image_mode"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_file_too_large"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "unsupported_image_media_type"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "empty_image_file"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed_to_download_image"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_file_not_found"
        }
      ],
      "oasRef": "#/components/schemas/ResponseError/anyOf/0/properties/code"
    },
    "oasRef": "#/components/schemas/ResponseError/anyOf/0/properties/code",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 0",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 1",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 2",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 3",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 4",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 5",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 6",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 7",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 8",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 9",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 10",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 11",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 12",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 13",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 14",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 15",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 16",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 17",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 18",
      "(resource) responses > (model) response_error > (schema) > (property) code > (member) 19"
    ]
  },
  "(resource) responses > (model) response_error > (schema) > (property) message": {
    "kind": "HttpDeclProperty",
    "docstring": "A human-readable description of the error.\n",
    "key": "message",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ResponseError/anyOf/0/properties/message",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_error > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponseError",
    "ident": "ResponseError",
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
    "docstring": "An error object returned when the model fails to generate a Response.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_error > (schema) > (property) code",
      "(resource) responses > (model) response_error > (schema) > (property) message"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) incomplete_details > (property) reason": {
    "kind": "HttpDeclProperty",
    "docstring": "The reason why the response is incomplete.",
    "key": "reason",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "max_output_tokens"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "content_filter"
        }
      ],
      "oasRef": "#/components/schemas/Response/allOf/2/properties/incomplete_details/anyOf/0/properties/reason"
    },
    "oasRef": "#/components/schemas/Response/allOf/2/properties/incomplete_details/anyOf/0/properties/reason",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) incomplete_details > (property) reason > (member) 0",
      "(resource) responses > (model) response > (schema) > (property) incomplete_details > (property) reason > (member) 1"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions/anyOf/0/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "docstring": "A text input to the model, equivalent to a text input with the\n`developer` role.\n",
    "children": []
  },
  "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions/anyOf/0/oneOf/1",
    "ident": "InputItemList",
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "EasyInputMessage",
            "$ref": "(resource) responses > (model) easy_input_message > (schema)"
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "content"
              },
              {
                "ident": "role"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseOutputMessage",
            "$ref": "(resource) responses > (model) response_output_message > (schema)"
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "queries"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              },
              {
                "ident": "results"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "pending_safety_checks"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              },
              {
                "ident": "action"
              },
              {
                "ident": "actions"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "call_id"
              },
              {
                "ident": "output"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "acknowledged_safety_checks"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "action"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "arguments"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "name"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              },
              {
                "ident": "namespace"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "call_id"
              },
              {
                "ident": "output"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "arguments"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "execution"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "tools"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "execution"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "role"
              },
              {
                "ident": "tools"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "summary"
              },
              {
                "ident": "type"
              },
              {
                "ident": "content"
              },
              {
                "ident": "encrypted_content"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "encrypted_content"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "result"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "code"
              },
              {
                "ident": "container_id"
              },
              {
                "ident": "outputs"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "action"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "output"
              },
              {
                "ident": "type"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "action"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              },
              {
                "ident": "environment"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "call_id"
              },
              {
                "ident": "output"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              },
              {
                "ident": "max_output_length"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "call_id"
              },
              {
                "ident": "operation"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "call_id"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              },
              {
                "ident": "output"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "server_label"
              },
              {
                "ident": "tools"
              },
              {
                "ident": "type"
              },
              {
                "ident": "error"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "arguments"
              },
              {
                "ident": "name"
              },
              {
                "ident": "server_label"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "approval_request_id"
              },
              {
                "ident": "approve"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "reason"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "arguments"
              },
              {
                "ident": "name"
              },
              {
                "ident": "server_label"
              },
              {
                "ident": "type"
              },
              {
                "ident": "approval_request_id"
              },
              {
                "ident": "error"
              },
              {
                "ident": "output"
              },
              {
                "ident": "status"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "call_id"
              },
              {
                "ident": "output"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "call_id"
              },
              {
                "ident": "input"
              },
              {
                "ident": "name"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "caller"
              },
              {
                "ident": "namespace"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "code"
              },
              {
                "ident": "fingerprint"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "id"
              },
              {
                "ident": "call_id"
              },
              {
                "ident": "result"
              },
              {
                "ident": "status"
              },
              {
                "ident": "type"
              }
            ]
          }
        ],
        "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions/anyOf/0/oneOf/1/items"
      },
      "oasRef": "#/components/schemas/Response/allOf/2/properties/instructions/anyOf/0/oneOf/1"
    },
    "docstring": "A list of one or many input items to the model, containing\ndifferent content types.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 0",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 1",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 2",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 3",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 4",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 5",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 6",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 7",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 8",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 9",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 10",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 11",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 12",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 13",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 14",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 15",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 16",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 17",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 18",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 19",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 20",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 21",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 22",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 23",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 24",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 25",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 26",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 27",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 28",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 29",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 30",
      "(resource) responses > (model) response > (schema) > (property) instructions > (variant) 1 > (items) > (variant) 31"
    ]
  },
  "(resource) responses > (model) easy_input_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/EasyInputMessage",
    "ident": "EasyInputMessage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content"
        },
        {
          "ident": "role"
        },
        {
          "ident": "phase"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "A message input to the model with a role indicating instruction following\nhierarchy. Instructions given with the `developer` or `system` role take\nprecedence over instructions given with the `user` role. Messages with the\n`assistant` role are presumed to have been generated by the model in previous\ninteractions.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) easy_input_message > (schema) > (property) content",
      "(resource) responses > (model) easy_input_message > (schema) > (property) role",
      "(resource) responses > (model) easy_input_message > (schema) > (property) phase",
      "(resource) responses > (model) easy_input_message > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputMessage",
    "ident": "ResponseOutputMessage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "content"
        },
        {
          "ident": "role"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "phase"
        }
      ]
    },
    "docstring": "An output message from the model.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) id",
      "(resource) responses > (model) response_output_message > (schema) > (property) content",
      "(resource) responses > (model) response_output_message > (schema) > (property) role",
      "(resource) responses > (model) response_output_message > (schema) > (property) status",
      "(resource) responses > (model) response_output_message > (schema) > (property) type",
      "(resource) responses > (model) response_output_message > (schema) > (property) phase"
    ]
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
  "(resource) $shared > (model) responses_model > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsShared/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) $shared > (model) responses_model > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsShared/anyOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.6-sol"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.6-terra"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.6-luna"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.4"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.4-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.4-nano"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.4-mini-2026-03-17"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.4-nano-2026-03-17"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.3-chat-latest"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.2"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.2-2025-12-11"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.2-chat-latest"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.2-pro"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.2-pro-2025-12-11"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.1"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.1-2025-11-13"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.1-codex"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.1-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.1-chat-latest"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-nano"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-2025-08-07"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-mini-2025-08-07"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-nano-2025-08-07"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-chat-latest"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4.1"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4.1-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4.1-nano"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4.1-2025-04-14"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4.1-mini-2025-04-14"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4.1-nano-2025-04-14"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o4-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o4-mini-2025-04-16"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3-2025-04-16"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3-mini-2025-01-31"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1-2024-12-17"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1-preview-2024-09-12"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1-mini-2024-09-12"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-2024-11-20"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-2024-08-06"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-2024-05-13"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-audio-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-audio-preview-2024-10-01"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-audio-preview-2024-12-17"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-audio-preview-2025-06-03"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-audio-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-audio-preview-2024-12-17"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-search-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-search-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-search-preview-2025-03-11"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-search-preview-2025-03-11"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "chatgpt-4o-latest"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "codex-mini-latest"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-2024-07-18"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-turbo"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-turbo-2024-04-09"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-0125-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-turbo-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-1106-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-vision-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-0314"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-0613"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-32k"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-32k-0314"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4-32k-0613"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-3.5-turbo"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-3.5-turbo-16k"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-3.5-turbo-0301"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-3.5-turbo-0613"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-3.5-turbo-1106"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-3.5-turbo-0125"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-3.5-turbo-16k-0613"
        }
      ],
      "oasRef": "#/components/schemas/ModelIdsShared/anyOf/1"
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 0",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 1",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 2",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 3",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 4",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 5",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 6",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 7",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 8",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 9",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 10",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 11",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 12",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 13",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 14",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 15",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 16",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 17",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 18",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 19",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 20",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 21",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 22",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 23",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 24",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 25",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 26",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 27",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 28",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 29",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 30",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 31",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 32",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 33",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 34",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 35",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 36",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 37",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 38",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 39",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 40",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 41",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 42",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 43",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 44",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 45",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 46",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 47",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 48",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 49",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 50",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 51",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 52",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 53",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 54",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 55",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 56",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 57",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 58",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 59",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 60",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 61",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 62",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 63",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 64",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 65",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 66",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 67",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 68",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 69",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 70",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 71",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 72",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 73",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 74",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 75",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 76",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 77",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 78",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 79",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1 > (member) 80"
    ]
  },
  "(resource) $shared > (model) responses_model > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsResponses/anyOf/1",
    "ident": "ResponsesOnlyModel",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1-pro"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o1-pro-2025-03-19"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3-pro"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3-pro-2025-06-10"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3-deep-research"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o3-deep-research-2025-06-26"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o4-mini-deep-research"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "o4-mini-deep-research-2025-06-26"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer-use-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer-use-preview-2025-03-11"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-codex"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-pro"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5-pro-2025-10-06"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-5.1-codex-max"
        }
      ],
      "oasRef": "#/components/schemas/ModelIdsResponses/anyOf/1"
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 0",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 1",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 2",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 3",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 4",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 5",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 6",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 7",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 8",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 9",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 10",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 11",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 12",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2 > (member) 13"
    ]
  },
  "(resource) $shared > (model) responses_model > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsResponses",
    "ident": "ResponsesModel",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.6-sol"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.6-terra"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.6-luna"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.4"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.4-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.4-nano"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.4-mini-2026-03-17"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.4-nano-2026-03-17"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.3-chat-latest"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.2"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.2-2025-12-11"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.2-chat-latest"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.2-pro"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.2-pro-2025-12-11"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.1"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.1-2025-11-13"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.1-codex"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.1-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.1-chat-latest"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-nano"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-2025-08-07"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-mini-2025-08-07"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-nano-2025-08-07"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-chat-latest"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4.1"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4.1-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4.1-nano"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4.1-2025-04-14"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4.1-mini-2025-04-14"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4.1-nano-2025-04-14"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o4-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o4-mini-2025-04-16"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3-2025-04-16"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3-mini-2025-01-31"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1-2024-12-17"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1-preview-2024-09-12"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1-mini-2024-09-12"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-2024-11-20"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-2024-08-06"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-2024-05-13"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-audio-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-audio-preview-2024-10-01"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-audio-preview-2024-12-17"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-audio-preview-2025-06-03"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-audio-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-audio-preview-2024-12-17"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-search-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-search-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-search-preview-2025-03-11"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-search-preview-2025-03-11"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "chatgpt-4o-latest"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "codex-mini-latest"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-2024-07-18"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-turbo"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-turbo-2024-04-09"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-0125-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-turbo-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-1106-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-vision-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-0314"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-0613"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-32k"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-32k-0314"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4-32k-0613"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-3.5-turbo"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-3.5-turbo-16k"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-3.5-turbo-0301"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-3.5-turbo-0613"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-3.5-turbo-1106"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-3.5-turbo-0125"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-3.5-turbo-16k-0613"
            }
          ],
          "oasRef": "#/components/schemas/ModelIdsShared/anyOf/1"
        },
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1-pro"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o1-pro-2025-03-19"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3-pro"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3-pro-2025-06-10"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3-deep-research"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o3-deep-research-2025-06-26"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o4-mini-deep-research"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "o4-mini-deep-research-2025-06-26"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "computer-use-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "computer-use-preview-2025-03-11"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-codex"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-pro"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5-pro-2025-10-06"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-5.1-codex-max"
            }
          ],
          "oasRef": "#/components/schemas/ModelIdsResponses/anyOf/1"
        }
      ],
      "oasRef": "#/components/schemas/ModelIdsResponses"
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) $shared > (model) responses_model > (schema) > (variant) 0",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 1",
      "(resource) $shared > (model) responses_model > (schema) > (variant) 2"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "response"
    }
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseOutputMessage",
      "$ref": "(resource) responses > (model) response_output_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) id",
      "(resource) responses > (model) response_output_message > (schema) > (property) content",
      "(resource) responses > (model) response_output_message > (schema) > (property) role",
      "(resource) responses > (model) response_output_message > (schema) > (property) status",
      "(resource) responses > (model) response_output_message > (schema) > (property) type",
      "(resource) responses > (model) response_output_message > (schema) > (property) phase"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/1",
    "ident": "FileSearchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "queries"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "results"
        }
      ]
    },
    "docstring": "The results of a file search tool call. See the\n[file search guide](/docs/guides/tools-file-search) for more information.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 1 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 1 > (property) queries",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 1 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 1 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 1 > (property) results"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/2",
    "ident": "FunctionCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "arguments"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "namespace"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A tool call to run a function. See the \n[function calling guide](/docs/guides/function-calling) for more information.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) arguments",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) name",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) namespace",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2 > (property) status"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/3",
    "ident": "FunctionCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3 > (property) output",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 4": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/4",
    "ident": "WebSearchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "action"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "The results of a web search tool call. See the\n[web search guide](/docs/guides/tools-web-search) for more information.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 4 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 4 > (property) action",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 4 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 4 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 5": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/5",
    "ident": "ComputerCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "pending_safety_checks"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "action"
        },
        {
          "ident": "actions"
        }
      ]
    },
    "docstring": "A tool call to a computer use tool. See the\n[computer use guide](/docs/guides/tools-computer-use) for more information.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5 > (property) pending_safety_checks",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5 > (property) action",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5 > (property) actions"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/6",
    "ident": "ComputerCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "acknowledged_safety_checks"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6 > (property) output",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6 > (property) acknowledged_safety_checks",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 7": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/7",
    "ident": "Reasoning",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "summary"
        },
        {
          "ident": "type"
        },
        {
          "ident": "content"
        },
        {
          "ident": "encrypted_content"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A description of the chain of thought used by a reasoning model while generating\na response. Be sure to include these items in your `input` to the Responses API\nfor subsequent turns of a conversation if you are manually\n[managing context](/docs/guides/conversation-state).\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7 > (property) summary",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7 > (property) content",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7 > (property) encrypted_content",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7 > (property) status"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 8": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/8",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "code"
        },
        {
          "ident": "fingerprint"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 8 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 8 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 8 > (property) code",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 8 > (property) fingerprint",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 8 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 9": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/9",
    "ident": "ProgramOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "result"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 9 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 9 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 9 > (property) result",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 9 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 9 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 10": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/10",
    "ident": "ToolSearchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "arguments"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "execution"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10 > (property) arguments",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10 > (property) execution",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 11": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/11",
    "ident": "ToolSearchOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "execution"
        },
        {
          "ident": "status"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11 > (property) execution",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11 > (property) tools",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 12": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/12",
    "ident": "AdditionalTools",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "role"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 12 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 12 > (property) role",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 12 > (property) tools",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 12 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 13": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/13",
    "ident": "Compaction",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "encrypted_content"
        },
        {
          "ident": "type"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "docstring": "A compaction item generated by the [`v1/responses/compact` API](/docs/api-reference/responses/compact).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 13 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 13 > (property) encrypted_content",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 13 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 13 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 14": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/14",
    "ident": "ImageGenerationCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "result"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "An image generation request made by the model.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 14 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 14 > (property) result",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 14 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 14 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 15": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/15",
    "ident": "CodeInterpreterCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "code"
        },
        {
          "ident": "container_id"
        },
        {
          "ident": "outputs"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "A tool call to run code.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15 > (property) code",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15 > (property) container_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15 > (property) outputs",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 16": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/16",
    "ident": "LocalShellCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "action"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "A tool call to run a command on the local shell.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 16 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 16 > (property) action",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 16 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 16 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 16 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 17": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/17",
    "ident": "LocalShellCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "type"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "The output of a local shell tool call.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 17 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 17 > (property) output",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 17 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 17 > (property) status"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 18": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/18",
    "ident": "ShellCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "action"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "environment"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "docstring": "A tool call that executes one or more shell commands in a managed environment.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) action",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) environment",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 19": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/19",
    "ident": "ShellCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "max_output_length"
        },
        {
          "ident": "output"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "docstring": "The output of a shell tool call that was emitted.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) max_output_length",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) output",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 20": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/20",
    "ident": "ApplyPatchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "operation"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "docstring": "A tool call that applies file diffs by creating, deleting, or updating files.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20 > (property) operation",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 21": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/21",
    "ident": "ApplyPatchCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "created_by"
        },
        {
          "ident": "output"
        }
      ]
    },
    "docstring": "The output emitted by an apply patch tool call.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21 > (property) created_by",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21 > (property) output"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 22": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/22",
    "ident": "McpCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "arguments"
        },
        {
          "ident": "name"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        },
        {
          "ident": "approval_request_id"
        },
        {
          "ident": "error"
        },
        {
          "ident": "output"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "An invocation of a tool on an MCP server.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) arguments",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) name",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) server_label",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) approval_request_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) error",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) output",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22 > (property) status"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 23": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/23",
    "ident": "McpListTools",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        },
        {
          "ident": "error"
        }
      ]
    },
    "docstring": "A list of tools available on an MCP server.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 23 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 23 > (property) server_label",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 23 > (property) tools",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 23 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 23 > (property) error"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 24": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/24",
    "ident": "McpApprovalRequest",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "arguments"
        },
        {
          "ident": "name"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "A request for human approval of a tool invocation.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 24 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 24 > (property) arguments",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 24 > (property) name",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 24 > (property) server_label",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 24 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 25": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/25",
    "ident": "McpApprovalResponse",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "approval_request_id"
        },
        {
          "ident": "approve"
        },
        {
          "ident": "type"
        },
        {
          "ident": "reason"
        }
      ]
    },
    "docstring": "A response to an MCP approval request.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 25 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 25 > (property) approval_request_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 25 > (property) approve",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 25 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 25 > (property) reason"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 26": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/26",
    "ident": "CustomToolCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "call_id"
        },
        {
          "ident": "input"
        },
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "namespace"
        }
      ]
    },
    "docstring": "A call to a custom tool created by the model.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26 > (property) input",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26 > (property) name",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26 > (property) namespace"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema) > (variant) 27": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem/oneOf/27",
    "ident": "CustomToolCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "created_by"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27 > (property) id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27 > (property) call_id",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27 > (property) output",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27 > (property) status",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27 > (property) type",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27 > (property) caller",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27 > (property) created_by"
    ]
  },
  "(resource) responses > (model) response_output_item > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputItem",
    "ident": "ResponseOutputItem",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseOutputMessage",
          "$ref": "(resource) responses > (model) response_output_message > (schema)"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "queries"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "results"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "arguments"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "name"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "namespace"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "action"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "pending_safety_checks"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "action"
            },
            {
              "ident": "actions"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "acknowledged_safety_checks"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "summary"
            },
            {
              "ident": "type"
            },
            {
              "ident": "content"
            },
            {
              "ident": "encrypted_content"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "code"
            },
            {
              "ident": "fingerprint"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "result"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "arguments"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "execution"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "execution"
            },
            {
              "ident": "status"
            },
            {
              "ident": "tools"
            },
            {
              "ident": "type"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "role"
            },
            {
              "ident": "tools"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "encrypted_content"
            },
            {
              "ident": "type"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "result"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "code"
            },
            {
              "ident": "container_id"
            },
            {
              "ident": "outputs"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "action"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "type"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "action"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "environment"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "max_output_length"
            },
            {
              "ident": "output"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "operation"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "created_by"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "created_by"
            },
            {
              "ident": "output"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "arguments"
            },
            {
              "ident": "name"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "type"
            },
            {
              "ident": "approval_request_id"
            },
            {
              "ident": "error"
            },
            {
              "ident": "output"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "tools"
            },
            {
              "ident": "type"
            },
            {
              "ident": "error"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "arguments"
            },
            {
              "ident": "name"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "approval_request_id"
            },
            {
              "ident": "approve"
            },
            {
              "ident": "type"
            },
            {
              "ident": "reason"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "call_id"
            },
            {
              "ident": "input"
            },
            {
              "ident": "name"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "namespace"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "created_by"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/OutputItem"
    },
    "docstring": "An output message from the model.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_output_item > (schema) > (variant) 0",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 1",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 2",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 3",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 4",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 5",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 6",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 7",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 8",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 9",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 10",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 11",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 12",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 13",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 14",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 15",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 16",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 17",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 18",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 19",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 20",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 21",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 22",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 23",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 24",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 25",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 26",
      "(resource) responses > (model) response_output_item > (schema) > (variant) 27"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceOptions",
      "$ref": "(resource) responses > (model) tool_choice_options > (schema)"
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) tool_choice_options > (schema) > (member) 0",
      "(resource) responses > (model) tool_choice_options > (schema) > (member) 1",
      "(resource) responses > (model) tool_choice_options > (schema) > (member) 2"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceAllowed",
      "$ref": "(resource) responses > (model) tool_choice_allowed > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_allowed > (schema) > (property) mode",
      "(resource) responses > (model) tool_choice_allowed > (schema) > (property) tools",
      "(resource) responses > (model) tool_choice_allowed > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceTypes",
      "$ref": "(resource) responses > (model) tool_choice_types > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_types > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceFunction",
      "$ref": "(resource) responses > (model) tool_choice_function > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_function > (schema) > (property) name",
      "(resource) responses > (model) tool_choice_function > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceMcp",
      "$ref": "(resource) responses > (model) tool_choice_mcp > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_mcp > (schema) > (property) server_label",
      "(resource) responses > (model) tool_choice_mcp > (schema) > (property) type",
      "(resource) responses > (model) tool_choice_mcp > (schema) > (property) name"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceCustom",
      "$ref": "(resource) responses > (model) tool_choice_custom > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_custom > (schema) > (property) name",
      "(resource) responses > (model) tool_choice_custom > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolChoiceParam/oneOf/6",
    "ident": "SpecificProgrammaticToolCallingParam",
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
      "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 6 > (property) type"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceApplyPatch",
      "$ref": "(resource) responses > (model) tool_choice_apply_patch > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_apply_patch > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property) tool_choice > (variant) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ToolChoiceShell",
      "$ref": "(resource) responses > (model) tool_choice_shell > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_shell > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) tool_choice_options > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolChoiceOptions",
    "ident": "ToolChoiceOptions",
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
      "oasRef": "#/components/schemas/ToolChoiceOptions"
    },
    "docstring": "Controls which (if any) tool is called by the model.\n\n`none` means the model will not call any tool and instead generates a message.\n\n`auto` means the model can pick between generating a message or calling one or\nmore tools.\n\n`required` means the model must call one or more tools.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) tool_choice_options > (schema) > (member) 0",
      "(resource) responses > (model) tool_choice_options > (schema) > (member) 1",
      "(resource) responses > (model) tool_choice_options > (schema) > (member) 2"
    ]
  },
  "(resource) responses > (model) tool_choice_allowed > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolChoiceAllowed",
    "ident": "ToolChoiceAllowed",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Constrains the tools available to the model to a pre-defined set.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_allowed > (schema) > (property) mode",
      "(resource) responses > (model) tool_choice_allowed > (schema) > (property) tools",
      "(resource) responses > (model) tool_choice_allowed > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) tool_choice_types > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolChoiceTypes",
    "ident": "ToolChoiceTypes",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Indicates that the model should use a built-in tool to generate a response.\n[Learn more about built-in tools](/docs/guides/tools).\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_types > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) tool_choice_function > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolChoiceFunction",
    "ident": "ToolChoiceFunction",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Use this option to force the model to call a specific function.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_function > (schema) > (property) name",
      "(resource) responses > (model) tool_choice_function > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) tool_choice_mcp > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolChoiceMCP",
    "ident": "ToolChoiceMcp",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        },
        {
          "ident": "name"
        }
      ]
    },
    "docstring": "Use this option to force the model to call a specific tool on a remote MCP server.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_mcp > (schema) > (property) server_label",
      "(resource) responses > (model) tool_choice_mcp > (schema) > (property) type",
      "(resource) responses > (model) tool_choice_mcp > (schema) > (property) name"
    ]
  },
  "(resource) responses > (model) tool_choice_custom > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolChoiceCustom",
    "ident": "ToolChoiceCustom",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Use this option to force the model to call a specific custom tool.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_custom > (schema) > (property) name",
      "(resource) responses > (model) tool_choice_custom > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) tool_choice_apply_patch > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/SpecificApplyPatchParam",
    "ident": "ToolChoiceApplyPatch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Forces the model to call the apply_patch tool when executing a tool call.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_apply_patch > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) tool_choice_shell > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/SpecificFunctionShellParam",
    "ident": "ToolChoiceShell",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Forces the model to call the shell tool when a tool call is required.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) tool_choice_shell > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response > (schema) > (property

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/responses/streaming-events.md
