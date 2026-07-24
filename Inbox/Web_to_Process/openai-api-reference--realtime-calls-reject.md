---
source_url: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/reject
title: "Reject call"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Reject call

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Realtime](/api/reference/resources/realtime)

[Calls](/api/reference/resources/realtime/subresources/calls)

# Reject call

POST /realtime/calls/{call_id}/reject

Decline an incoming SIP call by returning a SIP status code to the caller.

##### P ath Parameters Expand Collapse

call_id : string

[](#(resource)%20realtime.calls%20%3E%20(method)%20reject%20%3E%20(params)%20default%20%3E%20(param)%20call_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

status_code : optional number

SIP response code to send back to the caller. Defaults to `603` (Decline)
when omitted.

[](#(resource)%20realtime.calls%20%3E%20(method)%20reject%20%3E%20(params)%200%20%3E%20(param)%20status_code%20%3E%20(schema))

### Reject call

```
curl -X POST https://api.openai.com/v1/realtime/calls/$CALL_ID/reject \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{"status_code": 486}'
```

##### Returns Examples

---
Source: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/reject
