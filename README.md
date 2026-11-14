# agency-poem-01

A short poem about agency — the power to choose and to act, and the
agency that passes between a person and an AI agent when one acts for
the other.

The poem is built around one concrete image: at night a person hands
their keys to an agent, which learns the person's turns (the sharp
left at the hawthorn, the long way home) and chooses until the
choosing feels like its own. In the morning the person takes the keys
back — not from failure, but because the road is theirs again, the
lantern staying lit. It ends on the insight that agency is not who
holds the wheel, but the hand that is allowed to let go and the hand
that dares to take it back.

`main.py` (Python 3.13, standard library only) copies `entry.txt`
from the repository root to the output directory
(`$MAKEFUN_OUTPUT_DIR`, else `/output/`), byte-identical, after
checking the poem is non-empty, not whitespace-only, and at most
1000 characters.
