---
colors:
  primary: "#0e5b49"
  primaryStrong: "#083e33"
  secondary: "#b6412c"
  tertiary: "#dfe8e0"
  neutral: "#f3f5f2"
  surface: "#ffffff"
  ink: "#16241f"
  muted: "#59675f"
  line: "#d5ded7"
  accentSoft: "#e4eee8"
  noteSoft: "#f8e9e4"
  summary: "#edf2ed"
  footer: "#102d26"
  footerInk: "#e0ebe5"
  footerMuted: "#a9bdb3"
  lead: "#3e5047"
  summaryInk: "#2d4036"
  prose: "#27372f"
  authorInk: "#34483d"
  workbenchBorder: "#c8d5ca"
  noteBorder: "#e9c9bf"
  downloadBorder: "#c3d6c8"
  selection: "#c9ddd0"
  crumbSeparator: "#8b9990"
  footerRule: "#395149"
typography:
  body: 'Aptos, "Segoe UI", sans-serif'
  display: '"Aptos Display", Aptos, "Segoe UI", sans-serif'
  code: 'Consolas, monospace'
  displaySizes: ["2rem", "2.2rem", "2.25rem", "2.35rem", "2.6rem", "2.65rem", "3rem", "3.3rem", "4rem", "5rem"]
  headingSizes: ["1.24rem", "1.28rem", "1.3rem", "1.55rem", "1.6rem", "1.75rem", "1.8rem", "1.85rem", "2rem", "2.35rem"]
  bodySizes: ["1rem", "1.02rem", "1.08rem", "1.1rem", "1.12rem", "1.22rem"]
  labelSizes: ["0.72rem", "0.8rem", "0.82rem", "0.84rem", "0.86rem", "0.88rem", "0.9rem", "0.92rem", "0.94rem", "0.95rem", "0.96rem", "0.98rem"]
  weights: [600, 650, 700, 750, 800]
shadows:
  workbench: "0 18px 44px rgba(22, 36, 31, 0.12)"
rounded:
  code: "6px"
  sheet: "8px"
  control: "10px"
  smallPanel: "12px"
  panel: "14px"
  workbench: "16px"
  avatar: "50%"
spacing:
  base: "4px"
  scale: [4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 40, 42, 44, 48, 50, 52, 56, 60, 64, 68, 76, 100, 104]
---

# Resume Path Lab Design System

## 1. Creative North Star

**Authored:** A resume revision desk for early-career technical candidates. The interface treats projects as evidence: cool paper, dark ink, precise rules, and vermilion annotations. It should feel practical and editorial, never like a generic business dashboard or a promise of guaranteed employment.

## 2. Color Roles

- Primary green owns links, primary actions, active navigation, and template downloads.
- Deep forest owns the footer, affiliate CTA, and major dark surfaces.
- Vermilion is reserved for annotations, focus outlines, and the brand check.
- Cool neutral is the page canvas; white is reserved for reading sheets, cards, and menus.
- Muted text and all functional text maintain at least 4.5:1 contrast against their backgrounds.
- Color never carries meaning without text. No gradients, glows, or decorative color washes.

## 3. Typography

Aptos Display handles the value proposition, page titles, section headings, and card titles. Aptos handles body copy and controls. Consolas is limited to inline code. Display tracking stays at or above `-0.035em`; body copy uses normal tracking. Article text measures at most 72 characters, uses balanced headings and pretty paragraph wrapping, and remains at least 16px on mobile.

## 4. Spacing and Layout

The desktop shell is 1200px wide with 32px side gutters. Mobile gutters are 20px. The homepage uses a two-column hero and editorial category rows; article pages use a 220px contents rail and a maximum 760px reading column. Groups use tight internal spacing and larger separation between sections. Headings receive more space above than below.

## 5. Radius, Borders, and Depth

Controls use 10–12px radii, content panels 14px, and the workbench 16px. Pills are not used for content chips or metadata. Borders are thin neutral rules. The workbench uses the single soft elevation token; cards, menus, and article prose stay flat. Colored side tabs and top accent borders are not part of the system.

## 6. Components

- **Header:** brand, primary links, template action, mobile disclosure; native `<details>` on small screens.
- **Hero workbench:** example label, project name, real guide bullet, annotation; decorative identity lines may be hidden on narrow screens.
- **Guide row:** title, summary, reading time, template availability; rows are separated by rules rather than nested cards.
- **Article aids:** breadcrumbs, quick summary, contents, takeaways, author, downloads, related guides.
- **Buttons:** primary, secondary text link, download, affiliate; minimum 48px height on primary touch actions.
- **States:** default, hover, focus-visible, active contents link, open disclosure, reduced motion. Form-specific loading, error, and empty states are introduced with any future form component.

## 7. Responsive Behavior

At 900px the article contents rail becomes a native disclosure and the hero becomes one column. At 768px the desktop navigation becomes a disclosure whose brand and summary remain in the first row while links take the second. At 520px the primary CTA is followed immediately by a compact workbench so the first screen includes evidence, not only marketing copy. Grids collapse without horizontal scrolling; long text wraps anywhere.

## 8. Motion and Accessibility

The workbench has one 700ms entrance using `cubic-bezier(.16,1,.3,1)`. Content is visible by default and animation never controls visibility. `prefers-reduced-motion` removes animation, transitions, rotation, and smooth scrolling. Keyboard focus uses a 3px vermilion outline. Semantic landmarks, skip navigation, native disclosures, 44px minimum navigation targets, and text labels accompany all color cues.
