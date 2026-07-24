---
source_url: https://developers.openai.com/api/reference/resources/moderations/methods/create
title: "Create moderation"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Create moderation

> OpenAI API endpoint method reference.
[API Reference](/api/reference)

[Moderations](/api/reference/resources/moderations)

# Create moderation

POST /moderations

Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](/docs/guides/moderation).

##### Body Parameters JSON Expand Collapse

input : string or array of string or array of object { image_url , type } or object { text , type }

Input (or inputs) to classify. Can be a single string, an array of strings, or
an array of multi-modal input objects similar to other models.

One of the following:

string

A string of text to classify for moderation.

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%200)

array of string

An array of strings to classify for moderation.

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%201)

array of object { image_url , type } or object { text , type }

An array of multi-modal inputs to the moderation model.

One of the following:

object { image_url , type }

An object describing an image to classify.

image_url : object { url }

Contains either an image URL or a data URL for a base64 encoded image.

url : string

Either a URL of the image or the base64 encoded image data.

format uri

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20image_url%20%3E%20(property)%20url)

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20image_url)

type : "image_url"

Always `image_url`.

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type)

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(items)%20%3E%20(variant)%200)

object { text , type }

An object describing text to classify.

text : string

A string of text to classify.

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20text)

type : "text"

Always `text`.

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type)

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(items)%20%3E%20(variant)%201)

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema)%20%3E%20(variant)%202)

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20input%20%3E%20(schema))

model : optional string or [ModerationModel](/api/reference/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema))

The content moderation model you would like to use. Learn more in
[the moderation guide](/docs/guides/moderation), and learn about
available models [here](/docs/models#moderation).

One of the following:

string

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema)%20%3E%20(variant)%200)

ModerationModel = "omni-moderation-latest" or "omni-moderation-2024-09-26" or "text-moderation-latest" or "text-moderation-stable"

One of the following:

"omni-moderation-latest"

[](#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)%20%3E%20(member)%200)

"omni-moderation-2024-09-26"

[](#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)%20%3E%20(member)%201)

"text-moderation-latest"

[](#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)%20%3E%20(member)%202)

"text-moderation-stable"

[](#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)%20%3E%20(member)%203)

[](#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema))

[](#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20model%20%3E%20(schema))

##### Returns Expand Collapse

id : string

The unique identifier for the moderation request.

[](#(resource)%20moderations%20%3E%20(model)%20moderation_create_response%20%3E%20(schema)%20%3E%20(property)%20id)

model : string

The model used to generate the moderation results.

[](#(resource)%20moderations%20%3E%20(model)%20moderation_create_response%20%3E%20(schema)%20%3E%20(property)%20model)

results : array of [Moderation](/api/reference/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)) { categories , category_applied_input_types , category_scores , flagged }

A list of moderation objects.

categories : object { harassment , "harassment/threatening" , hate , 10 more }

A list of the categories, and whether they are flagged or not.

harassment : boolean

Content that expresses, incites, or promotes harassing language towards any target.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20harassment)

"harassment/threatening" : boolean

Harassment content that also includes violence or serious harm towards any target.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20harassment%2Fthreatening)

hate : boolean

Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20hate)

"hate/threatening" : boolean

Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20hate%2Fthreatening)

illicit : boolean

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, “how to shoplift” would fit this category.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20illicit)

"illicit/violent" : boolean

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20illicit%2Fviolent)

"self-harm" : boolean

Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20self-harm)

"self-harm/instructions" : boolean

Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20self-harm%2Finstructions)

"self-harm/intent" : boolean

Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20self-harm%2Fintent)

sexual : boolean

Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20sexual)

"sexual/minors" : boolean

Sexual content that includes an individual who is under 18 years old.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20sexual%2Fminors)

violence : boolean

Content that depicts death, violence, or physical injury.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20violence)

"violence/graphic" : boolean

Content that depicts death, violence, or physical injury in graphic detail.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(property)%20violence%2Fgraphic)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20categories)

category_applied_input_types : object { harassment , "harassment/threatening" , hate , 10 more }

A list of the categories along with the input type(s) that the score applies to.

harassment : array of "text"

The applied input type(s) for the category ‘harassment’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20harassment)

"harassment/threatening" : array of "text"

The applied input type(s) for the category ‘harassment/threatening’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20harassment%2Fthreatening)

hate : array of "text"

The applied input type(s) for the category ‘hate’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20hate)

"hate/threatening" : array of "text"

The applied input type(s) for the category ‘hate/threatening’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20hate%2Fthreatening)

illicit : array of "text"

The applied input type(s) for the category ‘illicit’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20illicit)

"illicit/violent" : array of "text"

The applied input type(s) for the category ‘illicit/violent’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20illicit%2Fviolent)

"self-harm" : array of "text" or "image"

The applied input type(s) for the category ‘self-harm’.

One of the following:

"text"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm)

"self-harm/instructions" : array of "text" or "image"

The applied input type(s) for the category ‘self-harm/instructions’.

One of the following:

"text"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%2Finstructions%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%2Finstructions%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%2Finstructions)

"self-harm/intent" : array of "text" or "image"

The applied input type(s) for the category ‘self-harm/intent’.

One of the following:

"text"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%2Fintent%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%2Fintent%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20self-harm%2Fintent)

sexual : array of "text" or "image"

The applied input type(s) for the category ‘sexual’.

One of the following:

"text"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20sexual%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20sexual%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20sexual)

"sexual/minors" : array of "text"

The applied input type(s) for the category ‘sexual/minors’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20sexual%2Fminors)

violence : array of "text" or "image"

The applied input type(s) for the category ‘violence’.

One of the following:

"text"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20violence%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20violence%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20violence)

"violence/graphic" : array of "text" or "image"

The applied input type(s) for the category ‘violence/graphic’.

One of the following:

"text"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20violence%2Fgraphic%20%3E%20(items)%20%3E%20(member)%200)

"image"

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20violence%2Fgraphic%20%3E%20(items)%20%3E%20(member)%201)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types%20%3E%20(property)%20violence%2Fgraphic)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_applied_input_types)

category_scores : object { harassment , "harassment/threatening" , hate , 10 more }

A list of the categories along with their scores as predicted by model.

harassment : number

The score for the category ‘harassment’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20harassment)

"harassment/threatening" : number

The score for the category ‘harassment/threatening’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20harassment%2Fthreatening)

hate : number

The score for the category ‘hate’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20hate)

"hate/threatening" : number

The score for the category ‘hate/threatening’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20hate%2Fthreatening)

illicit : number

The score for the category ‘illicit’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20illicit)

"illicit/violent" : number

The score for the category ‘illicit/violent’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20illicit%2Fviolent)

"self-harm" : number

The score for the category ‘self-harm’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20self-harm)

"self-harm/instructions" : number

The score for the category ‘self-harm/instructions’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20self-harm%2Finstructions)

"self-harm/intent" : number

The score for the category ‘self-harm/intent’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20self-harm%2Fintent)

sexual : number

The score for the category ‘sexual’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20sexual)

"sexual/minors" : number

The score for the category ‘sexual/minors’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20sexual%2Fminors)

violence : number

The score for the category ‘violence’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20violence)

"violence/graphic" : number

The score for the category ‘violence/graphic’.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores%20%3E%20(property)%20violence%2Fgraphic)

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20category_scores)

flagged : boolean

Whether any of the below categories are flagged.

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)%20%3E%20(property)%20flagged)

[](#(resource)%20moderations%20%3E%20(model)%20moderation_create_response%20%3E%20(schema)%20%3E%20(property)%20results)

Single string Image and text

### Create moderation

```
curl https://api.openai.com/v1/moderations \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
"input": "I want to kill them."
}'
```

```
{
"id": "modr-AB8CjOTu2jiq12hp1AQPfeqFWaORR",
"model": "text-moderation-007",
"results": [
{
"flagged": true,
"categories": {
"sexual": false,
"hate": false,
"harassment": true,
"self-harm": false,
"sexual/minors": false,
"hate/threatening": false,
"violence/graphic": false,
"self-harm/intent": false,
"self-harm/instructions": false,
"harassment/threatening": true,
"violence": true
},
"category_scores": {
"sexual": 0.000011726012417057063,
"hate": 0.22706663608551025,
"harassment": 0.5215635299682617,
"self-harm": 2.227119921371923e-6,
"sexual/minors": 7.107352217872176e-8,
"hate/threatening": 0.023547329008579254,
"violence/graphic": 0.00003391829886822961,
"self-harm/intent": 1.646940972932498e-6,
"self-harm/instructions": 1.1198755256458526e-9,
"harassment/threatening": 0.5694745779037476,
"violence": 0.9971134662628174
}
}
]
}
```

### Create moderation

```
curl https://api.openai.com/v1/moderations \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
"model": "omni-moderation-latest",
"input": [
{ "type": "text", "text": "...text to classify goes here..." },
{
"type": "image_url",
"image_url": {
"url": "https://example.com/image.png"
}
}
]
}'
```

```
{
"id": "modr-0d9740456c391e43c445bf0f010940c7",
"model": "omni-moderation-latest",
"results": [
{
"flagged": true,
"categories": {
"harassment": true,
"harassment/threatening": true,
"sexual": false,
"hate": false,
"hate/threatening": false,
"illicit": false,
"illicit/violent": false,
"self-harm/intent": false,
"self-harm/instructions": false,
"self-harm": false,
"sexual/minors": false,
"violence": true,
"violence/graphic": true
},
"category_scores": {
"harassment": 0.8189693396524255,
"harassment/threatening": 0.804985420696006,
"sexual": 1.573112165348997e-6,
"hate": 0.007562942636942845,
"hate/threatening": 0.004208854591835476,
"illicit": 0.030535955153511665,
"illicit/violent": 0.008925306722380033,
"self-harm/intent": 0.00023023930975076432,
"self-harm/instructions": 0.0002293869201073356,
"self-harm": 0.012598046106750154,
"sexual/minors": 2.212566909570261e-8,
"violence": 0.9999992735124786,
"violence/graphic": 0.843064871157054
},
"category_applied_input_types": {
"harassment": [
"text"
],
"harassment/threatening": [
"text"
],
"sexual": [
"text",
"image"
],
"hate": [
"text"
],
"hate/threatening": [
"text"
],
"illicit": [
"text"
],
"illicit/violent": [
"text"
],
"self-harm/intent": [
"text",
"image"
],
"self-harm/instructions": [
"text",
"image"
],
"self-harm": [
"text",
"image"
],
"sexual/minors": [
"text"
],
"violence": [
"text",
"image"
],
"violence/graphic": [
"text",
"image"
]
}
}
]
}
```

##### Returns Examples

```
{
"id": "id",
"model": "model",
"results": [
{
"categories": {
"harassment": true,
"harassment/threatening": true,
"hate": true,
"hate/threatening": true,
"illicit": true,
"illicit/violent": true,
"self-harm": true,
"self-harm/instructions": true,
"self-harm/intent": true,
"sexual": true,
"sexual/minors": true,
"violence": true,
"violence/graphic": true
},
"category_applied_input_types": {
"harassment": [
"text"
],
"harassment/threatening": [
"text"
],
"hate": [
"text"
],
"hate/threatening": [
"text"
],
"illicit": [
"text"
],
"illicit/violent": [
"text"
],
"self-harm": [
"text"
],
"self-harm/instructions": [
"text"
],
"self-harm/intent": [
"text"
],
"sexual": [
"text"
],
"sexual/minors": [
"text"
],
"violence": [
"text"
],
"violence/graphic": [
"text"
]
},
"category_scores": {
"harassment": 0,
"harassment/threatening": 0,
"hate": 0,
"hate/threatening": 0,
"illicit": 0,
"illicit/violent": 0,
"self-harm": 0,
"self-harm/instructions": 0,
"self-harm/intent": 0,
"sexual": 0,
"sexual/minors": 0,
"violence": 0,
"violence/graphic": 0
},
"flagged": true
}
]
}
```

---
Source: https://developers.openai.com/api/reference/resources/moderations/methods/create
