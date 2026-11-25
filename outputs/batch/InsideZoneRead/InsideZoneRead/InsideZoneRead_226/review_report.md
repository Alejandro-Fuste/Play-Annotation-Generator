# Play-Annotation-Generator Annotation Review — InsideZoneRead_226

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_226`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `23` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | LB2 | defense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | LB2 | defense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | LB2 | defense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RT | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 4 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `23` | `18` | 5 | START | 203 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 8 | START | 8 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 8 | START | 8 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 8 | START | 8 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `1` | 8 | START | 8 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 8 | START | 8 | 47 |
| ✅ EXACT | `Action_SnapReceive` | LB2 | `14` | `13` | 21 | END | 5 | 21 |
| ✅ EXACT | `Action_ReadDefender` | LB2 | `14` | `13` | 26 | START | 26 | 37 |
| ✅ EXACT | `Action_Handoff` | LB2 | `14` | `13` | 38 | START | 38 | 47 |
| ✅ EXACT | `Action_BallCarry` | RT | `5` | `4` | 48 | START | 48 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 80 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 137 | 133 | inferred_complete_timeline |
| `Action_None` | 142 | 184 | 43 | inferred_complete_timeline |
| `Action_None` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 193 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 80 | 73 | inferred_complete_timeline |
| `Action_None` | 81 | 195 | 115 | inferred_complete_timeline |
| `Action_None` | 202 | 299 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 80 | 73 | inferred_complete_timeline |
| `Action_None` | 81 | 134 | 54 | inferred_complete_timeline |
| `Action_None` | 138 | 288 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 50 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 80 | 29 | inferred_complete_timeline |
| `Action_None` | 81 | 106 | 26 | inferred_complete_timeline |
| `Action_None` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 80 | 73 | inferred_complete_timeline |
| `Action_None` | 81 | 199 | 119 | inferred_complete_timeline |
| `Action_None` | 207 | 260 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 47 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 48 | 299 | 252 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 284 | 280 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 194 | 190 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 13 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 145 | 141 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 21 | 17 | inferred_complete_timeline |
| `Action_None` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 26 | 37 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_None` | 48 | 131 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 136 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 286 | 282 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 114–150 | 26 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 146–299 | 141 | 4 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 167–219 | 53 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 178–243 | 56 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 203–299 | 97 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 215–299 | 85 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 229–249 | 21 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 263–298 | 36 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 269–299 | 31 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `23` (Position_Unknown): Annotated start 5 != Inferred start 203
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 34 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=203, end=21. Clamping end to start.
- ⚠️ Action 'Action_None' range [81-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-199] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-286] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [5-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-219] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-298] for track '21' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_226'; source metadata written as null.

</details>