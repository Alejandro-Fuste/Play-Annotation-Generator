# Play-Annotation-Generator Annotation Review — RPO_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_41`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `21` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | RB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 35 | START | 35 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 35 | START | 35 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 35 | START | 35 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `8` | 35 | START | 35 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 35 | START | 35 | 47 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `7` | 46 | START | 46 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | RB | `11` | `11` | 62 | START | 66 | 69 |
| ✅ EXACT | `Action_ThrowPass` | RB | `11` | `11` | 84 | START | 84 | 90 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_ReadDefender` | 46 | 64 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 39 | 60 | 22 | inferred_complete_timeline |
| `Action_PullBall` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_PullBall` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_ThrowPass` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 90 | 56 | inferred_complete_timeline |
| `Action_None` | 91 | 212 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 89 | 38 | inferred_complete_timeline |
| `Action_None` | 100 | 136 | 37 | inferred_complete_timeline |
| `Action_None` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 47 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 90 | 40 | inferred_complete_timeline |
| `Action_None` | 91 | 269 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 43 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 90 | 38 | inferred_complete_timeline |
| `Action_None` | 91 | 110 | 20 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 87 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 269 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 82 | 49 | inferred_complete_timeline |
| `Action_None` | 84 | 100 | 17 | inferred_complete_timeline |
| `Action_None` | 112 | 269 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 71 | 38 | inferred_complete_timeline |
| `Action_None` | 81 | 136 | 56 | inferred_complete_timeline |
| `Action_None` | 139 | 265 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 33 | 12 | inferred_complete_timeline |
| `Action_None` | 34 | 75 | 42 | inferred_complete_timeline |
| `Action_None` | 84 | 124 | 41 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 81 | 48 | inferred_complete_timeline |
| `Action_None` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_None` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 265 | 128 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 144 | 111 | inferred_complete_timeline |
| `Action_None` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 36 | 67 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 75 | 42 | inferred_complete_timeline |
| `Action_None` | 80 | 101 | 22 | inferred_complete_timeline |
| `Action_None` | 110 | 128 | 19 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 10–67 | 55 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 28–67 | 33 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 70–94 | 9 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 77–269 | 184 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 101–195 | 45 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 103–265 | 163 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 106–269 | 147 | 5 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 109–118 | 10 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 128–250 | 114 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 130–179 | 50 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 139–269 | 127 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 145–183 | 9 | 3 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 199–258 | 60 | 1 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 205–258 | 54 | 1 | Undefined position; Undefined team |
| `30` | `50` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 216–269 | 54 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 219–258 | 28 | 5 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 85 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' for track '0' starts at frame 34, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [34-34] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-67] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-144] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-75] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-128] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-82] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-124] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-265] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [46-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-43] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-50] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-60] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [66-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-75] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-39] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-136] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-265] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-177] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-179] for track '24' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '33' has 1 frames without a visible bounding box.
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

</details>