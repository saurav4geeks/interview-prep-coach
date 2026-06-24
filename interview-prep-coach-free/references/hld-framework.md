# HLD Session Framework

## The 6-Step Structure (Use Every Time)

Every HLD answer should follow this sequence. Claude will guide you through each step in a session.

---

### Step 1: Clarify Requirements (2–3 min)
Ask about:
- **Functional:** What core features? (read-heavy vs write-heavy? real-time?)
- **Non-functional:** Scale (DAU, QPS), latency SLA, availability target, consistency needs
- **Out of scope:** What you're NOT designing

**Output:** 3–5 bullet requirements you'll design to.

---

### Step 2: Capacity Estimation (2–3 min)
Back-of-envelope:
- **Users:** DAU → requests/day → QPS (peak = avg × 3–5)
- **Storage:** data size per record × records/day × retention period
- **Bandwidth:** data transferred per request × QPS

**Key numbers to memorize:**
- 1 million req/day ≈ 12 req/sec
- 1 billion req/day ≈ 12,000 req/sec
- 1 char = 1 byte; 1 image ≈ 300KB; 1 video/min ≈ 50MB

---

### Step 3: High-Level Design (5–7 min)
Draw the core components:
```
Client → Load Balancer → API Gateway → Services → DB/Cache
```

Typical components to know:
- **API Gateway:** auth, rate limiting, routing
- **Load Balancer:** round-robin, least connections, consistent hashing
- **CDN:** static assets, geographically distributed
- **Message Queue (Kafka/RabbitMQ):** async processing, decoupling
- **Cache (Redis):** read-heavy data, session storage
- **DB:** SQL for ACID, NoSQL for scale/flexibility

---

### Step 4: Data Model & API Design (3–5 min)
- Key entities and their schema
- Primary keys, indexes, foreign keys
- Main API endpoints (REST or describe at high level)

---

### Step 5: Deep Dive on 1–2 Components (10 min)
Interviewer picks or you pick the hardest part. Common deep dives:
- **Database sharding:** range-based vs hash-based; hotspot problem
- **Caching strategy:** cache-aside vs write-through vs write-behind; cache invalidation
- **Consistency:** strong vs eventual; leader-follower replication
- **Search:** inverted index, Elasticsearch
- **Feed generation:** fanout on write (push) vs fanout on read (pull) vs hybrid

---

### Step 6: Address Bottlenecks & Tradeoffs (3–5 min)
- What breaks first at scale?
- What tradeoffs did you make and why? (CAP theorem angle)
- Single points of failure → how to handle?

---

## Key Concepts to Know Cold

### CAP Theorem
You can only guarantee 2 of: **Consistency, Availability, Partition Tolerance**.
- CP: ZooKeeper, HBase
- AP: Cassandra, CouchDB, DynamoDB

### Consistent Hashing
Distribute keys across nodes such that adding/removing a node only remaps K/N keys. Used in: distributed caches, CDNs, load balancers.

### Database Choices
| Use Case | Choose |
|----------|--------|
| ACID transactions, complex queries | PostgreSQL / MySQL |
| Massive scale, flexible schema | Cassandra / DynamoDB |
| Graph relationships | Neo4j |
| Full-text search | Elasticsearch |
| Time-series data | InfluxDB |
| Caching / leaderboards | Redis |

### Message Queue (Kafka)
- **Topic → Partitions → Consumer Groups**
- Kafka retains messages (consumers control offset) vs RabbitMQ deletes on ack
- Use Kafka for: event streaming, audit logs, fan-out, decoupling services

### SQL vs NoSQL Sharding
- **Vertical scaling:** bigger machine (limited)
- **Horizontal scaling / sharding:** split data across machines
- **Shard key choice matters:** avoid hotspots (e.g., don't shard by timestamp)

### Rate Limiting Algorithms
| Algorithm | Pros | Cons |
|-----------|------|------|
| Token Bucket | Allows bursts | State per user |
| Leaky Bucket | Smooth output | Bursts get dropped |
| Fixed Window | Simple | Boundary burst problem |
| Sliding Window Log | Accurate | Memory heavy |
| Sliding Window Counter | Good balance | Approximate |

---

## HLD Problems — What to Know for Each

### URL Shortener
- Hash function (MD5 → take 6 chars), collision handling
- 301 vs 302 redirect (caching implications)
- Analytics: click count, async via Kafka

### Rate Limiter
- Where to put it (API Gateway or per service)
- Redis for distributed counter
- Algorithm choice: sliding window counter for most cases

### Notification System
- Push (FCM/APNs) vs Email vs SMS — separate workers
- Fan-out: who gets notified? Kafka topic per user group
- Idempotency: don't double-notify

### Chat System (WhatsApp)
- WebSocket for real-time bidirectional
- Message storage: Cassandra (append-heavy, time-series)
- Online presence: heartbeat + Redis TTL
- Group chat: fanout at message level vs at read time

### Twitter Feed
- Fanout on write: pre-compute feeds for followers (good for read-heavy, bad for celebrities)
- Fanout on read: compute on request (stale but no write amplification)
- Hybrid: fanout on write for normal users, pull for high-follower accounts

### Search Autocomplete
- Trie for prefix matching
- Cache top-k suggestions per prefix
- Ranking: frequency × recency decay
- CDN for static/common prefixes
