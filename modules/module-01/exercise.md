# Module 1 — Service Decomposition

**Duration**: 2h in class
**Branch to submit**: `module-01/<team-name>`

---

## Objective

Before writing a single line of code, you need to design the system on paper. Every decision you make here: where to draw service boundaries, who owns what data, how services talk to each other, is hard to reverse once you start coding.

This module is about slowing down and thinking like an architect, not a developer.

Read these two documents before doing anything else:

- `docs/domain.md` — what GameHub is and who uses it
- `docs/specs.md` — the tech stack and key architectural decisions

> The CTO has already laid out the `services/` folder structure. Use it as a starting point, but your job is to **justify** why each folder deserves to be its own service — not just accept it.

---

## Task 1 — Identify bounded contexts _(~40 min)_

A bounded context is a part of the system that has a clear responsibility and owns its data exclusively. No other service should reach into its database.

For each bounded context you identify, fill in the table:

| Bounded Context  | Responsibilities                                                  | Owned Entities             | Team         |
| ---------------- | ----------------------------------------------------------------- | -------------------------- | ------------ |
| Identity         | Manages who users are, handles registration and profiles          | User, Session              | Platform     |
| Game Library     | Maintains the game catalogue, search, and cached game summaries   | Game                       | Catalogue    |
| Activity Tracking| Records user actions against games (played, completed, etc.)      | Activity                   | Engagement   |
| Notifications    | Delivers in-app notifications to users from async events          | Notification               | Engagement   |
| Authentication   | Issues and validates JWT tokens; no user data owned here          | Token                      | Platform     |
| Compliance       | Stores GDPR consent decisions and structured activity log entries | ConsentRecord, ActivityLog | Legal        |

There is no single correct answer: what matters is that you can justify each row.

---

## Task 2 — Define service contracts _(~30 min)_

For each pair of services that need to communicate, define:

- **Direction**: A → B
- **Trigger**: what causes the call
- **Protocol**: REST or event (async)
- **Payload**: key fields exchanged

Example:

```
activity-service → logging-service
Trigger: an activity is logged
Protocol: RabbitMQ message (async — why not REST here?)
Payload: { activity_id, user_id, action, game_id, timestamp }
```

Focus on the flows that feel non-obvious. You do not need to document every possible pair.

```
activity-service → logging-service
Trigger: a user action is recorded
Protocol: RabbitMQ message (async) — logging must not block or fail the user's request
Payload: { activity_id, user_id, action, game_id, timestamp }
```

```
activity-service → notification-service
Trigger: a user action is recorded
Protocol: RabbitMQ message (async) — same event fan-out as above; notification delivery is not time-critical
Payload: { user_id, action, game_id, timestamp }
```

```
activity-service → game-service
Trigger: POST /v1/activities — need game details to enrich the response
Protocol: REST (sync, httpx) — caller needs the data immediately to return it; if game-service is down, return activity with game: null
Payload request: GET /v1/games/{game_id}
Payload response: { id, title, genre, platform, cover_url }
```

```
gateway → auth-service
Trigger: every authenticated inbound request
Protocol: REST (sync) — token must be validated before the request is forwarded
Payload: Authorization: Bearer <token> → { sub, role, exp }
```

---

## Task 3 — Draw the service map _(~20 min)_

Draw the full GameHub service map:

- One box per service
- Arrows between services (solid line = synchronous REST, dashed line = async event)
- Label each arrow with its protocol
- One box at the top labelled **gateway** — all client requests enter here, no client ever calls a service directly

This can be a sketch on paper, a whiteboard photo, or ASCII art committed to your branch.

```
                        +-------------------+
                        |      gateway      |  :8000
                        +---------+---------+
                                  |
          --------------------------------------------------------
          |              |              |              |
          v              v              v              v
  +-------------+  +-----------+  +-----------+  +-----------+
  | auth-service|  |user-service|  |game-service|<-| activity  |
  |    :8005    |  |   :8001   |  |   :8002   |  |  service  |
  +-------------+  +-----------+  | + Redis   |  |   :8003   |
                                   +-----------+  +-----+-----+
                                                        |
                                                 * * * *+* * * *
                                                 *               *
                                                 v               v
                                          +-----------+   +-----------+
                                          |notif-serv.|   |logging-svc|
                                          |   :8004   |   |   :8006   |
                                          | (Node.js) |   |  (Flask)  |
                                          +-----------+   +-----------+

Legend:
------> REST (sync)
* * *-> RabbitMQ event (async)
```

---

## Discussion _(~15 min)_

Three questions to discuss as a team before you leave:

1. Why does `notification-service` use Node.js instead of Python like the rest? What does that tell you about microservices and technology choices?
2. What is the risk of `activity-service` calling `logging-service` synchronously — why might you prefer an async event instead?
3. Why does `logging-service` need a GDPR consent check before recording any activity?

You do not need to write these answers down — they are warm-up for your REFLECTION.md.

---

## Minimum to submit this branch

- [X] Bounded context table filled in (at least 4 services justified)
- [X] At least 3 service contracts defined
- [X] Service map committed (sketch, photo, or ASCII)
- [X] `REFLECTION.md` completed and committed

The map does not need to be perfect. It needs to be yours.
