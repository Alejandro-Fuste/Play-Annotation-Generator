# Play-Annotation-Generator Annotation Review — OutsideZoneRead_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_99`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_Keep` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 2 | START | 2 | 16 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 5 | START | 5 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 5 | START | 5 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 5 | START | 5 | 51 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `21` | 5 | START | 17 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 5 | START | 5 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 16 | END | 2 | 16 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `16` | `15` | 19 | START | 19 | 37 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `20` | `19` | 28 | START | 28 | 86 |
| ✅ EXACT | `Action_Keep` | QB | `16` | `15` | 38 | START | 38 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `16` | `15` | 52 | START | 52 | 106 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_None` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 19 | 37 | 19 | inferred_complete_timeline |
| `Action_Keep` | 38 | 51 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 52 | 106 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 150 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 71 | 70 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 122 | 121 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 73 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 86 | 82 | inferred_complete_timeline |
| `Action_None` | 87 | 134 | 48 | inferred_complete_timeline |
| `Action_None` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 86 | 70 | inferred_complete_timeline |
| `Action_None` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 51 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 27 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 28 | 86 | 59 | inferred_complete_timeline |
| `Action_None` | 87 | 150 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 57 | 56 | inferred_complete_timeline |
| `Action_None` | 70 | 124 | 55 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 29 | 28 | inferred_complete_timeline |
| `Action_None` | 50 | 150 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 43 | 42 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 103 | 102 | inferred_complete_timeline |
| `Action_None` | 108 | 144 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 62 | 61 | inferred_complete_timeline |
| `Action_None` | 67 | 150 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 124 | 123 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 133 | 132 | inferred_complete_timeline |
| `Action_None` | 136 | 145 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 33–132 | 94 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 56–150 | 90 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 74–150 | 77 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 77–97 | 6 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 108–123 | 9 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 117–136 | 20 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 117–150 | 34 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 132–150 | 19 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 132–150 | 15 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 144–150 | 7 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 5 != Inferred start 17
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [2–16], lower_priority='Action_ZoneBlock' annotated_start=5, effective_Action_ZoneBlock_start=17.
- ⚠️ Action 'Action_None' range [2-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-43] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-133] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-51] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-63] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-129] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-136] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-150] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-143] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>