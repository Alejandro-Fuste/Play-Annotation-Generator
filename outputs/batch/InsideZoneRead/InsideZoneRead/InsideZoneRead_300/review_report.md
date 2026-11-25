# Play-Annotation-Generator Annotation Review — InsideZoneRead_300

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_300`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE2 | defense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | DE2 | defense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 19 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `18` | 20 | START | 132 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 23 | START | 23 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `13` | 23 | START | 23 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 23 | START | 23 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 23 | START | 23 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 23 | START | 23 | 90 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `13` | `12` | 35 | END | 20 | 35 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `13` | `12` | 39 | START | 39 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE2 | `13` | `12` | 44 | START | 44 | 49 |
| ✅ EXACT | `Action_BallCarry` | DE2 | `13` | `12` | 61 | START | 61 | 89 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 195 | 176 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 91 | 69 | inferred_complete_timeline |
| `Action_None` | 92 | 112 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 90 | 68 | inferred_complete_timeline |
| `Action_None` | 92 | 118 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 91 | 69 | inferred_complete_timeline |
| `Action_None` | 92 | 111 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 91 | 69 | inferred_complete_timeline |
| `Action_None` | 92 | 108 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 91 | 69 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 39 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_Keep` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_Keep` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 61 | 89 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 76 | 85 | 10 | inferred_complete_timeline |
| `Action_None` | 94 | 124 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 32 | 13 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 95 | 76 | inferred_complete_timeline |
| `Action_None` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 59 | 40 | inferred_complete_timeline |
| `Action_None` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_None` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_None` | 99 | 109 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 99 | 80 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 183 | 164 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 55–76 | 10 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 100–136 | 37 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 132–210 | 79 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 134–210 | 76 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 137–210 | 74 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 142–210 | 69 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 20 != Inferred start 132
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=132, end=35. Clamping end to start.
- ⚠️ Action 'Action_None' range [20-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-39] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-99] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-90] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-74] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [44-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [61-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-62] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '22' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_300'; source metadata written as null.

</details>