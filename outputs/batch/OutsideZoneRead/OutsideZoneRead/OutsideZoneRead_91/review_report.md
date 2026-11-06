# Play-Annotation-Generator Annotation Review — OutsideZoneRead_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_91`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 42
- **Ball Tracks:** 1
- **Action Segments:** 83
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

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
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Keep` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 59 | START | 59 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 59 | START | 59 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 59 | START | 59 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 59 | START | 59 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 59 | START | 59 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `13` | `13` | 68 | START | 68 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | `8` | `8` | 68 | START | 68 | 85 |
| ✅ EXACT | `Action_Keep` | QB | `8` | `8` | 91 | START | 91 | 168 |

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
- **Visible Frames:** 0–168
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 68 | 85 | 18 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_Keep` | 91 | 168 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PressEdge` | 68 | 86 | 19 | inferred_complete_timeline |
| `Action_PressEdge` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_None` | 95 | 112 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 118 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_None` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_None` | 89 | 121 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_None` | 77 | 124 | 48 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 221 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_None` | 77 | 94 | 18 | inferred_complete_timeline |
| `Action_None` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_None` | 112 | 130 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_None` | 77 | 128 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_None` | 77 | 178 | 102 | inferred_complete_timeline |
| `Action_None` | 183 | 231 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 249 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 106 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 289 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–8 | 9 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 108–359 | 183 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 115–123 | 9 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 120–359 | 240 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 128–359 | 226 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 145–278 | 132 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 162–265 | 104 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 173–272 | 100 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 174–359 | 182 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 183–359 | 177 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 186–359 | 147 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 188–203 | 15 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 190–253 | 64 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 195–263 | 69 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 199–359 | 159 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 200–204 | 5 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 208–359 | 149 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 209–304 | 94 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 213–359 | 147 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 225–359 | 135 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 226–230 | 5 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 247–254 | 7 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 310–359 | 50 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 330–354 | 10 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 346–354 | 8 | 2 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `37` | `44` | 228 | 233 | 4 | 66.7% | 229, 231 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadEdgeDefender` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 62 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-249] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-231] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-289] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [68-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [91-168] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [68-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [88-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-109] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-126] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-278] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-265] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-257] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-237] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-193] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-203] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-253] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-349] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-298] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-304] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-230] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-254] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-337] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-348] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-354] for track '41' has 1 frames without a visible bounding box.
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

</details>