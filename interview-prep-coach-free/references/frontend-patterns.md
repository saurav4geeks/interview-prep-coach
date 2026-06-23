# Frontend Patterns: JS/TS/React/Browser Concept Notes

Load this file during any frontend weekday session involving JavaScript fundamentals, browser internals, TypeScript, or React deep dives. For DSA problems in JS, also load `dsa-patterns.md`. For system design, load `frontend-system-design.md`.

---

## Part 1: JavaScript Execution Model

### Event Loop
**Core idea:** JS is single-threaded. The event loop moves tasks from queues to the call stack when the stack is empty.

**Execution order (per iteration of the loop):**
1. Run all synchronous code (call stack empties)
2. Run ALL microtasks (Promises, `queueMicrotask`, MutationObserver callbacks) — drain the queue completely
3. Run ONE macrotask (setTimeout, setInterval, I/O callbacks, setImmediate)
4. Render (browser only, if needed)
5. Repeat

**Recognition signal:** Any question about `setTimeout(..., 0)` vs Promise, or execution order of async code.

**Classic gotcha:**
```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
// Output: 1, 4, 3, 2
```

**Key insight:** Microtask queue must fully drain before any macrotask runs, even a `setTimeout(..., 0)`.

---

### Closures
**Core idea:** A function retains access to its lexical scope even when called outside that scope.

**Recognition signal:** Questions about "stale closures in useEffect", "factory functions", "module pattern", "IIFE", or the classic `var` in loop problem.

**The loop problem + fix:**
```js
// Bug: all print 3
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// Fix 1: let (block scope)
for (let i = 0; i < 3; i++) { setTimeout(() => console.log(i), 0); }
// Fix 2: IIFE closure
for (var i = 0; i < 3; i++) {
  ((j) => setTimeout(() => console.log(j), 0))(i);
}
```

**Stale closure in React useEffect:**
```js
// Bug: count is always 0 inside the interval
useEffect(() => {
  const id = setInterval(() => console.log(count), 1000);
  return () => clearInterval(id);
}, []); // missing dep
// Fix: add count to deps, or use functional update + ref
```

---

### `this` Binding Rules (priority order)
1. **`new` binding:** `this` = new object
2. **Explicit binding:** `call(ctx)` / `apply(ctx)` / `bind(ctx)` → `this` = `ctx`
3. **Implicit binding:** `obj.fn()` → `this` = `obj`
4. **Default binding:** standalone `fn()` → `this` = `undefined` (strict) or `window`
5. **Arrow functions:** no own `this`, inherit from lexical scope (cannot be bound)

**Interview pitfall:** `class` method passed as a callback loses `this`. Fix with arrow method or `.bind(this)` in constructor.

---

### Hoisting + TDZ
- `var` → hoisted and initialized to `undefined`. Can be used before declaration (value = undefined).
- `function` declarations → fully hoisted (can call before declaration).
- `let` / `const` → hoisted but NOT initialized → **Temporal Dead Zone (TDZ)**. Access before declaration throws `ReferenceError`.
- `class` → like `let`, in TDZ until declaration.

---

### Prototype Chain
```
obj → Object.prototype → null
arr → Array.prototype → Object.prototype → null
```
**`instanceof`:** walks the prototype chain checking `Constructor.prototype`.  
**`Object.create(proto)`:** creates object with `proto` as its prototype (no constructor call).  
**`class` syntax:** syntactic sugar over prototype-based inheritance.

**Interview question:** "Implement `new` from scratch":
```js
function myNew(Constructor, ...args) {
  const obj = Object.create(Constructor.prototype);
  const result = Constructor.apply(obj, args);
  return result instanceof Object ? result : obj;
}
```

---

## Part 2: Async JavaScript

### Promises
**States:** pending → fulfilled | rejected (immutable once settled).  
**Key methods:**
- `Promise.all([p1, p2])` — rejects fast if any rejects
- `Promise.allSettled([...])` — waits for all, returns `{status, value/reason}`
- `Promise.race([...])` — settles with first settled (any state)
- `Promise.any([...])` — resolves with first fulfilled; rejects only if ALL reject

**Implement `Promise.all` from scratch:**
```js
function promiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let remaining = promises.length;
    if (!remaining) return resolve(results);
    promises.forEach((p, i) => {
      Promise.resolve(p).then(val => {
        results[i] = val;
        if (--remaining === 0) resolve(results);
      }).catch(reject);
    });
  });
}
```

---

### Debounce vs Throttle
**Debounce:** delay execution until N ms after the LAST call. Use for: search input, resize handler.
```js
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
```

**Throttle:** execute at most once every N ms. Use for: scroll handler, mousemove.
```js
function throttle(fn, interval) {
  let lastTime = 0;
  return function(...args) {
    const now = Date.now();
    if (now - lastTime >= interval) {
      lastTime = now;
      return fn.apply(this, args);
    }
  };
}
```

---

### Async Patterns
**Retry with exponential backoff:**
```js
async function withRetry(fn, retries = 3, delay = 1000) {
  for (let i = 0; i < retries; i++) {
    try { return await fn(); }
    catch (e) {
      if (i === retries - 1) throw e;
      await new Promise(r => setTimeout(r, delay * 2 ** i));
    }
  }
}
```

**Concurrent with limit:**
```js
async function mapWithLimit(items, limit, fn) {
  const results = [];
  const executing = new Set();
  for (const [i, item] of items.entries()) {
    const p = fn(item).then(r => { results[i] = r; executing.delete(p); });
    executing.add(p);
    if (executing.size >= limit) await Promise.race(executing);
  }
  await Promise.all(executing);
  return results;
}
```

---

## Part 3: TypeScript Essentials

### Generics
```ts
function identity<T>(val: T): T { return val; }
function first<T>(arr: T[]): T | undefined { return arr[0]; }
```

### Utility Types (know these cold)
```ts
Partial<T>          // all keys optional
Required<T>         // all keys required
Readonly<T>         // all keys readonly
Pick<T, K>          // keep only keys K
Omit<T, K>          // remove keys K
Record<K, V>        // object with keys K and values V
ReturnType<F>       // infer return type of function F
Parameters<F>       // infer parameter types of function F
NonNullable<T>      // remove null and undefined
```

### Discriminated Unions
```ts
type Shape =
  | { kind: 'circle'; radius: number }
  | { kind: 'rect'; width: number; height: number };

function area(s: Shape): number {
  switch (s.kind) {
    case 'circle': return Math.PI * s.radius ** 2;
    case 'rect': return s.width * s.height;
  }
}
```

### Conditional Types + `infer`
```ts
type Awaited<T> = T extends Promise<infer R> ? R : T;
type ElementType<T> = T extends (infer E)[] ? E : never;
```

---

## Part 4: Browser Internals

### Critical Rendering Path (CRP)
**HTML → DOM → (parallel) CSS → CSSOM → Render Tree → Layout → Paint → Composite**

- **Render-blocking:** CSS blocks rendering; JS (without `defer`/`async`) blocks HTML parsing.
- **`<script defer>`:** execute after HTML parsed, in order. Good default for most scripts.
- **`<script async>`:** execute as soon as downloaded, regardless of parse state. Good for independent analytics.
- **Layout thrashing:** alternating DOM reads and writes forces reflow repeatedly. Batch reads, then batch writes.

### Reflow vs Repaint vs Composite
| Operation | Triggers | Cost |
|-----------|----------|------|
| Reflow (Layout) | width, height, margin, padding, font-size, DOM add/remove | Expensive — affects geometry |
| Repaint | color, background, visibility (no geometry change) | Medium |
| Composite only | transform, opacity, will-change | Cheap — GPU layer |

**Optimization:** use `transform`/`opacity` for animations; use `will-change: transform` sparingly.

### Event Delegation
Attach ONE listener on a parent instead of N listeners on children. Uses event bubbling.
```js
list.addEventListener('click', (e) => {
  if (e.target.matches('li.item')) handleClick(e.target);
});
```
**Pitfall:** `stopPropagation()` breaks delegation for listeners higher up.

---

## Part 5: React Deep Dive

### Reconciliation + Fiber
- **Virtual DOM diff:** React diffs two vDOM trees. Assumes different types → unmount+remount; same type → update in place.
- **`key` prop:** helps React match list items across renders. Wrong keys cause bugs (use stable IDs, not index if list reorders).
- **Fiber:** internal linked-list work unit. Enables incremental rendering, pausing, priority scheduling (Concurrent Mode).

### Hook Rules
1. Only call Hooks at the top level (no conditionals, loops, early returns).
2. Only call Hooks from React function components or other custom Hooks.

### `useEffect` Dependency Array
```js
useEffect(() => { /* runs after every render */ });
useEffect(() => { /* runs once on mount */ }, []);
useEffect(() => { /* runs when dep changes */ }, [dep]);
// Cleanup: return a function
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id); // runs on unmount or before next effect
}, []);
```
**StrictMode double-fire (React 18):** effects fire twice in dev to expose non-idempotent effects. Expected behavior.

### `useCallback` vs `useMemo`
```js
const memoizedFn = useCallback(() => doThing(a, b), [a, b]); // memoizes the function reference
const memoizedVal = useMemo(() => expensive(a, b), [a, b]);   // memoizes the return value
```
**When they matter:** only when passed to `React.memo` children or used as effect deps. Premature optimization otherwise.

### `useRef`
Two uses:
1. **DOM reference:** `const ref = useRef(null)` + `<div ref={ref}>` → `ref.current` is the DOM node.
2. **Mutable box:** store values that shouldn't trigger re-render (previous value, interval ID, abort controller).

### Rendering Optimization Checklist
- `React.memo(Component)` — skip re-render if props are shallowly equal
- `useMemo` on expensive calculations
- `useCallback` on functions passed to memoized children
- Lift state down or co-locate to avoid broad re-renders
- Context: split contexts so consumers only re-render when their slice changes; or use `useSyncExternalStore`

---

## Part 6: Web APIs to Know

### Intersection Observer
Efficient detection of element entering/leaving viewport. No scroll event listener needed.
```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) loadMore();
  });
}, { threshold: 0.1 });
observer.observe(sentinelEl);
```

### AbortController
Cancel fetch requests and async operations.
```js
const controller = new AbortController();
fetch(url, { signal: controller.signal }).catch(e => {
  if (e.name === 'AbortError') return; // expected
});
// Cancel:
controller.abort();
```
**Use in `useEffect`:** create controller on mount, abort on cleanup → prevents state updates on unmounted components.

### Web Worker
Run CPU-heavy work off the main thread. Communicate via `postMessage` (structured clone, no shared DOM).
```js
// main.js
const worker = new Worker('worker.js');
worker.postMessage({ data: bigArray });
worker.onmessage = (e) => console.log(e.data.result);
// worker.js
self.onmessage = (e) => {
  const result = heavyCompute(e.data.data);
  self.postMessage({ result });
};
```

### Service Worker + Caching Strategies
| Strategy | When to use |
|----------|-------------|
| Cache-first | Static assets, fonts — serve from cache, update in background |
| Network-first | API responses where freshness matters — try network, fall back to cache |
| Stale-while-revalidate | Balanced — serve cache instantly, fetch fresh copy for next time |
| Cache-only | Fully offline shell |

---

## Part 7: CSS Architecture & Layout

### Flexbox Quick Reference
```css
display: flex;
flex-direction: row | column;
justify-content: flex-start | center | space-between | space-around | space-evenly;
align-items: stretch | center | flex-start | flex-end | baseline;
flex: 1; /* flex-grow: 1, flex-shrink: 1, flex-basis: 0 */
gap: 16px;
```

### Grid Quick Reference
```css
display: grid;
grid-template-columns: repeat(3, 1fr);           /* 3 equal columns */
grid-template-columns: 200px 1fr 2fr;
grid-column: 1 / 3;   /* span cols 1–2 */
place-items: center;   /* shorthand for align-items + justify-items */
gap: 16px;
```

### CSS Architecture Trade-offs
| Approach | Pros | Cons |
|----------|------|------|
| BEM | No JS dependency, readable | Verbose class names |
| CSS Modules | Scoped locally, works with any bundler | Slightly more setup |
| Styled-components/Emotion | Co-located with component, theming | Runtime cost, larger bundle |
| Tailwind | Tiny final CSS, consistent design tokens | Long class strings, learning curve |

### Common Interview CSS Questions
- **Specificity order:** inline > ID > class/attr/pseudo-class > element/pseudo-element
- **`position: sticky`:** positioned relative to scroll container, sticks when threshold reached. Parent must not be `overflow: hidden`.
- **Stacking context:** created by `position + z-index`, `opacity < 1`, `transform`, `filter`, `isolation: isolate`.
- **`display: none` vs `visibility: hidden` vs `opacity: 0`:** none removes from flow + no events; hidden invisible but keeps space + no events; opacity 0 invisible + events still fire.

---

## Part 8: Security for Frontend

### XSS (Cross-Site Scripting)
- **Stored:** malicious script saved in DB, served to all users.
- **Reflected:** malicious script in URL param, reflected in response.
- **DOM-based:** client-side JS writes user input to DOM directly.
- **Mitigation:** sanitize all user input (DOMPurify), use `textContent` not `innerHTML`, strict CSP.

### CSRF (Cross-Site Request Forgery)
- Attack: malicious site makes authenticated requests to your API using the victim's cookies.
- **Mitigation:** `SameSite=Strict/Lax` cookies; CSRF tokens for state-changing requests; check `Origin`/`Referer` headers.

### Content Security Policy (CSP)
HTTP header that restricts what resources the page can load/execute.
```
Content-Security-Policy: default-src 'self'; script-src 'self' cdn.example.com; img-src *;
```

### CORS (Cross-Origin Resource Sharing)
- Same-origin policy blocks cross-origin fetches from JS.
- Server opts in with `Access-Control-Allow-Origin` response header.
- **Preflight:** `OPTIONS` request for non-simple methods. The browser sends it; you don't trigger it explicitly.

---

## Part 9: Accessibility (a11y)

### WCAG 2.1 AA Core Principles (POUR)
- **Perceivable:** alt text, captions, sufficient contrast (4.5:1 for normal text)
- **Operable:** keyboard accessible, focus visible, no timing traps
- **Understandable:** clear labels, consistent navigation, error identification
- **Robust:** valid HTML, ARIA used correctly, works with assistive tech

### ARIA Must-Knows
```html
<!-- Dialog -->
<div role="dialog" aria-modal="true" aria-labelledby="title-id">
  <h2 id="title-id">Title</h2>
</div>
<!-- Live region for dynamic content -->
<div aria-live="polite" aria-atomic="true">Status updates here</div>
<!-- Button that toggles -->
<button aria-expanded="false" aria-controls="panel-id">Toggle</button>
```
**Rule:** native HTML first (use `<button>`, `<a>`, `<input>`). Only add ARIA when native element can't do the job.

### Focus Management Patterns
- **Focus trap in modal:** cycle focus within the dialog; restore focus to trigger on close.
- **`tabindex="0"`:** add to non-interactive element to make focusable; avoid `tabindex > 0`.
- **Skip link:** `<a href="#main" class="sr-only focus:not-sr-only">Skip to main content</a>`

---

## Part 10: Performance (Core Web Vitals)

| Metric | What it measures | Good threshold |
|--------|-----------------|----------------|
| LCP (Largest Contentful Paint) | Loading — time for largest element to render | < 2.5s |
| INP (Interaction to Next Paint) | Interactivity — latency of all interactions | < 200ms |
| CLS (Cumulative Layout Shift) | Visual stability — unexpected layout shifts | < 0.1 |

### LCP Optimizations
- Preload hero image: `<link rel="preload" as="image" href="hero.jpg">`
- Avoid lazy-loading the LCP element
- Serve images from CDN with correct sizing + WebP format
- Reduce TTFB (server response time)

### INP / Responsiveness Optimizations
- Break up long tasks with `scheduler.yield()` or `setTimeout(..., 0)`
- Offload heavy computation to Web Worker
- Avoid large render-blocking JS

### CLS Optimizations
- Set explicit `width`/`height` on images and video to reserve space
- Avoid injecting content above existing content
- Use `transform` for animations (doesn't trigger layout)

### Bundle Optimization
- Tree-shaking: use ES modules (`import/export`), avoid side-effectful imports
- Code splitting: dynamic `import()` for routes and heavy libraries
- `<link rel="preload">` for critical resources; `<link rel="prefetch">` for likely-needed resources
- Analyze with: webpack-bundle-analyzer, source-map-explorer, Lighthouse
