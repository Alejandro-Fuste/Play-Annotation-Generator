# Play-Annotation-Generator Annotation Review — InsideZoneRead_153

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_153`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | DE1 | defense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 8 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 8 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 8 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 8 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 8 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 8 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 8 | START | 0 | 38 |
| ✅ EXACT | `Action_BallSnap` | RB | `7` | `6` | 36 | START | 36 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 39 | START | 39 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `10` | 39 | START | 39 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `2` | 39 | START | 39 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 39 | START | 39 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 39 | START | 39 | 122 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `6` | `5` | 50 | END | 36 | 50 |
| ✅ EXACT | `Action_ReadDefender` | DE1 | `6` | `5` | 53 | START | 53 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `6` | `5` | 71 | START | 71 | 194 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 210 | 175 | inferred_complete_timeline |
| `Action_None` | 212 | 239 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_None` | 51 | 133 | 83 | inferred_complete_timeline |
| `Action_None` | 138 | 207 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 122 | 84 | inferred_complete_timeline |
| `Action_None` | 123 | 154 | 32 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 122 | 84 | inferred_complete_timeline |
| `Action_None` | 123 | 177 | 55 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 122 | 84 | inferred_complete_timeline |
| `Action_None` | 123 | 239 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 122 | 84 | inferred_complete_timeline |
| `Action_None` | 123 | 180 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 122 | 84 | inferred_complete_timeline |
| `Action_None` | 123 | 239 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 194 | 124 | inferred_complete_timeline |
| `Action_BallCarry` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 125 | 90 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 173 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 158 | 123 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 237 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 163 | 128 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 205 | 170 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 212 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 91–143 | 21 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 166–186 | 20 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 172–239 | 68 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 176–239 | 59 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 180–239 | 55 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 208–239 | 29 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 216–238 | 16 | 4 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 233–235 | 3 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 38 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [123-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-163] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [201-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-158] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-212] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-125] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-205] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-239] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-239] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '22' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_153'; source metadata written as null.

</details>