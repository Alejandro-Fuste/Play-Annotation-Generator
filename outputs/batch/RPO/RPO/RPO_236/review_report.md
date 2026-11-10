# Play-Annotation-Generator Annotation Review — RPO_236

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_236`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSeamRoute` | actor_track_id `15` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 66 | START | 66 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 66 | START | 74 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 66 | START | 66 | 113 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 66 | START | 66 | 113 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `8` | `8` | 66 | START | N/A | N/A |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `5` | 70 | START | 70 | 81 |
| ✅ EXACT | `Action_PullBall` | QB | `5` | `5` | 82 | START | 82 | 96 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 107 | START | 107 | 113 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_PullBall` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_None` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_ThrowPass` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 234 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 98 | 34 | inferred_complete_timeline |
| `Action_None` | 101 | 122 | 22 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 220 | 36 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 105 | 41 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 113 | 48 | inferred_complete_timeline |
| `Action_None` | 114 | 229 | 116 | inferred_complete_timeline |
| `Action_None` | 231 | 236 | 6 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 113 | 48 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 99 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 113 | 13 | inferred_complete_timeline |
| `Action_None` | 114 | 167 | 54 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 113 | 48 | inferred_complete_timeline |
| `Action_None` | 114 | 146 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 101 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 115 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 86 | 22 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 86 | 22 | inferred_complete_timeline |
| `Action_None` | 145 | 160 | 16 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 115 | 51 | inferred_complete_timeline |
| `Action_None` | 125 | 157 | 33 | inferred_complete_timeline |
| `Action_None` | 161 | 189 | 29 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 99 | 35 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 194 | 130 | inferred_complete_timeline |
| `Action_None` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 239 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 84–239 | 151 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 87–206 | 112 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 104–239 | 135 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 123–183 | 60 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 133–138 | 6 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 166–239 | 47 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 168–239 | 72 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 171–239 | 69 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 175–239 | 65 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 182–239 | 55 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 195–233 | 33 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (LG)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '8' has invalid range: start=66, end=57. Clamping end to start.
- ⚠️ Action 'Action_None' range [65-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-122] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-143] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 65, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [65-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-86] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-146] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-149] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '27' has 1 frames without a visible bounding box.
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

</details>