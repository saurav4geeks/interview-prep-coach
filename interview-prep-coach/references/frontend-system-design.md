# Frontend System Design Framework + Problem Notes

Load this file for Frontend System Design (FSD) sessions and Component Design (Frontend LLD) sessions. FSD is the frontend analog of HLD; Component Design is the analog of LLD.

---

## The 5-Step FSD Framework (Use Every Time)

Every frontend system design answer should follow this sequence. Claude guides you through each step in a session.

---

### Step 1: Clarify Requirements (3–4 min)

**Functional:**
- What are the core features? (read vs write heavy? real-time updates?)
- What devices / viewports? (desktop-only, mobile-first, responsive?)
- Browser support targets? (modern evergreen, IE11, specific mobile browsers?)
- Accessibility requirements? (WCAG AA minimum assumed; any specific needs?)

**Non-functional:**
- Performance budget — what's the acceptable LCP? TTI? Bundle size target?
- Scale — concurrent users, data volume per view, update frequency
- Offline support needed?
- Internationalization (i18n) / RTL support?

**Out of scope:** What you're NOT designing (backend APIs, auth, infra).

**Output:** 4–6 bullet requirements you'll design to.

---

### Step 2: Component Architecture (5–7 min)

Sketch the component tree and data-ownership hierarchy:

```
App
├── Layout (Nav, Sidebar)
├── FeaturePage
│   ├── DataFetcher (or custom hook)
│   ├── ListContainer
│   │   ├── VirtualList
│   │   └── ListItem (× N)
│   └── DetailPanel
└── GlobalProviders (Theme, Auth, QueryClient)
```

Key decisions to call out explicitly:
- **Container vs Presentation split** — which components own data-fetching logic?
- **Composition strategy** — compound components, render props, or slot pattern?
- **Shared state scope** — prop drilling, context, or external store? (use the narrowest scope that works)
- **Rendering strategy** — CSR, SSR, SSG, ISR? Why?

---

### Step 3: State Design (4–5 min)

Categorize all state and put it in the right place:

| State type | Where it lives | Example |
|------------|---------------|---------|
| Server/remote data | React Query / SWR / Apollo cache | User list, posts |
| Global UI state | Zustand / Redux / Context | Theme, auth user, modals |
| Local component state | `useState` / `useReducer` | Form input, toggle, hovered row |
| URL-driven state | URL params / query string | Filters, pagination, selected tab |
| Ephemeral | `useRef` | Scroll position, interval ID |

**Derived state rule:** if it can be computed from existing state, don't store it — compute it.

**Form state:** controlled (React state) vs uncontrolled (refs + DOM). Prefer controlled for validation; prefer libraries (React Hook Form) for complex forms.

---

### Step 4: Data Fetching + API Integration (4–5 min)

- **Fetch strategy:** on-mount vs on-demand vs prefetch vs server-side
- **Caching:** React Query defaults (staleTime, cacheTime), cache invalidation on mutation
- **Loading + error states:** skeleton screens > spinners for layout-stable UX; error boundaries for unexpected failures
- **Optimistic updates:** update UI immediately, revert on error; use mutation callbacks
- **Pagination:** offset-based (simple, supports jumping) vs cursor-based (consistent with real-time data); prefer cursor for infinite scroll
- **Real-time:** WebSocket (bidirectional) vs SSE (server→client only, simpler) vs polling (last resort); don't forget reconnection logic
- **Abort on unmount:** always pass `AbortSignal` to fetch; cancel in `useEffect` cleanup

---

### Step 5: Performance, Accessibility, and Edge Cases (3–5 min)

**Performance:**
- Lazy load routes and heavy components (`React.lazy` + `Suspense`)
- Virtualize long lists (react-window, react-virtual) — only render visible rows
- Memoize expensive calculations (`useMemo`); stable callback refs for memoized children (`useCallback`)
- Image optimization: correct sizing, WebP, lazy loading, `srcset`
- Code split vendor bundles; preload critical resources
- Critical CSS inlined; non-critical deferred

**Accessibility:**
- Semantic HTML first (no `<div>` buttons)
- All interactive elements keyboard-operable
- Focus management on dynamic content (modal open/close, route change)
- ARIA live regions for async status updates
- Sufficient color contrast; no information conveyed by color alone

**Edge cases:**
- Empty states, error states, offline states
- Very large datasets (virtualize)
- Slow network (skeleton + timeout handling)
- Rapid user input (debounce, race condition prevention)
- Auth expiry mid-session (refresh token flow or redirect)

---

## Key Concepts to Know Cold

### Virtual DOM vs Real DOM
- Real DOM operations are expensive (reflow/repaint). React batches updates via vDOM diff, minimizing actual DOM changes.
- React 18 concurrent features: `startTransition` marks non-urgent updates, keeping UI responsive during heavy renders.

### Rendering Strategies
| Strategy | When to use | Example |
|----------|-------------|---------|
| CSR (Client-Side Rendering) | Highly interactive dashboards, auth-gated pages | Admin panel |
| SSR (Server-Side Rendering) | SEO-critical, personalized pages, fast first paint | E-commerce PDP |
| SSG (Static Site Generation) | Content that rarely changes | Blog, marketing pages |
| ISR (Incremental Static Regeneration) | Mostly static + occasional updates | News site, product catalog |

**Hydration:** SSR sends HTML; JS attaches event listeners. Mismatch between server and client HTML causes hydration errors.

### Micro-Frontend Architecture
Split a large frontend into independently deployable apps. Approaches:
- **Module Federation** (Webpack 5): share code between bundles at runtime
- **iframes:** strong isolation, poor UX integration
- **Web Components:** framework-agnostic, good for design system components

Trade-offs: team autonomy ↑, shared bundle size savings ↓, routing complexity ↑.

### Design System Architecture
- **Design tokens:** primitive values (colors, spacing, radii) expressed as CSS custom properties or JS constants
- **Theming:** CSS variables swapped at root level; avoid runtime theme computation when possible
- **Polymorphic components:** `as` prop pattern — `<Button as="a" href="...">` renders an anchor
- **Accessibility by default:** bake ARIA, keyboard nav, and focus styles into every component
- **Tree-shaking:** named exports only; avoid barrel files that import everything

---

## FSD Problem Notes

### Typeahead / Autocomplete
**Key decisions:**
- Debounce input (150–300ms) before firing API call
- Cancel in-flight request on new keystroke (AbortController)
- Cache results per query string (Map or React Query) — avoid refetching same prefix
- Keyboard nav: arrow up/down moves highlight; Enter selects; Escape closes
- Accessibility: `role="combobox"`, `aria-expanded`, `aria-activedescendant` on input, `role="listbox"` + `role="option"` on dropdown
- For large datasets: server-side prefix filtering; don't send full list to client

**Data flow:**
```
input → debounce → AbortController fetch → cache check → render options
keyboard → highlight state (local) → selection → callback
```

---

### Infinite Scroll Feed
**Key decisions:**
- `IntersectionObserver` on a sentinel element at the bottom — no scroll listener
- Cursor-based pagination preferred (stable with real-time inserts vs offset pagination)
- Virtualize the list when item count grows large (`react-window`'s `VariableSizeList` for varying heights)
- Prefetch next page when user is 80% through current page
- Skeleton placeholders for perceived performance

**State machine:**
```
idle → loading → loaded (append items) → idle
                      ↓ error → retry button
                      ↓ end-of-feed → stop observing
```

---

### File Upload Component
**Key decisions:**
- Chunked uploads for large files: split `File` into `Blob.slice()` chunks, upload in parallel with a concurrency limit, resume by tracking which chunks succeeded
- Progress: `XMLHttpRequest.upload.onprogress` or streaming fetch (not standard yet); aggregate chunk progress
- Drag-and-drop: `dragover`, `drop` events; `e.preventDefault()` on both; use `DataTransfer.files`
- State machine per file: `idle → validating → uploading → done | error | cancelled`
- Retry failed chunks; show partial progress on retry
- Accessibility: `<input type="file">` behind a styled button; `aria-live` for status

---

### Real-Time Dashboard
**Key decisions:**
- WebSocket for bidirectional (control + data); SSE for server→client push only (simpler, uses HTTP)
- **Throttle rendering:** don't re-render on every incoming message at 60fps data. Buffer incoming data, flush to state on `requestAnimationFrame` or at a fixed interval (e.g., 100ms)
- Virtualized chart: only render visible time window; sliding window buffer in memory
- **Reconnection:** exponential backoff on disconnect; show connection status indicator
- Normalize incoming data to a keyed structure for O(1) updates

---

### Google Docs (Collaborative Editor)
**Key decisions:**
- **OT (Operational Transformation):** server serializes concurrent ops; each client transforms its own pending ops against received ops. Used by Google Docs.
- **CRDT (Conflict-free Replicated Data Type):** ops can be applied in any order; merge is commutative. Simpler to reason about; used by Figma (Yjs).
- **WebSocket** for low-latency bidirectional sync
- Show cursors: broadcast cursor position as ephemeral state (not persisted); render other users' cursors in a separate overlay layer
- Autosave: debounce writes to server; optimistic local state
- Undo/redo: local stack + awareness of remote ops (complex with OT; CRDT makes this easier)
- Offline: queue ops locally, replay when reconnected

---

### YouTube Video Player
**Key decisions:**
- **Adaptive Bitrate Streaming (ABR):** HLS or DASH manifests; browser downloads segments and switches quality based on bandwidth. Use `hls.js` or `video.js` for cross-browser.
- **Playback state machine:** `idle → loading → playing → paused → buffering → ended | error`
- Buffer management: preload next N seconds; seek → flush buffer + reload segments
- **Controls UX:** custom controls overlay (keyboard shortcuts: Space=play/pause, ←/→=seek ±5s, f=fullscreen, m=mute); hide on inactivity (`setTimeout` reset on `mousemove`)
- Subtitles: WebVTT format; `<track>` element or custom overlay for styled captions
- Picture-in-Picture: `video.requestPictureInPicture()`
- Accessibility: `aria-label` on all controls; announce play/pause state; captions mandatory (WCAG 1.2.2)

---

## Component Design Problem Notes (Frontend LLD)

### Framework for any Component Design question
1. **Requirements:** What does it do? What are the must-have behaviors? What's out of scope?
2. **API Surface:** props, events, slots/children. Design for the caller, not the implementation.
3. **State Model:** what state is internal, what's controlled by the parent?
4. **Rendering + UX Details:** edge cases, loading states, empty states, overflow, truncation.
5. **Accessibility:** keyboard behavior, ARIA roles, focus management.
6. **Performance:** memoization, virtualization, lazy loading if applicable.

---

### Modal / Dialog
**API:** `isOpen`, `onClose`, `title`, `children`, `initialFocusRef?`

**Focus trap algorithm:**
1. On open: query all focusable elements inside dialog; store previously-focused element.
2. On `Tab`: move focus forward through list; wrap on last element.
3. On `Shift+Tab`: move backward; wrap on first element.
4. On close: restore focus to previously-focused element.

**Implementation choices:**
- Portal (`ReactDOM.createPortal`) to `document.body` — avoids z-index and overflow clipping issues
- Backdrop click closes modal (unless `closeOnBackdropClick={false}`)
- `Escape` key closes modal
- ARIA: `role="dialog"`, `aria-modal="true"`, `aria-labelledby`

---

### Data Table
**State:** sort column + direction, filter values, pagination (page/cursor), selected rows, column widths.

**Virtualization:** `react-window` `FixedSizeList` (uniform row height) or `VariableSizeList` (dynamic); measure row heights lazily.

**Column resizing:** `mousedown` on column divider → track `mousemove` delta → update column width in state; use `useRef` for divider position.

**Keyboard navigation:** arrow keys move focused cell; Enter/Space for interaction; `grid` ARIA role with `gridcell`, `rowheader`, `columnheader`.

**Sorting:** stable sort; indicate sort direction with `aria-sort` on column header.

---

### Toast / Notification System
**Architecture:**
- Global toast context + `useToast()` hook for triggering from anywhere
- Queue: FIFO with max visible (e.g., 3 at a time); stack newest on top or bottom
- Auto-dismiss: `setTimeout` per toast; pause on hover (clear timeout on `mouseenter`, restart on `mouseleave`)
- Accessibility: `role="alert"` (interrupts immediately) vs `aria-live="polite"` (waits for silence). Use `polite` for info toasts, `assertive` for errors.
- Animation: CSS transitions on mount/unmount; use `react-transition-group` or Framer Motion for enter/exit

**Toast interface:**
```ts
type Toast = {
  id: string;
  message: string;
  type: 'info' | 'success' | 'warning' | 'error';
  duration?: number; // ms; undefined = sticky
  action?: { label: string; onClick: () => void };
};
```

---

### Multi-Select Combobox
**Complexity:** search filter + keyboard nav + virtual options + accessibility + selection state.

**API:** `options`, `value` (selected IDs array), `onChange`, `placeholder`, `isLoading`, `filterOption?`

**Keyboard behavior:**
- `ArrowDown/Up`: move highlighted option (wrap); `Home/End`: jump to first/last
- `Enter`: select highlighted; `Space`: toggle (if multiselect)
- `Backspace` in input: remove last selected tag
- `Escape`: close; restore input to empty

**ARIA pattern:** `combobox` role on input + `listbox` on dropdown + `option` on each item. `aria-multiselectable="true"`, `aria-selected` on each option, `aria-activedescendant` on input pointing to highlighted option ID.

**Virtualize options if list > 200 items.**
