# Play-Annotation-Generator Annotation Review — RPO_108

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_108`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 172
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `17` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 35 | START | 35 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 35 | START | 35 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 35 | START | 35 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 35 | START | 35 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 35 | START | 35 | 47 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `10` | 44 | START | 44 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | `10` | `10` | 62 | START | 62 | 72 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 88 | START | 88 | 98 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 43 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 44 | 61 | 18 | inferred_complete_timeline |
| `Action_PullBall` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_PullBall` | 74 | 74 | 1 | inferred_complete_timeline |
| `Action_None` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_None` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_ThrowPass` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 186 | 198 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 79 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 67 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 47 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 60 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 89 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 117 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 80 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 87 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 89 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 117 | 19 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 196 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 81 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 98 | 16 | inferred_complete_timeline |
| `Action_None` | 99 | 120 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 98 | 64 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 117 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 92 | 59 | inferred_complete_timeline |
| `Action_None` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 118 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 104 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 61 | 28 | inferred_complete_timeline |
| `Action_None` | 63 | 116 | 54 | inferred_complete_timeline |
| `Action_None` | 136 | 143 | 8 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 151 | 156 | 6 | inferred_complete_timeline |
| `Action_None` | 165 | 172 | 8 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 244 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 104 | 71 | inferred_complete_timeline |
| `Action_None` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 228 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 109 | 76 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 106 | 73 | inferred_complete_timeline |
| `Action_None` | 115 | 134 | 20 | inferred_complete_timeline |
| `Action_None` | 138 | 264 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 76–231 | 135 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 77–115 | 33 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 106–269 | 164 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 109–269 | 157 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 124–269 | 145 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 134–269 | 136 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 134–185 | 52 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 136–221 | 84 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 136–186 | 51 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 137–150 | 14 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 139–177 | 39 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 139–178 | 39 | 2 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 139–149 | 11 | 1 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 141–145 | 5 | 1 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 141–201 | 61 | 1 | Undefined position; Undefined team |
| `30` | `30` | Position_Unknown | Team_Unknown | 142–201 | 60 | 1 | Undefined position; Undefined team |
| `31` | `31` | Position_Unknown | Team_Unknown | 143–244 | 99 | 2 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 154–180 | 27 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 160–178 | 19 | 1 | Undefined position; Undefined team |
| `34` | `35` | Position_Unknown | Team_Unknown | 163–216 | 54 | 1 | Undefined position; Undefined team |
| `35` | `37` | Position_Unknown | Team_Unknown | 170–209 | 38 | 2 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 229–233 | 5 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 233–235 | 3 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 238–269 | 32 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 246–268 | 19 | 3 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 250–268 | 18 | 2 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 250–264 | 15 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 255–269 | 14 | 2 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 256–269 | 10 | 3 | Undefined position; Undefined team |
| `45` | `52` | Position_Unknown | Team_Unknown | 261–269 | 8 | 2 | Undefined position; Undefined team |
| `46` | `54` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |
| `48` | `58` | Position_Unknown | Team_Unknown | 263–268 | 6 | 1 | Undefined position; Undefined team |
| `49` | `59` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `50` | `60` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `51` | `61` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `52` | `62` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `53` | `63` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 93 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [34-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-264] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-118] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-109] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-116] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-89] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [62-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-104] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-224] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-106] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-160] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-221] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-186] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-177] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-149] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-201] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-178] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-216] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-209] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-262] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-264] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '51' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.

</details>