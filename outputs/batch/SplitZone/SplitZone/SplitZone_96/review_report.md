# Play-Annotation-Generator Annotation Review — SplitZone_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_96`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `25` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 33 | START | 33 | 42 |
| ⚠️ START CHANGED | `Action_SplitBlock` | Position_Unknown | `25` | `17` | 34 | START | 128 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 36 | START | 43 | 88 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 36 | START | 36 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 36 | START | 36 | 58 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 36 | START | 36 | 136 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 36 | START | 36 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 42 | END | 33 | 42 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 45 | START | 45 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 58 | START | 58 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `3` | `3` | 59 | START | 59 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 136 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 42 | 10 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 45 | 57 | 13 | inferred_complete_timeline |
| `Action_None` | 58 | 144 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 261 | 186 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 186 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 59 | 110 | 52 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 112 | 133 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 136 | 136 | 1 | inferred_complete_timeline |
| `Action_None` | 137 | 236 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 136 | 101 | inferred_complete_timeline |
| `Action_None` | 137 | 222 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_BallSnap` | 33 | 42 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 88 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 136 | 39 | inferred_complete_timeline |
| `Action_None` | 137 | 144 | 8 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 136 | 101 | inferred_complete_timeline |
| `Action_None` | 137 | 197 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 94 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 74 | 42 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 194 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 88 | 56 | inferred_complete_timeline |
| `Action_None` | 94 | 104 | 11 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 47 | 15 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_None` | 112 | 125 | 14 | inferred_complete_timeline |
| `Action_None` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 108 | 76 | inferred_complete_timeline |
| `Action_None` | 115 | 262 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 79 | 47 | inferred_complete_timeline |
| `Action_None` | 81 | 269 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 269 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 269 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `21` | Position_Unknown | Team_Unknown | 106–269 | 164 | 1 | Undefined position; Undefined team |
| `16` | `24` | Position_Unknown | Team_Unknown | 125–269 | 145 | 1 | Undefined position; Undefined team |
| `17` | `25` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 129–180 | 52 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 150–269 | 120 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 153–218 | 66 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 155–269 | 115 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 258–265 | 8 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_SplitBlock` for actor_track_id `25` (Position_Unknown): Annotated start 34 != Inferred start 128
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 101 frames exceeds threshold 90 frames [start=36, end=136].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LG) duration 101 frames exceeds threshold 90 frames [start=36, end=136].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 101 frames exceeds threshold 90 frames [start=36, end=136].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [33–42], lower_priority='Action_ZoneBlock' annotated_start=36, effective_Action_ZoneBlock_start=43.
- ⚠️ Action 'Action_None' range [33-79] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-269] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [59-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [112-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-194] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-88] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [128-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '23' has 1 frames without a visible bounding box.
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

</details>