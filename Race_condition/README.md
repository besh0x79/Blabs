## What is a Race Condition?

A race condition occurs when two or more operations execute at the same time, competing to access or modify the same resource.

The final outcome depends on **which operation finishes first** — making the behavior unpredictable.

### Simple Analogy

Imagine two users trying to book the **last available seat** at the exact same moment:

- Both users check → *"Seat is available"*
- Both proceed to book
- System processes both requests simultaneously

Without proper synchronization, **both bookings may succeed**, even though only one seat exists.

### Why It Happens

Race conditions usually occur when:
- Multiple requests are handled concurrently
- Shared data is accessed without proper locking
- Validation and execution are not atomic (not done as a single step)

### In Web Applications

A common vulnerable flow:

1. Check if a resource is available  
2. Perform an action based on that check  

If an attacker sends many requests at once, they may:
- Bypass the check
- Execute the action multiple times before the system updates its state

### Key Idea

> The system assumes operations happen in order —  
> but in reality, they can overlap.

### Why It Matters

Race conditions can lead to:
- Bypassing security checks
- Duplicate actions (e.g., multiple purchases)
- Unauthorized access to sensitive data
