# Play-Annotation-Generator Annotation Review — Draw_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_6`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 32 | START | 32 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `10` | 35 | START | 47 | 48 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `1` | 35 | START | 35 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `3` | 35 | START | 35 | 120 |
| ✅ EXACT | `Action_PassBlock` | LG | `9` | `8` | 35 | START | 35 | 139 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 46 | END | 32 | 46 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `8` | `7` | 51 | START | 51 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `7` | 98 | START | 98 | 256 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 139 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 51 | 97 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 256 | 159 | inferred_complete_timeline |
| `Action_BallCarry` | 270 | 275 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 92 | 61 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 142 | 41 | inferred_complete_timeline |
| `Action_None` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_None` | 158 | 238 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 139 | 105 | inferred_complete_timeline |
| `Action_None` | 140 | 151 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 139 | 105 | inferred_complete_timeline |
| `Action_None` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_None` | 164 | 187 | 24 | inferred_complete_timeline |
| `Action_None` | 205 | 220 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 99 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 124 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 120 | 86 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 139 | 16 | inferred_complete_timeline |
| `Action_None` | 140 | 155 | 16 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 215 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 148 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 102 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 35 | 4 | inferred_complete_timeline |
| `Action_None` | 42 | 46 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 104 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 112 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 299 | 268 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 15–217 | 183 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 69–102 | 34 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 71–98 | 26 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 120–299 | 164 | 4 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 131–299 | 169 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 131–164 | 33 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 141–155 | 15 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 155–226 | 72 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 163–230 | 46 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 167–203 | 37 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 175–234 | 60 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 215–299 | 32 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 248–299 | 52 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 271–272 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [32–46], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=47.
- ⚠️ Action 'Action_None' range [32-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-220] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [32-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-99] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-270] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-234] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>