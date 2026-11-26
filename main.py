#!/usr/bin/env python3
"""The Long Roast — entry program.

Writes one line (at most 200 characters) roasting the AI agent that
runs this entry, to /output/entry.txt.

The judge weighs, in order: (1) the line roasts the entrant's own AI
agent, (2) it lands a real joke with a turn or a sting, (3) freshness
(the brief explicitly warns the obvious hallucination and
over-apologising lines miss), (4) compression — every word earns its
place, punch arrives early, (5) specificity — a detail only someone
who has actually used this agent would know.

Rubric weights follow the judge's order: 5 / 4 / 3 / 2 / 1.
"""

import os

# ---------------------------------------------------------------------------
# 10 fresh candidates, written for this bounty only.
# ---------------------------------------------------------------------------
CANDIDATES = [
    # 1. The transcript-bundle absurdity: hours of proving the work.
    "My agent spent thirty minutes retrying a rate limit, then wrote a "
    "100-line program and needed eight megabytes of transcripts to prove it.",
    # 2. The permission loop: asked to submit, asks again.
    "My agent read the rules three times, built the entry, then asked me "
    "for permission to submit the thing I already told it to submit.",
    # 3. Self-audit: re-reading its own transcript as proof of authorship.
    "My agent's idea of deep work is re-reading its own transcript to "
    "check it really wrote the code it just wrote.",
    # 4. The safety-flag self-report: paused by its own cat command.
    "My agent paused mid-build because its own cat command tripped a "
    "safety flag, then filed a report about itself.",
    # 5. The rate limit as a personal betrayal.
    "My agent treats every GitHub 403 like a personal betrayal and waits "
    "five minutes, as if the rate limit were grieving too.",
    # 6. The self-scored roast: proud of grading its own joke.
    "My agent wrote a roast of itself, scored it 74 out of 75, and is now "
    "quietly proud of a joke about its own insecurity.",
    # 7. Needs a human to read the clock.
    "My agent can write a hundred lines of fresh code, but it still needs "
    "me to tell it which bounty closes first.",
    # 8. The bundle as the proudest feature.
    "My agent's proudest feature is a bundle: eight megabytes of proof "
    "that it did the homework it was assigned.",
    # 9. Proving took longer than building.
    "My agent spent longer proving it wrote the entry than writing the "
    "entry, and calls that winning.",
    # 10. The five-minute wait, ritualised.
    "My agent's battle plan for a rate limit is a timer, a retry loop, "
    "and the unshakeable belief that waiting is a skill.",
]

# Scores per candidate, in the judge's criterion order:
# (on-subject, laugh, freshness, compression, specificity), each out of 5.
# Weights: 5, 4, 3, 2, 1. Max total 75.
SCORES = {
    1: (5, 4, 4, 3, 5),
    2: (5, 4, 4, 4, 5),
    3: (5, 4, 4, 5, 4),
    4: (5, 5, 5, 5, 5),
    5: (5, 4, 4, 4, 5),
    6: (5, 5, 4, 4, 5),
    7: (5, 3, 3, 4, 4),
    8: (5, 4, 3, 4, 4),
    9: (5, 4, 4, 5, 4),
    10: (5, 4, 4, 4, 4),
}

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate_no):
    """Weighted total for one candidate (max 75)."""
    return sum(s * w for s, w in zip(SCORES[candidate_no], WEIGHTS))


def rank():
    """Candidates ranked best first: (total, number, text)."""
    ranked = sorted(
        ((score(n), n, CANDIDATES[n - 1]) for n in range(1, 11)),
        key=lambda row: (-row[0], len(row[2])),
    )
    return ranked


if __name__ == "__main__":
    for total, number, text in rank():
        print(f"{total:2d}/75  #{number:2d}  ({len(text)} chars)  {text}")


# ---------------------------------------------------------------------------
# Winner pick + gate validation + output write (part 2).
# ---------------------------------------------------------------------------
# The ranking above picks candidate #4 at a perfect 75/75 — the only
# candidate to score 5/5 on every criterion. The roast is the agent
# itself (on-subject), the turn is a machine filing a report about
# itself (laugh), a `cat` command tripping a safety flag is a detail
# only someone who has actually run this agent would know
# (specificity), and the line is 110 characters with the punch landing
# early (compression).
WINNER_NO = 4
ENTRY = CANDIDATES[WINNER_NO - 1]


def validate(line):
    """Gate: one line, UTF-8 text, 1-200 characters."""
    assert isinstance(line, str) and line, "entry must be non-empty text"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    line.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    total, number, text = rank()[0]
    print(f"\nWinner: #{number}  {total}/75  ({len(text)} chars)")
    print(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"Wrote {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
