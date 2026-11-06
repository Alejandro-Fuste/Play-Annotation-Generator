# Play-Annotation-Generator Annotation Review — OutsideZoneRead_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_24`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 51
- **Ball Tracks:** 3
- **Action Segments:** 121
- **Validation Warnings:** 177
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_PressEdge` | RB | `4` | `4` | 33 | START | 33 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 33 | START | 33 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 33 | START | 33 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 33 | START | 33 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 33 | START | 33 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 33 | START | 33 | 71 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `8` | `8` | 39 | START | 39 | 55 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 56 | START | 56 | 67 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 39 | 55 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_None` | 68 | 107 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PressEdge` | 33 | 104 | 72 | inferred_complete_timeline |
| `Action_None` | 105 | 419 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 71 | 39 | inferred_complete_timeline |
| `Action_None` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 173 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 71 | 39 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 86 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 32 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 71 | 39 | inferred_complete_timeline |
| `Action_None` | 72 | 79 | 8 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 71 | 39 | inferred_complete_timeline |
| `Action_None` | 72 | 121 | 50 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 71 | 39 | inferred_complete_timeline |
| `Action_None` | 72 | 184 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 171 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 213 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 53 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 61 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 67 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 175 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–14
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 10–23 | 14 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 49–210 | 83 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 56–118 | 62 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 74–146 | 73 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 87–213 | 116 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 89–90 | 2 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 94–222 | 99 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 95–156 | 62 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 103–172 | 70 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 108–166 | 59 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 116–213 | 85 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 118–214 | 73 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 129–213 | 66 | 5 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 132–152 | 21 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 141–419 | 263 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 153–250 | 97 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 165–177 | 13 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 167–373 | 205 | 3 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 186–209 | 14 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 198–201 | 4 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 212–216 | 5 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 215–419 | 205 | 1 | Undefined position; Undefined team |
| `40` | `72` | Position_Unknown | Team_Unknown | 237–419 | 183 | 1 | Undefined position; Undefined team |
| `41` | `74` | Position_Unknown | Team_Unknown | 249–416 | 168 | 1 | Undefined position; Undefined team |
| `44` | `81` | Position_Unknown | Team_Unknown | 324–375 | 46 | 4 | Undefined position; Undefined team |
| `45` | `82` | Position_Unknown | Team_Unknown | 326–419 | 45 | 5 | Undefined position; Undefined team |
| `46` | `84` | Position_Unknown | Team_Unknown | 335–371 | 37 | 1 | Undefined position; Undefined team |
| `47` | `85` | Position_Unknown | Team_Unknown | 343–369 | 24 | 2 | Undefined position; Undefined team |
| `48` | `89` | Position_Unknown | Team_Unknown | 347–362 | 13 | 2 | Undefined position; Undefined team |
| `49` | `91` | Position_Unknown | Team_Unknown | 373–419 | 46 | 2 | Undefined position; Undefined team |
| `50` | `92` | Position_Unknown | Team_Unknown | 374–378 | 5 | 1 | Undefined position; Undefined team |
| `51` | `93` | Position_Unknown | Team_Unknown | 378–419 | 39 | 3 | Undefined position; Undefined team |
| `53` | `96` | Position_Unknown | Team_Unknown | 416–419 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `42` | `76` | 255 | 255 | 1 | 100.0% | None |
| `43` | `77` | 283 | 283 | 1 | 100.0% | None |
| `52` | `94` | 383 | 384 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 104 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-53] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-61] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-184] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [33-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-69] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-157] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-171] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-146] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-98] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-222] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-184] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-131] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-148] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-313] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-189] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-373] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-197] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-216] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-419] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-416] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-330] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-355] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-369] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-375] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-332] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-348] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-362] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-398] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-419] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-371] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-359] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-369] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-349] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-362] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-409] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-378] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-392] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-407] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-419] for track '53' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.

</details>