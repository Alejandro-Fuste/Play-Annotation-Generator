# Play-Annotation-Generator Annotation Review — RPO_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_89`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `20` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 7
- **Group Expanded Events:** 7
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 30 | START | 30 | 69 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 30 | START | 30 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `3` | 30 | START | 30 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 30 | START | 30 | 69 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 30 | START | 30 | 69 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `9` | 33 | START | 33 | 36 |
| ✅ EXACT | `Action_PullBall` | QB | `9` | `9` | 37 | START | 37 | 46 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 63 | START | 63 | 69 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_PullBall` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_None` | 56 | 62 | 7 | inferred_complete_timeline |
| `Action_ThrowPass` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 197 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 72 | 44 | inferred_complete_timeline |
| `Action_None` | 74 | 116 | 43 | inferred_complete_timeline |
| `Action_None` | 118 | 194 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 69 | 40 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 108 | 238 | 131 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 69 | 40 | inferred_complete_timeline |
| `Action_None` | 70 | 216 | 147 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 69 | 40 | inferred_complete_timeline |
| `Action_None` | 70 | 269 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 185 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 69 | 40 | inferred_complete_timeline |
| `Action_None` | 70 | 105 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 194 | 166 | inferred_complete_timeline |
| `Action_None` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 39 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 34 | 6 | inferred_complete_timeline |
| `Action_None` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 73 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 13–79 | 20 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 38–184 | 143 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 39–186 | 146 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 54–58 | 5 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 61–269 | 187 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 69–262 | 182 | 5 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 95–160 | 65 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 105–269 | 163 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 107–239 | 131 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 129–133 | 5 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 167–269 | 96 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 185–193 | 9 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 187–269 | 83 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 192–269 | 78 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 244–269 | 26 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 246–269 | 13 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [29-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-238] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-72] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-216] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-56] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-20] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 29, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [29-33] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-156] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-184] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-70] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-246] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '29' has 2 frames without a visible bounding box.
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

</details>