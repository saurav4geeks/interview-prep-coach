# Low-Level Design (LLD) Framework + Problem Notes

Load this file for all LLD sessions. LLD tests object-oriented design skill — you're designing classes, interfaces, and relationships for a real system, not distributed infrastructure.

---

## The LLD Framework (Use Every Time)

Every LLD answer follows this 6-step sequence. Time allocation for a 45-min session shown below.

---

### Step 1: Clarify Requirements (5 min)

Ask and nail down:
- **Functional requirements** — what must the system do? (list 4–6 core features)
- **Non-functional requirements** — scale? concurrency? persistence needed?
- **Out of scope** — what are you NOT designing? (distributed infra, APIs, UI)

Output: 4–6 bullet requirements you'll design to.

---

### Step 2: Identify Core Entities (5 min)

List the nouns in the problem — these become your classes:
- What are the real-world objects? (Car, Slot, Ticket, User, Booking...)
- What are the relationships? (has-a, is-a, uses)
- What are the enums/value types? (SlotType, BookingStatus, PaymentState...)

Draw a quick entity list before touching class design.

---

### Step 3: Define Class Interfaces + Relationships (10 min)

For each entity, define:
```
class Foo {
  // fields (data it owns)
  // methods (behavior it exposes)
}
```

Key decisions to call out explicitly:
- **Inheritance vs composition** — prefer composition; inherit only for true is-a
- **Interface vs abstract class** — interface when multiple unrelated classes share a contract; abstract when sharing implementation
- **Who owns what** — which class holds the reference to which
- **Encapsulation** — what's private vs public; avoid exposing internal state

---

### Step 4: Apply Design Patterns (10 min)

Pick the patterns that fit naturally — don't force them:

| Pattern | Use when |
|---------|----------|
| **Singleton** | One instance needed globally (Logger, Config, DBConnection) |
| **Factory / Abstract Factory** | Object creation logic varies by type (VehicleFactory → Car/Bike/Truck) |
| **Strategy** | Algorithm varies independently from the class that uses it (PricingStrategy, SortStrategy) |
| **Observer** | One-to-many event propagation (BookingSystem notifies EmailService, SMSService) |
| **Decorator** | Add behavior without modifying the class (CoffeeWithMilk extends Coffee) |
| **Command** | Encapsulate a request as an object — supports undo/queue (ElevatorRequest) |
| **State** | Object behavior changes based on internal state (VendingMachine states: Idle, HasMoney, Dispensing) |
| **Template Method** | Define skeleton of algorithm, subclasses fill in steps |
| **Repository** | Abstract data access (UserRepository hides DB queries) |

For each pattern used: name it, say WHY you chose it, show the class structure.

---

### Step 5: Handle Concurrency + Edge Cases (10 min)

Almost every LLD question has concurrency:
- **Race conditions** — two users booking the same slot simultaneously
- **Synchronization** — which methods need `synchronized`/locks? At what granularity?
- **Deadlock** — if multiple locks, always acquire in the same order
- **Atomic operations** — use `AtomicInteger`, `ConcurrentHashMap` where appropriate

Edge cases to always call out:
- What happens at capacity? (parking full, show sold out)
- What happens when a request fails mid-flow? (payment fails after seat reserved → rollback)
- Null / invalid inputs
- Duplicate requests (idempotency)

---

### Step 6: Walk Through a Flow (5 min)

Pick the most important use case and trace it end-to-end through your classes:

> "User calls `ParkingLot.park(vehicle)` → `findAvailableSlot(vehicleType)` → `Slot.assign(vehicle)` → `Ticket.create(slot, entryTime)` → return ticket"

This proves the design works. It's also where interviewers spot missing methods or wrong ownership.

---

## SOLID Principles — Know Cold

| Principle | One-line | Common violation |
|-----------|----------|-----------------|
| **S**ingle Responsibility | One class, one reason to change | `OrderService` that also sends emails |
| **O**pen/Closed | Open for extension, closed for modification | `if type == "visa" ... elif type == "mastercard"` instead of `PaymentStrategy` |
| **L**iskov Substitution | Subclass must be usable wherever parent is | `Square extends Rectangle` breaks when width ≠ height |
| **I**nterface Segregation | Don't force classes to implement unused methods | Fat interface with 10 methods when 3 are needed |
| **D**ependency Inversion | Depend on abstractions, not concretions | `OrderService` instantiates `MySQLDB` directly |

---

## LLD Problem Notes

### Parking Lot

**Requirements:** Multi-level lot, multiple vehicle types (bike/car/truck), find nearest available slot, issue ticket, compute fee on exit.

**Core entities:** `ParkingLot`, `Level`, `ParkingSlot`, `Vehicle` (+ subclasses `Bike`, `Car`, `Truck`), `Ticket`, `PricingStrategy`

**Key design decisions:**
- `ParkingSlot` has a `SlotType` enum (COMPACT, LARGE, MOTORBIKE) and `Vehicle` reference (null if empty)
- `ParkingLot` is a **Singleton** — one instance manages all levels
- `findAvailableSlot(VehicleType)` iterates levels top-to-bottom, returns first matching free slot
- **Strategy pattern** for pricing: `HourlyPricing`, `FlatRatePricing`, `WeekendPricing` all implement `PricingStrategy`
- **Concurrency:** `synchronized` on `ParkingSlot.assign()` and `release()` to prevent double-booking

**Class skeleton:**
```java
enum VehicleType { BIKE, CAR, TRUCK }
enum SlotType { MOTORBIKE, COMPACT, LARGE }

class Vehicle { String licensePlate; VehicleType type; }
class ParkingSlot { SlotType type; Vehicle vehicle; boolean isAvailable(); void assign(Vehicle v); void release(); }
class Level { int floor; List<ParkingSlot> slots; Optional<ParkingSlot> findSlot(VehicleType); }
class Ticket { String id; Vehicle vehicle; ParkingSlot slot; LocalDateTime entryTime; }
class ParkingLot { // Singleton
  List<Level> levels;
  PricingStrategy pricing;
  Ticket park(Vehicle v);
  double exit(Ticket t);
}
interface PricingStrategy { double compute(Ticket t, LocalDateTime exitTime); }
```

---

### BookMyShow (Movie Ticket Booking)

**Requirements:** Browse movies/shows, select seats, book (hold → payment → confirm), cancel booking.

**Core entities:** `Movie`, `Theatre`, `Screen`, `Show`, `Seat`, `Booking`, `User`, `Payment`

**Key design decisions:**
- `Seat` has a `SeatStatus` enum: AVAILABLE, HELD, BOOKED
- Booking flow is a **State machine**: `PENDING → CONFIRMED → CANCELLED`
- **Observer pattern:** `BookingService` notifies `EmailNotification`, `SMSNotification` on confirmation
- **Concurrency critical:** Two users can try to book the same seat simultaneously
  - Solution: optimistic locking or `synchronized` block on `Seat.hold(userId)`
  - Hold expires after N minutes if payment not completed (scheduled cleanup)
- **Factory** for payment: `PaymentFactory.create(method)` → `UPIPayment`, `CardPayment`, `WalletPayment`

**Flow trace:**
```
User.selectSeats([seatIds], showId)
→ SeatService.hold(seatIds, userId)        // synchronized, check AVAILABLE, set HELD + holdExpiry
→ BookingService.create(user, show, seats)  // create Booking in PENDING state
→ PaymentService.process(booking, method)   // PaymentFactory → payment
→ BookingService.confirm(booking)           // set BOOKED, notify observers
```

---

### Elevator System

**Requirements:** N elevators, M floors, dispatch requests efficiently, handle direction/idle states.

**Core entities:** `ElevatorSystem`, `Elevator`, `ElevatorRequest`, `Dispatcher`

**Key design decisions:**
- `Elevator` has a **State pattern**: `IDLE`, `MOVING_UP`, `MOVING_DOWN`, `MAINTENANCE`
- `ElevatorRequest` is a **Command object**: `{sourceFloor, destinationFloor, direction}`
- **Dispatcher strategies** (Strategy pattern):
  - `NearestCarDispatcher` — pick closest idle/same-direction elevator
  - `FCFSDispatcher` — first come first served
- Each `Elevator` has a `TreeSet<Integer>` of pending floors (sorted for efficient next-stop lookup)
- `processNextFloor()` polls the set: going UP → pick lowest floor above current; going DOWN → pick highest below

**Concurrency:** `synchronized` on `Elevator.addRequest()` since multiple external requests arrive concurrently.

---

### Library Management System

**Requirements:** Search books, borrow/return, track availability, manage members, fine for late returns.

**Core entities:** `Library`, `Book`, `BookItem` (physical copy), `Member`, `Lending`, `Catalog`

**Key design decisions:**
- `Book` (metadata: ISBN, title, author) vs `BookItem` (physical copy with `barcode`, `status`) — important distinction
- `BookItem.status`: AVAILABLE, BORROWED, RESERVED, LOST
- **Repository pattern:** `BookRepository`, `MemberRepository` abstract DB access
- **Strategy** for fine calculation: `FineStrategy` → `DailyFineStrategy`, `TieredFineStrategy`
- Member has a `borrowLimit` and active `List<Lending>`
- `Catalog.search(query)` supports by title/author/ISBN — internal: Map<String, List<Book>>

**Fine flow:**
```
returnBook(barcode, memberId)
→ Lending.computeFine(returnDate)   // FineStrategy.calculate(daysLate)
→ Member.chargeFine(amount)
→ BookItem.setStatus(AVAILABLE)
→ checkReservationQueue(bookItem)   // notify next member in queue
```

---

### Cab Booking (Uber/Ola simplified)

**Requirements:** Rider requests ride, match nearest driver, track trip, compute fare, rate after trip.

**Core entities:** `Rider`, `Driver`, `Trip`, `Location`, `FareStrategy`, `MatchingService`

**Key design decisions:**
- `Driver` has `DriverStatus`: AVAILABLE, ON_TRIP, OFFLINE
- `Trip` state machine: `REQUESTED → ACCEPTED → IN_PROGRESS → COMPLETED | CANCELLED`
- **Strategy** for fare: `BaseFare + DistanceFare + TimeFare + SurgePricing`
- **Strategy** for matching: `NearestDriverMatcher`, `RatingWeightedMatcher`
- **Observer:** `Trip` status changes notify `RiderNotification`, `DriverNotification`, `BillingService`
- Location updates: `Driver.updateLocation(lat, lng)` — in production uses geospatial index (QuadTree/geohash), in LLD a simple `List<Driver>` with distance calc is fine

---

### Vending Machine

**Requirements:** Select item, insert money, dispense item + change, handle out-of-stock/insufficient funds.

**Core entities:** `VendingMachine`, `Item`, `Slot`, `Coin/Note`, `State`

**Key design decisions:**
- **State pattern** is the core: `IdleState`, `HasMoneyState`, `DispensingState`, `OutOfStockState`
- Each state implements: `insertMoney()`, `selectItem()`, `dispense()`, `cancel()`
- Invalid transitions throw `IllegalStateException` (e.g., `selectItem()` in `IdleState`)
- `VendingMachine` holds current `State` reference; delegates all actions to it
- Change calculation: greedy coin selection from available denominations

**State transitions:**
```
IDLE --insertMoney()--> HAS_MONEY
HAS_MONEY --selectItem(valid, enough)--> DISPENSING
HAS_MONEY --selectItem(out of stock)--> OUT_OF_STOCK (temporary)
DISPENSING --dispense()--> IDLE (return change)
HAS_MONEY --cancel()--> IDLE (return money)
```

---

## Assessment Problems (test weekends)

Pick from this list for LLD portions of assessments — choose ones the user hasn't done:

**Tier 1 (Day 28 assessment — first LLD):**
- Parking Lot
- Library Management System
- Chess (just pieces + valid move logic)

**Tier 2 (Day 42 assessment):**
- BookMyShow (just seat booking + payment flow)
- ATM Machine
- Hotel Room Booking

**Tier 3 (Day 56 full mock):**
- Cab Booking (simplified)
- Food Delivery (restaurant → order → delivery assignment)
- Social Media Feed (User, Post, Follow, Feed generation)

**Stretch problems (if ahead of schedule):**
- Stock Brokerage (Order, Trade, Portfolio)
- Online Auction (Bid, Item, AuctionTimer)
- Splitwise (Expense, Split strategies: equal/exact/percentage)
