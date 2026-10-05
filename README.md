# The Unofficial Guide

Nithya Kondagari
corpus: advice_threads

---

# Unit 1

## What This Does
I picked the advice_threads corpus. This system answers questions that students may have about classes and life on campus. For example, whether professors actually answer their emails, if you should buy a bike for a 20 minute walking commute, if the edition of a textbook matters. Questions that are general to college life but not necessarily a specific class.


## Chunking Strategy

**Chunk size:** 800 characters
**Overlap:** 120 overlap

The baseline used 800/120. My strategy doesn't have a chunk size, it splits on --- reply n --- markers, so chunk length is set by the corpus (105–254 characters, 175 average) rather than by a number I picked. The 800/120 values remain in config.py for fallback_split, which I kept for comparison.

## Sample Chunks

**Chunk 1** — source: `` — produced by: ``

```
======================================================================
Chunk 1  |  source: thread_bike_commute.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Is a bike worth it for a 20 minute walk commute?

Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.
```

**Chunk 2** — source: `` — produced by: ``

```
======================================================================
Chunk 2  |  source: thread_first_gen.txt#1  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Anything specific for first-generation students?

The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happy to explain them and nobody volunteers them.

```

**Chunk 3** — source: `` — produced by: ``

```
======================================================================
Chunk 3  |  source: thread_laptop_specs.txt#2  |  produced by: chunker.py::split_documents
======================================================================
THREAD: How much laptop do I actually need for CS courses?

I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.

```

**Chunk 4** — source: `` — produced by: ``

```
======================================================================
Chunk 4  |  source: thread_parking.txt#1  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Worth getting a parking permit?

Street parking on Verrill is legal and free and unmarked, which is why half the upper years do it.

```

**Chunk 5** — source: `` — produced by: ``

```
======================================================================
Chunk 5  |  source: thread_sleep_schedule.txt#1  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Everyone says fix your sleep. Does it actually matter?

The library being open until 2am is a trap. It's a resource, not a schedule.

```

## Sample Answer

**Question:**

**Answer:**

```
(.venv) nithyakondagari@Nithyas-MacBook-Pro-2 ai201-project1-unofficial-guide-starter-v2026 % python app.py ask "What do people think about buying a bike for a 20 minute walking commute?"
  (best distance 0.150, cutoff 0.6)

Based on the provided documents, opinions on getting a bike for the commute are mixed:
- One person notes that a bike cuts an 18-minute walk down to about 6 minutes, but warns that covered bike parking fills up by 9 AM (`thread_bike_commute.txt`).
- Another person keeps a cheap $120 bike to use from September to November and walks the rest of the year (`thread_bike_commute.txt`).
- Another commenter recommends registering the bike for free on campus, which helped them recover their stolen bike (`thread_bike_commute.txt`).
- A counterpoint is offered by someone who sold their bike because winter salt (between November and March) destroys a drivetrain in a single season (`thread_bike_commute.txt`).

Sources retrieved: thread_bike_commute.txt, thread_commuting.txt

1 model calls this session, 602 tokens (436 in, 166 out)
```

**My relevance cutoff:** 0.5. I chose this because the higest best distance for a question in the corpus was still under 0.4, and the lowest best distance for a question that was not in the corpus was above 0.8. I felt that since it was performing well at 0.6, I could decrease it to 0.5 as the best distances for in corpus questions were still atleast 0.1 less.

| Question | In corpus? | Best distance |
| "What do people think about buying a bike for a 20 minute walking commute?" | Yes | 0.150 |
| "What are people saying about whether professors answer email?" | Y | 0.250 |
| "What are people saying about whether it is worth it to fix your sleep schedule?" | Y | 0.281 |
| "Do people say that the edition of a textbook matters?" | Y | 0.382 |
| "What do people say you need during the winter" | Y | 0.398 |
| "What is the capital of Mongolia?" | N | 0.899 |
| "How do I change the oil in a diesel engine?" | N | 0.905 |
| "Who won the 1994 World Cup?" | N | 0.898 |
| "What is the recommended dosage of ibuprofen for a headache?" | N | 0.819 |
| "How do I write a for loop in Rust?" | N | 0.861 |

## How I Used AI
**1.**
I used Claude to write the chunking function and used it to help me come up with the strategy for the algorithm. I also used it to help me understand the function itself. It gave me explanations and a walkthrough of the algorithm. 

**2.**
I used Claude again to help me validate my acceptance criterion and decide if they were measurable or not. It gave me feedback on whether they were good or not. Based on its feedback I either made small tweaks such as adding character lengths or just left them as is.
---

# Unit 2

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->
!!! NOTE: My run log says failed for all of the scorings because of the way I worded my expects during the first week. As a result, the substring method of the scorer does not work the way it is intended to. I used the actual output for each run to evaluate the criterion.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. No chunk is shorter than 60 characters. | 5 of 5| 5/5 | 5/5 | 5/5 | MET |
| 5. When I ask a question that covers a source document with multiple perspectives it shares all of them instead of only giving a few. | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
This text shows the 4th and 5th criterions working for the first question across all 3 runs:
### What do people think about buying a bike for a 20 minute walking commute? — run 1

- Best distance: 0.1497 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt

```
Based on the provided documents, opinions on getting a bike for a 20-minute walking commute include:

* A bike can significantly cut down travel time (reducing an 18-minute walk to about 6 minutes). 
* Some users only use a cheap bike for certain months (like September to November) and walk the rest of the year. 
* Downsides mentioned include storage issues (covered bike parking fills up by 9 am) and weather/maintenance concerns, as salt on the paths between November and March can destroy a drivetrain in a single season. 
* Free campus registration is recommended, as it helped one user recover a stolen bike.

*(Source: thread_bike_commute.txt)*
```

### What do people think about buying a bike for a 20 minute walking commute? — run 2

- Best distance: 0.1497 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt

```
Opinions on getting a bike for a 20-minute walking commute are mixed: one person notes it cuts an 18-minute walk down to about 6 minutes, and another keeps a cheap bike for part of the year. However, a counterpoint mentions selling a bike because winter salt destroys the drivetrain in one season, and another warns that covered bike parking fills up by 9 a.m. 

*(Source: thread_bike_commute.txt)*
```

### What do people think about buying a bike for a 20 minute walking commute? — run 3

- Best distance: 0.1497 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt

```
Opinions vary on getting a bike for a 20-minute walk commute: one person notes it cuts an 18-minute walk down to about 6 minutes, but warns that covered bike parking fills up by 9 AM. Another keeps a cheap bike for September through November, while someone else sold theirs because salt on the paths destroys the drivetrain between November and March. Additionally, one user recommends taking advantage of free campus bike registration, which helped them recover their stolen bike. 

Source: `thread_bike_commute.txt`
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
