---
source_url: https://developers.openai.com/api/reference/resources/images/methods/create_variation
title: "Create image variation"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create image variation

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Images](/api/reference/resources/images)

# Create image variation

POST /images/variations

Creates a variation of a given image. This endpoint only supports `dall-e-2`.

##### Body Parameters Form Data Expand Collapse

image : file

The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20image%20%3E%20(schema))

model : optional string or [ImageModel](/api/reference/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema))

The model to use for image generation. Only `dall-e-2` is supported at this time.

One of the following:

string

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%200)

ImageModel = "gpt-image-1.5" or "dall-e-2" or "dall-e-3" or 2 more

One of the following:

"gpt-image-1.5"

[](#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)%20%3E%20(member)%200)

"dall-e-2"

[](#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)%20%3E%20(member)%201)

"dall-e-3"

[](#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)%20%3E%20(member)%202)

"gpt-image-1"

[](#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)%20%3E%20(member)%203)

"gpt-image-1-mini"

[](#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)%20%3E%20(member)%204)

[](#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema))

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema))

n : optional number

The number of images to generate. Must be between 1 and 10.

minimum 1

maximum 10

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20n%20%3E%20(schema))

response_format : optional "url" or "b64_json"

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

One of the following:

"url"

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%200)

"b64_json"

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema)%20%3E%20(member)%201)

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20response_format%20%3E%20(schema))

size : optional "256x256" or "512x512" or "1024x1024"

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

One of the following:

"256x256"

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema)%20%3E%20(member)%200)

"512x512"

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema)%20%3E%20(member)%201)

"1024x1024"

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema)%20%3E%20(member)%202)

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20size%20%3E%20(schema))

user : optional string

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).

[](#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%200%20%3E%20(param)%20user%20%3E%20(schema))

##### Returns Expand Collapse

ImagesResponse object { created , background , data , 4 more }

The response from the image generation endpoint.

created : number

The Unix timestamp (in seconds) of when the image was created.

format unixtime

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20created)

background : optional "transparent" or "opaque"

The background parameter used for the image generation. Either `transparent` or `opaque`.

One of the following:

"transparent"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20background%20%3E%20(member)%200)

"opaque"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20background%20%3E%20(member)%201)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20background)

data : optional array of [Image](/api/reference/resources/images#(resource)%20images%20%3E%20(model)%20image%20%3E%20(schema)) { b64_json , revised_prompt , url }

The list of generated images.

b64_json : optional string

The base64-encoded JSON of the generated image. Returned by default for the GPT image models, and only present if `response_format` is set to `b64_json` for `dall-e-2` and `dall-e-3`.

[](#(resource)%20images%20%3E%20(model)%20image%20%3E%20(schema)%20%3E%20(property)%20b64_json)

revised_prompt : optional string

For `dall-e-3` only, the revised prompt that was used to generate the image.

[](#(resource)%20images%20%3E%20(model)%20image%20%3E%20(schema)%20%3E%20(property)%20revised_prompt)

url : optional string

When using `dall-e-2` or `dall-e-3`, the URL of the generated image if `response_format` is set to `url` (default value). Unsupported for the GPT image models.

format uri

[](#(resource)%20images%20%3E%20(model)%20image%20%3E%20(schema)%20%3E%20(property)%20url)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20data)

output_format : optional "png" or "webp" or "jpeg"

The output format of the image generation. Either `png`, `webp`, or `jpeg`.

One of the following:

"png"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20output_format%20%3E%20(member)%200)

"webp"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20output_format%20%3E%20(member)%201)

"jpeg"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20output_format%20%3E%20(member)%202)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20output_format)

quality : optional "low" or "medium" or "high"

The quality of the image generated. Either `low`, `medium`, or `high`.

One of the following:

"low"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20quality%20%3E%20(member)%200)

"medium"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20quality%20%3E%20(member)%201)

"high"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20quality%20%3E%20(member)%202)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20quality)

size : optional "1024x1024" or "1024x1536" or "1536x1024"

The size of the image generated. Either `1024x1024`, `1024x1536`, or `1536x1024`.

One of the following:

"1024x1024"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20size%20%3E%20(member)%200)

"1024x1536"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20size%20%3E%20(member)%201)

"1536x1024"

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20size%20%3E%20(member)%202)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20size)

usage : optional object { input_tokens , input_tokens_details , output_tokens , 2 more }

For `gpt-image-1` only, the token usage information for the image generation.

input_tokens : number

The number of tokens (images and text) in the input prompt.

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_tokens)

input_tokens_details : object { image_tokens , text_tokens }

The input tokens detailed information for the image generation.

image_tokens : number

The number of image tokens in the input prompt.

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_tokens_details%20%3E%20(property)%20image_tokens)

text_tokens : number

The number of text tokens in the input prompt.

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_tokens_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20input_tokens_details)

output_tokens : number

The number of output tokens generated by the model.

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20output_tokens)

total_tokens : number

The total number of tokens (images and text) used for the image generation.

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20total_tokens)

output_tokens_details : optional object { image_tokens , text_tokens }

The output token details for the image generation.

image_tokens : number

The number of image output tokens generated by the model.

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20output_tokens_details%20%3E%20(property)%20image_tokens)

text_tokens : number

The number of text output tokens generated by the model.

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20output_tokens_details%20%3E%20(property)%20text_tokens)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage%20%3E%20(property)%20output_tokens_details)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)%20%3E%20(property)%20usage)

[](#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema))

### Create image variation

```
curl https://api.openai.com/v1/images/variations \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-F image="@otter.png" \
-F n=2 \
-F size="1024x1024"
```

```
{
"created": 1589478378,
"data": [
{
"url": "https://..."
},
{
"url": "https://..."
}
]
}
```

##### Returns Examples

```
{
"created": 1589478378,
"data": [
{
"url": "https://..."
},
{
"url": "https://..."
}
]
}
```

---
Source: https://developers.openai.com/api/reference/resources/images/methods/create_variation
