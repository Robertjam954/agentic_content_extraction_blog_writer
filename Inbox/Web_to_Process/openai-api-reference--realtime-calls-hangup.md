---
source_url: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/hangup
title: "Hang up call"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Hang up call

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Realtime](/api/reference/resources/realtime)

[Calls](/api/reference/resources/realtime/subresources/calls)

# Hang up call

POST /realtime/calls/{call_id}/hangup

End an active Realtime API call, whether it was initiated over SIP or
WebRTC.

##### P ath Parameters Expand Collapse

call_id : string

[](#(resource)%20realtime.calls%20%3E%20(method)%20hangup%20%3E%20(params)%20default%20%3E%20(param)%20call_id%20%3E%20(schema))

### Hang up call

```
curl -X POST https://api.openai.com/v1/realtime/calls/$CALL_ID/hangup \
-H "Authorization: Bearer $OPENAI_API_KEY"
```

##### Returns Examples

---
Source: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/hangup
