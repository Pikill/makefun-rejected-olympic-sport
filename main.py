# Rejected Olympic Sports — one-line entry writer.
#
# The line was chosen by scoring every draft against the judge brief's
# five criteria in priority order (funny rejected sport, twist lands in
# one read, broadcaster-plausible, no wasted words, quotable). The
# highest-scoring draft wins; ties break toward the shorter text, then
# the earlier draft, matching the contest's own tie-break order.
#
# One-variable eval loop on the winner: "stand in line" -> "queue"
# kept the 23/25 score and cut 8 characters (127 -> 119), which helps
# the smaller-text tie-break. Two other single changes were tried and
# reverted: "four hours" -> "six hours" (no score gain) and
# "for impatience" -> "for rushing" (22/25, weaker punchline).

import os

# (text, c1, c2, c3, c4, c5) — criteria scored out of 5 each.
DRAFTS = [
    (
        "Competitive queueing: eight athletes queue for four hours. "
        "The first to reach the front is disqualified for impatience.",
        5, 5, 4, 5, 4,
    ),
    (
        "Competitive sleeping: athletes sleep for eight hours before a "
        "live audience. The gold medallist is still asleep.",
        4, 5, 4, 5, 4,
    ),
    (
        "Extreme ironing: competitors iron shirts on a cliff edge, in a "
        "kayak, during a storm. Judges deduct points for creases, not "
        "for drowning.",
        4, 5, 4, 4, 4,
    ),
    (
        "Synchronised napping: two athletes, one duvet, judged on how "
        "little they move. The gold went to a man asleep since Tuesday.",
        4, 4, 4, 4, 4,
    ),
    (
        "Underwater basket weaving: divers weave baskets at the bottom "
        "of the pool. The event was dropped when every basket floated "
        "away.",
        4, 4, 3, 4, 3,
    ),
]


def total(draft):
    """Sum of the five criterion scores for one draft."""
    return sum(draft[1:])


def pick(drafts):
    """Best draft: highest total, then fewest characters, then earliest."""
    ranked = sorted(drafts, key=lambda d: (-total(d), len(d[0]), drafts.index(d)))
    return ranked[0][0]


def main():
    line = pick(DRAFTS)
    if not (1 <= len(line) <= 200) or not line.strip():
        raise SystemExit("chosen line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
