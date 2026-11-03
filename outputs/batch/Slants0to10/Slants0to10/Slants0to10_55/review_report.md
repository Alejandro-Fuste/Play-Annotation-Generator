# Play-Annotation-Generator Annotation Review — Slants0to10_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_55`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 144
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 125
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_RunSlantRoute` | WR4 | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 1 | START | 1 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 4 | START | 15 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 4 | START | 4 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 4 | START | 4 | 44 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 4 | START | 4 | 299 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 14 | END | 1 | 14 |
| ✅ EXACT | `Action_RunSlantRoute` | WR4 | `7` | `7` | 18 | START | 18 | 79 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 53 | START | 53 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | `7` | `7` | 92 | START | 92 | 216 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 14 | 14 | inferred_complete_timeline |
| `Action_None` | 15 | 52 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 53 | 63 | 11 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 143 | 143 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 203 | 22 | inferred_complete_timeline |
| `Action_None` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 134 | 134 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 241 | 241 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 18 | 79 | 62 | inferred_complete_timeline |
| `Action_None` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 216 | 125 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 235 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 299 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 14 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 51 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 44 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 66 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 77 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 75 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 90 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 188 | 188 | inferred_complete_timeline |
| `Action_None` | 194 | 199 | 6 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 165 | 165 | inferred_complete_timeline |
| `Action_None` | 168 | 234 | 67 | inferred_complete_timeline |
| `Action_None` | 236 | 279 | 44 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 226 | 226 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 169 | 169 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 176 | 268 | 93 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 131 | 131 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 132 | 132 | inferred_complete_timeline |
| `Action_None` | 134 | 299 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–299 | 295 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 64–299 | 236 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 70–299 | 171 | 9 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 85–299 | 208 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 87–118 | 30 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 96–127 | 28 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 145–148 | 4 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 150–299 | 147 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 151–299 | 149 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 156–299 | 144 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 167–288 | 27 | 6 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 172–291 | 67 | 5 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 185–299 | 29 | 11 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 213–223 | 8 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 249–299 | 47 | 4 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 250–299 | 47 | 3 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 258–292 | 24 | 4 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 261–264 | 4 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 294–299 | 4 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [1–14], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=15.
- ⚠️ Action 'Action_None' range [1-134] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-241] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-299] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-132] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-216] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-235] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-268] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-188] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-226] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-44] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-66] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-77] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-96] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-154] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-187] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-239] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-276] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-284] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-213] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-244] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-266] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-292] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-282] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>