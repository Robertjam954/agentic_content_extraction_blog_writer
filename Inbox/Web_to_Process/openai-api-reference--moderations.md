---
source_url: https://developers.openai.com/api/reference/resources/moderations
title: "Moderations"
scraped: 2026-07-24
type: doc
source: openai-api-reference
full_text: true
---

# Moderations

> OpenAI API endpoint reference.
[API Reference](/api/reference)

# Moderations

Given text and/or image inputs, classifies if those inputs are potentially harmful.

##### [Create moderation](/api/reference/resources/moderations/methods/create)

POST /moderations

##### Models Expand Collapse

Moderation object { categories , category_applied_input_types , category_scores , flagged }

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

[](#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema))

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

ModerationCreateResponse object { id , model , results }

Represents if a given text input is potentially harmful.

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

[](#(resource)%20moderations%20%3E%20(model)%20moderation_create_response%20%3E%20(schema))

---
Source: https://developers.openai.com/api/reference/resources/moderations
