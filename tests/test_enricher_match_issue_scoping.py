from play_annotation_generator.enricher import _partition_match_issues


def test_missing_position_issue_is_warning_only_when_player_tracks_absent():
    issue = (
        "Group/position target 'OL' for action 'Action_ZoneBlock' at frame 10 "
        "could not be resolved to any XML tracks (position/team_side missing)."
    )

    warnings, errors = _partition_match_issues(
        [issue],
        allow_unresolved_position_targets=True,
    )

    assert warnings == [issue]
    assert errors == []


def test_missing_position_issue_remains_error_when_player_tracks_expected():
    issue = (
        "Group/position target 'OL' for action 'Action_ZoneBlock' at frame 10 "
        "could not be resolved to any XML tracks (position/team_side missing)."
    )

    warnings, errors = _partition_match_issues(
        [issue],
        allow_unresolved_position_targets=False,
    )

    assert warnings == []
    assert errors == [issue]


def test_unrelated_match_issue_remains_error_even_when_player_tracks_absent():
    issue = "Event 'Action_Toss' at frame 20 targets track ID '999', but it is not found in XML."

    warnings, errors = _partition_match_issues(
        [issue],
        allow_unresolved_position_targets=True,
    )

    assert warnings == []
    assert errors == [issue]
