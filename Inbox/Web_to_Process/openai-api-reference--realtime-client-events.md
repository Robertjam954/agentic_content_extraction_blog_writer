---
source_url: https://developers.openai.com/api/reference/resources/realtime/client-events.md
title: "Realtime client events"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Realtime client events

> OpenAI API streaming event reference.
These are events that the OpenAI Realtime WebSocket server will accept from the client.

## session.update

Send this event to update the session’s configuration.
The client may send this event at any time to update any field
except for `voice` and `model`. `voice` can be updated only if there have been no other audio outputs yet.

When the server receives a `session.update`, it will respond
with a `session.updated` event showing the full, effective configuration.
Only the fields that are present in the `session.update` are updated. To clear a field like
`instructions`, pass an empty string. To clear a field like `tools`, pass an empty array.
To clear a field like `turn_detection`, pass `null`.

### Schema

Schema name: `RealtimeClientEventSessionUpdate`

```json
{
  "(resource) realtime > (model) session_update_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeClientEventSessionUpdate",
    "ident": "SessionUpdateEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "session"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "docstring": "Send this event to update the session’s configuration.\nThe client may send this event at any time to update any field\nexcept for `voice` and `model`. `voice` can be updated only if there have been no other audio outputs yet.\n\nWhen the server receives a `session.update`, it will respond\nwith a `session.updated` event showing the full, effective configuration.\nOnly the fields that are present in the `session.update` are updated. To clear a field like\n`instructions`, pass an empty string. To clear a field like `tools`, pass an empty array.\nTo clear a field like `turn_detection`, pass `null`.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) session_update_event > (schema) > (property) session",
      "(resource) realtime > (model) session_update_event > (schema) > (property) type",
      "(resource) realtime > (model) session_update_event > (schema) > (property) event_id"
    ]
  },
  "(resource) realtime > (model) session_update_event > (schema) > (property) session": {
    "kind": "HttpDeclProperty",
    "docstring": "Update the Realtime session. Choose either a realtime\nsession or a transcription session.\n",
    "key": "session",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeSessionCreateRequest",
          "$ref": "(resource) realtime > (model) realtime_session_create_request > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeTranscriptionSessionCreateRequest",
          "$ref": "(resource) realtime > (model) realtime_transcription_session_create_request > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeClientEventSessionUpdate/properties/session"
    },
    "oasRef": "#/components/schemas/RealtimeClientEventSessionUpdate/properties/session",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) session_update_event > (schema) > (property) session > (variant) 0",
      "(resource) realtime > (model) session_update_event > (schema) > (property) session > (variant) 1"
    ]
  },
  "(resource) realtime > (model) session_update_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be `session.update`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.update"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeClientEventSessionUpdate/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeClientEventSessionUpdate/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) session_update_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) session_update_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional client-generated ID used to identify this event. This is an arbitrary string that a client may assign. It will be passed back if there is an error with the event, but the corresponding `session.updated` event will not include it.",
    "key": "event_id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "oasRef": "#/components/schemas/RealtimeClientEventSessionUpdate/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) session_update_event > (schema) > (property) session > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeSessionCreateRequest",
      "$ref": "(resource) realtime > (model) realtime_session_create_request > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) type",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) audio",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) include",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) instructions",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) output_modalities",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) parallel_tool_calls",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) prompt",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) reasoning",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tool_choice",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tools",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tracing",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) truncation"
    ]
  },
  "(resource) realtime > (model) session_update_event > (schema) > (property) session > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeTranscriptionSessionCreateRequest",
      "$ref": "(resource) realtime > (model) realtime_transcription_session_create_request > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) type",
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) audio",
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) include"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA",
    "ident": "RealtimeSessionCreateRequest",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "audio"
        },
        {
          "ident": "include"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "max_output_tokens"
        },
        {
          "ident": "model"
        },
        {
          "ident": "output_modalities"
        },
        {
          "ident": "parallel_tool_calls"
        },
        {
          "ident": "prompt"
        },
        {
          "ident": "reasoning"
        },
        {
          "ident": "tool_choice"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "tracing"
        },
        {
          "ident": "truncation"
        }
      ]
    },
    "docstring": "Realtime session object configuration.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) type",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) audio",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) include",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) instructions",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) output_modalities",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) parallel_tool_calls",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) prompt",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) reasoning",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tool_choice",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tools",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tracing",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) truncation"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_create_request > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA",
    "ident": "RealtimeTranscriptionSessionCreateRequest",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "audio"
        },
        {
          "ident": "include"
        }
      ]
    },
    "docstring": "Realtime transcription session object configuration.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) type",
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) audio",
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) include"
    ]
  },
  "(resource) realtime > (model) session_update_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.update"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of session to create. Always `realtime` for the Realtime API.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) audio": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for input and output audio.\n",
    "key": "audio",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeAudioConfig",
      "$ref": "(resource) realtime > (model) realtime_audio_config > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_audio_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config > (schema) > (property) input",
      "(resource) realtime > (model) realtime_audio_config > (schema) > (property) output"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) include": {
    "kind": "HttpDeclProperty",
    "docstring": "Additional fields to include in server outputs.\n\n`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.\n",
    "key": "include",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "item.input_audio_transcription.logprobs"
          }
        ],
        "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/include/items"
      },
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/include"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/include",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) include > (items) > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "docstring": "The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. \"be extremely succinct\", \"act friendly\", \"here are examples of good responses\") and on audio behavior (e.g. \"talk quickly\", \"inject emotion into your voice\", \"laugh frequently\"). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.\n\nNote that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.\n",
    "key": "instructions",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/instructions",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Maximum number of output tokens for a single assistant response,\ninclusive of tool calls. Provide an integer between 1 and 4096 to\nlimit output tokens, or `inf` for the maximum available tokens for a\ngiven model. Defaults to `inf`.\n",
    "key": "max_output_tokens",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeNumber"
        },
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "inf"
            }
          ],
          "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/max_output_tokens/oneOf/1"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/max_output_tokens"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/max_output_tokens",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens > (variant) 0",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "docstring": "The Realtime model used for this session.\n",
    "key": "model",
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
              "literal": "gpt-realtime"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-1.5"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-2"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-2.1"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-2.1-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-2025-08-28"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-realtime-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-realtime-preview-2024-10-01"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-realtime-preview-2024-12-17"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-realtime-preview-2025-06-03"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-realtime-preview"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-realtime-preview-2024-12-17"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-mini-2025-10-06"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-mini-2025-12-15"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-audio-1.5"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-audio-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-audio-mini-2025-10-06"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-audio-mini-2025-12-15"
            }
          ],
          "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/model/anyOf/1"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/model"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/model",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 0",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) output_modalities": {
    "kind": "HttpDeclProperty",
    "docstring": "The set of modalities the model can respond with. It defaults to `[\"audio\"]`, indicating\nthat the model will respond with audio plus a transcript. `[\"text\"]` can be used to make\nthe model respond with text only. It is not possible to request both `text` and `audio` at the same time.\n",
    "key": "output_modalities",
    "optional": true,
    "nullable": false,
    "default": [
      "audio"
    ],
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "text"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "audio"
          }
        ],
        "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/output_modalities/items"
      },
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/output_modalities"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/output_modalities",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) output_modalities > (items) > (member) 0",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) output_modalities > (items) > (member) 1"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether the model may call multiple tools in parallel. Only supported by\nreasoning Realtime models such as `gpt-realtime-2`.\n",
    "key": "parallel_tool_calls",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/parallel_tool_calls",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) prompt": {
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
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/prompt",
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
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) reasoning": {
    "kind": "HttpDeclProperty",
    "title": "Realtime reasoning configuration",
    "docstring": "Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.\n",
    "key": "reasoning",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeReasoning",
      "$ref": "(resource) realtime > (model) realtime_reasoning > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/reasoning",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_reasoning",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_reasoning > (schema) > (property) effort"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "docstring": "How the model chooses tools. Provide one of the string modes or force a specific\nfunction/MCP tool.\n",
    "key": "tool_choice",
    "optional": true,
    "nullable": false,
    "default": "auto",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeToolChoiceConfig",
      "$ref": "(resource) realtime > (model) realtime_tool_choice_config > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tool_choice",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_tool_choice_config",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 1",
      "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "docstring": "Tools available to the model.",
    "key": "tools",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeToolsConfig",
      "$ref": "(resource) realtime > (model) realtime_tools_config > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tools",
    "deprecated": false,
    "schemaType": "array",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_tools_config",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) tracing": {
    "kind": "HttpDeclProperty",
    "title": "Tracing Configuration",
    "docstring": "Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once\ntracing is enabled for a session, the configuration cannot be modified.\n\n`auto` will create a trace for the session with default values for the\nworkflow name, group id, and metadata.\n",
    "key": "tracing",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeTracingConfig",
      "$ref": "(resource) realtime > (model) realtime_tracing_config > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_tracing_config",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) truncation": {
    "kind": "HttpDeclProperty",
    "title": "Realtime Truncation Controls",
    "docstring": "When the number of tokens in a conversation exceeds the model's input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model's context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.\n\nClients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.\n\nTruncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.\n\nTruncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model's input token limit.\n",
    "key": "truncation",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeTruncation",
      "$ref": "(resource) realtime > (model) realtime_truncation > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/truncation",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_truncation",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of session to create. Always `transcription` for transcription sessions.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transcription"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) audio": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for input and output audio.\n",
    "key": "audio",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeTranscriptionSessionAudio",
      "$ref": "(resource) realtime > (model) realtime_transcription_session_audio > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_transcription_session_audio",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio > (schema) > (property) input"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) include": {
    "kind": "HttpDeclProperty",
    "docstring": "Additional fields to include in server outputs.\n\n`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.\n",
    "key": "include",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "item.input_audio_transcription.logprobs"
          }
        ],
        "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/include/items"
      },
      "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/include"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/include",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) include > (items) > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "realtime"
    }
  },
  "(resource) realtime > (model) realtime_audio_config > (schema) > (property) input": {
    "kind": "HttpDeclProperty",
    "key": "input",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeAudioConfigInput",
      "$ref": "(resource) realtime > (model) realtime_audio_config_input > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_audio_config_input",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) format",
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) noise_reduction",
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) transcription",
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) turn_detection"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config > (schema) > (property) output": {
    "kind": "HttpDeclProperty",
    "key": "output",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeAudioConfigOutput",
      "$ref": "(resource) realtime > (model) realtime_audio_config_output > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/output",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_audio_config_output",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) format",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) speed",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio",
    "ident": "RealtimeAudioConfig",
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
    "docstring": "Configuration for input and output audio.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config > (schema) > (property) input",
      "(resource) realtime > (model) realtime_audio_config > (schema) > (property) output"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) include > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "item.input_audio_transcription.logprobs"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/max_output_tokens/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "children": []
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/max_output_tokens/oneOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "inf"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/max_output_tokens/oneOf/1"
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens > (variant) 1 > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/model/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/model/anyOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-1.5"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-2"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-2.1"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-2.1-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-2025-08-28"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-realtime-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-realtime-preview-2024-10-01"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-realtime-preview-2024-12-17"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-realtime-preview-2025-06-03"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-realtime-preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-realtime-preview-2024-12-17"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-mini-2025-10-06"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-mini-2025-12-15"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-audio-1.5"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-audio-mini"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-audio-mini-2025-10-06"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-audio-mini-2025-12-15"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/model/anyOf/1"
    },
    "docstring": "The Realtime model used for this session.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 0",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 1",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 2",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 3",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 4",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 5",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 6",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 7",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 8",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 9",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 10",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 11",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 12",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 13",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 14",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 15",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 16",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 17",
      "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 18"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) output_modalities > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "text"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) output_modalities > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "audio"
    }
  },
  "(resource) responses > (model) response_prompt > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique identifier of the prompt template to use.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/Prompt/anyOf/0/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_prompt > (schema) > (property) variables": {
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
              "ident": "ResponseInputText",
              "$ref": "(resource) responses > (model) response_input_text > (schema)"
            },
            {
              "kind": "HttpTypeReference",
              "ident": "ResponseInputImage",
              "$ref": "(resource) responses > (model) response_input_image > (schema)"
            },
            {
              "kind": "HttpTypeReference",
              "ident": "ResponseInputFile",
              "$ref": "(resource) responses > (model) response_input_file > (schema)"
            }
          ],
          "oasRef": "#/components/schemas/ResponsePromptVariables/anyOf/0/additionalProperties"
        }
      ],
      "oasRef": "#/components/schemas/Prompt/anyOf/0/properties/variables"
    },
    "oasRef": "#/components/schemas/Prompt/anyOf/0/properties/variables",
    "deprecated": false,
    "schemaType": "map",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 0",
      "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 1",
      "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 2",
      "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 3"
    ]
  },
  "(resource) responses > (model) response_prompt > (schema) > (property) version": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional version of the prompt template.",
    "key": "version",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/Prompt/anyOf/0/properties/version",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_prompt > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Prompt",
    "ident": "ResponsePrompt",
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
      "(resource) responses > (model) response_prompt > (schema) > (property) id",
      "(resource) responses > (model) response_prompt > (schema) > (property) variables",
      "(resource) responses > (model) response_prompt > (schema) > (property) version"
    ]
  },
  "(resource) realtime > (model) realtime_reasoning > (schema) > (property) effort": {
    "kind": "HttpDeclProperty",
    "docstring": "Constrains effort on reasoning for reasoning-capable Realtime models such as\n`gpt-realtime-2`.\n",
    "key": "effort",
    "optional": true,
    "nullable": false,
    "default": "low",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeReasoningEffort",
      "$ref": "(resource) realtime > (model) realtime_reasoning_effort > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeReasoning/properties/effort",
    "deprecated": false,
    "schemaType": "enum",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_reasoning_effort",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 0",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 1",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 2",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 3",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 4"
    ]
  },
  "(resource) realtime > (model) realtime_reasoning > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeReasoning",
    "ident": "RealtimeReasoning",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "effort"
        }
      ]
    },
    "docstring": "Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_reasoning > (schema) > (property) effort"
    ]
  },
  "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 0": {
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
  "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 1": {
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
  "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 2": {
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
  "(resource) realtime > (model) realtime_tool_choice_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tool_choice",
    "ident": "RealtimeToolChoiceConfig",
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
          "ident": "ToolChoiceFunction",
          "$ref": "(resource) responses > (model) tool_choice_function > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ToolChoiceMcp",
          "$ref": "(resource) responses > (model) tool_choice_mcp > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tool_choice"
    },
    "docstring": "How the model chooses tools. Provide one of the string modes or force a specific\nfunction/MCP tool.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 1",
      "(resource) realtime > (model) realtime_tool_choice_config > (schema) > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeFunctionTool",
      "$ref": "(resource) realtime > (model) realtime_function_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) description",
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) name",
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) parameters",
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tools/items/oneOf/1",
    "ident": "McpTool",
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
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) server_label",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) type",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_callers",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) authorization",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) defer_loading",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) headers",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) server_description",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) server_url",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) tunnel_id"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tools",
    "ident": "RealtimeToolsConfig",
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "RealtimeToolsConfigUnion",
        "$ref": "(resource) realtime > (model) realtime_tools_config_union > (schema)"
      },
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tools"
    },
    "docstring": "Tools available to the model.",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing/oneOf/0",
    "ident": "Auto",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing/oneOf/0"
    },
    "docstring": "Enables tracing and sets default values for tracing configuration options. Always `auto`.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 0 > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing/oneOf/1",
    "ident": "TracingConfiguration",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "group_id"
        },
        {
          "ident": "metadata"
        },
        {
          "ident": "workflow_name"
        }
      ]
    },
    "docstring": "Granular configuration for tracing.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1 > (property) group_id",
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1 > (property) metadata",
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1 > (property) workflow_name"
    ]
  },
  "(resource) realtime > (model) realtime_tracing_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing",
    "ident": "RealtimeTracingConfig",
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
          "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing/oneOf/0"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "group_id"
            },
            {
              "ident": "metadata"
            },
            {
              "ident": "workflow_name"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing"
    },
    "docstring": "Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once\ntracing is enabled for a session, the configuration cannot be modified.\n\n`auto` will create a trace for the session with default values for the\nworkflow name, group id, and metadata.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/0",
    "ident": "UnionMember0",
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
      "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/0"
    },
    "docstring": "The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit.",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 0 > (member) 0",
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 0 > (member) 1"
    ]
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/1",
    "ident": "RetentionRatioTruncation",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "retention_ratio"
        },
        {
          "ident": "type"
        },
        {
          "ident": "token_limits"
        }
      ]
    },
    "docstring": "Retain a fraction of the conversation tokens when the conversation exceeds the input token limit. This allows you to amortize truncations across multiple turns, which can help improve cached token usage.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) retention_ratio",
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) type",
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) token_limits"
    ]
  },
  "(resource) realtime > (model) realtime_truncation > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTruncation",
    "ident": "RealtimeTruncation",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
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
          "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/0"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "retention_ratio"
            },
            {
              "ident": "type"
            },
            {
              "ident": "token_limits"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/RealtimeTruncation"
    },
    "docstring": "When the number of tokens in a conversation exceeds the model's input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model's context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.\n\nClients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.\n\nTruncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.\n\nTruncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model's input token limit.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transcription"
    }
  },
  "(resource) realtime > (model) realtime_transcription_session_audio > (schema) > (property) input": {
    "kind": "HttpDeclProperty",
    "key": "input",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeTranscriptionSessionAudioInput",
      "$ref": "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_transcription_session_audio_input",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) format",
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) noise_reduction",
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) transcription",
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) turn_detection"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio",
    "ident": "RealtimeTranscriptionSessionAudio",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "input"
        }
      ]
    },
    "docstring": "Configuration for input and output audio.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio > (schema) > (property) input"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_create_request > (schema) > (property) include > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "item.input_audio_transcription.logprobs"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) format": {
    "kind": "HttpDeclProperty",
    "docstring": "The format of the input audio.",
    "key": "format",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeAudioFormats",
      "$ref": "(resource) realtime > (model) realtime_audio_formats > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input/properties/format",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_audio_formats",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) noise_reduction": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for input audio noise reduction. This can be set to `null` to turn off.\nNoise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.\nFiltering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.\n",
    "key": "noise_reduction",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input/properties/noise_reduction",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) noise_reduction > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) transcription": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for input audio transcription, defaults to off and can be set to `null` to turn off once on. Input audio transcription is not native to the model, since the model consumes audio directly. Transcription runs asynchronously through [the /audio/transcriptions endpoint](/docs/api-reference/audio/createTranscription) and should be treated as guidance of input audio content rather than precisely what the model heard. The client can optionally set the language and prompt for transcription, these offer additional guidance to the transcription service.\n",
    "key": "transcription",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AudioTranscription",
      "$ref": "(resource) realtime > (model) audio_transcription > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input/properties/transcription",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) audio_transcription",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) language",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) prompt"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) turn_detection": {
    "kind": "HttpDeclProperty",
    "title": "Realtime Turn Detection",
    "docstring": "Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.\n\nServer VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.\n\nSemantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with \"uhhm\", the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.\n\nFor `gpt-realtime-whisper` transcription sessions, turn detection must be\nset to `null`; VAD is not supported.\n",
    "key": "turn_detection",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeAudioInputTurnDetection",
      "$ref": "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input/properties/turn_detection",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_audio_input_turn_detection",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_input > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input",
    "ident": "RealtimeAudioConfigInput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        },
        {
          "ident": "noise_reduction"
        },
        {
          "ident": "transcription"
        },
        {
          "ident": "turn_detection"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) format",
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) noise_reduction",
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) transcription",
      "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) turn_detection"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) format": {
    "kind": "HttpDeclProperty",
    "docstring": "The format of the output audio.",
    "key": "format",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeAudioFormats",
      "$ref": "(resource) realtime > (model) realtime_audio_formats > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/output/properties/format",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_audio_formats",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) speed": {
    "kind": "HttpDeclProperty",
    "docstring": "The speed of the model's spoken response as a multiple of the original speed.\n1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.\n\nThis parameter is a post-processing adjustment to the audio after it is generated, it's\nalso possible to prompt the model to speak faster or slower.\n",
    "key": "speed",
    "optional": true,
    "nullable": false,
    "default": 1,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "maximum": 1.5,
      "minimum": 0.25
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/output/properties/speed",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice": {
    "kind": "HttpDeclProperty",
    "title": "Voice",
    "docstring": "The voice the model uses to respond. Supported built-in voices are\n`alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`,\n`marin`, and `cedar`. You may also provide a custom voice object with\nan `id`, for example `{ \"id\": \"voice_1234\" }`. Voice cannot be changed\nduring the session once the model has responded with audio at least once.\nWe recommend `marin` and `cedar` for best quality.\n",
    "key": "voice",
    "optional": true,
    "nullable": false,
    "default": "alloy",
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
              "literal": "alloy"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "ash"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "ballad"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "coral"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "echo"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "sage"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "shimmer"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "verse"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "marin"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "cedar"
            }
          ],
          "oasRef": "#/components/schemas/VoiceIdsShared/anyOf/1"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/output/properties/voice"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/output/properties/voice",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 0",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/output",
    "ident": "RealtimeAudioConfigOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        },
        {
          "ident": "speed"
        },
        {
          "ident": "voice"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) format",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) speed",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice"
    ]
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) max_output_tokens > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "inf"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-1.5"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-2"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-2.1"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-2.1-mini"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-2025-08-28"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-4o-realtime-preview"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-4o-realtime-preview-2024-10-01"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-4o-realtime-preview-2024-12-17"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 9": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-4o-realtime-preview-2025-06-03"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 10": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-4o-mini-realtime-preview"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 11": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-4o-mini-realtime-preview-2024-12-17"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 12": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-mini"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 13": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-mini-2025-10-06"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 14": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-realtime-mini-2025-12-15"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 15": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-audio-1.5"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 16": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-audio-mini"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 17": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-audio-mini-2025-10-06"
    }
  },
  "(resource) realtime > (model) realtime_session_create_request > (schema) > (property) model > (variant) 1 > (member) 18": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-audio-mini-2025-12-15"
    }
  },
  "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ResponsePromptVariables/anyOf/0/additionalProperties/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputText",
      "$ref": "(resource) responses > (model) response_input_text > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) text",
      "(resource) responses > (model) response_input_text > (schema) > (property) type",
      "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputImage",
      "$ref": "(resource) responses > (model) response_input_image > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) detail",
      "(resource) responses > (model) response_input_image > (schema) > (property) type",
      "(resource) responses > (model) response_input_image > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_image > (schema) > (property) image_url",
      "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_prompt > (schema) > (property) variables > (items) > (variant) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputFile",
      "$ref": "(resource) responses > (model) response_input_file > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) type",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_data",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_url",
      "(resource) responses > (model) response_input_file > (schema) > (property) filename",
      "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_text > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputTextContent",
    "ident": "ResponseInputText",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "text"
        },
        {
          "ident": "type"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "docstring": "A text input to the model.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) text",
      "(resource) responses > (model) response_input_text > (schema) > (property) type",
      "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputImageContent",
    "ident": "ResponseInputImage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "detail"
        },
        {
          "ident": "type"
        },
        {
          "ident": "file_id"
        },
        {
          "ident": "image_url"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "docstring": "An image input to the model. Learn about [image inputs](/docs/guides/vision).",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) detail",
      "(resource) responses > (model) response_input_image > (schema) > (property) type",
      "(resource) responses > (model) response_input_image > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_image > (schema) > (property) image_url",
      "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputFileContent",
    "ident": "ResponseInputFile",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "detail"
        },
        {
          "ident": "file_data"
        },
        {
          "ident": "file_id"
        },
        {
          "ident": "file_url"
        },
        {
          "ident": "filename"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "docstring": "A file input to the model.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) type",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_data",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_url",
      "(resource) responses > (model) response_input_file > (schema) > (property) filename",
      "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "minimal"
    }
  },
  "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) realtime > (model) realtime_reasoning_effort > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeReasoningEffort",
    "ident": "RealtimeReasoningEffort",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
        }
      ],
      "oasRef": "#/components/schemas/RealtimeReasoningEffort"
    },
    "docstring": "Constrains effort on reasoning for reasoning-capable Realtime models such as\n`gpt-realtime-2`.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 0",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 1",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 2",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 3",
      "(resource) realtime > (model) realtime_reasoning_effort > (schema) > (member) 4"
    ]
  },
  "(resource) responses > (model) tool_choice_options > (schema) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) responses > (model) tool_choice_options > (schema) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) responses > (model) tool_choice_options > (schema) > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "required"
    }
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
  "(resource) responses > (model) tool_choice_function > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function to call.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ToolChoiceFunction/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) tool_choice_function > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "For function calling, the type is always `function`.",
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
      "oasRef": "#/components/schemas/ToolChoiceFunction/properties/type"
    },
    "oasRef": "#/components/schemas/ToolChoiceFunction/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) tool_choice_function > (schema) > (property) type > (member) 0"
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
  "(resource) responses > (model) tool_choice_mcp > (schema) > (property) server_label": {
    "kind": "HttpDeclProperty",
    "docstring": "The label of the MCP server to use.\n",
    "key": "server_label",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ToolChoiceMCP/properties/server_label",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) tool_choice_mcp > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "For MCP tools, the type is always `mcp`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp"
        }
      ],
      "oasRef": "#/components/schemas/ToolChoiceMCP/properties/type"
    },
    "oasRef": "#/components/schemas/ToolChoiceMCP/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) tool_choice_mcp > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) tool_choice_mcp > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the tool to call on the server.\n",
    "key": "name",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/ToolChoiceMCP/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
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
  "(resource) realtime > (model) realtime_function_tool > (schema) > (property) description": {
    "kind": "HttpDeclProperty",
    "docstring": "The description of the function, including guidance on when and how\nto call it, and guidance about what to tell the user when calling\n(if anything).\n",
    "key": "description",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeFunctionTool/properties/description",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_function_tool > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function.",
    "key": "name",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeFunctionTool/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_function_tool > (schema) > (property) parameters": {
    "kind": "HttpDeclProperty",
    "docstring": "Parameters of the function in JSON Schema.",
    "key": "parameters",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "oasRef": "#/components/schemas/RealtimeFunctionTool/properties/parameters",
    "deprecated": false,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) realtime > (model) realtime_function_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the tool, i.e. `function`.",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeFunctionTool/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeFunctionTool/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_function_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeFunctionTool",
    "ident": "RealtimeFunctionTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "description"
        },
        {
          "ident": "name"
        },
        {
          "ident": "parameters"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) description",
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) name",
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) parameters",
      "(resource) realtime > (model) realtime_function_tool > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "docstring": "A label for this MCP server, used to identify it in tool calls.\n",
    "key": "server_label",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/server_label",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the MCP tool. Always `mcp`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp"
        }
      ],
      "oasRef": "#/components/schemas/MCPTool/properties/type"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "docstring": "The tool invocation context(s).",
    "key": "allowed_callers",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeUnion",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ],
        "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers/anyOf/0/items"
      },
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_callers > (items) > (member) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools": {
    "kind": "HttpDeclProperty",
    "docstring": "List of allowed tool names or a filter object.\n",
    "key": "allowed_tools",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeArray",
          "elementType": {
            "kind": "HttpTypeString"
          },
          "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "read_only"
            },
            {
              "ident": "tool_names"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools > (variant) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) authorization": {
    "kind": "HttpDeclProperty",
    "docstring": "An OAuth access token that can be used with a remote MCP server, either\nwith a custom MCP server URL or a service connector. Your application\nmust handle the OAuth authorization flow and provide the token here.\n",
    "key": "authorization",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/authorization",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for service connectors, like those available in ChatGPT. One of\n`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more\nabout service connectors [here](/docs/guides/tools-remote-mcp#connectors).\n\nCurrently supported `connector_id` values are:\n\n- Dropbox: `connector_dropbox`\n- Gmail: `connector_gmail`\n- Google Calendar: `connector_googlecalendar`\n- Google Drive: `connector_googledrive`\n- Microsoft Teams: `connector_microsoftteams`\n- Outlook Calendar: `connector_outlookcalendar`\n- Outlook Email: `connector_outlookemail`\n- SharePoint: `connector_sharepoint`\n",
    "key": "connector_id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_dropbox"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_gmail"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_googlecalendar"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_googledrive"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_microsoftteams"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_outlookcalendar"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_outlookemail"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_sharepoint"
        }
      ],
      "oasRef": "#/components/schemas/MCPTool/properties/connector_id"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/connector_id",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 1",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 2",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 3",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 4",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 5",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 6",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 7"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether this MCP tool is deferred and discovered via tool search.\n",
    "key": "defer_loading",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/defer_loading",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) headers": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional HTTP headers to send to the MCP server. Use for authentication\nor other purposes.\n",
    "key": "headers",
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
      "oasRef": "#/components/schemas/MCPTool/properties/headers"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/headers",
    "deprecated": false,
    "schemaType": "map",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval": {
    "kind": "HttpDeclProperty",
    "docstring": "Specify which of the MCP server's tools require approval.",
    "key": "require_approval",
    "optional": true,
    "nullable": true,
    "default": "always",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "always"
            },
            {
              "ident": "never"
            }
          ]
        },
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "always"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "never"
            }
          ],
          "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/1"
        }
      ],
      "oasRef": "#/components/schemas/MCPTool/properties/require_approval"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) server_description": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional description of the MCP server, used to provide more context.\n",
    "key": "server_description",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/server_description",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) server_url": {
    "kind": "HttpDeclProperty",
    "docstring": "The URL for the MCP server. One of `server_url`, `connector_id`, or\n`tunnel_id` must be provided.\n",
    "key": "server_url",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/server_url",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) tunnel_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The Secure MCP Tunnel ID to use instead of a direct server URL. One of\n`server_url`, `connector_id`, or `tunnel_id` must be provided.\n",
    "key": "tunnel_id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/MCPTool/properties/tunnel_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tools/items",
    "ident": "RealtimeToolsConfigUnion",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeFunctionTool",
          "$ref": "(resource) realtime > (model) realtime_function_tool > (schema)"
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
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tools/items"
    },
    "docstring": "Give the model access to additional tools via remote Model Context Protocol\n(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1 > (property) group_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The group id to attach to this trace to enable filtering and\ngrouping in the Traces Dashboard.\n",
    "key": "group_id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing/oneOf/1/properties/group_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1 > (property) metadata": {
    "kind": "HttpDeclProperty",
    "docstring": "The arbitrary metadata to attach to this trace to enable\nfiltering in the Traces Dashboard.\n",
    "key": "metadata",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing/oneOf/1/properties/metadata",
    "deprecated": false,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) realtime > (model) realtime_tracing_config > (schema) > (variant) 1 > (property) workflow_name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the workflow to attach to this trace. This is used to\nname the trace in the Traces Dashboard.\n",
    "key": "workflow_name",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/tracing/oneOf/1/properties/workflow_name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "disabled"
    }
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) retention_ratio": {
    "kind": "HttpDeclProperty",
    "docstring": "Fraction of post-instruction conversation tokens to retain (`0.0` - `1.0`) when the conversation exceeds the input token limit. Setting this to `0.8` means that messages will be dropped until 80% of the maximum allowed tokens are used. This helps reduce the frequency of truncations and improve cache rates.\n",
    "key": "retention_ratio",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 1
    },
    "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/1/properties/retention_ratio",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "Use retention ratio truncation.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "retention_ratio"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/1/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/1/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) token_limits": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional custom token limits for this truncation strategy. If not provided, the model's default token limits will be used.",
    "key": "token_limits",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "post_instructions"
        }
      ]
    },
    "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/1/properties/token_limits",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) token_limits > (property) post_instructions"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) format": {
    "kind": "HttpDeclProperty",
    "docstring": "The PCM audio format. Only a 24kHz sample rate is supported.",
    "key": "format",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeAudioFormats",
      "$ref": "(resource) realtime > (model) realtime_audio_formats > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input/properties/format",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_audio_formats",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) noise_reduction": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for input audio noise reduction. This can be set to `null` to turn off.\nNoise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.\nFiltering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.\n",
    "key": "noise_reduction",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input/properties/noise_reduction",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) noise_reduction > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) transcription": {
    "kind": "HttpDeclProperty",
    "docstring": "Configuration for input audio transcription, defaults to off and can be set to `null` to turn off once on. Input audio transcription is not native to the model, since the model consumes audio directly. Transcription runs asynchronously through [the /audio/transcriptions endpoint](/docs/api-reference/audio/createTranscription) and should be treated as guidance of input audio content rather than precisely what the model heard. The client can optionally set the language and prompt for transcription, these offer additional guidance to the transcription service.\n",
    "key": "transcription",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AudioTranscription",
      "$ref": "(resource) realtime > (model) audio_transcription > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input/properties/transcription",
    "deprecated": false,
    "schemaType": "object",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) audio_transcription",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) language",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) prompt"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) turn_detection": {
    "kind": "HttpDeclProperty",
    "title": "Realtime Turn Detection",
    "docstring": "Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.\n\nServer VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.\n\nSemantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with \"uhhm\", the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.\n\nFor `gpt-realtime-whisper` transcription sessions, turn detection must be\nset to `null`; VAD is not supported.\n",
    "key": "turn_detection",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeTranscriptionSessionAudioInputTurnDetection",
      "$ref": "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input/properties/turn_detection",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input",
    "ident": "RealtimeTranscriptionSessionAudioInput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        },
        {
          "ident": "noise_reduction"
        },
        {
          "ident": "transcription"
        },
        {
          "ident": "turn_detection"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) format",
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) noise_reduction",
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) transcription",
      "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) turn_detection"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/0",
    "ident": "PCMAudioFormat",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "rate"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "The PCM audio format. Only a 24kHz sample rate is supported.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0 > (property) rate",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0 > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/1",
    "ident": "PCMUAudioFormat",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "The G.711 μ-law format.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1 > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/2",
    "ident": "PCMAAudioFormat",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "The G.711 A-law format.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2 > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeAudioFormats",
    "ident": "RealtimeAudioFormats",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "rate"
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
        }
      ],
      "oasRef": "#/components/schemas/RealtimeAudioFormats"
    },
    "docstring": "The PCM audio format. Only a 24kHz sample rate is supported.",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1",
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_input > (schema) > (property) noise_reduction > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.\n",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "NoiseReductionType",
      "$ref": "(resource) realtime > (model) noise_reduction_type > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input/properties/noise_reduction/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) noise_reduction_type",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 0",
      "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 1"
    ]
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) delay": {
    "kind": "HttpDeclProperty",
    "docstring": "Controls how long the model waits before emitting transcription text.\nHigher values can improve transcription accuracy at the cost of latency.\nOnly supported with `gpt-realtime-whisper` in GA Realtime sessions.\n",
    "key": "delay",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
        }
      ],
      "oasRef": "#/components/schemas/AudioTranscription/properties/delay"
    },
    "oasRef": "#/components/schemas/AudioTranscription/properties/delay",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 0",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 1",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 2",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 3",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 4"
    ]
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) language": {
    "kind": "HttpDeclProperty",
    "docstring": "The language of the input audio. Supplying the input language in\n[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format\nwill improve accuracy and latency.\n",
    "key": "language",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/AudioTranscription/properties/language",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "docstring": "The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.\n",
    "key": "model",
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
              "literal": "whisper-1"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-transcribe"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-mini-transcribe-2025-12-15"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-transcribe"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-4o-transcribe-diarize"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-realtime-whisper"
            }
          ],
          "oasRef": "#/components/schemas/AudioTranscription/properties/model/anyOf/1"
        }
      ],
      "oasRef": "#/components/schemas/AudioTranscription/properties/model"
    },
    "oasRef": "#/components/schemas/AudioTranscription/properties/model",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 0",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1"
    ]
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) prompt": {
    "kind": "HttpDeclProperty",
    "docstring": "An optional text to guide the model's style or continue a previous audio\nsegment.\nFor `whisper-1`, the [prompt is a list of keywords](/docs/guides/speech-to-text#prompting).\nFor `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example \"expect words related to technology\".\nPrompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.\n",
    "key": "prompt",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/AudioTranscription/properties/prompt",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) audio_transcription > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AudioTranscription",
    "ident": "AudioTranscription",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "delay"
        },
        {
          "ident": "language"
        },
        {
          "ident": "model"
        },
        {
          "ident": "prompt"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) audio_transcription > (schema) > (property) delay",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) language",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) prompt"
    ]
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0",
    "ident": "ServerVad",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "create_response"
        },
        {
          "ident": "idle_timeout_ms"
        },
        {
          "ident": "interrupt_response"
        },
        {
          "ident": "prefix_padding_ms"
        },
        {
          "ident": "silence_duration_ms"
        },
        {
          "ident": "threshold"
        }
      ]
    },
    "docstring": "Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) type",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) create_response",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) idle_timeout_ms",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) interrupt_response",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) prefix_padding_ms",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) silence_duration_ms",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) threshold"
    ]
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1",
    "ident": "SemanticVad",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "create_response"
        },
        {
          "ident": "eagerness"
        },
        {
          "ident": "interrupt_response"
        }
      ]
    },
    "docstring": "Server-side semantic turn detection which uses a model to determine when the user has finished speaking.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) type",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) create_response",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) eagerness",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) interrupt_response"
    ]
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input/properties/turn_detection",
    "ident": "RealtimeAudioInputTurnDetection",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "create_response"
            },
            {
              "ident": "idle_timeout_ms"
            },
            {
              "ident": "interrupt_response"
            },
            {
              "ident": "prefix_padding_ms"
            },
            {
              "ident": "silence_duration_ms"
            },
            {
              "ident": "threshold"
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
              "ident": "create_response"
            },
            {
              "ident": "eagerness"
            },
            {
              "ident": "interrupt_response"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/RealtimeSessionCreateRequestGA/properties/audio/properties/input/properties/turn_detection"
    },
    "docstring": "Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.\n\nServer VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.\n\nSemantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with \"uhhm\", the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.\n\nFor `gpt-realtime-whisper` transcription sessions, turn detection must be\nset to `null`; VAD is not supported.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/VoiceIdsShared/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/VoiceIdsShared/anyOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "alloy"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ash"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ballad"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "coral"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "echo"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "sage"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "shimmer"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "verse"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "marin"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "cedar"
        }
      ],
      "oasRef": "#/components/schemas/VoiceIdsShared/anyOf/1"
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 0",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 1",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 2",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 3",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 4",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 5",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 6",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 7",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 8",
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 9"
    ]
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/VoiceIdsOrCustomVoice/anyOf/1",
    "ident": "ID",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        }
      ]
    },
    "docstring": "Custom voice reference.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 2 > (property) id"
    ]
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "docstring": "The text input to the model.",
    "key": "text",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/InputTextContent/properties/text",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the input item. Always `input_text`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "default": "input_text",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_text"
        }
      ],
      "oasRef": "#/components/schemas/InputTextContent/properties/type"
    },
    "oasRef": "#/components/schemas/InputTextContent/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "title": "Prompt cache breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "key": "prompt_cache_breakpoint",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "oasRef": "#/components/schemas/InputTextContent/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) detail": {
    "kind": "HttpDeclProperty",
    "docstring": "The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.",
    "key": "detail",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "original"
        }
      ],
      "oasRef": "#/components/schemas/InputImageContent/properties/detail"
    },
    "oasRef": "#/components/schemas/InputImageContent/properties/detail",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 0",
      "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 1",
      "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 2",
      "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 3"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the input item. Always `input_image`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "default": "input_image",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_image"
        }
      ],
      "oasRef": "#/components/schemas/InputImageContent/properties/type"
    },
    "oasRef": "#/components/schemas/InputImageContent/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the file to be sent to the model.",
    "key": "file_id",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/InputImageContent/properties/file_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) image_url": {
    "kind": "HttpDeclProperty",
    "docstring": "The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.",
    "key": "image_url",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "oasRef": "#/components/schemas/InputImageContent/properties/image_url",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "title": "Prompt cache breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "key": "prompt_cache_breakpoint",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "oasRef": "#/components/schemas/InputImageContent/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the input item. Always `input_file`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "default": "input_file",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_file"
        }
      ],
      "oasRef": "#/components/schemas/InputFileContent/properties/type"
    },
    "oasRef": "#/components/schemas/InputFileContent/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) detail": {
    "kind": "HttpDeclProperty",
    "docstring": "The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.",
    "key": "detail",
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
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ],
      "oasRef": "#/components/schemas/InputFileContent/properties/detail"
    },
    "oasRef": "#/components/schemas/InputFileContent/properties/detail",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 0",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 1",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 2"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) file_data": {
    "kind": "HttpDeclProperty",
    "docstring": "The content of the file to be sent to the model.\n",
    "key": "file_data",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/InputFileContent/properties/file_data",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the file to be sent to the model.",
    "key": "file_id",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/InputFileContent/properties/file_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) file_url": {
    "kind": "HttpDeclProperty",
    "docstring": "The URL of the file to be sent to the model.",
    "key": "file_url",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "oasRef": "#/components/schemas/InputFileContent/properties/file_url",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) filename": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the file to be sent to the model.",
    "key": "filename",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/InputFileContent/properties/filename",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "title": "Prompt cache breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "key": "prompt_cache_breakpoint",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "oasRef": "#/components/schemas/InputFileContent/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) tool_choice_function > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) responses > (model) tool_choice_mcp > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp"
    }
  },
  "(resource) realtime > (model) realtime_function_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0",
    "ident": "McpAllowedTools",
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeString"
      },
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0"
    },
    "docstring": "A string array of allowed tool names",
    "children": []
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/1",
    "ident": "McpToolFilter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "read_only"
        },
        {
          "ident": "tool_names"
        }
      ]
    },
    "docstring": "A filter object to specify which tools are allowed.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools > (variant) 1 > (property) read_only",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) allowed_tools > (variant) 1 > (property) tool_names"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_dropbox"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_gmail"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_googlecalendar"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_googledrive"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_microsoftteams"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_outlookcalendar"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_outlookemail"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) connector_id > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_sharepoint"
    }
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/0",
    "ident": "McpToolApprovalFilter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "always"
        },
        {
          "ident": "never"
        }
      ]
    },
    "docstring": "Specify which of the MCP server's tools require approval. Can be\n`always`, `never`, or a filter object associated with tools\nthat require approval.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 0 > (property) always",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 0 > (property) never"
    ]
  },
  "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/1",
    "ident": "McpToolApprovalSetting",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "always"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "never"
        }
      ],
      "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/1"
    },
    "docstring": "Specify a single approval policy for all tools. One of `always` or\n`never`. When set to `always`, all tools will require approval. When\nset to `never`, all tools will not require approval.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 1 > (member) 0",
      "(resource) realtime > (model) realtime_tools_config_union > (schema) > (variant) 1 > (property) require_approval > (variant) 1 > (member) 1"
    ]
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "retention_ratio"
    }
  },
  "(resource) realtime > (model) realtime_truncation > (schema) > (variant) 1 > (property) token_limits > (property) post_instructions": {
    "kind": "HttpDeclProperty",
    "docstring": "Maximum tokens allowed in the conversation after instructions (which including tool definitions). For example, setting this to 5,000 would mean that truncation would occur when the conversation exceeds 5,000 tokens after instructions. This cannot be higher than the model's context window size minus the maximum output tokens.",
    "key": "post_instructions",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0
    },
    "oasRef": "#/components/schemas/RealtimeTruncation/oneOf/1/properties/token_limits/properties/post_instructions",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input > (schema) > (property) noise_reduction > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.\n",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "NoiseReductionType",
      "$ref": "(resource) realtime > (model) noise_reduction_type > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input/properties/noise_reduction/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) noise_reduction_type",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 0",
      "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 1"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0",
    "ident": "ServerVad",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "create_response"
        },
        {
          "ident": "idle_timeout_ms"
        },
        {
          "ident": "interrupt_response"
        },
        {
          "ident": "prefix_padding_ms"
        },
        {
          "ident": "silence_duration_ms"
        },
        {
          "ident": "threshold"
        }
      ]
    },
    "docstring": "Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0 > (property) type",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0 > (property) create_response",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0 > (property) idle_timeout_ms",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0 > (property) interrupt_response",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0 > (property) prefix_padding_ms",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0 > (property) silence_duration_ms",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0 > (property) threshold"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1",
    "ident": "SemanticVad",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "create_response"
        },
        {
          "ident": "eagerness"
        },
        {
          "ident": "interrupt_response"
        }
      ]
    },
    "docstring": "Server-side semantic turn detection which uses a model to determine when the user has finished speaking.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 1 > (property) type",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 1 > (property) create_response",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 1 > (property) eagerness",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 1 > (property) interrupt_response"
    ]
  },
  "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input/properties/turn_detection",
    "ident": "RealtimeTranscriptionSessionAudioInputTurnDetection",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "create_response"
            },
            {
              "ident": "idle_timeout_ms"
            },
            {
              "ident": "interrupt_response"
            },
            {
              "ident": "prefix_padding_ms"
            },
            {
              "ident": "silence_duration_ms"
            },
            {
              "ident": "threshold"
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
              "ident": "create_response"
            },
            {
              "ident": "eagerness"
            },
            {
              "ident": "interrupt_response"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/RealtimeTranscriptionSessionCreateRequestGA/properties/audio/properties/input/properties/turn_detection"
    },
    "docstring": "Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.\n\nServer VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.\n\nSemantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with \"uhhm\", the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.\n\nFor `gpt-realtime-whisper` transcription sessions, turn detection must be\nset to `null`; VAD is not supported.\n",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 0",
      "(resource) realtime > (model) realtime_transcription_session_audio_input_turn_detection > (schema) > (variant) 1"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0 > (property) rate": {
    "kind": "HttpDeclProperty",
    "docstring": "The sample rate of the audio. Always `24000`.",
    "key": "rate",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": 24000
        }
      ],
      "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/0/properties/rate"
    },
    "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/0/properties/rate",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0 > (property) rate > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The audio format. Always `audio/pcm`.",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "audio/pcm"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/0/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/0/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The audio format. Always `audio/pcmu`.",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "audio/pcmu"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/1/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/1/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The audio format. Always `audio/pcma`.",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "audio/pcma"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/2/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeAudioFormats/anyOf/2/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_formats > (schema) > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "near_field"
    }
  },
  "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "far_field"
    }
  },
  "(resource) realtime > (model) noise_reduction_type > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/NoiseReductionType",
    "ident": "NoiseReductionType",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "near_field"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "far_field"
        }
      ],
      "oasRef": "#/components/schemas/NoiseReductionType"
    },
    "docstring": "Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 0",
      "(resource) realtime > (model) noise_reduction_type > (schema) > (member) 1"
    ]
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "minimal"
    }
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) delay > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AudioTranscription/properties/model/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/AudioTranscription/properties/model/anyOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "whisper-1"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-transcribe"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-mini-transcribe-2025-12-15"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-transcribe"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-4o-transcribe-diarize"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-realtime-whisper"
        }
      ],
      "oasRef": "#/components/schemas/AudioTranscription/properties/model/anyOf/1"
    },
    "docstring": "The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.\n",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1 > (member) 0",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1 > (member) 1",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1 > (member) 2",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1 > (member) 3",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1 > (member) 4",
      "(resource) realtime > (model) audio_transcription > (schema) > (property) model > (variant) 1 > (member) 5"
    ]
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "Type of turn detection, `server_vad` to turn on simple Server VAD.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "default": "server_vad",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "server_vad"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) create_response": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.\n\nIf both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.\n",
    "key": "create_response",
    "optional": true,
    "nullable": false,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/create_response",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) idle_timeout_ms": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional timeout after which a model response will be triggered automatically. This is\nuseful for situations in which a long pause from the user is unexpected, such as a phone\ncall. The model will effectively prompt the user to continue the conversation based\non the current context.\n\nThe timeout value will be applied after the last model response's audio has finished playing,\ni.e. it's set to the `response.done` time plus audio playback duration.\n\nAn `input_audio_buffer.timeout_triggered` event (plus events\nassociated with the Response) will be emitted when the timeout is reached.\nIdle timeout is currently only supported for `server_vad` mode.\n",
    "key": "idle_timeout_ms",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 5000,
      "maximum": 30000
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/idle_timeout_ms",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) interrupt_response": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether or not to automatically interrupt (cancel) any ongoing response with output to the default\nconversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.\n\nIf both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.\n",
    "key": "interrupt_response",
    "optional": true,
    "nullable": false,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/interrupt_response",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) prefix_padding_ms": {
    "kind": "HttpDeclProperty",
    "docstring": "Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in\nmilliseconds). Defaults to 300ms.\n",
    "key": "prefix_padding_ms",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/prefix_padding_ms",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) silence_duration_ms": {
    "kind": "HttpDeclProperty",
    "docstring": "Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults\nto 500ms. With shorter values the model will respond more quickly,\nbut may jump in on short pauses from the user.\n",
    "key": "silence_duration_ms",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/silence_duration_ms",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 0 > (property) threshold": {
    "kind": "HttpDeclProperty",
    "docstring": "Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A\nhigher threshold will require louder audio to activate the model, and\nthus might perform better in noisy environments.\n",
    "key": "threshold",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/0/properties/threshold",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "Type of turn detection, `semantic_vad` to turn on Semantic VAD.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "semantic_vad"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) create_response": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether or not to automatically generate a response when a VAD stop event occurs.\n",
    "key": "create_response",
    "optional": true,
    "nullable": false,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1/properties/create_response",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) eagerness": {
    "kind": "HttpDeclProperty",
    "docstring": "Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.\n",
    "key": "eagerness",
    "optional": true,
    "nullable": false,
    "default": "auto",
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
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1/properties/eagerness"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1/properties/eagerness",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) eagerness > (member) 0",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) eagerness > (member) 1",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) eagerness > (member) 2",
      "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) eagerness > (member) 3"
    ]
  },
  "(resource) realtime > (model) realtime_audio_input_turn_detection > (schema) > (variant) 1 > (property) interrupt_response": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether or not to automatically interrupt any ongoing response with output to the default\nconversation (i.e. `conversation` of `auto`) when a VAD start event occurs.\n",
    "key": "interrupt_response",
    "optional": true,
    "nullable": false,
    "default": true,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RealtimeTurnDetection/anyOf/0/oneOf/1/properties/interrupt_response",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "alloy"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ash"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ballad"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "coral"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "echo"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "sage"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "shimmer"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "verse"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "marin"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 1 > (member) 9": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "cedar"
    }
  },
  "(resource) realtime > (model) realtime_audio_config_output > (schema) > (property) voice > (variant) 2 > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The custom voice ID, e.g. `voice_1234`.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "voice_1234"
    ],
    "oasRef": "#/components/schemas/VoiceIdsOrCustomVoice/anyOf/1/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_text"
    }
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint > (property) mode": {
    "kind": "HttpDeclProperty",
    "docstring": "The breakpoint mode. Always `explicit`.",
    "key": "mode",
    "optional": false,
    "nullable": false,
    "default": "explicit",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "explicit"
        }
      ],
      "oasRef": "#/components/schemas/PromptCacheBreakpointConfig/properties/mode"
    },
    "oasRef": "#/components/schemas/PromptCacheBreakpointConfig/properties/mode",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) detail > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "original"
    }
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_image"
    }
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint > (property) mode": {
    "kind": "HttpDeclProperty",
    "docstring": "The breakpoint mode. Always `explicit`.",
    "key": "mode",
    "optional": false,
    "nullable": false,
    "default": "explicit",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "explicit"
        }
      ],
      "oasRef": "#/components/schemas/PromptCacheBreakpointConfig/properties/mode"
    },
    "oasRef": "#/components/schemas/PromptCacheBreakpointConfig/properties/mode",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_file"
    }
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint > (property) mode": {
    "kind": "HttpDeclProperty",
    "docstring": "The breakpoint mode. Always `explicit`.",
    "key": "mode",
    "optional": false,
    "nullable": false,
    "default": "explicit",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "explicit"
        }
      ],
      "oasRef": "#/component

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/realtime/client-events.md
