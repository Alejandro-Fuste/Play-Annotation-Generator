# Play-Annotation-Generator Annotation Review — RPO_184

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_184`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunOutRoute` | actor_track_id `47` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 3 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `0` | `0` | 63 | START | 63 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 63 | START | 63 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 63 | START | 63 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `14` | 63 | START | 63 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `6` | 63 | START | 63 | 75 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `13` | 69 | START | 69 | 96 |
| ✅ EXACT | `Action_PullBall` | QB | `13` | `13` | 97 | START | 97 | 104 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 115 | START | 115 | 121 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 69 | 96 | 28 | inferred_complete_timeline |
| `Action_PullBall` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_ThrowPass` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_None` | 122 | 187 | 66 | inferred_complete_timeline |
| `Action_None` | 196 | 208 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 102 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 99 | 38 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 128 | 21 | inferred_complete_timeline |
| `Action_None` | 135 | 154 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 121 | 59 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 121 | 44 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 192 | 55 | inferred_complete_timeline |
| `Action_None` | 194 | 203 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–159
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 12 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 59 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 121 | 59 | inferred_complete_timeline |
| `Action_None` | 122 | 159 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 121 | 59 | inferred_complete_timeline |
| `Action_None` | 122 | 156 | 35 | inferred_complete_timeline |
| `Action_None` | 159 | 184 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 121 | 59 | inferred_complete_timeline |
| `Action_None` | 123 | 129 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 200 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 88 | 27 | inferred_complete_timeline |
| `Action_None` | 98 | 238 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 118 | 125 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 96 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 109 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 66–269 | 165 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 72–269 | 198 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 80–269 | 190 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 80–197 | 38 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 87–269 | 181 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 99–180 | 70 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 123–190 | 32 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 129–131 | 3 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 134–269 | 133 | 2 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 135–137 | 3 | 1 | Undefined position; Undefined team |
| `25` | `45` | Position_Unknown | Team_Unknown | 139–269 | 130 | 2 | Undefined position; Undefined team |
| `26` | `47` | Position_Unknown | Team_Unknown | 141–149 | 9 | 1 | Undefined position; Undefined team |
| `27` | `48` | Position_Unknown | Team_Unknown | 141–144 | 4 | 1 | Undefined position; Undefined team |
| `28` | `50` | Position_Unknown | Team_Unknown | 143–156 | 14 | 1 | Undefined position; Undefined team |
| `29` | `51` | Position_Unknown | Team_Unknown | 146–210 | 63 | 2 | Undefined position; Undefined team |
| `30` | `53` | Position_Unknown | Team_Unknown | 148–157 | 5 | 2 | Undefined position; Undefined team |
| `31` | `54` | Position_Unknown | Team_Unknown | 148–227 | 54 | 7 | Undefined position; Undefined team |
| `32` | `56` | Position_Unknown | Team_Unknown | 150–232 | 83 | 1 | Undefined position; Undefined team |
| `33` | `60` | Position_Unknown | Team_Unknown | 226–231 | 6 | 1 | Undefined position; Undefined team |
| `34` | `61` | Position_Unknown | Team_Unknown | 226–269 | 39 | 3 | Undefined position; Undefined team |
| `35` | `64` | Position_Unknown | Team_Unknown | 243–267 | 7 | 3 | Undefined position; Undefined team |
| `36` | `65` | Position_Unknown | Team_Unknown | 244–269 | 26 | 1 | Undefined position; Undefined team |
| `37` | `66` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 67 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [63-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-128] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-192] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-156] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-88] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-238] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-187] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-238] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-269] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-217] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-232] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-247] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '35' has 1 frames without a visible bounding box.
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

</details>