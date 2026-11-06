# Play-Annotation-Generator Annotation Review — OutsideZoneRead_118

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_118`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Keep` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 21 | START | 21 | 34 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 24 | START | 35 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 24 | START | 24 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 24 | START | 24 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 24 | START | 24 | 67 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 24 | START | 24 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 34 | END | 21 | 34 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `11` | `10` | 37 | START | 37 | 41 |
| ✅ EXACT | `Action_Keep` | QB | `11` | `10` | 42 | START | 42 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 65 | START | 65 | 257 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 79 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_Keep` | 42 | 64 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 257 | 193 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 291 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 38 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 101 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 79 | 56 | inferred_complete_timeline |
| `Action_None` | 80 | 97 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 79 | 56 | inferred_complete_timeline |
| `Action_None` | 80 | 124 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 79 | 45 | inferred_complete_timeline |
| `Action_None` | 80 | 90 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 67 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 79 | 56 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 47 | 27 | inferred_complete_timeline |
| `Action_None` | 55 | 70 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 299 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 50 | 30 | inferred_complete_timeline |
| `Action_None` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 299 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 54 | 34 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 125 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 61 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 80 | 60 | inferred_complete_timeline |
| `Action_None` | 90 | 114 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 50 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_None` | 31 | 39 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 37–118 | 76 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 70–109 | 37 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 81–115 | 21 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 88–107 | 18 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 91–110 | 20 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 109–299 | 191 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 111–299 | 189 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 117–299 | 183 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 122–138 | 17 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 128–299 | 172 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 135–299 | 156 | 4 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 144–299 | 155 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 149–299 | 66 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 218–299 | 82 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 247–299 | 53 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 255–272 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 24 != Inferred start 35
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [21–34], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=35.
- ⚠️ Action 'Action_None' range [21-80] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-61] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-257] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-291] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [295-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-70] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-39] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '33' has 1 frames without a visible bounding box.
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