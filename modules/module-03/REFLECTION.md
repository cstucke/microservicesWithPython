# Module 3 — Reflection

**Team name**: _______________
**Branch**: `module-03/<team-name>`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:*

The single entry point serves a massive role for all audiences, not just the client's QoL (like my use of industry lingo? ;P). It abstracts the confusing architecture of the interworkings of the microservices into one central place. If the client needed to know and manage everything itself, it would be impossible. Creating an abstraction layer like the gateway is also great for scaling: we already have the system set up, adding another microservice will be easier than managing it in some decentralized manner (albeit, i guess it never gets extremely easy adding a feature like that).

---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:*

Validating the user and fetching game data are two very different tasks. If we, for instance, tried to save data for a user that doesn't exist through the activity service, that would create a big issue in our data integrity (smth we learned the value of in GDPR). However, in the case of some external error/factor, we allow a retry. For the game data fetch, failing silently is completely reasonable. This is not critical for our data integrity, or any other functionality's integrity., so we can fail gracefully (as you put it).

---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:*

Synchronizing (? on spelling) the calls is good for the purpose of simplifying and centralizing our activities. However, it does carry one major risk: to access any of these calls, we must wait for all of the calls to be complete. Like in your example, if the slowest service in the chain takes 3 seconds to respond, then all of the other calls chained to it will also suffer from that additional 3 second delay.

---

*Keep this file. You will refer back to it during the oral presentation.*
