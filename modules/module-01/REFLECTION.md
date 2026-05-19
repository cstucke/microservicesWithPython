## YOU NEED TO COMMIT THIS FILE BEFORE MOVING ON TO THE NEXT MODULE ! 🚨

**feel free to delete this comment**

# Module 1 — Reflection

**Team name**: **\*\***\_\_\_**\*\***
**Branch**: `module-01/<team-name>`
**Submitted**: before Module 2 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You started from a painful monolith. Now you're splitting it into separate services.

**What concrete problem does that split solve: and for whom?**

Think about it from three angles: the developer who has to change code, the team that has to deploy it, and the user who has to live with its failures. You don't need to cover all three, pick the one that felt most real to you today.

```
In a monolithic architecture, everything is built in one application / development space. So, for instance, if a bug in notifications were to happen, the entire application would crash. By splitting the services, we can reduce the exposure (surface area) for failure. It also allows you to develop each part separately, without concern for the other parts: Separation of Duties.
```

---

## 2. Your choice

Look at your service map. Every arrow between two services is a decision someone made.

**Pick one boundary, one place where you decided service A should not be part of service B. Explain why that line exists.**

What would break, slow down, or become harder to manage if you merged those two services back together?

```
The activity service sends async events to both the notification and logging services. This is because the current activity and logs must be updated with every activity. Likewise, the activity service makes a call to the game service. This is where one boundary exists: the games must remain its own source of truth, unalterable by the other services. For this reason, I've separated and made a distinct REST API for the game service.
```

---

## 3. The tradeoff

Microservices solve the monolith's problems. But they create new ones.

**Name one thing that was simpler in the monolith and is now harder in your distributed design.**

No need to solve it: just name it honestly. This is exactly the tension the rest of the course is about.

```
One of the biggest issues that I've noticed when working with monolithic vs distributed designs in the past is that following an error is much harder. This is because the failure isn't from one central fault, you have to track it through several different layers.
```

---

_Keep this file. You will refer back to it during the oral presentation._
