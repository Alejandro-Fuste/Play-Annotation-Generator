# Play-Annotation-Generator Annotation Review — JetSweep_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_93`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 46
- **Ball Tracks:** 3
- **Action Segments:** 96
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 9
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SealBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `24` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 61 | START | 61 | 72 |
| ✅ EXACT | `Action_SealBlock` | Position_Unknown | `2` | `1` | 62 | START | 62 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 62 | START | 62 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 62 | START | 62 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 62 | START | 62 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 62 | START | 62 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `8` | 62 | START | 73 | 86 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `17` | `16` | 69 | START | 69 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 72 | END | 61 | 72 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 80 | START | 80 | 88 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `17` | `16` | 89 | START | 89 | 111 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `24` | `21` | 90 | START | 90 | 102 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 102 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 72 | 12 | inferred_complete_timeline |
| `Action_None` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_Toss` | 80 | 88 | 9 | inferred_complete_timeline |
| `Action_None` | 89 | 102 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 87 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 75 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 91 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 99 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 72 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 86 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 84 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 102 | 41 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 72 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 92 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 116 | 56 | inferred_complete_timeline |
| `Action_None` | 119 | 157 | 39 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 95 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 90 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 94 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–99 | 100 | 2 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–359 | 360 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 60–102 | 29 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 69–111 | 43 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 71–305 | 233 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 73–104 | 17 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 78–105 | 27 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 82–83 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 84–124 | 41 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 85–105 | 21 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 85–121 | 36 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 90–116 | 27 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 98–107 | 8 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 99–103 | 4 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 104–359 | 251 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 105–327 | 208 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 105–359 | 255 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 106–359 | 254 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 111–119 | 9 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 133–359 | 189 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 136–359 | 214 | 4 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 161–359 | 199 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 221–225 | 5 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 224–230 | 7 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 279–285 | 7 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 296–359 | 48 | 4 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 298–359 | 62 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 308–359 | 52 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 317–327 | 11 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 321–326 | 6 | 1 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 331–359 | 25 | 2 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 343–354 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `34` | `44` | 144 | 144 | 1 | 100.0% | None |
| `35` | `45` | 146 | 148 | 3 | 100.0% | None |
| `46` | `64` | 326 | 333 | 5 | 62.5% | 329–331 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [61–72], lower_priority='Action_ZoneBlock' annotated_start=62, effective_Action_ZoneBlock_start=73.
- ⚠️ Action 'Action_None' range [61-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [62-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-94] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-72] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [69-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-111] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-265] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-305] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-104] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-102] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [90-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-105] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-119] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-211] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-268] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-359] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-290] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-334] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-340] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-327] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-326] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-344] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-354] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>