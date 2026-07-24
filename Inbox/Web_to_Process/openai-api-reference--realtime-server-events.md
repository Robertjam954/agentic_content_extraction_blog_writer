---
source_url: https://developers.openai.com/api/reference/resources/realtime/server-events.md
title: "Realtime server events"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Realtime server events

> OpenAI API streaming event reference.
These are events emitted from the OpenAI Realtime WebSocket server to the client.

## conversation.created

Returned when a conversation is created. Emitted right after session creation.

### Schema

Schema name: `RealtimeServerEventConversationCreated`

```json
{
  "(resource) realtime > (model) conversation_created_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationCreated",
    "ident": "ConversationCreatedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "conversation"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Returned when a conversation is created. Emitted right after session creation.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_created_event > (schema) > (property) conversation",
      "(resource) realtime > (model) conversation_created_event > (schema) > (property) event_id",
      "(resource) realtime > (model) conversation_created_event > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) conversation_created_event > (schema) > (property) conversation": {
    "kind": "HttpDeclProperty",
    "docstring": "The conversation resource.",
    "key": "conversation",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "object"
        }
      ]
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationCreated/properties/conversation",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_created_event > (schema) > (property) conversation > (property) id",
      "(resource) realtime > (model) conversation_created_event > (schema) > (property) conversation > (property) object"
    ]
  },
  "(resource) realtime > (model) conversation_created_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the server event.",
    "key": "event_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationCreated/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_created_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be `conversation.created`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "conversation.created"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationCreated/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationCreated/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_created_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_created_event > (schema) > (property) conversation > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the conversation.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationCreated/properties/conversation/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_created_event > (schema) > (property) conversation > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "The object type, must be `realtime.conversation`.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationCreated/properties/conversation/properties/object",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_created_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "conversation.created"
    }
  }
}
```

### Example

```json
{
    "event_id": "event_9101",
    "type": "conversation.created",
    "conversation": {
        "id": "conv_001",
        "object": "realtime.conversation"
    }
}
```

## conversation.item.created

Returned when a conversation item is created. There are several scenarios that produce this event:
  - The server is generating a Response, which if successful will produce
    either one or two Items, which will be of type `message`
    (role `assistant`) or type `function_call`.
  - The input audio buffer has been committed, either by the client or the
    server (in `server_vad` mode). The server will take the content of the
    input audio buffer and add it to a new user message Item.
  - The client has sent a `conversation.item.create` event to add a new Item
    to the Conversation.

### Schema

Schema name: `RealtimeServerEventConversationItemCreated`

```json
{
  "(resource) realtime > (model) conversation_item_created_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemCreated",
    "ident": "ConversationItemCreatedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "item"
        },
        {
          "ident": "type"
        },
        {
          "ident": "previous_item_id"
        }
      ]
    },
    "docstring": "Returned when a conversation item is created. There are several scenarios that produce this event:\n  - The server is generating a Response, which if successful will produce\n    either one or two Items, which will be of type `message`\n    (role `assistant`) or type `function_call`.\n  - The input audio buffer has been committed, either by the client or the\n    server (in `server_vad` mode). The server will take the content of the\n    input audio buffer and add it to a new user message Item.\n  - The client has sent a `conversation.item.create` event to add a new Item\n    to the Conversation.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) event_id",
      "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) item",
      "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) type",
      "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) previous_item_id"
    ]
  },
  "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the server event.",
    "key": "event_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemCreated/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) item": {
    "kind": "HttpDeclProperty",
    "docstring": "A single item within a Realtime conversation.",
    "key": "item",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ConversationItem",
      "$ref": "(resource) realtime > (model) conversation_item > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemCreated/properties/item",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) conversation_item",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 0",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 1",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 2",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 3",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 4",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 5",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 6",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 7",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 8"
    ]
  },
  "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be `conversation.item.created`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "conversation.item.created"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemCreated/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemCreated/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) previous_item_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the preceding item in the Conversation context, allows the\nclient to understand the order of the conversation. Can be `null` if the\nitem has no predecessor.\n",
    "key": "previous_item_id",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemCreated/properties/previous_item_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemSystemMessage",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_system_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemUserMessage",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_user_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemAssistantMessage",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemFunctionCall",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) name",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) call_id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemFunctionCallOutput",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) call_id",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) output",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpApprovalResponse",
      "$ref": "(resource) realtime > (model) realtime_mcp_approval_response > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approval_request_id",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approve",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) reason"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpListTools",
      "$ref": "(resource) realtime > (model) realtime_mcp_list_tools > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) id"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpToolCall",
      "$ref": "(resource) realtime > (model) realtime_mcp_tool_call > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) name",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) approval_request_id",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) output"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpApprovalRequest",
      "$ref": "(resource) realtime > (model) realtime_mcp_approval_request > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) name",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItem",
    "ident": "ConversationItem",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemSystemMessage",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_system_message > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemUserMessage",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_user_message > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemAssistantMessage",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemFunctionCall",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemFunctionCallOutput",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpApprovalResponse",
          "$ref": "(resource) realtime > (model) realtime_mcp_approval_response > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpListTools",
          "$ref": "(resource) realtime > (model) realtime_mcp_list_tools > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpToolCall",
          "$ref": "(resource) realtime > (model) realtime_mcp_tool_call > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpApprovalRequest",
          "$ref": "(resource) realtime > (model) realtime_mcp_approval_request > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItem"
    },
    "docstring": "A single item within a Realtime conversation.",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 0",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 1",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 2",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 3",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 4",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 5",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 6",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 7",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 8"
    ]
  },
  "(resource) realtime > (model) conversation_item_created_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "conversation.item.created"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "docstring": "The content of the message.",
    "key": "content",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "text"
          },
          {
            "ident": "type"
          }
        ]
      },
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/content"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/content",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) text",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "docstring": "The role of the message sender. Always `system`.",
    "key": "role",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "system"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/role"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/role",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `message`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem",
    "ident": "RealtimeConversationItemSystemMessage",
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
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation's behavior, use instructions, but for smaller updates (e.g. \"the user is now asking about a different topic\"), use system messages.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "docstring": "The content of the message.",
    "key": "content",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "audio"
          },
          {
            "ident": "detail"
          },
          {
            "ident": "image_url"
          },
          {
            "ident": "text"
          },
          {
            "ident": "transcript"
          },
          {
            "ident": "type"
          }
        ]
      },
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) audio",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) image_url",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) text",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) transcript",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "docstring": "The role of the message sender. Always `user`.",
    "key": "role",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "user"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/role"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/role",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `message`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser",
    "ident": "RealtimeConversationItemUserMessage",
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
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A user message item in a Realtime conversation.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "docstring": "The content of the message.",
    "key": "content",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "audio"
          },
          {
            "ident": "text"
          },
          {
            "ident": "transcript"
          },
          {
            "ident": "type"
          }
        ]
      },
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) audio",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) text",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) transcript",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "docstring": "The role of the message sender. Always `assistant`.",
    "key": "role",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "assistant"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/role"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/role",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `message`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant",
    "ident": "RealtimeConversationItemAssistantMessage",
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
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "An assistant message item in a Realtime conversation.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) arguments": {
    "kind": "HttpDeclProperty",
    "docstring": "The arguments of the function call. This is a JSON-encoded string representing the arguments passed to the function, for example `{\"arg1\": \"value1\", \"arg2\": 42}`.",
    "key": "arguments",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/arguments",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function being called.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `function_call`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function_call"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) call_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the function call.",
    "key": "call_id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/call_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall",
    "ident": "RealtimeConversationItemFunctionCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "arguments"
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
          "ident": "call_id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A function call item in a Realtime conversation.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) name",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) call_id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) call_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the function call this output is for.",
    "key": "call_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/call_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) output": {
    "kind": "HttpDeclProperty",
    "docstring": "The output of the function call, this is free text and can contain any information or simply be empty.",
    "key": "output",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/output",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `function_call_output`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function_call_output"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCallOutput",
    "ident": "RealtimeConversationItemFunctionCallOutput",
    "type": {
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
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A function call output item in a Realtime conversation.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) call_id",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) output",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the approval response.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalResponse/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approval_request_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the approval request being answered.",
    "key": "approval_request_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalResponse/properties/approval_request_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approve": {
    "kind": "HttpDeclProperty",
    "docstring": "Whether the request was approved.",
    "key": "approve",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalResponse/properties/approve",
    "deprecated": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `mcp_approval_response`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_approval_response"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPApprovalResponse/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalResponse/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) reason": {
    "kind": "HttpDeclProperty",
    "docstring": "Optional reason for the decision.",
    "key": "reason",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalResponse/properties/reason",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_response > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeMCPApprovalResponse",
    "ident": "RealtimeMcpApprovalResponse",
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
    "docstring": "A Realtime item responding to an MCP approval request.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approval_request_id",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approve",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) reason"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) server_label": {
    "kind": "HttpDeclProperty",
    "docstring": "The label of the MCP server.",
    "key": "server_label",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPListTools/properties/server_label",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "docstring": "The tools available on the server.",
    "key": "tools",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "input_schema"
          },
          {
            "ident": "name"
          },
          {
            "ident": "annotations"
          },
          {
            "ident": "description"
          }
        ]
      },
      "oasRef": "#/components/schemas/RealtimeMCPListTools/properties/tools"
    },
    "oasRef": "#/components/schemas/RealtimeMCPListTools/properties/tools",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) input_schema",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) name",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) annotations",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) description"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `mcp_list_tools`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_list_tools"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPListTools/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeMCPListTools/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the list.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPListTools/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeMCPListTools",
    "ident": "RealtimeMcpListTools",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
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
          "ident": "id"
        }
      ]
    },
    "docstring": "A Realtime item listing tools available on an MCP server.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) id"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the tool call.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) arguments": {
    "kind": "HttpDeclProperty",
    "docstring": "A JSON string of the arguments passed to the tool.",
    "key": "arguments",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/arguments",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the tool that was run.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) server_label": {
    "kind": "HttpDeclProperty",
    "docstring": "The label of the MCP server running the tool.",
    "key": "server_label",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/server_label",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `mcp_call`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_call"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) approval_request_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of an associated approval request, if any.",
    "key": "approval_request_id",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/approval_request_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error": {
    "kind": "HttpDeclProperty",
    "docstring": "The error from the tool call, if any.",
    "key": "error",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpProtocolError",
          "$ref": "(resource) realtime > (model) realtime_mcp_protocol_error > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpToolExecutionError",
          "$ref": "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcphttpError",
          "$ref": "(resource) realtime > (model) realtime_mcphttp_error > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/error"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/error",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error > (variant) 0",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error > (variant) 1",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error > (variant) 2"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) output": {
    "kind": "HttpDeclProperty",
    "docstring": "The output from the tool call.",
    "key": "output",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolCall/properties/output",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeMCPToolCall",
    "ident": "RealtimeMcpToolCall",
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
        }
      ]
    },
    "docstring": "A Realtime item representing an invocation of a tool on an MCP server.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) name",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) approval_request_id",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) output"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the approval request.",
    "key": "id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalRequest/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) arguments": {
    "kind": "HttpDeclProperty",
    "docstring": "A JSON string of arguments for the tool.",
    "key": "arguments",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalRequest/properties/arguments",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the tool to run.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalRequest/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) server_label": {
    "kind": "HttpDeclProperty",
    "docstring": "The label of the MCP server making the request.",
    "key": "server_label",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalRequest/properties/server_label",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `mcp_approval_request`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_approval_request"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPApprovalRequest/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeMCPApprovalRequest/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_approval_request > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeMCPApprovalRequest",
    "ident": "RealtimeMcpApprovalRequest",
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
    "docstring": "A Realtime item requesting human approval of a tool invocation.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) name",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) text": {
    "kind": "HttpDeclProperty",
    "docstring": "The text content.",
    "key": "text",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/content/items/properties/text",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The content type. Always `input_text` for system messages.",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_text"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/content/items/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/content/items/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "system"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "realtime.item"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) audio": {
    "kind": "HttpDeclProperty",
    "docstring": "Base64-encoded audio bytes (for `input_audio`), these will be parsed as the format specified in the session input audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.",
    "key": "audio",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/audio",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail": {
    "kind": "HttpDeclProperty",
    "docstring": "The detail level of the image (for `input_image`). `auto` will default to `high`.",
    "key": "detail",
    "optional": true,
    "nullable": false,
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
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/detail"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/detail",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) image_url": {
    "kind": "HttpDeclProperty",
    "docstring": "Base64-encoded image bytes (for `input_image`) as a data URI. For example `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...`. Supported formats are PNG and JPEG.",
    "key": "image_url",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/image_url",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) text": {
    "kind": "HttpDeclProperty",
    "docstring": "The text content (for `input_text`).",
    "key": "text",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/text",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) transcript": {
    "kind": "HttpDeclProperty",
    "docstring": "Transcript of the audio (for `input_audio`). This is not sent to the model, but will be attached to the message item for reference.",
    "key": "transcript",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/transcript",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The content type (`input_text`, `input_audio`, or `input_image`).",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_text"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_audio"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_image"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content/items/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "user"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "realtime.item"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) audio": {
    "kind": "HttpDeclProperty",
    "docstring": "Base64-encoded audio bytes, these will be parsed as the format specified in the session output audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.",
    "key": "audio",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content/items/properties/audio",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) text": {
    "kind": "HttpDeclProperty",
    "docstring": "The text content.",
    "key": "text",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content/items/properties/text",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) transcript": {
    "kind": "HttpDeclProperty",
    "docstring": "The transcript of the audio content, this will always be present if the output type is `audio`.",
    "key": "transcript",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content/items/properties/transcript",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The content type, `output_text` or `output_audio` depending on the session `output_modalities` configuration.",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "output_text"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "output_audio"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content/items/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content/items/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) type > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) type > (member) 1"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "assistant"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "realtime.item"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function_call"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "realtime.item"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function_call_output"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) object > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "realtime.item"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_approval_response"
    }
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) input_schema": {
    "kind": "HttpDeclProperty",
    "docstring": "The JSON schema describing the tool's input.\n",
    "key": "input_schema",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/input_schema",
    "deprecated": false,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the tool.\n",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) annotations": {
    "kind": "HttpDeclProperty",
    "docstring": "Additional annotations about the tool.\n",
    "key": "annotations",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/annotations",
    "deprecated": false,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools > (items) > (property) description": {
    "kind": "HttpDeclProperty",
    "docstring": "The description of the tool.\n",
    "key": "description",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/description",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_list_tools"
    }
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_call"
    }
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpProtocolError",
      "$ref": "(resource) realtime > (model) realtime_mcp_protocol_error > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) code",
      "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) message",
      "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpToolExecutionError",
      "$ref": "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) message",
      "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcphttpError",
      "$ref": "(resource) realtime > (model) realtime_mcphttp_error > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) code",
      "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) message",
      "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_protocol_error > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeMCPProtocolError",
    "ident": "RealtimeMcpProtocolError",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "message"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) code",
      "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) message",
      "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeMCPToolExecutionError",
    "ident": "RealtimeMcpToolExecutionError",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "message"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) message",
      "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_mcphttp_error > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeMCPHTTPError",
    "ident": "RealtimeMcphttpError",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "message"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) code",
      "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) message",
      "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_approval_request"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_text"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_text"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_audio"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_image"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "output_text"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "output_audio"
    }
  },
  "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) code": {
    "kind": "HttpDeclProperty",
    "key": "code",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeMCPProtocolError/properties/code",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) message": {
    "kind": "HttpDeclProperty",
    "key": "message",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPProtocolError/properties/message",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "protocol_error"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPProtocolError/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeMCPProtocolError/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) message": {
    "kind": "HttpDeclProperty",
    "key": "message",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolExecutionError/properties/message",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "tool_execution_error"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPToolExecutionError/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeMCPToolExecutionError/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) code": {
    "kind": "HttpDeclProperty",
    "key": "code",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeMCPHTTPError/properties/code",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) message": {
    "kind": "HttpDeclProperty",
    "key": "message",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeMCPHTTPError/properties/message",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "http_error"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeMCPHTTPError/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeMCPHTTPError/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_mcp_protocol_error > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "protocol_error"
    }
  },
  "(resource) realtime > (model) realtime_mcp_tool_execution_error > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "tool_execution_error"
    }
  },
  "(resource) realtime > (model) realtime_mcphttp_error > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "http_error"
    }
  }
}
```

### Example

```json
{
    "event_id": "event_1920",
    "type": "conversation.item.created",
    "previous_item_id": "msg_002",
    "item": {
        "id": "msg_003",
        "object": "realtime.item",
        "type": "message",
        "status": "completed",
        "role": "user",
        "content": []
    }
}
```

## conversation.item.deleted

Returned when an item in the conversation is deleted by the client with a
`conversation.item.delete` event. This event is used to synchronize the
server's understanding of the conversation history with the client's view.

### Schema

Schema name: `RealtimeServerEventConversationItemDeleted`

```json
{
  "(resource) realtime > (model) conversation_item_deleted_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemDeleted",
    "ident": "ConversationItemDeletedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "item_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Returned when an item in the conversation is deleted by the client with a \n`conversation.item.delete` event. This event is used to synchronize the \nserver's understanding of the conversation history with the client's view.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) event_id",
      "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) item_id",
      "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the server event.",
    "key": "event_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemDeleted/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) item_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the item that was deleted.",
    "key": "item_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemDeleted/properties/item_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be `conversation.item.deleted`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "conversation.item.deleted"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemDeleted/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemDeleted/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item_deleted_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "conversation.item.deleted"
    }
  }
}
```

### Example

```json
{
    "event_id": "event_2728",
    "type": "conversation.item.deleted",
    "item_id": "msg_005"
}
```

## conversation.item.input_audio_transcription.completed

This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (when VAD is enabled). Transcription runs
asynchronously with Response creation, so this event may come before or after
the Response events.

Realtime API models accept audio natively, and thus input transcription is a
separate process run on a separate ASR (Automatic Speech Recognition) model.
The transcript may diverge somewhat from the model's interpretation, and
should be treated as a rough guide.

### Schema

Schema name: `RealtimeServerEventConversationItemInputAudioTranscriptionCompleted`

```json
{
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted",
    "ident": "ConversationItemInputAudioTranscriptionCompletedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content_index"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "item_id"
        },
        {
          "ident": "transcript"
        },
        {
          "ident": "type"
        },
        {
          "ident": "usage"
        },
        {
          "ident": "logprobs"
        }
      ]
    },
    "docstring": "This event is the output of audio transcription for user audio written to the\nuser audio buffer. Transcription begins when the input audio buffer is\ncommitted by the client or server (when VAD is enabled). Transcription runs\nasynchronously with Response creation, so this event may come before or after\nthe Response events.\n\nRealtime API models accept audio natively, and thus input transcription is a\nseparate process run on a separate ASR (Automatic Speech Recognition) model.\nThe transcript may diverge somewhat from the model's interpretation, and\nshould be treated as a rough guide.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) content_index",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) event_id",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) item_id",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) transcript",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) type",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) logprobs"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) content_index": {
    "kind": "HttpDeclProperty",
    "docstring": "The index of the content part containing the audio.",
    "key": "content_index",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/content_index",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the server event.",
    "key": "event_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) item_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the item containing the audio that is being transcribed.",
    "key": "item_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/item_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) transcript": {
    "kind": "HttpDeclProperty",
    "docstring": "The transcribed text.",
    "key": "transcript",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/transcript",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be\n`conversation.item.input_audio_transcription.completed`.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "conversation.item.input_audio_transcription.completed"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage": {
    "kind": "HttpDeclProperty",
    "docstring": "Usage statistics for the transcription, this is billed according to the ASR model's pricing rather than the realtime model's pricing.",
    "key": "usage",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "input_tokens"
            },
            {
              "ident": "output_tokens"
            },
            {
              "ident": "total_tokens"
            },
            {
              "ident": "type"
            },
            {
              "ident": "input_token_details"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "seconds"
            },
            {
              "ident": "type"
            }
          ]
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/usage"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/usage",
    "deprecated": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) logprobs": {
    "kind": "HttpDeclProperty",
    "docstring": "The log probabilities of the transcription.",
    "key": "logprobs",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "LogProbProperties",
        "$ref": "(resource) realtime > (model) log_prob_properties > (schema)"
      },
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/logprobs"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/logprobs",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) token",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) bytes",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) logprob"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "conversation.item.input_audio_transcription.completed"
    }
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/usage/oneOf/0",
    "ident": "TokenUsage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "input_tokens"
        },
        {
          "ident": "output_tokens"
        },
        {
          "ident": "total_tokens"
        },
        {
          "ident": "type"
        },
        {
          "ident": "input_token_details"
        }
      ]
    },
    "docstring": "Usage statistics for models billed by token usage.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_tokens",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) output_tokens",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) total_tokens",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) type",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_token_details"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionCompleted/properties/usage/oneOf/1",
    "ident": "DurationUsage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "seconds"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Usage statistics for models billed by audio input duration.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1 > (property) seconds",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1 > (property) type"
    ]
  },
  "(resource) realtime > (model) log_prob_properties > (schema) > (property) token": {
    "kind": "HttpDeclProperty",
    "docstring": "The token that was used to generate the log probability.\n",
    "key": "token",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/LogProbProperties/properties/token",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) log_prob_properties > (schema) > (property) bytes": {
    "kind": "HttpDeclProperty",
    "docstring": "The bytes that were used to generate the log probability.\n",
    "key": "bytes",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeNumber"
      },
      "oasRef": "#/components/schemas/LogProbProperties/properties/bytes"
    },
    "oasRef": "#/components/schemas/LogProbProperties/properties/bytes",
    "deprecated": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) realtime > (model) log_prob_properties > (schema) > (property) logprob": {
    "kind": "HttpDeclProperty",
    "docstring": "The log probability of the token.\n",
    "key": "logprob",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/LogProbProperties/properties/logprob",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) realtime > (model) log_prob_properties > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LogProbProperties",
    "ident": "LogProbProperties",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "token"
        },
        {
          "ident": "bytes"
        },
        {
          "ident": "logprob"
        }
      ]
    },
    "docstring": "A log probability object.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) token",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) bytes",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) logprob"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of input tokens billed for this request.",
    "key": "input_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/input_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) output_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of output tokens generated.",
    "key": "output_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/output_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) total_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Total number of tokens used (input + output).",
    "key": "total_tokens",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/total_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the usage object. Always `tokens` for this variant.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "tokens"
        }
      ],
      "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/type"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_token_details": {
    "kind": "HttpDeclProperty",
    "docstring": "Details about the input tokens billed for this request.",
    "key": "input_token_details",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "audio_tokens"
        },
        {
          "ident": "text_tokens"
        }
      ]
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/input_token_details",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_token_details > (property) audio_tokens",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_token_details > (property) text_tokens"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1 > (property) seconds": {
    "kind": "HttpDeclProperty",
    "docstring": "Duration of the input audio in seconds.",
    "key": "seconds",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "double"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageDuration/properties/seconds",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the usage object. Always `duration` for this variant.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "duration"
        }
      ],
      "oasRef": "#/components/schemas/TranscriptTextUsageDuration/properties/type"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageDuration/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "tokens"
    }
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_token_details > (property) audio_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of audio tokens billed for this request.",
    "key": "audio_tokens",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/input_token_details/properties/audio_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 0 > (property) input_token_details > (property) text_tokens": {
    "kind": "HttpDeclProperty",
    "docstring": "Number of text tokens billed for this request.",
    "key": "text_tokens",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/TranscriptTextUsageTokens/properties/input_token_details/properties/text_tokens",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_completed_event > (schema) > (property) usage > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "duration"
    }
  }
}
```

### Example

```json
{
  "type": "conversation.item.input_audio_transcription.completed",
  "event_id": "event_CCXGRvtUVrax5SJAnNOWZ",
  "item_id": "item_CCXGQ4e1ht4cOraEYcuR2",
  "content_index": 0,
  "transcript": "Hey, can you hear me?",
  "usage": {
    "type": "tokens",
    "total_tokens": 22,
    "input_tokens": 13,
    "input_token_details": {
      "text_tokens": 0,
      "audio_tokens": 13
    },
    "output_tokens": 9
  }
}
```

## conversation.item.input_audio_transcription.delta

Returned when the text value of an input audio transcription content part is updated with incremental transcription results.

### Schema

Schema name: `RealtimeServerEventConversationItemInputAudioTranscriptionDelta`

```json
{
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta",
    "ident": "ConversationItemInputAudioTranscriptionDeltaEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "item_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "content_index"
        },
        {
          "ident": "delta"
        },
        {
          "ident": "logprobs"
        }
      ]
    },
    "docstring": "Returned when the text value of an input audio transcription content part is updated with incremental transcription results.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) event_id",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) item_id",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) type",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) content_index",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) delta",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) logprobs"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the server event.",
    "key": "event_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) item_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the item containing the audio that is being transcribed.",
    "key": "item_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/item_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be `conversation.item.input_audio_transcription.delta`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "conversation.item.input_audio_transcription.delta"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) content_index": {
    "kind": "HttpDeclProperty",
    "docstring": "The index of the content part in the item's content array.",
    "key": "content_index",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/content_index",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) delta": {
    "kind": "HttpDeclProperty",
    "docstring": "The text delta.",
    "key": "delta",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/delta",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) logprobs": {
    "kind": "HttpDeclProperty",
    "docstring": "The log probabilities of the transcription. These can be enabled by configurating the session with `\"include\": [\"item.input_audio_transcription.logprobs\"]`. Each entry in the array corresponds a log probability of which token would be selected for this chunk of transcription. This can help to identify if it was possible there were multiple valid options for a given chunk of transcription.",
    "key": "logprobs",
    "optional": true,
    "nullable": true,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "LogProbProperties",
        "$ref": "(resource) realtime > (model) log_prob_properties > (schema)"
      },
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/logprobs"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionDelta/properties/logprobs",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) token",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) bytes",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) logprob"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_delta_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "conversation.item.input_audio_transcription.delta"
    }
  },
  "(resource) realtime > (model) log_prob_properties > (schema) > (property) token": {
    "kind": "HttpDeclProperty",
    "docstring": "The token that was used to generate the log probability.\n",
    "key": "token",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/LogProbProperties/properties/token",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) log_prob_properties > (schema) > (property) bytes": {
    "kind": "HttpDeclProperty",
    "docstring": "The bytes that were used to generate the log probability.\n",
    "key": "bytes",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeNumber"
      },
      "oasRef": "#/components/schemas/LogProbProperties/properties/bytes"
    },
    "oasRef": "#/components/schemas/LogProbProperties/properties/bytes",
    "deprecated": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) realtime > (model) log_prob_properties > (schema) > (property) logprob": {
    "kind": "HttpDeclProperty",
    "docstring": "The log probability of the token.\n",
    "key": "logprob",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/LogProbProperties/properties/logprob",
    "deprecated": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) realtime > (model) log_prob_properties > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LogProbProperties",
    "ident": "LogProbProperties",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "token"
        },
        {
          "ident": "bytes"
        },
        {
          "ident": "logprob"
        }
      ]
    },
    "docstring": "A log probability object.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) token",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) bytes",
      "(resource) realtime > (model) log_prob_properties > (schema) > (property) logprob"
    ]
  }
}
```

### Example

```json
{
  "type": "conversation.item.input_audio_transcription.delta",
  "event_id": "event_CCXGRxsAimPAs8kS2Wc7Z",
  "item_id": "item_CCXGQ4e1ht4cOraEYcuR2",
  "content_index": 0,
  "delta": "Hey",
  "obfuscation": "aLxx0jTEciOGe"
}
```

## conversation.item.input_audio_transcription.failed

Returned when input audio transcription is configured, and a transcription
request for a user message failed. These events are separate from other
`error` events so that the client can identify the related Item.

### Schema

Schema name: `RealtimeServerEventConversationItemInputAudioTranscriptionFailed`

```json
{
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed",
    "ident": "ConversationItemInputAudioTranscriptionFailedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content_index"
        },
        {
          "ident": "error"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "item_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Returned when input audio transcription is configured, and a transcription \nrequest for a user message failed. These events are separate from other \n`error` events so that the client can identify the related Item.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) content_index",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) event_id",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) item_id",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) content_index": {
    "kind": "HttpDeclProperty",
    "docstring": "The index of the content part containing the audio.",
    "key": "content_index",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeNumber"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/content_index",
    "deprecated": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error": {
    "kind": "HttpDeclProperty",
    "docstring": "Details of the transcription error.",
    "key": "error",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "message"
        },
        {
          "ident": "param"
        },
        {
          "ident": "type"
        }
      ]
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/error",
    "deprecated": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) code",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) message",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) param",
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) type"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the server event.",
    "key": "event_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) item_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the user message item.",
    "key": "item_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/item_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be\n`conversation.item.input_audio_transcription.failed`.\n",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "conversation.item.input_audio_transcription.failed"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) code": {
    "kind": "HttpDeclProperty",
    "docstring": "Error code, if any.",
    "key": "code",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/error/properties/code",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) message": {
    "kind": "HttpDeclProperty",
    "docstring": "A human-readable error message.",
    "key": "message",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/error/properties/message",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) param": {
    "kind": "HttpDeclProperty",
    "docstring": "Parameter related to the error, if any.",
    "key": "param",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/error/properties/param",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) error > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of error.",
    "key": "type",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemInputAudioTranscriptionFailed/properties/error/properties/type",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) conversation_item_input_audio_transcription_failed_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "conversation.item.input_audio_transcription.failed"
    }
  }
}
```

### Example

```json
{
    "event_id": "event_2324",
    "type": "conversation.item.input_audio_transcription.failed",
    "item_id": "msg_003",
    "content_index": 0,
    "error": {
        "type": "transcription_error",
        "code": "audio_unintelligible",
        "message": "The audio could not be transcribed.",
        "param": null
    }
}
```

## conversation.item.retrieved

Returned when a conversation item is retrieved with `conversation.item.retrieve`. This is provided as a way to fetch the server's representation of an item, for example to get access to the post-processed audio data after noise cancellation and VAD. It includes the full content of the Item, including audio data.

### Schema

Schema name: `(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6`

```json
{
  "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeServerEvent/anyOf/6",
    "ident": "ConversationItemRetrieved",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "item"
        },
        {
          "ident": "type"
        }
      ]
    },
    "docstring": "Returned when a conversation item is retrieved with `conversation.item.retrieve`. This is provided as a way to fetch the server's representation of an item, for example to get access to the post-processed audio data after noise cancellation and VAD. It includes the full content of the Item, including audio data.\n",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) event_id",
      "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) item",
      "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) event_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the server event.",
    "key": "event_id",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemRetrieved/properties/event_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) item": {
    "kind": "HttpDeclProperty",
    "docstring": "A single item within a Realtime conversation.",
    "key": "item",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ConversationItem",
      "$ref": "(resource) realtime > (model) conversation_item > (schema)"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemRetrieved/properties/item",
    "deprecated": false,
    "schemaType": "union",
    "modelImplicit": false,
    "modelPath": "(resource) realtime > (model) conversation_item",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 0",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 1",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 2",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 3",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 4",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 5",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 6",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 7",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 8"
    ]
  },
  "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The event type, must be `conversation.item.retrieved`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "conversation.item.retrieved"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeServerEventConversationItemRetrieved/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeServerEventConversationItemRetrieved/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemSystemMessage",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_system_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemUserMessage",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_user_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemAssistantMessage",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemFunctionCall",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) name",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) call_id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeConversationItemFunctionCallOutput",
      "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) call_id",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) output",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpApprovalResponse",
      "$ref": "(resource) realtime > (model) realtime_mcp_approval_response > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approval_request_id",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) approve",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_approval_response > (schema) > (property) reason"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpListTools",
      "$ref": "(resource) realtime > (model) realtime_mcp_list_tools > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) tools",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_list_tools > (schema) > (property) id"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpToolCall",
      "$ref": "(resource) realtime > (model) realtime_mcp_tool_call > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) name",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) type",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) approval_request_id",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) error",
      "(resource) realtime > (model) realtime_mcp_tool_call > (schema) > (property) output"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema) > (variant) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "RealtimeMcpApprovalRequest",
      "$ref": "(resource) realtime > (model) realtime_mcp_approval_request > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) id",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) name",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) server_label",
      "(resource) realtime > (model) realtime_mcp_approval_request > (schema) > (property) type"
    ]
  },
  "(resource) realtime > (model) conversation_item > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItem",
    "ident": "ConversationItem",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemSystemMessage",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_system_message > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemUserMessage",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_user_message > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemAssistantMessage",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemFunctionCall",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeConversationItemFunctionCallOutput",
          "$ref": "(resource) realtime > (model) realtime_conversation_item_function_call_output > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpApprovalResponse",
          "$ref": "(resource) realtime > (model) realtime_mcp_approval_response > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpListTools",
          "$ref": "(resource) realtime > (model) realtime_mcp_list_tools > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpToolCall",
          "$ref": "(resource) realtime > (model) realtime_mcp_tool_call > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "RealtimeMcpApprovalRequest",
          "$ref": "(resource) realtime > (model) realtime_mcp_approval_request > (schema)"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItem"
    },
    "docstring": "A single item within a Realtime conversation.",
    "childrenParentSchema": "union",
    "children": [
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 0",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 1",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 2",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 3",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 4",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 5",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 6",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 7",
      "(resource) realtime > (model) conversation_item > (schema) > (variant) 8"
    ]
  },
  "(resource) realtime > (model) realtime_server_event > (schema) > (variant) 6 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "conversation.item.retrieved"
    }
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "docstring": "The content of the message.",
    "key": "content",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "text"
          },
          {
            "ident": "type"
          }
        ]
      },
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/content"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/content",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) text",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content > (items) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "docstring": "The role of the message sender. Always `system`.",
    "key": "role",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "system"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/role"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/role",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `message`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_system_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageSystem",
    "ident": "RealtimeConversationItemSystemMessage",
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
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation's behavior, use instructions, but for smaller updates (e.g. \"the user is now asking about a different topic\"), use system messages.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_system_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "docstring": "The content of the message.",
    "key": "content",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "audio"
          },
          {
            "ident": "detail"
          },
          {
            "ident": "image_url"
          },
          {
            "ident": "text"
          },
          {
            "ident": "transcript"
          },
          {
            "ident": "type"
          }
        ]
      },
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/content",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) audio",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) detail",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) image_url",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) text",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) transcript",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content > (items) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "docstring": "The role of the message sender. Always `user`.",
    "key": "role",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "user"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/role"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/role",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `message`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_user_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageUser",
    "ident": "RealtimeConversationItemUserMessage",
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
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A user message item in a Realtime conversation.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_user_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "docstring": "The content of the message.",
    "key": "content",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeArray",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "audio"
          },
          {
            "ident": "text"
          },
          {
            "ident": "transcript"
          },
          {
            "ident": "type"
          }
        ]
      },
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/content",
    "deprecated": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) audio",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) text",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) transcript",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content > (items) > (property) type"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "docstring": "The role of the message sender. Always `assistant`.",
    "key": "role",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "assistant"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/role"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/role",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `message`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemMessageAssistant",
    "ident": "RealtimeConversationItemAssistantMessage",
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
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "An assistant message item in a Realtime conversation.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) content",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) role",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_assistant_message > (schema) > (property) status"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) arguments": {
    "kind": "HttpDeclProperty",
    "docstring": "The arguments of the function call. This is a JSON-encoded string representing the arguments passed to the function, for example `{\"arg1\": \"value1\", \"arg2\": 42}`.",
    "key": "arguments",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/arguments",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "docstring": "The name of the function being called.",
    "key": "name",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/name",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "docstring": "The type of the item. Always `function_call`.",
    "key": "type",
    "optional": false,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function_call"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/type"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/type",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "docstring": "The unique ID of the item. This may be provided by the client or generated by the server.",
    "key": "id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) call_id": {
    "kind": "HttpDeclProperty",
    "docstring": "The ID of the function call.",
    "key": "call_id",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeString"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/call_id",
    "deprecated": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object": {
    "kind": "HttpDeclProperty",
    "docstring": "Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.",
    "key": "object",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "realtime.item"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/object"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/object",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object > (member) 0"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "docstring": "The status of the item. Has no effect on the conversation.",
    "key": "status",
    "optional": true,
    "nullable": false,
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
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
          "literal": "in_progress"
        }
      ],
      "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/status"
    },
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall/properties/status",
    "deprecated": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 0",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 1",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) realtime > (model) realtime_conversation_item_function_call > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RealtimeConversationItemFunctionCall",
    "ident": "RealtimeConversationItemFunctionCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "arguments"
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
          "ident": "call_id"
        },
        {
          "ident": "object"
        },
        {
          "ident": "status"
        }
      ]
    },
    "docstring": "A function call item in a Realtime conversation.",
    "childrenParentSchema": "object",
    "children": [
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) arguments",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) name",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) type",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) call_id",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) object",
      "(resource) realtime > (model) realtime_conversation_item_function_call > (schema) > (property) status"
    ]
  },
  "(resource) rea

_Content truncated at 200000 characters; read the full page at the source link._

---
Source: https://developers.openai.com/api/reference/resources/realtime/server-events.md
