# Play-Annotation-Generator Annotation Review — Slants0to10_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_41`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 1 | START | 1 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `11` | 4 | START | 4 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 4 | START | 17 | 25 |
| ✅ EXACT | `Action_PassBlock` | RG | `17` | `17` | 4 | START | 4 | 284 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 4 | START | 4 | 13 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 4 | START | 4 | 255 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `12` | `12` | 16 | START | 16 | 60 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 16 | END | 1 | 16 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 50 | START | 50 | 58 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `12` | `12` | 79 | START | 79 | 299 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 16 | 16 | inferred_complete_timeline |
| `Action_None` | 17 | 49 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_None` | 59 | 68 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 40 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 16 | 60 | 45 | inferred_complete_timeline |
| `Action_None` | 61 | 78 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 299 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 167 | 167 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 255 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 13 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 103 | 83 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 113 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 279 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 16 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 25 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 122 | 96 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 267 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 284 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 28 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 66 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 257 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 39 | 39 | inferred_complete_timeline |
| `Action_None` | 42 | 257 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 71 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 279 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 131 | 131 | inferred_complete_timeline |
| `Action_None` | 133 | 299 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 50 | 50 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 80 | 80 | inferred_complete_timeline |
| `Action_None` | 82 | 89 | 8 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 237 | 237 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 105 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

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
<summary>CB4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 249 | 249 | inferred_complete_timeline |
| `Action_None` | 251 | 267 | 17 | inferred_complete_timeline |
| `Action_None` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

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

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 73–106 | 34 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 74–265 | 182 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 101–202 | 95 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 108–299 | 192 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 109–273 | 165 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 118–265 | 143 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 130–250 | 120 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 194–196 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 217–263 | 10 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 222–224 | 3 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [1–16], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=17.
- ⚠️ Action 'Action_None' range [1-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-249] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-28] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-257] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-122] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-279] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-13] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-279] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-249] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-202] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-273] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-243] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>