# COMP433 Chapter 4 slides, UML: Use case and Activity diagrams (+ effort/cost estimation)

**How to use this file.** Each slide is delimited by a `---` rule. The `# Title` and bullet lines are the on-slide content (paste into Keynote's outline view). Text under **Speaker notes** goes in the presenter-notes pane, not the slide face. A `🖼 DIAGRAM` line names the image to drop on the slide.

**Diagram sources.** This deck follows Prof. Adel Taweel's Chapter 4 lecture deck (the `L4-UML-p89` PDF) closely, so the cleanest images are Adel's own slides. Export the named slide from his PDF, or use the two vector figures generated next to this file:

- `fig3_usecase_library.png` / `.svg`: a clean Library use-case diagram (simplified, matches the structure of Adel's slides 37/59)
- `fig4_activity_collect_history.png` / `.svg`: the Collect-medical-history activity diagram with swimlanes (matches Adel's slide 85)

Where a richer diagram exists only in Adel's deck (the full Library diagram with all refinements, the MHC-PMS diagrams, the multi-level diagrams, Process-order, Sell-a-product), the `🖼 DIAGRAM` line cites the exact Adel slide number to export.

Running examples follow Adel: **Library system** and **MHC-PMS** (the Mentcare mental-health patient management system from Sommerville). Cost-estimation figures are Adel's exact worked example.

---

# UML: Unified Modelling Language
## Use case diagrams → activity diagrams, and effort/cost estimation
### COMP433 Software Engineering · Chapter 4 · after Prof. Adel Taweel

- The examinable behavioural views: use case diagrams, use case descriptions, activity diagrams
- Plus the simplified developer-driven effort/cost estimate

**Speaker notes.** This covers the front half of UML modelling, the views produced during analysis: use case diagrams and descriptions during requirements analysis and specification, activity diagrams for the workflow of complex use cases, and the estimation method that turns the requirement list into time and cost. The through-line: a model is selective, it is for a reader and a decision, and each diagram answers a question the previous one raised.

---

# What is UML?

- **Unified**: combines the main preceding OO methods: Booch (Grady Booch), OMT (Jim Rumbaugh), OOSE (Ivar Jacobson), the *Three Amigos*
- **Modelling**: primarily for visually modelling systems; many system views, each by an appropriate model
- **Language**: a syntax for expressing modelled knowledge
- Born from the 1980s/90s *method wars*; submitted to the **OMG** Jan 1997, accepted Nov 1997; now the de facto standard for OO modelling (current UML 2.5)

**Speaker notes.** Three rival notations (Booch for design, Rumbaugh's OMT for analysis/data, Jacobson's OOSE for requirements and use cases) were unified at Rational into one notation, standardised by the Object Management Group in late 1997. The key framing, which the exam rewards: UML is a *language*, a notation only. It does not prescribe *when* to draw each diagram; that is the *process* (Chapter 3). Jacobson's contribution is the one we start with: the use case.

---

# Models, and the UML diagram families

- A model is the **language of the designer**: a representation of the system to-be-built or as-built, from one perspective; a tool for communicating with stakeholders; a way to reason about one characteristic
- A **diagram** is a view into the model. UML has 14+ diagrams; **9 are standard**, in two groups:
  - **Structure diagrams (static view):** use case, class, object, component, deployment
  - **Behaviour / interaction diagrams (dynamic view):** activity, sequence, communication/collaboration, state

**Speaker notes.** Adel groups the standard diagrams into static (structure) and dynamic (behaviour/interaction). Use case sits in the structure group as the static picture of usage; activity sits in the behaviour group as the dynamic picture of workflow. A model captures both structural and behavioural aspects, and no single diagram is enough, which is why we draw several complementary ones.

---

# Where each diagram fits the lifecycle

- **Analysis**
  - Requirements *elicitation/discovery*: user + system requirements → scenarios, interviews
  - Requirements *analysis* (of a business/system): **[use case] + [activity]**
  - *Specification*: **[use case description]**
- **Design**
  - Design options: [component]
  - System/object modelling: [class] + [object]; interactions: [sequence/communication] + [state]
  - System design: architecture/component view [component]; execution view [deployment]

**Speaker notes.** This is Adel's map (his slide 16). The two diagrams in this deck, use case and activity, are the requirements-analysis artefacts; the use case *description* is the specification artefact. Everything from class diagrams onward is design. Knowing where a diagram sits tells you what question it is answering and who reads it.

---

# Use cases: what use case modelling is

The basis for a **user-oriented** approach to system development:

- Identify the **users** of the system (**actors**)
- Identify the **tasks** they must undertake with the system (**use cases**)
- Relate users and tasks (**association**); this helps identify the **system boundary**
- Capture the system **functionality as seen by users**

**Speaker notes.** Use the cellular-telephone picture (Adel slide 20) if you want a non-library example: actors Cellular network and User, use cases Place phone call, Receive phone call, Use scheduler, with Place conference call extending Place phone call. Four building blocks: actors (stick figures, outside), use cases (ellipses, inside), associations (plain solid lines), and the system boundary (rectangle). The diagram captures the system as its users see it, before any commitment to how it is built.

---

# What are use cases (and what they are for)

- Represent that an **actor has a case for using** the system: the **tasks** the system must provide for the actor to undertake
- Built in the **early stages** of development, by **analysts and domain experts** during requirements analysis

Use cases aid to:

- **Specify the context** of a system
- **Plan iterations** of development
- **Validate** a system's architecture
- **Drive implementation** and **generate test cases**

**Speaker notes.** This "aid to" list (Adel slide 21) is examinable: use cases are not only a requirements artefact, they feed iteration planning, architecture validation, implementation, and test-case generation. Each use case is later backed by a textual description and, if its workflow is non-trivial, an activity diagram.

---

# How to identify actors

- Observe the **direct users** of the system (could be people or other systems)
  - What **roles** do they play? Who **provides** information? Who **receives** information?
- Actors can be:
  - **Principal**: initiates/benefits (a human role)
  - **Secondary**: external hardware, other systems, a system-triggered event
- Describe each actor precisely: **short name is always a Noun**; one-sentence description of the role and how it interacts

**Speaker notes.** Adel's two examples (slide 22): *BookBorrower*, someone who uses the library to borrow books [Principal]; *SystemTimer*, a system event that regularly and automatically triggers checking expired loans [Secondary]. The SystemTimer is the canonical secondary actor: no human, the system's own clock initiates the use case. An actor is a role, not a person; the same human can be two actors.

---

# Worked actor list: MHC-PMS

| Actor | Semantics / description |
|---|---|
| Doctor | Member of the PMS, registered; can view and edit patient records only |
| Nurse | Member, registered; can view and edit patient records |
| Receptionist | Member, registered; can view, edit and **create** patient records |
| Patient | Their information is registered, but cannot view or edit their records |
| IT Staff | Can maintain patient records |
| Lab Staff | Can edit patient records to enter lab tests only |

**Speaker notes.** Adel's PMS actor exercise (slide 24). The discriminator between Doctor, Nurse and Receptionist is *permission*, not job title: receptionist creates, doctor/nurse view and edit, lab staff edit only test results, patient is a passive subject. This is how you turn a requirements document into a precise actor inventory: each actor is one role with one access profile.

---

# Worked actor list: Library

| Actor | Semantics / description |
|---|---|
| BookBorrower | Member, registered; can borrow books only |
| JournalBorrower | Member, registered; can borrow books **and** journals |
| BookBrowser | Can search for books/journals; may not be a member, cannot borrow |
| BookClassifier | Classifies/catalogs new books and registers them |
| BookReturnRegistrar | Receives returned books and registers them |
| BookLendRegistrar | Lends (or renews) books and registers them |
| BookShelver | Shelves books and registers shelving status |

**Speaker notes.** Adel's Library actor exercise (slide 26). The crucial modelling move: *BookClassifier, BookReturnRegistrar and BookLendRegistrar are all the same human, the Librarian.* They are listed separately as fine-grained roles, then grouped. This sets up the actor-generalisation hierarchy on the next slide. Note JournalBorrower can do everything a BookBorrower can plus journals, another generalisation cue.

---

# Actor generalisation (inheritance)

- Actors can be organised into a **generalisation hierarchy** (hollow triangle, specialised → general)
- Library "Primary Actors" tree:
  - **LibraryUser** → **Browser** → **BookBorrower** → **JournalBorrower**
  - **Browser** → **Librarian**
- A specialised actor **inherits** the use cases of its parent and adds its own

**Speaker notes.** This is Adel's "Primary Actors" panel (slides 37, 59). LibraryUser is the most general; Browser can search; BookBorrower is a Browser who can also borrow books; JournalBorrower is a BookBorrower who can also borrow journals; Librarian is a Browser with staff use cases. Drawing the inheritance once means JournalBorrower's association lines do not have to repeat every BookBorrower use case. This is the actor-side counterpart of use case generalisation later in the deck.

---

# What are use cases (notation)

- **Things actors do with the system**: a *task* an actor needs to perform with the help of the system (for example, Borrow a book), or an interaction with another system
- Describe the system's behaviour **from the user's standpoint**; a role an actor takes in using the system
- Represented by **ellipses**, labelled with a **verb phrase**

**Speaker notes.** Adel's slide 27. The ellipse "Borrow copy of a book" is the canonical shape. The verb-first rule is the fast discriminator: a noun-phrase label ("Book borrowing") is the sign someone has confused a use case with a class. The substance of the use case is in its description, not the ellipse.

---

# How to find use cases

- **Scenario-based analysis**: write the system's processes/services as scenarios; each interaction with the system is a candidate use case
- **Actor-based analysis**: from the actor list, for each actor ask:
  - what they **need** from the system (use cases of value to them)
  - any **other interactions** they take part in for **someone else's benefit**
- How do you know it is a use case? Estimate frequency of use, examine differences between use cases, distinguish **normal** vs **alternative** courses of events, create new use cases when necessary

**Speaker notes.** Adel slides 28/41. The two techniques are complementary: scenario-based surfaces the flows, actor-based surfaces actors who appear in nobody's happy path but still need access. The "someone else's benefit" prompt catches the Librarian who acts on the BookBorrower's behalf, and secondary actors like the Email System.

---

# Constructing the diagram: noun-verb analysis

From the requirements text:

- **Nouns / noun phrases → candidate ACTORS** (and some candidate classes/attributes)
- **Verbs / verb phrases → candidate USE CASES**
- **Noun-verb interactions → ASSOCIATIONS**

Discard inappropriate candidates: redundant or omnipotent nouns, vague entities, meta-language, entities outside system scope, pure attributes, constraints/events.

**Speaker notes.** This is Adel's construction method (slides 35-36), the bridge from a written requirements document to a use case diagram. Underline nouns in one colour and verbs in another, list candidates, apply the discard rules, then read off actors, use cases, and the associations between them. The same noun-verb pass is reused later to seed the class diagram, so it is worth doing carefully.

---

# Library requirements (the source text)

- The library holds **books and journals**, with several **copies** of a book; some are **short-term loans**
- A **library member** may borrow for **three weeks**; members borrow up to **six items**, **staff up to 12**; only staff borrow journals
- **Members of the public** (non-members) can **browse/search** but cannot borrow
- Late returns **pay a fine**, in cash or by **credit card**; an **email reminder** is sent automatically for late loans
- The system tracks borrow / renew / return, and lets staff **manage** books: add / update / catalog / remove

**Speaker notes.** This is the richer Library text Adel marks up (slides 35-36). Highlight the nouns (library member, staff, public, book, journal, copy, fine, credit card, email, loan period) and verbs (borrow, renew, return, browse/search, pay a fine, pay, send, manage, add, update, catalog, remove). Nouns become actors (BookBorrower, JournalBorrower, BookBrowser, Librarian) and entities; verbs become use cases; the email and bank introduce secondary actors. This text drives the diagram on the next slides.

---

# The Library use case diagram (first cut)

🖼 DIAGRAM: Adel slide 37 or 39 (full first-cut Library diagram). Clean alternative: `fig3_usecase_library.png`

- Primary actors: **BookBorrower**, **JournalBorrower** (member of staff), **BookBrowser**, **Librarian**
- Secondary actors: **SystemTimer**, **Email System**
- Use cases include: Borrow / Return / Renew copy of a book; Borrow / Return / Renew copy of a journal; Pay fine; Browse/Search for books; Send reminder to late loans by Email; Add new / Update / Remove / Catalog books

**Speaker notes.** Walk Adel's slide 37/39. Note the secondary-actor mechanics: SystemTimer initiates "Send reminder to late loans by Email", and that use case reaches out to the Email System (a secondary actor on the right). The boundary rectangle (added on slide 39) separates the use cases inside from all actors outside. The manage-books use cases (add/update/remove/catalog) all associate with the Librarian. My `fig3` image is a deliberately simplified six-use-case version if you want a less crowded slide for first teaching, then show Adel's full diagram.

---

# MHC-PMS use cases (the Mentcare example)

🖼 DIAGRAM: `figC_mhcpms_usecase.png` (clean export; matches Adel slide 47, MHC-PMS with system boundary)

- Actors: **Medical receptionist**, **Nurse**, **Doctor**, **Manager**, and **Patient record system** (secondary)
- Use cases: Register / Unregister patient, View patient info, **Transfer data**, Contact patient, View / Edit patient medical record, Setup consultation, Export statistics report, Generate medical report

**Speaker notes.** This is Sommerville's standard example (Adel slides 42-47), so it is high-probability exam material. Two teaching points. First, one actor can have several use cases (the medical receptionist has five). Second, **Transfer data** has an arrow leaving the boundary to the Patient record system: that is the system as a *secondary actor*, the receptionist triggers the use case and the external records system receives the data. Adel draws this hand-off explicitly on slide 43 ("triggers" on both sides).

---

# Refinements: include, extend, generalisation

- Once you have several use cases, you see shared sub-tasks, conditional paths, and variants. UML provides three refinement relationships:
  - `<<include>>` and `<<extend>>` (the two common **stereotypes**)
  - generalisation / `<<inherit>>`
- Extensions provide opportunities for: **optional parts**, **alternative complex cases**, **separate sub-cases**, **insertion of use cases**

**Speaker notes.** Adel's slide 48. Stereotypes (the `<<...>>` labels) attach additional classification to a relationship. The next slides take each one in turn with its precise meaning, its arrow direction, and a Library example, because confusing include and extend is the single most common notation error on this material.

---

# `<<extend>>`: conditional / alternative behaviour

Use `<<extend>>` to:

- refine functionality, handle **different/alternative scenarios**
- show **constraints / conditional behaviour** (model business rules)

Add it when:

- a part of a use case is **optional or alternative** behaviour
- a sub-flow runs **only under certain conditions**
- behaviour segments **may be inserted** in a base use case

Arrow direction: from the **extending** case **to the base**.

**Speaker notes.** Adel slides 50-51. The Library example: **Refuse loan** extends **Borrow copy of a book**, guard `[too many books on loan]`. The normal Borrow flow is unchanged; Refuse loan exists only to describe what happens when the rule is violated. Stress the arrow: it points from the *less central* case (Refuse loan) to the *base* (Borrow), the opposite of include. Refuse loan is "conditionally invoked".

---

# Extension points

🖼 DIAGRAM: Adel slide 51 (Borrow ellipse with extension points + extend arrow)

- An **extension point** is a named position in the base where the extension may fire
- Borrow copy of a book declares:
  - **maximum no of items on loan**
  - **status validation: after confirming BookBorrower identity**
- The `<<extend>>` arrow carries the guard, for example `[too many books on loan]`

**Speaker notes.** Extension points (Adel slide 51) are written in a compartment inside the base ellipse and answer "where in the base does the extension fire?". Without a named extension point, an extend is just an unstructured alternative path; with one, the base stays auditable: a reader sees the hooks and looks up which extensions attach to each. The guard sits on the extend arrow next to its tail.

---

# `<<include>>`: unconditional reuse

Use `<<include>>` to:

- model how the system **reuses a pre-existing component**; maximise reuse
- identify and show **common functionality** among use cases
- **avoid duplicating** functionality (good engineering practice)

Add it when:

- behaviour is **common to two or more** use cases (or to simplify a large use case by splitting it)
- the **result** of the included behaviour matters to the base, **not the behaviour itself**

Arrow direction: from the **base** **to the included** case.

**Speaker notes.** Adel slide 52, with the decomposition pictures: a sub-use-case drawn inside a base is pulled out as a separate ellipse joined by an include arrow. Two reuse shapes: shared by several bases, or factored out of one large base for clarity. The phrase to quote: the base cares about the *result* of the include, not how it is done, which is exactly why it can be reused and changed in one place.

---

# `<<include>>` example: Compute Return-Dates

🖼 DIAGRAM: Adel slide 53 (Borrow & Renew → Compute Return-Dates)

- **Borrow copy of a book** and **Renew loan of copy of a book** both `<<include>>` **Compute Return-Dates**
- "**Always invoked**": every borrow and every renewal needs a return date
- The included sub-use-case does **not change** the normal behaviour of the base cases

**Speaker notes.** Adel slide 53. Factoring Compute Return-Dates out gives the loan-period rule (ShortLoan 2 days, MediumLoan 2 weeks, LongLoan 3 months) a single home, so it changes once. Contrast with extend: include is *always* invoked and unconditional; extend is *conditionally* invoked under a guard. Direction note Adel writes on the slide: the arrow goes from the central/base use case to the less-central sub use case.

---

# include and extend together

🖼 DIAGRAM: Adel slide 55 (BookBorrower + JournalBorrower, Compute Return-Dates included, Refuse loan extending)

- **Borrow** and **Renew** `<<include>>` **Compute Return-Dates** (always)
- **Refuse loan** `<<extend>>`s **Borrow** and **Borrow journal** (conditionally, on the guard)
- The two arrows point **opposite ways**: include = base → sub; extend = extension → base

**Speaker notes.** Adel slides 54-55 combine both on one diagram, which is the best single slide for the directionality contrast. Say the rule out loud: *the arrow tail sits on the use case that knows about the other.* The base names its includes as steps (base → include); the extension names the base and the extension point it attaches to (extension → base). This contrast is the most-marked notation point in the exam.

---

# Generalisation / `<<inherit>>`

🖼 DIAGRAM: Adel slide 56 (Pay fine ← Pay by credit card / Pay by cash)

- One use case is a **more specific version** of another (specialisation)
- **Pay fine** is inherited by **Pay by credit card** and **Pay by cash**: the actor can pay a fine in two different ways
- Notation: solid line with a **hollow triangle**, pointing from the **specialised** case to the **general** one

**Speaker notes.** Adel slide 56 (UML v2.5). Both specialised cases inherit the general "pay fine" workflow and add their own payment-specific steps. Use case generalisation is the rarest of the three refinements in business systems; prefer include for shared sub-tasks and extend for guarded variants, and reach for generalisation only when two use cases are genuinely the same use case at different levels of specificity.

---

# Combined refinement: Pay fine, fully modelled

🖼 DIAGRAM: Adel slide 57 or 58 (Pay fine with inherit + include + extend, Email System & Bank System)

- **Pay by credit card** and **Pay by cash** `<<inherit>>` **Pay fine**
- **Pay by credit card** `<<include>>` **Send payment confirmation** (reaches the **Email System**)
- **Pay by credit card** `<<extend>>` **Validate Payment** (reaches the **Bank System**)
- Reuse: **Send message (by Email)** is `<<include>>`d by both *Send reminder to late loans* and *Send payment confirmation*

**Speaker notes.** Adel slides 57-58, the capstone refinement example showing all three relationships and two secondary actors together. For every successful "Pay by credit card", a confirmation email is sent (include, always part of a successful card payment); the bank must approve the payment and may refuse it (extend, the conditional/failure path). And "Send message (by Email)" is itself factored out so both the late-loan reminder and the payment confirmation reuse it. This is the slide that shows the refinements are not academic: they fall out naturally from a realistic requirement.

---

# The complete Library use case diagram

🖼 DIAGRAM: `figA_library_refinements.png` (clean export, all three refinements + secondary actors). Fuller alternative: Adel slide 59 (adds the Primary Actors generalisation tree and the journal/manage-books use cases)

- All use cases inside the boundary, with `<<include>>`, `<<extend>>`, `<<inherit>>` shown
- Secondary actors: SystemTimer, Email System, Bank System
- The actor generalisation tree on the right (LibraryUser → Browser → BookBorrower → JournalBorrower; Librarian)

**Speaker notes.** This is the payoff slide (Adel slide 59): everything assembled. Use it as a recap. Trace one include (Borrow → Compute Return-Dates), one extend (Refuse loan → Borrow), one inherit (Pay by cash → Pay fine), and one secondary-actor reach-out (Send reminder → Email System). Point at the Primary Actors tree to recap actor generalisation. Mnemonic to leave them with: an *include*'s base cannot complete without it; an *extend*'s base usually runs fine without it.

---

# Detailing a use case (the specification)

A use case ellipse is only a label. Write a **specification** for it. Good practice covers:

- **Pre-conditions**: the system state before the use case begins (facts that must be true)
- **Flow of events**: the steps (actions) in the use case, normal and alternative/error paths
- **Post-conditions**: the system state after the use case completes

**Speaker notes.** Adel slides 62-63. The flow of events is numbered, with the normal ("If yes...") path and the alternative/error ("If no...") path branching at the decision step. Example skeleton for Borrow: pre-conditions (member; below the loan limit); flow (1. attempts to borrow; 2. system checks if OK; 3. if yes, record and issue; else report reason); post-condition (loan count updated if successful). The full template on the next slide structures this.

---

# Use case description: Borrow Copy of a Book

| Field | Content |
|---|---|
| System | Library System |
| Title | Borrow Copy of a Book |
| Description | A BookBorrower may borrow a copy; the book must exist and be available, issued by the Librarian. Status → `<on-loan>`; loan period by type: ShortLoan 2 days, MediumLoan 2 weeks, LongLoan 3 months |
| Actors | BookBorrower, Librarian |
| Data | Book information; borrow information; book status |
| Stimulus / Trigger | Command issued by Librarian on behalf of BookBorrower |
| Pre-conditions | 1. Borrower is a member. 2. Borrower is below the permitted number of books on loan |
| Workflow / Flow of events | 1. Borrower asks to borrow. 2. System (or Librarian) checks allowance. 3. If yes: 3.1 record copy on borrowed list; 3.2 issue copy on loan. 4. Else: alternative/error path |
| Post-conditions / Response | 1. Loan count updated (if successful). 2. Copy status → `<on-loan>` (if successful) |
| Comments | Librarian needs security permission to access BookBorrower information |

**Speaker notes.** Adel slide 64. Walk a couple of rows. The fields are System, Title, Description, Actors, Data, Stimulus/Trigger, Pre-conditions, Workflow, Post-conditions/Response, Comments. The pre-conditions become testable requirements ("enforce a maximum of six items on loan"); step 4 is the seam where the error scenarios attach. This is the contract the team builds against.

---

# Use case description: Transfer Patient Data (MHC-PMS)

| Field | Content |
|---|---|
| System | Medical System (MHC-PMS) |
| Title | Transfer Patient Data |
| Description | A receptionist may transfer data from the MHC-PMS to a general patient record database maintained by a health authority. Transferred info is either updated personal information (address, phone, etc.) or a summary of diagnosis and treatment |
| Actors | Medical receptionist, Patient records system (PRS) |
| Data | Patient's personal information; treatment summary |
| Stimulus / Trigger | Command issued by medical receptionist |
| Pre-conditions | 1. Patient is a member of the clinic. 2. Patient information is accessible |
| Workflow / Flow of events | 1. Receptionist selects patient records to transfer. 2. Transfers selected records to authority. 3. If successful... 4. Else, if not successful... (alternative/error path) |
| Post-conditions / Response | Confirmation that the PRS has been updated |
| Comments | Receptionist needs security permission to access patient information and the PRS |

**Speaker notes.** Adel slide 65, the second worked description. Same template, different domain, and note the PRS appears as a (secondary) actor in the Actors row, matching the boundary-leaving arrow on the MHC-PMS diagram. Two descriptions across two domains show the template is general, not Library-specific.

---

# Scenarios

- Each time an actor interacts with the system, the triggered use case **instantiates a scenario**
- A scenario is a **specific path** through a use case, **with no branching**
- Scenarios are documented as **text alongside** the use case and activity diagrams
- A use case with an extension is expected to have **more than one** scenario / alternative flow

**Speaker notes.** Adel slides 67-68. A scenario is a single branch-free trace; "if X then Y else Z" is two scenarios, not one. Because Borrow has the Refuse-loan extension and the alternative kiosk path, it has several scenarios. Scenarios are the readable narratives the customer and testers confirm against, the human-readable counterpart of the formal description.

---

# Scenarios for Borrow copy of a book

- **Initial assumption**: BookBorrower Joe is a member of the library
- **Normal (success)**: Joe (no books on loan) takes a copy to the Librarian, who checks his allowance, scans the barcode, and issues it; system updated
- **Alternative (success)**: Joe uses the auto-librarian kiosk; it scans his ID and the barcode, checks his allowance, and issues automatically; system updated
- **Error (failure)**: Joe is refused because he already has six books on loan (his maximum)
- **Error (failure)**: the barcode is damaged; the copy is not issued

**Speaker notes.** Adel slides 69-70. Note the two errors fail differently: the six-book refusal is a *business-rule* violation (generates "enforce a maximum of six items on loan"); the damaged barcode is a *data/physical* failure (generates "provide a manual barcode-entry option"). Both are valid requirement sources. The normal and alternative both succeed but by different routes (counter vs kiosk), which is why the alternative is a separate scenario rather than a footnote.

---

# Multi-level (composite) use cases

🖼 DIAGRAM: Adel slide 71 (MHC-PMS top-level with composite use cases)

- For large systems, draw a **top-level** diagram of **composite** use cases (marked with the composite icon)
- MHC-PMS top level: **Manage patient registration**, **Manage patient medical record**, **Generate medical report** (composites), plus View patient info, Export statistics report, Setup consultation

**Speaker notes.** Adel slide 71. A composite use case (small grid icon) is one that decomposes into several lower-level use cases. Treat the top-level diagram as a map of the whole system; it stays readable because each composite hides its internals. This is decomposition, one of the core modelling moves.

---

# Multi-level: 1st and 2nd level

🖼 DIAGRAM: Adel slide 72 (1st-level and 2nd-level MHC-PMS decompositions)

- **Manage patient registration** → Register new patient, De-register existing patient
- **Manage patient medical record** → View patient medical record, Edit patient medical record
- **Generate reports** → Generate prescribed drugs report, **Generate patient reports** (itself composite)
- **2nd level**: Generate patient reports → Generate admitted-patient report, Generate discharged-patient reports

**Speaker notes.** Adel slide 72. Each composite from the top level gets its own first-level diagram that magnifies one region of the map; a first-level use case that is still composite (Generate patient reports) gets a second-level diagram. Each level keeps the same boundary (MHC-PMS) and shows only the relevant actors. Decompose only as far as readability requires.

---

# Activity diagrams

- Represent **workflows and business processes**; model the **behaviours (activities)** of the system
- Show the **dependencies and coordination** between activities
  - the activity flow **should not get "stuck"**
  - useful in **requirements elicitation**: to see how use cases interact to achieve business processes, and to help **identify use cases and the operations** that realise a use case
- Generally, can be **attached to any model element** to model its **dynamic behaviour**

**Speaker notes.** Adel slide 75. Two roles worth stressing: an activity diagram is not only for documenting a known workflow, it is an *elicitation* tool that surfaces use cases and operations and exposes where a flow could get stuck (a path that never reaches a final node, or a decision branch with no continuation). It is the dynamic counterpart to the static use case view.

---

# Activity diagram notation

| Symbol | Meaning |
|---|---|
| Filled circle | **Initial node**: start. Exactly one |
| Bull's-eye (filled circle in a ring) | **Final node**: end. May be more than one |
| Rounded rectangle | **Action / activity state**: a unit of work (verb phrase) |
| Diamond | **Decision** (one in, guarded outs) or **Merge** (guarded paths rejoin) |
| Thick bar | **Fork** (parallel paths start) or **Join** (parallel paths synchronise) |
| Vertical columns | **Swimlanes**: assign activities to actors / departments / systems |

- **A Fork requires a matching Join.** **A Decision requires a matching Merge.**

**Speaker notes.** Adel slide 76. The pairing rule is examinable and is the deepest correctness check: every fork must be closed by a join, every decision by a merge. Decision/merge model *alternative* paths (one branch runs); fork/join model *parallel* paths (all branches run, the join waits for all). Choosing a fork where you mean a decision asserts concurrency that does not exist.

---

# Activity example: Process order

🖼 DIAGRAM: `figB_process_order.png` (clean export; matches Adel slide 76). Fork → Fill Order / Send Invoice; decision [priority order]/[else]; join → Close Order

- Initial node → **Receive Order** → **fork** into two parallel paths
- Left: Fill Order → decision `[priority order]` Overnight / `[else]` Regular Delivery → merge
- Right: Send Invoice → Receive Payment
- Both paths **join** → Close Order → final node

**Speaker notes.** Adel slide 76. This one diagram shows all the machinery: a fork (filling the order and invoicing happen in parallel), a decision/merge inside the left branch (priority vs regular delivery), and a join that waits for both the goods and the payment before closing the order. Contrast the fork (both happen) with the decision (one happens), the cleanest illustration of the difference.

---

# Activity example: Collect medical history (flows)

🖼 DIAGRAM: Adel slide 77 (Collect Medical History: normal flow beside normal/alternative/error flows)

- Normal flow (left): Search for patient → Create record → Record personal info → Record medical history
- Full flow (right): decision `[New patient?]`; `[Patient found?]`; `[Patient provide data?]` with a **fork/join** for the refusal path (sign exclusion form ∥ nurse records exclusion); `[medication in menu?]` → Record as code / Record as free text

**Speaker notes.** Adel slide 77. Show the simple normal flow first, then the full version with all the decisions and the one fork/join (when the patient refuses to provide data, the patient signs an exclusion form *and* the nurse records the exclusion, in parallel, then join). The medication sub-decision is a real clinical trade-off: coded (consistent, analysable, harder to enter) vs free text (easy to enter, hard to aggregate).

---

# Two levels: use-case flow vs business process

🖼 DIAGRAM: Adel slide 80 (left: Borrow/Return book flow; right: book-a-journey with fork/join + repeat-until)

- **Specific flow of one use case** (business-process view): Borrow copy of a book, decision `[borrow]`/`[return]`, fork to Stamp book ∥ Record borrowing, join
- **General business process** (business view): book a journey, parallel flight ∥ hotel ∥ car reservation, with a **repeat-until** loop on car reservation, then confirm

**Speaker notes.** Adel slide 80. The point: the same notation works at two granularities, one use case's internal flow, or a whole business process spanning several use cases. The journey example also shows iteration ("repeat until car reservation was successful"), which the simple library flow does not need. Keep one granularity per diagram; do not mix a single use case and a whole business process on one page.

---

# Swimlanes: who does what

🖼 DIAGRAM: `figD_borrow_return_activity.png` (clean export; matches Adel slide 84, Borrow/Return across Member and Librarian lanes, with the `[another book]` loop)

- A **swimlane** is a column assigning activities to one actor (Member, Librarian)
- An arrow that **crosses a lane** is a **hand-off** of responsibility
- The `[another book]` edge loops back so a member can borrow several books in one visit

**Speaker notes.** Adel slide 84 combines two use cases (Borrow and Return) across two actor lanes. Swimlanes are the one thing an activity diagram does that a flowchart cannot: they make "who is responsible for each step" explicit, and the cross-lane arrows are exactly where coordination bugs hide on real projects. Worth drawing as soon as more than one actor is involved.

---

# Swimlanes: Collect medical history

🖼 DIAGRAM: `fig4_activity_collect_history.png` (matches Adel slide 85)

- Three lanes: **Patient**, **Receptionist**, **Nurse**
- `[New patient?]` → Create vs Search record (Receptionist), then merge → Record personal info
- Hand-off to the **Nurse** → Record medical history → `[medication in menu?]` Record as code / free text → merge → final

**Speaker notes.** This is the same scenario as the earlier non-swimlane version, now with the actor responsible for each step made explicit (Adel slide 85). Use my `fig4` export here, it reproduces this exact diagram cleanly. Trace the cross-lane hand-off from Receptionist to Nurse and note that ownership of the workflow changes there. Decisions each have a matching merge; the flow starts in the Patient lane and ends in the Nurse lane.

---

# Swimlanes: Sell a product

🖼 DIAGRAM: Adel slide 86 (Sell a product across Customer / Sales Department Officer / Stockroom Officer)

- Lanes: **Customer**, **Sales Department Officer**, **Stockroom Officer**
- Place Order → Take Order → Check Product → branch `[Yes]` Confirm Order / `[No]` Arrange Product (loops back)
- → Make Payment → Dispatch Order → Collect Order → end state

**Speaker notes.** Adel slide 86, labelled with the formal terms: Start State, Swim lane, Branch, Activity State, End State. The branch on product availability either confirms the order or arranges the product and loops back to re-check, another example of iteration. Three lanes show the work crossing from customer to sales to stockroom and back, with each hand-off visible.

---

# Activity diagrams: getting them right

- Every **decision** needs a matching **merge**; every **fork** needs a matching **join**
- The flow must **not get stuck**: every path reaches a final node
- **Decision** (one branch runs) vs **fork** (all branches run), choose deliberately
- Guards in `[brackets]` should be **mutually exclusive and exhaustive**
- Use **swimlanes** once more than one actor is involved; do not mix granularities; do not model a trivial linear flow

**Speaker notes.** Phrase these as practitioner pitfalls, the failure modes that show up in real workflow modelling. The pairing and no-stuck-flow rules are the correctness checks; the decision-vs-fork choice and the swimlane omission are the modelling-judgement ones. An activity diagram of a multi-actor process without lanes throws away the one advantage it has over a flowchart.

---

# Effort + cost estimation (Prof. Adel)
## A simplified, developer-driven method

- Built **per User Requirement (UR)**, bottom-up
- For each UR, estimate: how many developers can work on it **concurrently**, and the **average effort** (person-weeks) at that concurrency
- Acronyms: **pw** = person-week, **pm** = person-month; **w** = week, **m** = month
- *Effort* assumes full-time work (day = 8h, week = 7 days, month = 30 days)
- *Schedule time* = actual elapsed time, based on working days (allowing for holidays)

**Speaker notes.** Adel's estimation slide. The method starts from the requirement list and asks the team, per requirement, for the concurrency and the effort. Two numbers fall out per UR: the *average/parallel* effort (time if the estimated developers all work together) and the *total effort for one developer* (the same work done by one person). Summing them gives an optimistic and a pessimistic bound.

---

# Worked example (Adel's exact figures)

| UR | Developers (concurrent) | Avg effort | Total effort (one dev) |
|---|---|---|---|
| UR1 | 2 | 2 pw | 2 × 2 = **4 pw** |
| UR2 | 1 | 3 pw | 3 × 1 = **3 pw** |
| UR3 | 3 | 2 pw | 2 × 3 = **6 pw** |
| UR4 | 4 | 1 pw | 1 × 4 = **4 pw** |
| **Total** | avg = (2+1+3+4)/4 = **2.5 devs** | **8 pw** (min) | **17 pw** (max) |

**Speaker notes.** Read the columns. "Avg effort" is the parallel duration of each UR; its sum (8 pw) is the lower bound, what you spend if the developers are always available to parallelise. "Total effort for one developer" multiplies avg effort by the developer count to get full person-weeks; its sum (17 pw) is the upper bound, one developer doing everything sequentially. Average team size needed is 2.5 developers. Hold 8 and 17, they drive the rest.

---

# From effort to schedule, cost, and price

- **Schedule time** adds a 30% buffer (working-day reality, holidays):
  - min: 8 × 1.30 = **11 w** (fastest completion)
  - max: 17 × 1.30 = **22 w** (slowest completion)
- **Cost** at avg salary **$250 / week**: 250 × 22 = **$5,500**
- **Profit margin** (min 10%, max 30%):
  - min price: 5,500 × 1.10 = **$6,050**
  - max price: 5,500 × 1.30 = **$7,150**

**Speaker notes.** Three steps turn effort into a quote. Inflate raw effort by 30% for a realistic schedule (nobody is 100% utilised; calendars have holidays), giving an 11-to-22-week window. Cost it on the conservative (max) effort: 22 weeks at $250/week is $5,500. Add margin to get the quoted price: 10% to 30%, so $6,050 to $7,150. The exam can ask for any row, so be able to run effort → schedule → cost → price in both directions.

---

# What to be able to do in the exam

- **Use case diagram**: noun-verb construction; actors (principal/secondary) and actor generalisation; correct `<<include>>` / `<<extend>>` / `<<inherit>>` with right arrow direction, and the *reason* for each
- **Description + scenarios**: complete the template (pre/flow/post); normal, alternative, error scenarios
- **Activity diagram**: correct notation; swimlanes for multiple actors; decision vs fork; decisions paired with merges, forks with joins; no stuck flow
- **Estimation**: reproduce the per-UR table and the schedule → cost → price chain

**Speaker notes.** The verbs the exam uses are draw, explain why, complete, compute. The recurring discriminators: include vs extend direction (who knows about whom), and decision vs fork (one branch vs all branches). For estimation, rebuild Adel's exact table from the two estimated columns and carry it to the price range.

---

# Sources

- Prof. Adel Taweel (2025/26), *COMP433: UML (Chapter 4)* and *Effort + Cost Estimation: Very Simplified Method*, the primary source; running examples (Library, MHC-PMS) and the estimation worked example follow Adel's slides
- Sommerville (2015), *Software Engineering*, 10th ed., ch.5 (MHC-PMS, system models)
- Booch (1999), *Rational* notation; Jacobson (1992), *OOSE* (origin of use cases); Fowler (2003), *UML Distilled*

**Speaker notes.** Diagram images are best exported directly from Adel's Chapter 4 deck (slide numbers are cited on each diagram slide), with two clean vector versions (`fig3`, `fig4`) generated alongside this file. For a contested notation question, the OMG UML 2.5.1 specification is the authority; for daily use, Fowler's *UML Distilled* is the compact reference.
