# Play-Annotation-Generator Annotation Review — JetSweep_216

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_216`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `24` | `20` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 45 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `24` | `20` | 38 | START | 98 | 99 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 46 | START | 46 | 57 |
| ✅ EXACT | `Action_LeadBlock` | TE | `10` | `9` | 47 | START | 47 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 47 | START | 47 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 47 | START | 58 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `12` | 47 | START | 47 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 47 | START | 47 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 47 | START | 47 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 57 | END | 46 | 57 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 65 | START | 65 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `17` | 71 | START | 71 | 73 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 166 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_None` | 58 | 64 | 7 | inferred_complete_timeline |
| `Action_Toss` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_None` | 71 | 116 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 246 | 201 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_LeadBlock` | 47 | 87 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 114 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 95 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 113 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 110 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 107 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 98 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 233 | 188 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 93 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 61 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 269 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 110 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 116 | 71 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 124 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 37–176 | 133 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 38–215 | 175 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 78–112 | 23 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 87–105 | 19 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 98–99 | 2 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 110–269 | 153 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 126–269 | 144 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 128–238 | 111 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 179–196 | 10 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 184–269 | 86 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 235–255 | 17 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `24` (Position_Unknown): Annotated start 38 != Inferred start 98
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [46–57], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=58.
- ⚠️ Action 'Action_ZoneBlock' range [47-63] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-107] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-113] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-269] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-246] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-110] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [47-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-116] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-269] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-176] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [75-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [98-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-165] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-255] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '29' has 3 frames without a visible bounding box.
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

</details>