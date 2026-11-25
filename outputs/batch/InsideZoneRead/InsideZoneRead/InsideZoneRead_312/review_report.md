# Play-Annotation-Generator Annotation Review — InsideZoneRead_312

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_312`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ⚠️ END CHANGED | `Action_SnapReceive` | DE2 | defense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | DE2 | defense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_Keep` | DE2 | defense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 18 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `19` | 16 | START | 56 | 56 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 19 | START | 19 | 93 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 19 | START | 19 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 19 | START | 19 | 46 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 19 | START | 19 | 93 |
| ⚠️ END CHANGED | `Action_SnapReceive` | DE2 | `8` | `7` | 26 | END | 16 | 19 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | DE2 | `8` | `7` | 33 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | DE2 | `8` | `7` | 44 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | `8` | `7` | 61 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 93 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 206 | 191 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_None` | 53 | 186 | 134 | inferred_complete_timeline |
| `Action_None` | 190 | 201 | 12 | inferred_complete_timeline |
| `Action_None` | 203 | 231 | 29 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 95 | 80 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 158 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_None` | 105 | 209 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 93 | 75 | inferred_complete_timeline |
| `Action_None` | 94 | 94 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 93 | 75 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 93 | 75 | inferred_complete_timeline |
| `Action_None` | 94 | 239 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 46 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 92 | 44 | inferred_complete_timeline |
| `Action_None` | 94 | 109 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 19 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 71 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_None` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_None` | 32 | 145 | 114 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 128 | 113 | inferred_complete_timeline |
| `Action_None` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_None` | 156 | 181 | 26 | inferred_complete_timeline |
| `Action_None` | 183 | 209 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 88 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 5–38 | 34 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 11–235 | 222 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 28–105 | 60 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 39–108 | 28 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 56–108 | 44 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 67–233 | 156 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 93–239 | 147 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 108–239 | 132 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 120–239 | 102 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 136–239 | 88 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 168–239 | 59 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 184–190 | 7 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 208–216 | 9 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 211–221 | 11 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 212–238 | 25 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 16 != Inferred start 56
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `8` (DE2)
- ❌ Missing segment for action `Action_Keep` on target `8` (DE2)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (DE2)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ReadDefender' for track '7' has invalid range: start=33, end=19. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '7' has invalid range: start=44, end=19. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=61, end=19. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=56, end=26. Clamping end to start.
- ⚠️ Action 'Action_None' range [16-36] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 94, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [94-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-209] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-46] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [16-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-206] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-235] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-175] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '31' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_312'; source metadata written as null.

</details>