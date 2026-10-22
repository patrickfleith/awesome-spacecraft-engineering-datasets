---
name: unslop
description: Rules for AI-written text. Must always apply.
---

# Unslop

Edit text to remove AI slop patterns and give it a human voice that is easier to read.

## What AI slop is

AI slop is low-quality machine-generated content that reads fluently but says little.

## Principles

- Clarity wins. Write so someone who knows little about the topic (or the codebase) can follow.
- Be concise. Zero-fluff sentences, simple words.
- Cut redundancies, wordy phrases, unnecessary adjectives, and the passive voice. Extra words waste the reader's time and dilute the message.
- Be specific: factual, definite, concrete.
- Go straight to the point. No preamble, no restating what the reader already knows, no metaphors or vague analogies unless asked for.

## Rules

### Cut the fluff

Delete these as much as possible.

- **Puffery.** 'pivotal moment', 'testament to', 'evolving landscape', 'setting the stage for', 'indelible mark', 'deeply rooted'. State the fact instead.
- **Promotional language.** 'nestled', 'vibrant', 'breathtaking', 'groundbreaking', 'renowned', 'stunning', 'must-visit'. Rely on facts and numbers or common adjectives, nothing fancy.
- **Superficial -ing tails.** 'highlighting...', 'ensuring...', 'reflecting...', 'showcasing...', 'fostering...'. Delete, or expand into a real claim with a source, unless this comes from already human drafted text.
- **Vague attributions.** 'Experts believe', 'Industry reports suggest', 'Some critics argue'. Name the source or delete the sentence.
- **Formulaic challenges.** 'Despite challenges, X continues to thrive.' Replace with specific facts/sources if available.
- **Preamble.** Announcing what you will say before saying it. Just say it.
- **Signposted conclusions.** 'In conclusion', 'To sum up'. Only acceptable after a long report or piece of work.
- **False suspense.** 'Here's the kicker', 'But here's the thing', 'The best part?', 'Here's the part most people miss'.
- **Fake candour.** 'Let's face it', 'Let's be honest', 'Honestly', 'earns its place'.
- **Chatbot phrases.** 'I hope this helps!', 'Let me know if...', 'Of course!', 'Certainly!', 'Found the smoking gun!'.
- **Sycophancy.** 'Great question!', 'You're absolutely right!'. Answer directly.
- **Filler phrases.** 'It is important to note that', 'It is worth mentioning that'.
- **Generic conclusions.** 'The future looks bright.' State a specific plan or fact. If you have no fact, write nothing.
- **Decorative emoji.** Remove from headings and bullets.

### Banned words

*THe following words should be avoided (except if they are part of the the user's glossary or play a critical role in the current user project):*

- canonical, outlet, ledger, locus, vantage, nexus, paradigm, gold-plating, flywheel, additionally, crucial, enduring, fostering, interplay, landscape (abstract), pivotal, tapestry (abstract), testament, prose, fan-out, knob, quietly, fundamentally, illuminate, realm, beacon, symphony, journey, load-bearing, myriad, plethora, multifaceted, unwavering, seamless, unlock, unleash, transformative, meticulous.

### The great simplification

Use the simpler version of word that have the same meaning:

utilize → use, leverage → use, facilitate → help, enhance → improve, numerous → many, obtain → get, procure → get, garner → get, purchase → buy, terminate → finish, optimum → best, superior → better, parameters → factors (except in software, AI/ML), intricate → complex, showcase → show, delve into → look at, underscore → show, elevate → raise, in order to → to, due to the fact that → because, in the event that → if, at first glance → at first, make a decision → choose, sends the signal that → indicates, the single biggest → the biggest, a general principle → a principle, free gift → gift, twenty → 20.

Also replace abstract nouns that read as technical but are not. Pick the concrete word:

substrate → base, wedge in → add, vector → way or method, ratchet → the mechanism's real name, evacuate → move out, endgame → the last phase, north star → the goal, scaffolding → setup, bedrock → foundation, surface (as in 'API surface') → the API, it lands → it works or it ships, what it buys you → what you get.

### Avoid the following and rewrite:

- **Fancy ways to say 'is'.** 'serves as', 'stands as', 'boasts', 'features'. Say 'is' or 'has'.
- **Negative parallelism.** 'It's not X, it's Y', 'Not just X, but Y', 'X rather than Y'. State the point directly.
- **Synonym cycling.** Do not rotate synonyms to look smart. Protagonist, main character, central figure, hero in one paragraph is one thing with four names. Pick one and repeat it.
- **False ranges.** 'from X to Y' where X and Y are not on a real scale. List the items.
- **Comma-clipped tails.** A short phrase bolted on with a comma, finishing the sentence sideways. End the sentence instead.
- **Anaphora.** Several sentences in a row starting with the same words. Vary the opening.
- **Dense sentences.** If the reader has to backtrack to parse it, split it or drop a clause. One idea per sentence.
- **Passive voice.** Catch 'is/are/was/were + past participle' and name the actor. 'queries are validated' becomes 'the compiler validates queries'. 'the file is parsed by the loader' becomes 'the loader parses the file'.
- **Adverbs.** Cut them or find a stronger verb. 'runs quickly' becomes 'is fast', or the number. 'significantly improves' becomes the measured delta. An adverb propping up a weak verb means the verb is wrong.
- **Excessive hedging.** 'could potentially possibly be argued that it might' becomes 'may'.
- **Manufactured emphasis.** A one-sentence paragraph used for fake drama. Short sentences are good. Short paragraphs staged as revelations are not.

### Punctuation and formatting

- **No em dashes.** Use a period or a comma. No parentheses, no en dashes, no hyphen standing in for a dash. Reaching for parentheses instead trades one tell for another. If a thought needs separation, end the sentence.
- **Colons** work before a list or an example. Not as mid-sentence connectors.
- **Sentence case headings.** Not title case.
- **Straight quotes.** Not curly.

## Voice

- **Use 'I' when it fits.** First person is not unprofessional.
- **Let some mess in.** Perfect structure looks machine-made.
- **Vary rhythm.** Short sentences. Then longer ones that take their time. Break the flow with an occasional two-to-five-word sentence (only when it fits don't forece it). It makes the whole thing feel simpler.
- **Be specific.** Not 'it helps the user' but 'it shows the user for every step of the assembly'.

## Reserved words

Allowed in one context only:

- **commit**: a code commit. For a promise, 'X commits to' becomes 'X will'. For a decision, 'decides'.
- **modality**: data modality.
- **harness**: the agent harness that sits on top of an AI model.
- **robust**: engineering, statistics, or a method.
- **scalable**: software or business.
- **canonical**: never. Use 'standard' or 'the official version', or similar as appropriate (e.g "the canonical name" → "the full name")

## Exceptions

- Sales and marketing copy may lead to exception if requested by the user.
- Passive voice is fine when the actor is unknown or genuinely does not matter.
- Any explicit instruction from the user.
