# Play-Annotation-Generator Annotation Review — Counter_393

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_393`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | defense | `21` | `18` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `22` | `19` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 56 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 111 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 69 | START | 69 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 72 | START | 86 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | `21` | `18` | 72 | START | 72 | 90 |
| ✅ EXACT | `Action_DownBlock` | LT | `22` | `19` | 72 | START | 72 | 89 |
| ✅ EXACT | `Action_PullBlock` | RG | `18` | `17` | 72 | START | 72 | 94 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `16` | `15` | 72 | START | 72 | 94 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 85 | END | 69 | 85 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 93 | START | 93 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 112 | START | 112 | 169 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 163 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_SnapReceive` | 69 | 85 | 17 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_None` | 112 | 269 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 169 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 191 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 220 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 232 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 193 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 269 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 269 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 68 | 21 | inferred_complete_timeline |
| `Action_None` | 69 | 102 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 56–89
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 56 | 71 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 72 | 89 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_BallSnap` | 69 | 85 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 71 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 72 | 94 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 71 | 24 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 72 | 94 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `23`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 56–153
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 56 | 68 | 13 | inferred_complete_timeline |
| `Action_None` | 69 | 94 | 26 | inferred_complete_timeline |
| `Action_None` | 131 | 148 | 18 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 68 | 18 | inferred_complete_timeline |
| `Action_None` | 69 | 86 | 18 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 148 | 18 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 52–269
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 72 | 90 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 153 | 20 | inferred_complete_timeline |
| `Action_None` | 221 | 232 | 12 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 98 | 30 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 94 | 26 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 138 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 108 | 40 | inferred_complete_timeline |
| `Action_None` | 110 | 135 | 26 | inferred_complete_timeline |
| `Action_None` | 138 | 145 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 191 | 123 | inferred_complete_timeline |
| `Action_None` | 193 | 269 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 269 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 269 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 243 | 175 | inferred_complete_timeline |
| `Action_None` | 256 | 259 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–103 | 57 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 56–90 | 34 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 122–269 | 129 | 7 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 123–141 | 17 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 141–269 | 99 | 8 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 143–148 | 6 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 146–191 | 43 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 181–193 | 13 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 184–269 | 86 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 202–206 | 4 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 210–269 | 60 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 212–214 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 215–261 | 26 | 5 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 219–269 | 51 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 237–243 | 7 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 254–269 | 16 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 255–267 | 13 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 255–269 | 15 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 259–269 | 9 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 788: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ Row 788: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [69–85], lower_priority='Action_DownBlock' annotated_start=72, effective_Action_DownBlock_start=86.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (DT2) duration 92 frames exceeds threshold 90 frames [start=72, end=163].
- ⚠️ Action 'Action_None' range [69-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-169] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-220] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-30] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-68] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-102] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-138] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [72-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-148] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [72-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [72-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-153] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [72-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-94] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-148] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-199] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-228] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-174] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-161] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-191] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-228] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-267] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>