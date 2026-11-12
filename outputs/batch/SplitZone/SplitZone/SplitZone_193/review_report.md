# Play-Annotation-Generator Annotation Review — SplitZone_193

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_193`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR1 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 27 | START | 28 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 27 | START | 28 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 27 | START | 28 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 27 | START | 28 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 27 | START | 28 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 27 | START | 28 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 27 | START | 28 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 27 | START | 28 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `23` | `Group` | 27 | START | 44 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 27 | START | 28 | 139 |
| ✅ EXACT | `Action_BallSnap` | WR1 | `3` | `3` | 140 | START | 140 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `0` | `0` | 143 | START | 143 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 143 | START | 143 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 143 | START | 143 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 143 | START | 143 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 143 | START | 143 | 157 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 156 | END | 140 | 156 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 162 | START | 162 | 178 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `19` | `19` | 177 | START | 177 | 194 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `21` | `21` | 179 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 328 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 28–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_SnapReceive` | 140 | 156 | 17 | inferred_complete_timeline |
| `Action_None` | 157 | 161 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 162 | 178 | 17 | inferred_complete_timeline |
| `Action_None` | 179 | 389 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 28–132
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 34 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 51 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 28–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_BallSnap` | 140 | 156 | 17 | inferred_complete_timeline |
| `Action_None` | 157 | 389 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 28–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 389 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 44–389
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 44 | 139 | 96 | inferred_complete_timeline |
| `Action_None` | 140 | 370 | 231 | inferred_complete_timeline |
| `Action_None` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 28–194
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 142 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 176 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 177 | 194 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 28–389
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 142 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 177 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 213 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 328 | 105 | inferred_complete_timeline |
| `Action_None` | 329 | 363 | 35 | inferred_complete_timeline |
| `Action_None` | 368 | 389 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 28–153
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 142 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 153 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 28–389
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 142 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 328 | 172 | inferred_complete_timeline |
| `Action_None` | 329 | 389 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 28–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 142 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 174 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 272 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 328 | 53 | inferred_complete_timeline |
| `Action_None` | 329 | 389 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 28–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 389 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 28–200
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 167 | 28 | inferred_complete_timeline |
| `Action_None` | 183 | 200 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 28–389
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 285 | 146 | inferred_complete_timeline |
| `Action_None` | 332 | 334 | 3 | inferred_complete_timeline |
| `Action_None` | 339 | 351 | 13 | inferred_complete_timeline |
| `Action_None` | 356 | 361 | 6 | inferred_complete_timeline |
| `Action_None` | 369 | 371 | 3 | inferred_complete_timeline |
| `Action_None` | 374 | 389 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 28–389
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 196 | 57 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 389 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 28–223
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 223 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 28–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 245 | 106 | inferred_complete_timeline |
| `Action_None` | 247 | 271 | 25 | inferred_complete_timeline |
| `Action_None` | 273 | 389 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 28–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 389 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 28–179
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 179 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 28–344
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 344 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 28–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 223 | 84 | inferred_complete_timeline |
| `Action_None` | 225 | 280 | 56 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 389 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 28–298
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 139 | 112 | inferred_complete_timeline |
| `Action_None` | 140 | 265 | 126 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 28–389 | 362 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 28–46 | 19 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 147–382 | 232 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 155–184 | 19 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 190–389 | 200 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 194–299 | 104 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 195–389 | 195 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 205–332 | 40 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 220–365 | 142 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 223–389 | 143 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 245–389 | 121 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 300–307 | 8 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 300–389 | 90 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 306–333 | 23 | 4 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 333–389 | 51 | 3 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 374–389 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `21` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 186 frames exceeds threshold 90 frames [start=143, end=328].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 186 frames exceeds threshold 90 frames [start=143, end=328].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 186 frames exceeds threshold 90 frames [start=143, end=328].
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=179, end=132. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [143-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-272] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-344] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-285] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-351] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-223] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-280] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-195] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [197-213] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-220] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-363] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [177-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-51] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-370] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-382] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-389] for track '28' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-229] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-332] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-365] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-302] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-389] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-307] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-318] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-327] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-344] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-365] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>