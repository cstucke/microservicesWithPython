# Module 5 — Reflection

**Team name**: _______________
**Branch**: `module-05/<team-name>`
**Submitted**: before Module 6 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The game-service now has two models for the same data: SQLite for writes, Redis for reads. They store the same games in two different shapes.

**Why go through the trouble of maintaining two representations of the same data?**

Think about what kind of queries each model is optimised for, and what would happen if you tried to use the write model for high-traffic read operations.

```text
> Among several reasons, we chose to maintain two representations of the same data (in both SQLite and Redis) for the purpose of speeding up transactions. If everything is to go through one representation of the data (one database, that is to say), a large number of reads  and writes at the same time, the transactions would become very slow and cause too much latency for the optimal operations of our server. Ultimately, we still have one source of truth: SQLite, and this is how we can maintain data integrity.
```

---

## 2. Your choice

The logging-service checks GDPR consent before recording any activity. If a user has not opted in, the log is silently dropped.

**What does this consent check force you to accept about your data?** It is incomplete by design — some activities will never be recorded.

From a system design perspective: where is the right place to enforce this rule — in the logging-service, in the activity-service, or at the gateway? Why?

```text
> This consent check means that data will not always be of the same structure: some data will have all of the fields, while other will be 'incomplete'. This adds another layer of complexity to the structure of the application. The gateway and activity services are not the correct place to enforce this rule, they already have distinct purposes that are not directly related to relating logs to an individual. On the other hand, the logging-service is responsible for maintaining (i feel like there are too many i's in that word) the logs and owns the consent records.
```

---

## 3. The tradeoff

With CQRS, your write model and read model can drift out of sync — a game is updated in SQLite but the Redis projection still shows the old data.

**In what scenario does this inconsistency matter to the user? In what scenario is it completely acceptable?**

Is there a class of applications where eventual consistency is never acceptable? What are they?

```text
> From the user's POV, the consistency of the data matters whenever they want to view/use it. If the data isn't being actually accessed or used in some ulterior facet, it won't directly matter to the user. There are several applications where inconsistency isn't allowed, and those are primarily ones where finance is related: for instance, a stock ticker or banking application.
```

---

*Keep this file. You will refer back to it during the oral presentation.*