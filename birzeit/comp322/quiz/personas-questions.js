// Shared question set for the COMP322 Personas quiz.
// Used by personas.html (static self-study), personas-live.html (student),
// and personas-host.html (instructor dashboard). Edit in one place.
window.PERSONAS_QUESTIONS = [
  {
    type: 'mc',
    text: 'A persona, as used in HCI design, is best described as:',
    options: [
      'A real user invited to test the product in usability sessions',
      'A fictitious archetype representing a segment of real users, derived from research',
      "The team's preferred customer profile",
      'A demographic chart showing user age, gender, and income'
    ],
    correct: 1,
    explanation: 'A persona is a research-derived fictional user who stands in for a real user segment. It is neither a real person nor a demographic average; it is a memorable archetype the team can refer to when making design decisions.'
  },
  {
    type: 'mc',
    text: 'Why do designers create personas?',
    options: [
      'To replace the need for user research',
      'To give the team a shared, concrete mental model of users that guides design decisions',
      'To impress stakeholders with detailed user profiles',
      'To target advertising and marketing campaigns'
    ],
    correct: 1,
    explanation: 'Personas crystallise findings from research into a memorable archetype the whole team can refer back to. They do not replace research, they communicate and apply it.'
  },
  {
    type: 'multi',
    text: 'Which of these should appear on a well-formed persona?',
    options: [
      'Photo and a name',
      'Goals and motivations',
      'Frustrations or pain points',
      "The user's bank account number",
      'Behaviour patterns and context of use',
      'A representative quote in their own voice',
      'Internal product roadmap and pricing strategy'
    ],
    correct: [0, 1, 2, 4, 5],
    explanation: 'A good persona makes the user concrete with personal identifiers (name, photo, quote) and captures what matters for design (goals, frustrations, behaviour patterns). It does not include sensitive personal data or internal company information.'
  },
  {
    type: 'mc',
    text: 'The primary persona for a product is:',
    options: [
      'The most photogenic or relatable one',
      'The persona representing the largest demographic',
      'The persona whose needs cannot be satisfied by designing for any other persona',
      'The persona the design team finds most likeable'
    ],
    correct: 2,
    explanation: "Cooper's definition: the primary persona is one whose needs must be specifically targeted, because designing for someone else would fail them. Photogenic looks and demographic size are not the criteria."
  },
  {
    type: 'multi',
    text: 'Common pitfalls when creating personas include:',
    options: [
      'Inventing demographic detail without research to back it',
      'Stereotyping based on age, gender, or nationality',
      'Creating more than five primary personas for a single product',
      'Including a memorable name and photograph',
      'Creating the personas after the product has shipped',
      'Sourcing data from interviews with real users'
    ],
    correct: [0, 1, 2, 4],
    explanation: 'Personas are powerful when they are research-backed, focused (typically three to five), and built before design decisions. The usual failure modes are gut-feel personas, demographic stereotypes, too many of them, and creating them retrospectively to justify decisions already made.'
  },
  {
    type: 'mc',
    text: 'Where should the data for a good persona come from?',
    options: [
      "The designer's intuition about likely users",
      'Stakeholder gut feel about who buys the product',
      'Direct user research: interviews, observation, contextual inquiry',
      'Marketing demographics from third-party data providers'
    ],
    correct: 2,
    explanation: 'Personas distil findings from primary user research. Marketing demographics describe who buys, not how users think, decide, or struggle, which is what design needs to address.'
  },
  {
    type: 'match',
    text: 'Match each persona element to its primary purpose in design.',
    leftLabel: 'Persona element',
    rightLabel: 'Why it is on the persona',
    pairs: [
      { left: 'Goals',                right: 'Drive which features matter most for this user' },
      { left: 'Frustrations',         right: 'Reveal what the product must avoid or actively solve' },
      { left: 'Representative quote', right: "Capture the user's voice in their own words" },
      { left: 'Photo and name',       right: 'Make the persona feel like a real, memorable person' },
      { left: 'Behaviour patterns',   right: 'Predict how this user will actually interact with the product' }
    ],
    explanation: 'Each persona field exists for a reason. The personal identifiers (photo, name, quote) make the persona memorable; the goals, frustrations, and behaviour drive concrete design decisions.'
  },
  {
    type: 'rank',
    text: 'Put the steps of creating personas in the correct order, from first to last.',
    items: [
      'Use the personas to guide ongoing design decisions',
      'Validate the drafts with stakeholders and additional users',
      'Identify recurring patterns and user segments across participants',
      'Draft preliminary persona archetypes',
      'Conduct user research (interviews, observation, contextual inquiry)'
    ],
    correctOrder: [4, 2, 3, 1, 0],
    explanation: 'Personas are research-first artefacts: data comes before drafting. The typical pipeline is research → pattern identification → drafting → validation → ongoing use throughout design.'
  },
  {
    type: 'mc',
    text: "A secondary persona's needs should be:",
    options: [
      'Ignored entirely so the team can focus',
      "Accommodated as long as they do not compromise the primary persona's needs",
      "Weighted equally with the primary persona's needs",
      'Deferred to a later version of the product'
    ],
    correct: 1,
    explanation: 'Secondary personas are supplemental: their needs are addressed wherever possible, but never at the cost of the primary persona. Equal weighting would dilute the design focus; deferring would lose the data the persona captures.'
  },
  {
    type: 'mc',
    text: "Microsoft's Persona Spectrum framework emphasises that limitations or disabilities are:",
    options: [
      'Always permanent and unchanging',
      'Permanent, temporary, or situational, all relevant to design',
      'Rare and best handled by specialised accessibility teams',
      'Best addressed by separate products for each group'
    ],
    correct: 1,
    explanation: 'The Persona Spectrum reframes accessibility as the union of permanent (e.g. one arm), temporary (e.g. broken arm), and situational (e.g. holding a baby) conditions. A design that works for the permanent case usually also helps the temporary and situational cases.'
  },
  {
    type: 'match',
    text: 'Match each user situation to its category on the Persona Spectrum.',
    leftLabel: 'User situation',
    rightLabel: 'Spectrum category',
    pairs: [
      { left: 'A user with congenital low vision',           right: 'Permanent limitation' },
      { left: 'A user with a cast on their dominant wrist',  right: 'Temporary limitation' },
      { left: 'A user holding a baby in one arm',            right: 'Situational limitation' },
      { left: 'A user in bright sunlight with screen glare', right: 'Situational limitation (environment)' }
    ],
    explanation: 'Permanent, temporary, and situational are not just disability categories; they are conditions of use. Each one yields design constraints the team can target.'
  },
  {
    type: 'multi',
    text: 'Which of these are genuine advantages of personas for a design team?',
    options: [
      'Shared vocabulary across the team when discussing users',
      'Anchor design decisions to specific, named users',
      'Replaces the need for user testing later',
      'Helps prioritise features by user value',
      'Makes user needs concrete and memorable',
      'Guarantees the product will succeed in the market'
    ],
    correct: [0, 1, 3, 4],
    explanation: 'Personas align teams and inform priorities, but they complement rather than replace ongoing user research and testing. They are not a guarantee of success; they are a guard against designing for nobody in particular.'
  },
  {
    type: 'mc',
    text: 'Personas and user stories: which statement is correct?',
    options: [
      'They are the same thing under different names',
      'Personas describe WHO the user is; user stories describe what that user wants to DO and WHY',
      'Personas come from marketing; user stories from engineering',
      'User stories make personas unnecessary once written'
    ],
    correct: 1,
    explanation: 'A persona is the actor; a user story is one action that actor wants and the reason: "As <persona>, I want to <action> so that <benefit>." Personas without stories are static descriptions; stories without personas drift toward abstract, generic users.'
  },
  {
    type: 'rank',
    text: 'Rank these sources of data for persona creation, from most reliable to least reliable.',
    items: [
      "Designer's assumptions and personal experience",
      'Marketing demographics and purchase records',
      'Stakeholder interviews about who their users are',
      'User surveys with open-ended response questions',
      'Direct user interviews and field observation'
    ],
    correctOrder: [4, 3, 2, 1, 0],
    explanation: 'The closer the data is to actual users speaking and acting, the more reliable it is for design. Designer assumptions and pure demographics tend to produce "paper personas" that lead the design astray.'
  },
  {
    type: 'mc',
    text: 'When in the design process should personas be created?',
    options: [
      'After product launch, to retroactively validate decisions already made',
      'After initial user research is gathered and before significant design decisions are taken',
      'Only when the product is failing and the team needs to course-correct',
      'Once development is complete, as documentation for handover'
    ],
    correct: 1,
    explanation: 'Personas are at their most useful between user research and design decisions: they translate research insights into a form designers can reason with, before commitments are made.'
  }
];
