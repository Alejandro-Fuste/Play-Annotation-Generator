# Play-Annotation-Generator Annotation Review — SplitZone_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_94`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 107 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 105 | START | 105 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `13` | `13` | 108 | START | 108 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 108 | START | 108 | 126 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `12` | `12` | 108 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 108 | START | 108 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `4` | 108 | START | 108 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 108 | START | 108 | 194 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 114 | END | 105 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `2` | 116 | START | 116 | 133 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `10` | 134 | START | 134 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 194 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_SnapReceive` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_None` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 134 | 204 | 71 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_SplitBlock` | 108 | 166 | 59 | inferred_complete_timeline |
| `Action_SplitBlock` | 169 | 194 | 26 | inferred_complete_timeline |
| `Action_None` | 195 | 217 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 126 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 232 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 143 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 157 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 185 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_BallSnap` | 105 | 110 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 127 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 150 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_None` | 222 | 237 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 194 | 87 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 203 | 99 | inferred_complete_timeline |
| `Action_None` | 209 | 239 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 217 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 152 | 48 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 234 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 185 | 81 | inferred_complete_timeline |
| `Action_None` | 188 | 196 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 58–151 | 48 | 6 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 108–153 | 24 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 182–222 | 40 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 195–235 | 35 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 195–239 | 37 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 197–230 | 34 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [105–110], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=111.
- ⚠️ Action 'Action_None' range [105-217] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-127] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-183] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-234] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [105-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [108-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-128] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-239] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-222] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-235] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-230] for track '22' has 1 frames without a visible bounding box.
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