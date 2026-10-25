# Play-Annotation-Generator Annotation Review — BootPass_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `18` | `18` | 25 | START | 25 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `15` | `15` | 33 | START | 33 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `18` | `18` | 33 | START | 42 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `19` | `19` | 33 | START | 33 | 77 |
| ✅ EXACT | `Action_RunBlock` | LT | `20` | `20` | 33 | START | 33 | 52 |
| ✅ EXACT | `Action_RunBlock` | RT | `9` | `9` | 33 | START | 33 | 88 |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | `0` | `0` | 41 | START | 41 | 133 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 41 | END | 25 | 41 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `10` | `10` | 48 | START | 48 | 59 |
| ✅ EXACT | `Action_BootAway` | QB | `10` | `10` | 62 | START | 62 | 98 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 103 | START | 103 | 114 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 134 | START | 134 | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_FakeHandoff` | 48 | 59 | 12 | inferred_complete_timeline |
| `Action_BootAway` | 62 | 98 | 37 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 103 | 114 | 12 | inferred_complete_timeline |
| `Action_None` | 115 | 141 | 27 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 224 | 200 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 41 | 133 | 93 | inferred_complete_timeline |
| `Action_SecureCatch` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_None` | 142 | 207 | 66 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 45 | 21 | inferred_complete_timeline |
| `Action_None` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 59 | 178 | 120 | inferred_complete_timeline |
| `Action_None` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 158 | 134 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 33 | 52 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 33 | 77 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 93 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 101 | 129 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 137 | 182 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 42 | 64 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 33 | 133 | 101 | inferred_complete_timeline |
| `Action_RunBlock` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 142 | 161 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 169 | 181 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 206 | 227 | 22 | inferred_complete_timeline |
| `Action_RunBlock` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 33 | 88 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 80 | 56 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 54 | 30 | inferred_complete_timeline |
| `Action_None` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 142 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 60 | 36 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 68 | 135 | 68 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–239 | 239 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–239 | 237 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 3–239 | 201 | 12 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 98–180 | 82 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 143–239 | 89 | 4 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 146–239 | 93 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 183–190 | 7 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 203–239 | 35 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 211–239 | 19 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 221–235 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 28: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [25–41], lower_priority='Action_RunBlock' annotated_start=33, effective_Action_RunBlock_start=42.
- ⚠️ Action 'Action_None' range [142-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-54] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-178] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-135] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [33-88] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [48-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [33-133] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [136-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [142-161] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [169-181] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [206-227] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [230-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-229] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [25-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [42-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [72-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [33-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [80-93] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [101-129] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [134-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [137-182] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [33-52] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-16] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-188] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-163] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-227] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>