# Play-Annotation-Generator Annotation Review — SplitZone_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_106`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 97
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
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | RB1 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 11 | START | 12 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 11 | START | 12 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 11 | START | 12 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `4` | `Group` | 11 | START | 12 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 11 | START | 12 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `6` | `Group` | 11 | START | 12 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 11 | START | 12 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 11 | START | 12 | 60 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 58 | START | 58 | 69 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `13` | 61 | START | 70 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 61 | START | 61 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 61 | START | 61 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 61 | START | 61 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 61 | START | 61 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | RB1 | `6` | `6` | 64 | START | 64 | 87 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 69 | END | 58 | 69 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 71 | START | 71 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | `4` | `4` | 82 | START | 82 | 106 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 138 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–132
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 70 | 70 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 71 | 81 | 11 | inferred_complete_timeline |
| `Action_None` | 82 | 132 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–103
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 63 | 52 | inferred_complete_timeline |
| `Action_SplitBlock` | 64 | 87 | 24 | inferred_complete_timeline |
| `Action_SplitBlock` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–131
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 81 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 106 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 131 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 138 | 78 | inferred_complete_timeline |
| `Action_None` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–100
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 100 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–163
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 138 | 69 | inferred_complete_timeline |
| `Action_None` | 139 | 163 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–159
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 138 | 78 | inferred_complete_timeline |
| `Action_None` | 140 | 155 | 16 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–157
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 138 | 78 | inferred_complete_timeline |
| `Action_None` | 139 | 157 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–125
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 120 | 63 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 120 | 63 | inferred_complete_timeline |
| `Action_None` | 122 | 239 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–65
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 65 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 121 | 64 | inferred_complete_timeline |
| `Action_None` | 137 | 239 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–113
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 92 | 35 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–122
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 122 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 72–157 | 86 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 93–223 | 129 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 111–239 | 120 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 114–239 | 119 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 121–239 | 115 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 129–239 | 111 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 137–239 | 98 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 142–234 | 63 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 160–164 | 5 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 208–239 | 32 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 208–223 | 16 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 209–239 | 29 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 212–239 | 10 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 213–236 | 8 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 221–239 | 17 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 227–239 | 9 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 61 != Inferred start 70
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [58–69], lower_priority='Action_ZoneBlock' annotated_start=61, effective_Action_ZoneBlock_start=70.
- ⚠️ Action 'Action_None' range [58-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-106] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [64-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [102-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-157] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-226] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '34' has 1 frames without a visible bounding box.
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

</details>