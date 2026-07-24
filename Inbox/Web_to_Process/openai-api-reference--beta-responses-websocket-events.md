---
source_url: https://developers.openai.com/api/reference/resources/beta/subresources/responses/websocket-events.md
title: "Beta Responses WebSocket events"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Beta Responses WebSocket events

> OpenAI API streaming event reference.
Send client events and receive server events over a persistent Responses API WebSocket connection. [Learn more about WebSocket mode.](https://developers.openai.com/api/docs/guides/websocket-mode)

## Client events

Events sent by the client over a Responses API WebSocket connection.

### response.create

Client event for creating a response over a persistent WebSocket connection.
This payload uses the same top-level fields as `POST /v1/responses`.

Notes:
- `stream` is implicit over WebSocket and should not be sent.
- `background` is not supported over WebSocket.

#### Schema

Schema name: `BetaResponsesClientEventResponseCreate`

```json
{
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaResponsesClientEvent/anyOf/0",
    "ident": "ResponseCreate",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "background"
        },
        {
          "ident": "context_management"
        },
        {
          "ident": "conversation"
        },
        {
          "ident": "include"
        },
        {
          "ident": "input"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "max_output_tokens"
        },
        {
          "ident": "max_tool_calls"
        },
        {
          "ident": "metadata"
        },
        {
          "ident": "model"
        },
        {
          "ident": "moderation"
        },
        {
          "ident": "multi_agent"
        },
        {
          "ident": "parallel_tool_calls"
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
          "ident": "store"
        },
        {
          "ident": "stream"
        },
        {
          "ident": "stream_options"
        },
        {
          "ident": "temperature"
        },
        {
          "ident": "text"
        },
        {
          "ident": "tool_choice"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "top_logprobs"
        },
        {
          "ident": "top_p"
        },
        {
          "ident": "truncation"
        },
        {
          "ident": "user"
        }
      ]
    },
    "docstring": "Client event for creating a response over a persistent WebSocket connection.\nThis payload uses the same top-level fields as `POST /v1/responses`.\n\nNotes:\n- `stream` is implicit over WebSocket and should not be sent.\n- `background` is not supported over WebSocket.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) background",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) context_management",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) conversation",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) include",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) instructions",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) max_output_tokens",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) max_tool_calls",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) metadata",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) multi_agent",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) parallel_tool_calls",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) previous_response_id",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_key",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_retention",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) safety_identifier",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) store",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) stream",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) stream_options",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) temperature",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) text",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) top_logprobs",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) top_p",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) truncation",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) user"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the client event. Always `response.create`.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "response.create"
        }
      ],
      "oasRef": "#/components/schemas/BetaResponsesClientEventResponseCreate/allOf/0/properties/type"
    },
    "oasRef": "#/components/schemas/BetaResponsesClientEventResponseCreate/allOf/0/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) background": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to run the model response in the background.\n[Learn more](/docs/guides/background).\n",
    "key": "background",
    "optional": true,
    "nullable": true,
    "default": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/background",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) context_management": {
    "kind": "HttpDeclProperty",
    "docstring": "Context management configuration for this request.\n",
    "key": "context_management",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "type"
          },
          {
            "ident": "compact_threshold"
          }
        ]
      },
      "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/context_management"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/context_management",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) context_management > (items) > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) context_management > (items) > (property) compact_threshold"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) conversation": {
    "kind": "HttpDeclProperty",
    "docstring": "The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.\nInput items and output items from this response are automatically added to this conversation after this response completes.\n",
    "key": "conversation",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "BetaResponseConversationParam",
          "$ref": "(resource) beta.responses > (model) beta_response_conversation_param > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/conversation"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/conversation",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) conversation > (variant) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) conversation > (variant) 1"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) include": {
    "kind": "HttpDeclProperty",
    "docstring": "Specify additional output data to include in the model response. Currently supported values are:\n- `web_search_call.action.sources`: Include the sources of the web search tool call.\n- `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.\n- `computer_call_output.output.image_url`: Include image urls from the computer call output.\n- `file_search_call.results`: Include the search results of the file search tool call.\n- `message.input_image.image_url`: Include image urls from the input message.\n- `message.output_text.logprobs`: Include logprobs with assistant messages.\n- `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).",
    "key": "include",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "BetaResponseIncludable",
        "$ref": "(resource) beta.responses > (model) beta_response_includable > (schema)"
      },
      "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/include"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/include",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 0",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 1",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 2",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 3",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 4",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 5",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 6",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 7"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input": {
    "kind": "HttpDeclProperty",
    "docstring": "Text, image, or file inputs to the model, used to generate a response.\n\nLearn more:\n- [Text inputs and outputs](/docs/guides/text)\n- [Image inputs](/docs/guides/images)\n- [File inputs](/docs/guides/pdf-files)\n- [Conversation state](/docs/guides/conversation-state)\n- [Function calling](/docs/guides/function-calling)\n",
    "key": "input",
    "optional": true,
    "nullable": false,
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
                "ident": "BetaEasyInputMessage",
                "$ref": "(resource) beta.responses > (model) beta_easy_input_message > (schema)"
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
                    "ident": "agent"
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
                "ident": "BetaResponseOutputMessage",
                "$ref": "(resource) beta.responses > (model) beta_response_output_message > (schema)"
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
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "author"
                  },
                  {
                    "ident": "content"
                  },
                  {
                    "ident": "recipient"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "agent"
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
                    "ident": "arguments"
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
                    "ident": "agent"
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
                    "ident": "output"
                  },
                  {
                    "ident": "type"
                  },
                  {
                    "ident": "id"
                  },
                  {
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
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
                  },
                  {
                    "ident": "agent"
                  }
                ]
              }
            ],
            "oasRef": "#/components/schemas/BetaInputParam/oneOf/1/items"
          },
          "oasRef": "#/components/schemas/BetaInputParam/oneOf/1"
        }
      ],
      "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/input"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/input",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) instructions": {
    "kind": "HttpDeclProperty",
    "docstring": "A system (or developer) message inserted into the model's context.\n\nWhen using along with `previous_response_id`, the instructions from a previous\nresponse will not be carried over to the next response. This makes it simple\nto swap out system (or developer) messages in new responses.\n",
    "key": "instructions",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/instructions",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) max_output_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](/docs/guides/reasoning).\n",
    "key": "max_output_tokens",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 16
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/max_output_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) max_tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.\n",
    "key": "max_tool_calls",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/max_tool_calls",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) metadata": {
    "kind": "HttpDeclProperty",
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard.\n\nKeys are strings with a maximum length of 64 characters. Values are strings\nwith a maximum length of 512 characters.\n",
    "key": "metadata",
    "optional": true,
    "nullable": true,
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
      "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/metadata"
    },
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/metadata",
    "deprecated": false,
    "schemaType": "map",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model": {
    "kind": "HttpDeclProperty",
    "docstring": "Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI\noffers a wide range of models with different capabilities, performance\ncharacteristics, and price points. Refer to the [model guide](/docs/models)\nto browse and compare available models.\n",
    "key": "model",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
            },
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
          ]
        },
        {
          "kind": "HttpTypeString"
        }
      ],
      "oasRef": "#/components/schemas/BetaResponseProperties/properties/model"
    },
    "examples": [
      "gpt-5.1"
    ],
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/model",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 1"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for running moderation on the input and output of this response.\n",
    "key": "moderation",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "model"
        },
        {
          "ident": "policy"
        }
      ]
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/moderation",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation > (property) model",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation > (property) policy"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) multi_agent": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for server-hosted multi-agent execution.",
    "key": "multi_agent",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "enabled"
        },
        {
          "ident": "max_concurrent_subagents"
        }
      ]
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/multi_agent",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) multi_agent > (property) enabled",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) multi_agent > (property) max_concurrent_subagents"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to allow the model to run tool calls in parallel.\n",
    "key": "parallel_tool_calls",
    "optional": true,
    "nullable": true,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/parallel_tool_calls",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) previous_response_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the previous response to the model. Use this to\ncreate multi-turn conversations. Learn more about\n[conversation state](/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.\n",
    "key": "previous_response_id",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/previous_response_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt": {
    "kind": "HttpDeclProperty",
    "docstring": "Reference to a prompt template and its variables.\n[Learn more](/docs/guides/text?api-mode=responses#reusable-prompts).\n",
    "key": "prompt",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaResponsePrompt",
      "$ref": "(resource) beta.responses > (model) beta_response_prompt > (schema)"
    },
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/prompt",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.responses > (model) beta_response_prompt",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) id",
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) variables",
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) version"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_key": {
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
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/prompt_cache_key",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options": {
    "kind": "HttpDeclProperty",
    "title": "Prompt cache options",
    "docstring": "Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](/docs/guides/prompt-caching) for current details.",
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
    "oasRef": "#/components/schemas/BetaCreateModelResponseProperties/allOf/1/properties/prompt_cache_options",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options > (property) mode",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options > (property) ttl"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_retention": {
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
      "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/prompt_cache_retention"
    },
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/prompt_cache_retention",
    "deprecated": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_retention > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_retention > (member) 1"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning": {
    "kind": "HttpDeclProperty",
    "title": "Reasoning",
    "docstring": "**gpt-5 and o-series models only**\n\nConfiguration options for\n[reasoning models](https://platform.openai.com/docs/guides/reasoning).\n",
    "key": "reasoning",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "context"
        },
        {
          "ident": "effort"
        },
        {
          "ident": "generate_summary"
        },
        {
          "ident": "mode"
        },
        {
          "ident": "summary"
        }
      ]
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/reasoning",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) context",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) generate_summary",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) mode",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) summary"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) safety_identifier": {
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
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/safety_identifier",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier": {
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
      "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/service_tier"
    },
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/service_tier",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 2",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 3",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 4"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) store": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to store the generated model response for later retrieval via\nAPI.\n",
    "key": "store",
    "optional": true,
    "nullable": true,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/store",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) stream": {
    "kind": "HttpDeclProperty",
    "docstring": "If set to true, the model response data will be streamed to the client\nas it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).\nSee the [Streaming section below](/docs/api-reference/responses-streaming)\nfor more information.\n",
    "key": "stream",
    "optional": true,
    "nullable": true,
    "default": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/stream",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) stream_options": {
    "kind": "HttpDeclProperty",
    "docstring": "Options for streaming responses. Only set this when you set `stream: true`.\n",
    "key": "stream_options",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "include_obfuscation"
        }
      ]
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/stream_options",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) stream_options > (property) include_obfuscation"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) temperature": {
    "kind": "HttpDeclProperty",
    "docstring": "What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.\nWe generally recommend altering this or `top_p` but not both.\n",
    "key": "temperature",
    "optional": true,
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
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/temperature",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) text": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration options for a text response from the model. Can be plain\ntext or structured JSON data. Learn more:\n- [Text inputs and outputs](/docs/guides/text)\n- [Structured Outputs](/docs/guides/structured-outputs)\n",
    "key": "text",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaResponseTextConfig",
      "$ref": "(resource) beta.responses > (model) beta_response_text_config > (schema)"
    },
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/text",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) beta.responses > (model) beta_response_text_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) format",
      "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) verbosity"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "docstring": "How the model should select which tool (or tools) to use when generating\na response. See the `tools` parameter to see how to specify which tools\nthe model can call.\n",
    "key": "tool_choice",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "BetaToolChoiceOptions",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_options > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "BetaToolChoiceAllowed",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "BetaToolChoiceTypes",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_types > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "BetaToolChoiceFunction",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_function > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "BetaToolChoiceMcp",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "BetaToolChoiceCustom",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_custom > (schema)"
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
          "ident": "BetaToolChoiceApplyPatch",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_apply_patch > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "BetaToolChoiceShell",
          "$ref": "(resource) beta.responses > (model) beta_tool_choice_shell > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/BetaResponseProperties/properties/tool_choice"
    },
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/tool_choice",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 2",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 3",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 4",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 5",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 6",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 7",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 8"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools": {
    "kind": "HttpDeclProperty",
    "docstring": "An array of tools the model may call while generating a response. You\ncan specify which tool to use by setting the `tool_choice` parameter.\n\nWe support the following categories of tools:\n- **Built-in tools**: Tools that are provided by OpenAI that extend the\n  model's capabilities, like [web search](/docs/guides/tools-web-search)\n  or [file search](/docs/guides/tools-file-search). Learn more about\n  [built-in tools](/docs/guides/tools).\n- **MCP Tools**: Integrations with third-party systems via custom MCP servers\n  or predefined connectors such as Google Drive and SharePoint. Learn more about\n  [MCP Tools](/docs/guides/tools-connectors-mcp).\n- **Function calls (custom tools)**: Functions that are defined by you,\n  enabling the model to call your own code with strongly typed arguments\n  and outputs. Learn more about\n  [function calling](/docs/guides/function-calling). You can also use\n  custom tools to call your own code.\n",
    "key": "tools",
    "optional": true,
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
        "oasRef": "#/components/schemas/BetaTool"
      },
      "oasRef": "#/components/schemas/BetaResponseProperties/properties/tools"
    },
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/tools",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 2",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 3",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 4",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 6",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 7",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 9",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 10",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 11",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 12",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 13",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 14",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 15"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) top_logprobs": {
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
    "oasRef": "#/components/schemas/BetaCreateModelResponseProperties/allOf/1/properties/top_logprobs",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) top_p": {
    "kind": "HttpDeclProperty",
    "docstring": "An alternative to sampling with temperature, called nucleus sampling,\nwhere the model considers the results of the tokens with top_p probability\nmass. So 0.1 means only the tokens comprising the top 10% probability mass\nare considered.\n\nWe generally recommend altering this or `temperature` but not both.\n",
    "key": "top_p",
    "optional": true,
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
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/top_p",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) truncation": {
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
      "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/truncation"
    },
    "oasRef": "#/components/schemas/BetaCreateResponse/allOf/2/properties/truncation",
    "deprecated": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) truncation > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) truncation > (member) 1"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) user": {
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
    "oasRef": "#/components/schemas/BetaModelResponseProperties/properties/user",
    "deprecated": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "response.create"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) context_management > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The context management entry type. Currently only 'compaction' is supported.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/BetaContextManagementParam/properties/type",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) context_management > (items) > (property) compact_threshold": {
    "kind": "HttpDeclProperty",
    "docstring": "Token threshold at which compaction should be triggered for this entry.",
    "key": "compact_threshold",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 1000
    },
    "oasRef": "#/components/schemas/BetaContextManagementParam/properties/compact_threshold",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) conversation > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaConversationParam/oneOf/0",
    "ident": "ConversationID",
    "type": {
      "kind": "HttpTypeString"
    },
    "docstring": "The unique ID of the conversation.\n",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) conversation > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaResponseConversationParam",
      "$ref": "(resource) beta.responses > (model) beta_response_conversation_param > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_response_conversation_param > (schema) > (property) id"
    ]
  },
  "(resource) beta.responses > (model) beta_response_conversation_param > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaConversationParam-2",
    "ident": "BetaResponseConversationParam",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        }
      ]
    },
    "docstring": "The conversation that this response belongs to.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_response_conversation_param > (schema) > (property) id"
    ]
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search_call.results"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_call.results"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_call.action.sources"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message.input_image.image_url"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer_call_output.output.image_url"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter_call.outputs"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "reasoning.encrypted_content"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message.output_text.logprobs"
    }
  },
  "(resource) beta.responses > (model) beta_response_includable > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaIncludeEnum",
    "ident": "BetaResponseIncludable",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search_call.results"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search_call.results"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search_call.action.sources"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "message.input_image.image_url"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer_call_output.output.image_url"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter_call.outputs"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "reasoning.encrypted_content"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "message.output_text.logprobs"
        }
      ],
      "oasRef": "#/components/schemas/BetaIncludeEnum"
    },
    "docstring": "Specify additional output data to include in the model response. Currently supported values are:\n- `web_search_call.results`: Include the search results of the web search tool call.\n- `web_search_call.action.sources`: Include the sources of the web search tool call.\n- `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.\n- `computer_call_output.output.image_url`: Include image urls from the computer call output.\n- `file_search_call.results`: Include the search results of the file search tool call.\n- `message.input_image.image_url`: Include image urls from the input message.\n- `message.output_text.logprobs`: Include logprobs with assistant messages.\n- `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 0",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 1",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 2",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 3",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 4",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 5",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 6",
      "(resource) beta.responses > (model) beta_response_includable > (schema) > (member) 7"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaInputParam/oneOf/0",
    "ident": "TextInput",
    "type": {
      "kind": "HttpTypeString"
    },
    "docstring": "A text input to the model, equivalent to a text input with the\n`user` role.\n",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaInputParam/oneOf/1",
    "ident": "InputItemList",
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "BetaEasyInputMessage",
            "$ref": "(resource) beta.responses > (model) beta_easy_input_message > (schema)"
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
                "ident": "agent"
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
            "ident": "BetaResponseOutputMessage",
            "$ref": "(resource) beta.responses > (model) beta_response_output_message > (schema)"
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
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "author"
              },
              {
                "ident": "content"
              },
              {
                "ident": "recipient"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "agent"
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
                "ident": "arguments"
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
                "ident": "agent"
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
                "ident": "output"
              },
              {
                "ident": "type"
              },
              {
                "ident": "id"
              },
              {
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
                "ident": "agent"
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
              },
              {
                "ident": "agent"
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
              },
              {
                "ident": "agent"
              }
            ]
          }
        ],
        "oasRef": "#/components/schemas/BetaInputParam/oneOf/1/items"
      },
      "oasRef": "#/components/schemas/BetaInputParam/oneOf/1"
    },
    "docstring": "A list of one or many input items to the model, containing\ndifferent content types.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 2",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 3",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 4",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 5",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 6",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 7",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 8",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 9",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 10",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 11",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 12",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 13",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 14",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 15",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 16",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 17",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 18",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 19",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 20",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 21",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 22",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 23",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 24",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 25",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 26",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 27",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 28",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 29",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 30",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 31",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 32",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 33",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) input > (variant) 1 > (items) > (variant) 34"
    ]
  },
  "(resource) beta.responses > (model) beta_easy_input_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaEasyInputMessage",
    "ident": "BetaEasyInputMessage",
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
      "(resource) beta.responses > (model) beta_easy_input_message > (schema) > (property) content",
      "(resource) beta.responses > (model) beta_easy_input_message > (schema) > (property) role",
      "(resource) beta.responses > (model) beta_easy_input_message > (schema) > (property) phase",
      "(resource) beta.responses > (model) beta_easy_input_message > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_response_output_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaOutputMessage",
    "ident": "BetaResponseOutputMessage",
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
          "ident": "agent"
        },
        {
          "ident": "phase"
        }
      ]
    },
    "docstring": "An output message from the model.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_response_output_message > (schema) > (property) id",
      "(resource) beta.responses > (model) beta_response_output_message > (schema) > (property) content",
      "(resource) beta.responses > (model) beta_response_output_message > (schema) > (property) role",
      "(resource) beta.responses > (model) beta_response_output_message > (schema) > (property) status",
      "(resource) beta.responses > (model) beta_response_output_message > (schema) > (property) type",
      "(resource) beta.responses > (model) beta_response_output_message > (schema) > (property) agent",
      "(resource) beta.responses > (model) beta_response_output_message > (schema) > (property) phase"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "ident": "UnionMember0",
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
        },
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
      ]
    },
    "docstring": "Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI\noffers a wide range of models with different capabilities, performance\ncharacteristics, and price points. Refer to the [model guide](/docs/models)\nto browse and compare available models.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 2",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 3",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 4",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 5",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 6",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 7",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 8",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 9",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 10",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 11",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 12",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 13",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 14",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 15",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 16",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 17",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 18",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 19",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 20",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 21",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 22",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 23",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 24",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 25",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 26",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 27",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 28",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 29",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 30",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 31",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 32",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 33",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 34",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 35",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 36",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 37",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 38",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 39",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 40",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 41",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 42",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 43",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 44",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 45",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 46",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 47",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 48",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 49",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 50",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 51",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 52",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 53",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 54",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 55",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 56",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 57",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 58",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 59",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 60",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 61",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 62",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 63",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 64",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 65",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 66",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 67",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 68",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 69",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 70",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 71",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 72",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 73",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 74",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 75",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 76",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 77",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 78",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 79",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 80",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 81",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 82",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 83",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 84",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 85",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 86",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 87",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 88",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 89",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 90",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 91",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 92",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 93",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 0 > (member) 94"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaModelIdsShared/anyOf/0",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation > (property) model": {
    "kind": "HttpDeclProperty",
    "docstring": "The moderation model to use for moderated completions, e.g. 'omni-moderation-latest'.",
    "key": "model",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/BetaModerationParam/properties/model",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation > (property) policy": {
    "kind": "HttpDeclProperty",
    "docstring": "The policy to apply to moderated response input and output.",
    "key": "policy",
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
    "oasRef": "#/components/schemas/BetaModerationParam/properties/policy",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation > (property) policy > (property) input",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) moderation > (property) policy > (property) output"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) multi_agent > (property) enabled": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether to enable server-hosted multi-agent execution for this response.",
    "key": "enabled",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/BetaMultiAgentParam/properties/enabled",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) multi_agent > (property) max_concurrent_subagents": {
    "kind": "HttpDeclProperty",
    "docstring": "`max_concurrent_subagents` sets the maximum number of subagents that can be active simultaneously across the entire agent tree. It includes all descendants—children, grandchildren, and deeper subagents—but excludes the root agent.\nThe API does not impose a fixed upper bound on this setting. The default is `3`, which is recommended for most workloads. Multi-agent runs also have no fixed limit on tree depth or the total number of subagents created during a run.",
    "key": "max_concurrent_subagents",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 1
    },
    "oasRef": "#/components/schemas/BetaMultiAgentParam/properties/max_concurrent_subagents",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique identifier of the prompt template to use.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/BetaPrompt/anyOf/0/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) variables": {
    "kind": "HttpDeclProperty",
    "title": "Prompt Variables",
    "docstring": "Optional map of values to substitute in for variables in your\nprompt. The substitution values can either be strings, or other\nResponse input types like images or files.\n",
    "key": "variables",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeString"
            },
            {
              "kind": "HttpTypeReference",
              "ident": "BetaResponseInputText",
              "$ref": "(resource) beta.responses > (model) beta_response_input_text > (schema)"
            },
            {
              "kind": "HttpTypeReference",
              "ident": "BetaResponseInputImage",
              "$ref": "(resource) beta.responses > (model) beta_response_input_image > (schema)"
            },
            {
              "kind": "HttpTypeReference",
              "ident": "BetaResponseInputFile",
              "$ref": "(resource) beta.responses > (model) beta_response_input_file > (schema)"
            }
          ],
          "oasRef": "#/components/schemas/BetaResponsePromptVariables/anyOf/0/additionalProperties"
        }
      ],
      "oasRef": "#/components/schemas/BetaPrompt/anyOf/0/properties/variables"
    },
    "oasRef": "#/components/schemas/BetaPrompt/anyOf/0/properties/variables",
    "deprecated": false,
    "schemaType": "map",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) variables > (items) > (variant) 0",
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) variables > (items) > (variant) 1",
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) variables > (items) > (variant) 2",
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) variables > (items) > (variant) 3"
    ]
  },
  "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) version": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional version of the prompt template.",
    "key": "version",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/BetaPrompt/anyOf/0/properties/version",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) beta.responses > (model) beta_response_prompt > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaPrompt",
    "ident": "BetaResponsePrompt",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "variables"
        },
        {
          "ident": "version"
        }
      ]
    },
    "docstring": "Reference to a prompt template and its variables.\n[Learn more](/docs/guides/text?api-mode=responses#reusable-prompts).\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) id",
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) variables",
      "(resource) beta.responses > (model) beta_response_prompt > (schema) > (property) version"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options > (property) mode": {
    "kind": "HttpDeclProperty",
    "docstring": "Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.",
    "key": "mode",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "implicit"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "explicit"
        }
      ],
      "oasRef": "#/components/schemas/BetaPromptCacheOptionsParam/properties/mode"
    },
    "oasRef": "#/components/schemas/BetaPromptCacheOptionsParam/properties/mode",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options > (property) mode > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options > (property) mode > (member) 1"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options > (property) ttl": {
    "kind": "HttpDeclProperty",
    "docstring": "The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.",
    "key": "ttl",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "30m"
        }
      ],
      "oasRef": "#/components/schemas/BetaPromptCacheOptionsParam/properties/ttl"
    },
    "oasRef": "#/components/schemas/BetaPromptCacheOptionsParam/properties/ttl",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_options > (property) ttl > (member) 0"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_retention > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_memory"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) prompt_cache_retention > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "24h"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) context": {
    "kind": "HttpDeclProperty",
    "docstring": "Controls which reasoning items are rendered back to the model on later turns.\nIf omitted or set to `auto`, the model determines the context mode. The\n`gpt-5.6` model family defaults to `all_turns`; earlier models default to\n`current_turn`.\n\nWhen returned on a response, this is the effective reasoning context mode\nused for the response.\n",
    "key": "context",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "current_turn"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "all_turns"
        }
      ],
      "oasRef": "#/components/schemas/BetaReasoning/properties/context"
    },
    "oasRef": "#/components/schemas/BetaReasoning/properties/context",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) context > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) context > (member) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) context > (member) 2"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort": {
    "kind": "HttpDeclProperty",
    "docstring": "Constrains effort on reasoning for reasoning models. Currently supported\nvalues are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.\nReducing reasoning effort can result in faster responses and fewer tokens\nused on reasoning in a response. Not all reasoning models support every\nvalue. See the\n[reasoning guide](https://platform.openai.com/docs/guides/reasoning)\nfor model-specific support.\n",
    "key": "effort",
    "optional": true,
    "nullable": true,
    "default": "medium",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "none"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "minimal"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "xhigh"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "max"
        }
      ],
      "oasRef": "#/components/schemas/BetaReasoning/properties/effort"
    },
    "oasRef": "#/components/schemas/BetaReasoning/properties/effort",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort > (member) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort > (member) 2",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort > (member) 3",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort > (member) 4",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort > (member) 5",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) effort > (member) 6"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) generate_summary": {
    "kind": "HttpDeclProperty",
    "docstring": "**Deprecated:** use `summary` instead.\n\nA summary of the reasoning performed by the model. This can be\nuseful for debugging and understanding the model's reasoning process.\nOne of `auto`, `concise`, or `detailed`.\n",
    "key": "generate_summary",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "concise"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "detailed"
        }
      ],
      "oasRef": "#/components/schemas/BetaReasoning/properties/generate_summary"
    },
    "oasRef": "#/components/schemas/BetaReasoning/properties/generate_summary",
    "deprecated": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) generate_summary > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) generate_summary > (member) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) generate_summary > (member) 2"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) mode": {
    "kind": "HttpDeclProperty",
    "docstring": "Controls the reasoning execution mode for the request.\n\nWhen returned on a response, this is the effective execution mode.\n",
    "key": "mode",
    "optional": true,
    "nullable": false,
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
              "literal": "standard"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "pro"
            }
          ],
          "oasRef": "#/components/schemas/BetaReasoningModeEnum/anyOf/1"
        }
      ],
      "oasRef": "#/components/schemas/BetaReasoning/properties/mode"
    },
    "oasRef": "#/components/schemas/BetaReasoning/properties/mode",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) mode > (variant) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) mode > (variant) 1"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) summary": {
    "kind": "HttpDeclProperty",
    "docstring": "A summary of the reasoning performed by the model. This can be\nuseful for debugging and understanding the model's reasoning process.\nOne of `auto`, `concise`, or `detailed`.\n\n`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.\n",
    "key": "summary",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "concise"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "detailed"
        }
      ],
      "oasRef": "#/components/schemas/BetaReasoning/properties/summary"
    },
    "oasRef": "#/components/schemas/BetaReasoning/properties/summary",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) summary > (member) 0",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) summary > (member) 1",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) reasoning > (property) summary > (member) 2"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "flex"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "scale"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) service_tier > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "priority"
    }
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) stream_options > (property) include_obfuscation": {
    "kind": "HttpDeclProperty",
    "docstring": "When true, stream obfuscation will be enabled. Stream obfuscation adds\nrandom characters to an `obfuscation` field on streaming delta events to\nnormalize payload sizes as a mitigation to certain side-channel attacks.\nThese obfuscation fields are included by default, but add a small amount\nof overhead to the data stream. You can set `include_obfuscation` to\nfalse to optimize for bandwidth if you trust the network links between\nyour application and the OpenAI API.\n",
    "key": "include_obfuscation",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/BetaResponseStreamOptions/anyOf/0/properties/include_obfuscation",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) format": {
    "kind": "HttpDeclProperty",
    "docstring": "An object specifying the format that the model must output.\n\nConfiguring `{ \"type\": \"json_schema\" }` enables Structured Outputs, \nwhich ensures the model will match your supplied JSON schema. Learn more in the \n[Structured Outputs guide](/docs/guides/structured-outputs).\n\nThe default format is `{ \"type\": \"text\" }` with no additional options.\n\n**Not recommended for gpt-4o and newer models:**\n\nSetting to `{ \"type\": \"json_object\" }` enables the older JSON mode, which\nensures the message the model generates is valid JSON. Using `json_schema`\nis preferred for models that support it.\n",
    "key": "format",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaResponseFormatTextConfig",
      "$ref": "(resource) beta.responses > (model) beta_response_format_text_config > (schema)"
    },
    "oasRef": "#/components/schemas/BetaResponseTextParam/properties/format",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) beta.responses > (model) beta_response_format_text_config",
    "childrenParentSchema": "union",
    "children": [
      "(resource) beta.responses > (model) beta_response_format_text_config > (schema) > (variant) 0",
      "(resource) beta.responses > (model) beta_response_format_text_config > (schema) > (variant) 1",
      "(resource) beta.responses > (model) beta_response_format_text_config > (schema) > (variant) 2"
    ]
  },
  "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) verbosity": {
    "kind": "HttpDeclProperty",
    "docstring": "Constrains the verbosity of the model's response. Lower values will result in\nmore concise responses, while higher values will result in more verbose responses.\nCurrently supported values are `low`, `medium`, and `high`. The default is\n`medium`.\n",
    "key": "verbosity",
    "optional": true,
    "nullable": true,
    "default": "medium",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ],
      "oasRef": "#/components/schemas/BetaResponseTextParam/properties/verbosity"
    },
    "oasRef": "#/components/schemas/BetaResponseTextParam/properties/verbosity",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) verbosity > (member) 0",
      "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) verbosity > (member) 1",
      "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) verbosity > (member) 2"
    ]
  },
  "(resource) beta.responses > (model) beta_response_text_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaResponseProperties/properties/text",
    "ident": "BetaResponseTextConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        },
        {
          "ident": "verbosity"
        }
      ]
    },
    "docstring": "Configuration options for a text response from the model. Can be plain\ntext or structured JSON data. Learn more:\n- [Text inputs and outputs](/docs/guides/text)\n- [Structured Outputs](/docs/guides/structured-outputs)\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) format",
      "(resource) beta.responses > (model) beta_response_text_config > (schema) > (property) verbosity"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceOptions",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_options > (schema)"
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_options > (schema) > (member) 0",
      "(resource) beta.responses > (model) beta_tool_choice_options > (schema) > (member) 1",
      "(resource) beta.responses > (model) beta_tool_choice_options > (schema) > (member) 2"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceAllowed",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema) > (property) mode",
      "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema) > (property) tools",
      "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceTypes",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_types > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_types > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceFunction",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_function > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_function > (schema) > (property) name",
      "(resource) beta.responses > (model) beta_tool_choice_function > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceMcp",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema) > (property) server_label",
      "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema) > (property) type",
      "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema) > (property) name"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceCustom",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_custom > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_custom > (schema) > (property) name",
      "(resource) beta.responses > (model) beta_tool_choice_custom > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaToolChoiceParam/oneOf/6",
    "ident": "BetaSpecificProgrammaticToolCallingParam",
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
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 6 > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceApplyPatch",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_apply_patch > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_apply_patch > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tool_choice > (variant) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "BetaToolChoiceShell",
      "$ref": "(resource) beta.responses > (model) beta_tool_choice_shell > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_shell > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_options > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaToolChoiceOptions",
    "ident": "BetaToolChoiceOptions",
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
      "oasRef": "#/components/schemas/BetaToolChoiceOptions"
    },
    "docstring": "Controls which (if any) tool is called by the model.\n\n`none` means the model will not call any tool and instead generates a message.\n\n`auto` means the model can pick between generating a message or calling one or\nmore tools.\n\n`required` means the model must call one or more tools.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) beta.responses > (model) beta_tool_choice_options > (schema) > (member) 0",
      "(resource) beta.responses > (model) beta_tool_choice_options > (schema) > (member) 1",
      "(resource) beta.responses > (model) beta_tool_choice_options > (schema) > (member) 2"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaToolChoiceAllowed",
    "ident": "BetaToolChoiceAllowed",
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
      "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema) > (property) mode",
      "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema) > (property) tools",
      "(resource) beta.responses > (model) beta_tool_choice_allowed > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_types > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaToolChoiceTypes",
    "ident": "BetaToolChoiceTypes",
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
      "(resource) beta.responses > (model) beta_tool_choice_types > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_function > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaToolChoiceFunction",
    "ident": "BetaToolChoiceFunction",
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
      "(resource) beta.responses > (model) beta_tool_choice_function > (schema) > (property) name",
      "(resource) beta.responses > (model) beta_tool_choice_function > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaToolChoiceMCP",
    "ident": "BetaToolChoiceMcp",
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
      "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema) > (property) server_label",
      "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema) > (property) type",
      "(resource) beta.responses > (model) beta_tool_choice_mcp > (schema) > (property) name"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_custom > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaToolChoiceCustom",
    "ident": "BetaToolChoiceCustom",
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
      "(resource) beta.responses > (model) beta_tool_choice_custom > (schema) > (property) name",
      "(resource) beta.responses > (model) beta_tool_choice_custom > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_apply_patch > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaSpecificApplyPatchParam",
    "ident": "BetaToolChoiceApplyPatch",
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
      "(resource) beta.responses > (model) beta_tool_choice_apply_patch > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_tool_choice_shell > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaSpecificFunctionShellParam",
    "ident": "BetaToolChoiceShell",
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
      "(resource) beta.responses > (model) beta_tool_choice_shell > (schema) > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/0",
    "ident": "Function",
    "type": {
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
    "docstring": "Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) name",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) parameters",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) strict",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) allowed_callers",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) defer_loading",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) description",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 0 > (property) output_schema"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/1",
    "ident": "FileSearch",
    "type": {
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
    "docstring": "A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 1 > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 1 > (property) vector_store_ids",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 1 > (property) filters",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 1 > (property) max_num_results",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 1 > (property) ranking_options"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/2",
    "ident": "Computer",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 2 > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/3",
    "ident": "ComputerUsePreview",
    "type": {
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
    "docstring": "A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 3 > (property) display_height",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 3 > (property) display_width",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 3 > (property) environment",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 3 > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 4": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/4",
    "ident": "WebSearch",
    "type": {
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
    "docstring": "Search the Internet for sources related to the prompt. Learn more about the\n[web search tool](/docs/guides/tools-web-search).\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 4 > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 4 > (property) filters",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 4 > (property) search_context_size",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 4 > (property) user_location"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/5",
    "ident": "Mcp",
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
    "docstring": "Give the model access to additional tools via remote Model Context Protocol\n(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) server_label",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) allowed_callers",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) allowed_tools",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) authorization",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) connector_id",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) defer_loading",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) headers",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) require_approval",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) server_description",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) server_url",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 5 > (property) tunnel_id"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/6",
    "ident": "CodeInterpreter",
    "type": {
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
    "docstring": "A tool that runs Python code to help generate a response to a prompt.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 6 > (property) container",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 6 > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 6 > (property) allowed_callers"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 7": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/7",
    "ident": "ProgrammaticToolCalling",
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
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 7 > (property) type"
    ]
  },
  "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/BetaTool/oneOf/8",
    "ident": "ImageGeneration",
    "type": {
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
    "docstring": "A tool that generates images using the GPT image models.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) type",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) action",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) background",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) input_fidelity",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) input_image_mask",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) model",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) moderation",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) output_compression",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) output_format",
      "(resource) beta.responses > (model) beta_responses_client_event > (schema) > (variant) 0 > (property) tools > (items) > (variant) 8 > (property) partial_images",
      "(resource) beta.responses > (model) beta_responses_client_event > (

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/beta/subresources/responses/websocket-events.md
