# Introduction

## Purpose

- Design an Intelligent Virtual Assistant (IVA) to guide users through a series of simple questions to determine what’s needed for an individualized, flexible experience and then respond with personalized information and proactive services. 
- The IVA will be accessible on all channels: the company website, existing mobile app, and third-party platforms such as Amazon Alexa or Google Assistant. 

## Project Scope

- Shall be an intelligent virtual assistance, which has abilities to drive meaningful One on One conversations, carry out business transactions and solve customer problems. 
	- Shall be able to learn from its conversations about the individual customer, and overall as conversational AI. 
	- Shall work with fulfilment layer and carry out business transactions.
	- Shall showcase learning from past conversations and following the user journey across touch points: If user starts interacting on mobile app and then carries the conversation on Alexa, user should not repeat itself.
- Shall apply a ML algorithm to identify and learn new details about the user – likes and dislikes, history of interacting with the brand, social profile. 
- Shall be channel-agonistic and should be able to integrate with any device/channel (e.g. Mobile App, Website, Alexa) with minimum effort.


# Product Description

## Perspective

- Shall connect to existing functionality, such as completing business transactions and utilizing interaction history between the user and the brand. 
- Shall introduce new functionality, including ML of user interests to suggest new experiences for the user and seamless integration on multiple channels.

## Features

### 1. Conversations with Virtual Assistant 

- User will be able to create a new account/guest. 
- User will be able ask VA questions about the weather, nearby restaurants, and order transportation. 
- The VA will “remember” user preferences via access to an account database/file store.

### 2. Using Keywords from Yelp Client-Facing API

- System will take keywords from the Yelp pages of companies the user has visited and from companies in their current location.

### 3. Machine-Learning Algorithm

- System will compare the visited and non-visited keywords to determine recommendations.


## Non-Functional Requirements

- Accessibility: Shall be channel-agnostic with both voice and visual access, allowing all kinds of users to access the system equally. 
- Disaster recovery: Shall match existing recovery plan for hotel systems/website.
- Effectiveness: Shall give the most relevant suggestions for the user.
- Interoperability: Shall work consistently and identically, regardless of platform (e.g. same performance on Siri and Amazon Alexa).
- Maintainability: Shall be stored alongside the hotel system/website code, and updated by the same team members, including development, dev-ops, and IT.
- Privacy: Shall protect user information, only allowing the user to access their own account and data.
- Reliability: Shall be available 24/7 with minimal downtime during updates.
- Robustness 
- Scalability 
- Testability


# User Experience

- User: Customer of the brand 
- Frequency of use: Varied, may be most often before/during certain events such as:
	- Family vacations
	- Business trips
	- High school students viewing colleges
- Security or Privilege Levels: Only access personal account information 
- Educational Level or Experience: Must be comfortable using existing platforms and services, including the following: 
	- Navigating the internet
	- Downloading and navigating a mobile app
	- Setting up and using Virtual Assistants such as Amazon Alexa
	- Creating an account and adding personal information

## Operating a Virtual Assistant 
For testing purposes, the team used an Amazon Alexa.

### 1. {insert interaction}
- {interaction details}

### 2. {insert interaction}
- {interaction details}

### 3. {insert interaction}
- {interaction details}


# References

Industry Challenge – Travel & Hospitality – Project Description https://lion.app.box.com/s/zcbkyk8vppmlmq8o223a43ub28grtqvu/file/469652883053?sb=/details 

Requirements Document Template http://www.se.rit.edu/~emad/teaching/slides/srs_template_sep14.pdf

Yelp Fusion API https://github.com/Yelp/yelp-fusion/blob/master/fusion/python/sample.py
