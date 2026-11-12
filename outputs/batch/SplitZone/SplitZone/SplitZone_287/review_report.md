# Play-Annotation-Generator Annotation Review — SplitZone_287

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_287`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `17` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | `10` | `10` | 70 | START | 70 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `7` | 75 | START | 75 | 88 |
| ✅ EXACT | `Action_SplitBlock` | TE | `14` | `14` | 81 | START | 81 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 82 | START | 82 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 82 | START | 82 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 82 | START | 82 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 82 | START | 82 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `7` | 82 | START | 89 | 114 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 88 | END | 75 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `15` | 113 | START | 113 | 162 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 120 | START | 120 | 125 |

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
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PressEdge` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_PressEdge` | 89 | 119 | 31 | inferred_complete_timeline |
| `Action_Handoff` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_PressEdge` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_None` | 130 | 177 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–402
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 162 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 187 | 385 | 199 | inferred_complete_timeline |
| `Action_BallCarry` | 388 | 399 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 401 | 402 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_None` | 75 | 90 | 16 | inferred_complete_timeline |
| `Action_None` | 108 | 126 | 19 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 155 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SplitBlock` | 81 | 113 | 33 | inferred_complete_timeline |
| `Action_None` | 114 | 163 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 121 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 160 | 37 | inferred_complete_timeline |
| `Action_None` | 161 | 194 | 34 | inferred_complete_timeline |
| `Action_None` | 201 | 354 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 103 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_BallSnap` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 114 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 158 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 92 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 157 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 97 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 157 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 74 | 15 | inferred_complete_timeline |
| `Action_None` | 75 | 108 | 34 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 100 | 26 | inferred_complete_timeline |
| `Action_None` | 108 | 154 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 112 | 38 | inferred_complete_timeline |
| `Action_None` | 120 | 180 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 158 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 419 | 345 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 150 | 76 | inferred_complete_timeline |
| `Action_None` | 155 | 163 | 9 | inferred_complete_timeline |
| `Action_None` | 168 | 419 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 146 | 72 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 128 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 128 | 54 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 30–419 | 284 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 52–150 | 57 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 85–86 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 93–132 | 40 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 118–198 | 51 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 123–150 | 28 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 155–364 | 209 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 161–419 | 259 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 165–419 | 255 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 213–313 | 90 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 215–224 | 4 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 224–281 | 58 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 238–330 | 84 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 248–419 | 172 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 288–294 | 4 | 2 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 348–419 | 72 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 353–371 | 12 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 392–398 | 6 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 392–394 | 3 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 400–419 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [75–88], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=89.
- ⚠️ Action 'Action_None' range [75-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-354] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-114] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-158] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-154] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [81-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-162] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [187-385] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [388-399] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [401-402] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-126] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-347] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-364] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-231] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-301] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-313] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-362] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-394] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>