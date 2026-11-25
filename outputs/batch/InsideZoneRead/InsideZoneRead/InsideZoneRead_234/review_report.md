# Play-Annotation-Generator Annotation Review — InsideZoneRead_234

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_234`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 56
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 37
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `22` | `19` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `22` | `19` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 90 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `17` | 91 | START | 238 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 94 | START | 94 | 161 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `11` | 94 | START | 94 | 165 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 94 | START | 94 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 94 | START | 94 | 165 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 94 | START | 94 | 165 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `22` | `19` | 105 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `22` | `19` | 112 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `22` | `19` | 119 | START | 250 | 250 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `17` | `15` | 134 | START | 217 | 218 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 165 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 198 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 269 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 161 | 68 | inferred_complete_timeline |
| `Action_None` | 168 | 225 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 165 | 72 | inferred_complete_timeline |
| `Action_None` | 166 | 199 | 34 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 165 | 72 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_None` | 173 | 269 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 165 | 72 | inferred_complete_timeline |
| `Action_None` | 166 | 269 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 165 | 72 | inferred_complete_timeline |
| `Action_None` | 166 | 269 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 237 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 269 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 133 | 43 | inferred_complete_timeline |
| `Action_None` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 269 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 160 | 70 | inferred_complete_timeline |
| `Action_None` | 162 | 269 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 166 | 76 | inferred_complete_timeline |
| `Action_None` | 171 | 232 | 62 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 90 | 38 | inferred_complete_timeline |
| `Action_None` | 91 | 237 | 147 | inferred_complete_timeline |
| `Action_None` | 240 | 253 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 165–269 | 105 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 186–269 | 84 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 236–243 | 7 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 238–239 | 2 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 240–258 | 19 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 250–255 | 5 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 91 != Inferred start 238
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `22` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `22` (Position_Unknown)
- ⚠️ `Action_Handoff` for actor_track_id `22` (Position_Unknown): Annotated start 119 != Inferred start 250
- ⚠️ `Action_BallCarry` for actor_track_id `17` (Position_Unknown): Annotated start 134 != Inferred start 217

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=238, end=105. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '19' has invalid range: start=250, end=105. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '19' has invalid range: start=250, end=118. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '19' has invalid range: start=250, end=133. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [94-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-30] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-44] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-269] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-218] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 239, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [239-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 251, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [251-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '19' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_234'; source metadata written as null.

</details>