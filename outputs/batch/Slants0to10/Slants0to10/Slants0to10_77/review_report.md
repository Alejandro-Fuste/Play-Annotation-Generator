# Play-Annotation-Generator Annotation Review — Slants0to10_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_77`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 47
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 12 | START | 12 | 27 |
| ✅ EXACT | `Action_PassBlock` | LT | `11` | `11` | 15 | START | 15 | 239 |
| ✅ EXACT | `Action_PassBlock` | LG | `16` | `16` | 15 | START | 15 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 15 | START | 28 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 15 | START | 15 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 15 | START | 15 | 52 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `3` | `3` | 27 | START | 27 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 27 | END | 12 | 27 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 61 | START | 61 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `3` | 93 | START | 93 | 189 |

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
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 27 | 16 | inferred_complete_timeline |
| `Action_None` | 28 | 60 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 61 | 70 | 10 | inferred_complete_timeline |
| `Action_None` | 71 | 131 | 61 | inferred_complete_timeline |
| `Action_None` | 135 | 239 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 27 | 88 | 62 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 189 | 97 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 40 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 27 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 40 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 44 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 111 | 97 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 52 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 239 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 62 | 51 | inferred_complete_timeline |
| `Action_None` | 64 | 76 | 13 | inferred_complete_timeline |
| `Action_None` | 80 | 238 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_None` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 204 | 193 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 155 | 144 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–198 | 199 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 39–109 | 71 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 95–239 | 145 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 120–239 | 120 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 171–239 | 68 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 197–199 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [12–27], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=28.
- ⚠️ Action 'Action_BallCarry' range [93-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-113] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-131] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-198] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-155] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-40] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-111] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>