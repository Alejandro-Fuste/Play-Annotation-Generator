# Play-Annotation-Generator Annotation Review — Counter_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_84`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 247 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `18` | `17` | 212 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | LT | `11` | `10` | 212 | START | 212 | 297 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 212 | START | 212 | 229 |
| ✅ EXACT | `Action_PullBlock` | C | `18` | `17` | 212 | START | 212 | 298 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `5` | `4` | 212 | START | 212 | 235 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 223 | END | 212 | 223 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 233 | START | 233 | 249 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `8` | `7` | 250 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 298 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_SnapReceive` | 212 | 223 | 12 | inferred_complete_timeline |
| `Action_None` | 224 | 232 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 233 | 249 | 17 | inferred_complete_timeline |
| `Action_None` | 250 | 336 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_None` | 212 | 246 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 117 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 211 | 78 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 212 | 235 | 24 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 238 | 298 | 61 | inferred_complete_timeline |
| `Action_None` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_DownBlock` | 212 | 297 | 86 | inferred_complete_timeline |
| `Action_None` | 303 | 312 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 211 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 212 | 229 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 253 | 298 | 46 | inferred_complete_timeline |
| `Action_None` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 211 | 101 | inferred_complete_timeline |
| `Action_PullBlock` | 212 | 298 | 87 | inferred_complete_timeline |
| `Action_None` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_None` | 212 | 287 | 76 | inferred_complete_timeline |
| `Action_None` | 289 | 359 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 211 | 74 | inferred_complete_timeline |
| `Action_None` | 212 | 289 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_None` | 212 | 359 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 152 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_None` | 212 | 335 | 124 | inferred_complete_timeline |
| `Action_None` | 337 | 359 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_None` | 212 | 359 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_None` | 212 | 359 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–130 | 41 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 7–37 | 27 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 118–122 | 5 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 119–359 | 157 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 157–359 | 134 | 8 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 187–355 | 154 | 5 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 223–234 | 12 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 230–323 | 84 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 257–337 | 81 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 270–359 | 90 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 305–359 | 55 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 319–359 | 41 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 338–359 | 22 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 349–359 | 8 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `18` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=250, end=247. Clamping end to start.
- ⚠️ Overlapping action conflict at frame 212 for track '17': 'Action_BallSnap' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-287] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-289] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [212-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-335] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [212-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-312] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-336] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [212-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [212-298] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-280] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-211] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-283] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-355] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-234] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-323] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-337] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>