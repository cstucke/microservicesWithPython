# Module 4 — Reflection

**Team name**: _______________
**Branch**: `module-04/<team-name>`
**Submitted**: before Module 5 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

In Module 3, services called each other directly over HTTP. Now activity-service drops a message into a broker and moves on — it never waits for a reply.

**What does the activity-service gain by not waiting? And what does the notification-service gain by consuming at its own pace?**

Think about what happens under load, or when notification-service is temporarily down.

> Due to the fact that activity-service no longer waits for notification-service to respond, activity service can finish its tasks quicker. The practical point of this is that we are decoupling these two activities: now, if a large number of activities are logged, activity service will not have to wait for notification service and can process them on its own. By creating a queue for the activities, even if notification service becomes temporarily unavailable, it will be able to start at the same spot and have access to the unfinished jobs through the queue. It's good for both services!

---

## 2. Your choice

In Module 3 you already knew how to call another service directly over HTTP — you did it for user validation and game enrichment.

**Why not use the same approach for notifications? What does introducing a broker give you that a direct HTTP call doesn't?**

Think about what happens if notification-service is slow, or crashes mid-message.

> I guess I inadvertedly answered this in the previous question: by implementing a broker, even if notification service goes completely down, the activity linked to the notification is still saved in queue and, when the service becomes available again, the notification service can process the activity. If we were using the same approach (HTTP that is) for notifications, the activity request would fail if the notification service isn't available.

---

## 3. The tradeoff

With synchronous REST, you get an immediate answer: success or failure. With async messaging, the activity is saved and the message is sent — but you have no idea if the notification was ever delivered.

**How would a user know if their notification was never sent? How would you know as a developer?**

What visibility do you lose when you go async?

> The user doesn't have access to the async messaging system, so the user would not be able to see anything about the notification. As a developer, the method that you can use to check if the notification was never sent is exactly what we did in the exercises: go to rabbitmq and check the queue.

---

*Keep this file. You will refer back to it during the oral presentation.*
