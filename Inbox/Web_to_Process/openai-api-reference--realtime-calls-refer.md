---
source_url: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/refer
title: "Refer call"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Refer call

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Realtime](/api/reference/resources/realtime)

[Calls](/api/reference/resources/realtime/subresources/calls)

# Refer call

POST /realtime/calls/{call_id}/refer

Transfer an active SIP call to a new destination using the SIP REFER verb.

##### P ath Parameters Expand Collapse

call_id : string

[](#(resource)%20realtime.calls%20%3E%20(method)%20refer%20%3E%20(params)%20default%20%3E%20(param)%20call_id%20%3E%20(schema))

##### Body Parameters JSON Expand Collapse

target_uri : string

URI that should appear in the SIP Refer-To header. Supports values like
`tel:+14155550123` or `sip:agent@example.com`.

[](#(resource)%20realtime.calls%20%3E%20(method)%20refer%20%3E%20(params)%200%20%3E%20(param)%20target_uri%20%3E%20(schema))

### Refer call

```
curl -X POST https://api.openai.com/v1/realtime/calls/$CALL_ID/refer \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{"target_uri": "tel:+14155550123"}'
```

##### Returns Examples

---
Source: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/refer
