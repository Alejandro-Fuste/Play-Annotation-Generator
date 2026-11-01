# Play-Annotation-Generator Annotation Review — InsideZoneRead_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_80`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 6
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 55 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `14` | `12` | 53 | START | 54 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 56 | START | 56 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 56 | START | 56 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 56 | START | 56 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 56 | START | 56 | 107 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 62 | END | 53 | 62 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 67 | START | 67 | 76 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 77 | START | 77 | 83 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 84 | START | 84 | 154 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_SnapReceive` | 53 | 62 | 10 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 67 | 76 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_None` | 84 | 114 | 31 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 162 | 38 | inferred_complete_timeline |
| `Action_None` | 171 | 184 | 14 | inferred_complete_timeline |
| `Action_None` | 210 | 239 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 154 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 127 | 72 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 196 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 107 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 117 | 9 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_None` | 150 | 208 | 59 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 120 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 100 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 162 | 110 | inferred_complete_timeline |
| `Action_None` | 173 | 239 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 69 | 17 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 54 | 68 | 15 | inferred_complete_timeline |
| `Action_None` | 127 | 239 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 72 | 20 | inferred_complete_timeline |
| `Action_None` | 76 | 120 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 109 | 57 | inferred_complete_timeline |
| `Action_None` | 111 | 118 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | Position_Unknown | Team_Unknown | 38–239 | 188 | 6 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 69–137 | 69 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 78–237 | 156 | 3 | Undefined position; Undefined team |
| `15` | `21` | Position_Unknown | Team_Unknown | 96–105 | 5 | 2 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 101–239 | 137 | 2 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 117–126 | 6 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 117–232 | 111 | 4 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 121–239 | 115 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 124–237 | 110 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 134–137 | 4 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 142–239 | 49 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 144–239 | 96 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 148–189 | 27 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 165–168 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 178–239 | 62 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 178–239 | 62 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 197–235 | 31 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 207–239 | 31 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `14` (Position_Unknown): Annotated start 53 != Inferred start 54
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 63 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [56-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-196] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-162] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-184] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-117] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-49] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-137] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-167] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-174] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-237] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-235] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>