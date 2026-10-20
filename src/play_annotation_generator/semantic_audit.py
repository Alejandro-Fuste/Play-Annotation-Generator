"""
Semantic Action Alias Audit Table for Play-Annotation-Generator.
Tracks classifications and rationale for approximate/inferred action mappings.
"""

from typing import Dict, List, TypedDict


class SemanticAliasEntry(TypedDict):
    source_header: str
    mapped_canonical_action: str
    classification: str  # EXACT, INTENTIONAL_ALIAS, NEEDS_SOURCE_REVIEW
    reason: str


SEMANTIC_ACTION_ALIAS_AUDIT: List[SemanticAliasEntry] = [
    {
        "source_header": "Press Interior Gap",
        "mapped_canonical_action": "Action_PressGap",
        "classification": "EXACT",
        "reason": (
            "Exact functional synonym. Actions.json defines Action_PressGap as the ball carrier "
            "pressing directly into a designated gap in the offensive line."
        ),
    },
    {
        "source_header": "Pass Drop",
        "mapped_canonical_action": "Action_FakePassDroptoHandoff",
        "classification": "INTENTIONAL_ALIAS",
        "reason": (
            "In Draw plays (Draw_1), the quarterback takes pass drop steps to simulate a pass play "
            "before handing off. Matches Action_FakePassDroptoHandoff definition in actions.json."
        ),
    },
    {
        "source_header": "Clear Out Route",
        "mapped_canonical_action": "Action_ClearToEdge",
        "classification": "INTENTIONAL_ALIAS",
        "reason": (
            "Actions.json defines Action_ClearToEdge as receiver route movement to draw defenders away "
            "and create space in the middle of the field for another offensive player (Dagger_1 clear-out)."
        ),
    },
    {
        "source_header": "Dig Route",
        "mapped_canonical_action": "Action_BreakInside",
        "classification": "INTENTIONAL_ALIAS",
        "reason": (
            "Actions.json defines Action_BreakInside explicitly as changing direction from stem toward "
            "the inside of the field, specifically noting 'as used on slants, digs, posts' (Dagger_1 dig)."
        ),
    },
    {
        "source_header": "Sell Slant",
        "mapped_canonical_action": "Action_SellRoute",
        "classification": "INTENTIONAL_ALIAS",
        "reason": (
            "Actions.json defines Action_SellRoute as initially running a deceptive fake route to make "
            "the defender anticipate a different break (used in SlantAndGo_1 double move)."
        ),
    },
    {
        "source_header": "Run Go Route",
        "mapped_canonical_action": "Action_VerticalStem",
        "classification": "INTENTIONAL_ALIAS",
        "reason": (
            "Actions.json defines Action_VerticalStem as running vertically upfield to threaten depth "
            "and establish leverage (used in SlantAndGo_1 and OutAndUp_1)."
        ),
    },
    {
        "source_header": "Onside Kick",
        "mapped_canonical_action": "Action_KickBall",
        "classification": "INTENTIONAL_ALIAS",
        "reason": (
            "Actions.json defines Action_KickBall as striking the football to initiate a kickoff, free kick, "
            "or legal kicking play. Captures kicker striking the onside kick in OnsideKickRecovery."
        ),
    },
]


def get_alias_audit_map() -> Dict[str, SemanticAliasEntry]:
    return {entry["source_header"].lower().strip(): entry for entry in SEMANTIC_ACTION_ALIAS_AUDIT}
