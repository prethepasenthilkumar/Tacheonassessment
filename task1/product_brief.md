# Task 1: Product Brief — Work in Progress
# Marketing Performance Tool — Product Brief

## The Problem

Right now when someone asks "how is our marketing doing?" a team 
member has to manually open Google Ads, Meta Ads, pull numbers 
from each tool, and stitch together an answer. It takes too long, 
looks different every time, and if that person is away the question 
just sits there unanswered.

## What I Want to Build

A simple internal tool where anyone on the team can pick a client, 
pick a date range, and instantly see how each marketing channel is 
performing — with a short plain-English summary of what is working 
and what is not. Nothing fancy. Just one place that answers the 
question reliably.

## Who Is It For

The internal team first. Not the client yet. The team needs to use 
it, trust it, and verify the numbers before we ever put it in front 
of a client. Client-facing views come in v2.

## What a Good Session Looks Like

Someone opens the tool, picks a brand and a date range. Within 
30 seconds they see spend, clicks, and conversions per channel, 
which channel is doing best, and a short summary like "Paid search 
is driving most conversions right now. Social spend went up but 
results did not — worth a look." They also see when the data was 
last updated. They close the tool knowing what to tell the client 
without opening anything else.

## Where the Data Comes From

The platforms the team already uses. Nothing changes about how 
they work today.

- Google Ads → Google Ads API
- Meta Ads → Meta Ads API

A Python script pulls from both APIs every day, cleans the data, 
and loads it into BigQuery. The dashboard reads from BigQuery.
## What Is In V1

- Google Ads and Meta Ads connected
- Daily data load into BigQuery
- Simple dashboard — pick brand, pick dates, see metrics by channel
- AI-generated plain-English performance summary
- Last refreshed timestamp on all data

## What Is NOT In V1 and Why

| Leaving Out | Reason |
|---|---|
| Client-facing view | Trust needs to be built internally first |
| Email and organic | Simpler to start with paid channels only |
| Alerts and notifications | Not needed to answer the core question |
| Mobile view | Internal tool, desktop is enough |
| More than 90 days history | Current performance is what gets asked about |

I would rather ship something small that works than something big 
that nobody trusts.

## What Would Make People Trust It

Show the last updated time on every number. If an API fails to 
sync, show a clear warning — never show stale data silently. For 
the first two weeks manually check the tool output against the 
actual platforms to confirm everything matches.

## What I Would Add With More Time

Slack alerts when something spikes unexpectedly. Email and organic 
channels once the core pipeline is stable. A read-only client view 
once the internal team is confident in the data quality.

---
*Prethepa Senthilkumar — Tacheon Assessment Submission*
