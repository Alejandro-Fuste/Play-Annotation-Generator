# Play-Annotation-Generator Annotation Review — SplitZone_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_30`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 87
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 11 | START | 11 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 11 | START | 11 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 11 | START | 11 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 11 | START | 11 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 11 | START | 11 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 11 | START | 11 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 11 | START | 11 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 11 | START | 11 | 117 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 115 | START | 115 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 118 | START | 118 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 118 | START | 131 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 118 | START | 118 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 118 | START | 118 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 118 | START | 118 | 140 |
| ✅ EXACT | `Action_SplitBlock` | TE | `1` | `1` | 121 | START | 121 | 187 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 130 | END | 115 | 130 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 139 | START | 139 | 159 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `8` | `8` | 152 | START | 152 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 160 | START | 160 | 160 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 187 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–259
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 115 | 130 | 16 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 139 | 159 | 21 | inferred_complete_timeline |
| `Action_None` | 160 | 242 | 83 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–226
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 159 | 149 | inferred_complete_timeline |
| `Action_BallCarry` | 160 | 160 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 176 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 222 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 226 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 11–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 120 | 110 | inferred_complete_timeline |
| `Action_SplitBlock` | 121 | 187 | 67 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–267
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 117 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 162 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 187 | 22 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 208 | 225 | 18 | inferred_complete_timeline |
| `Action_None` | 240 | 264 | 25 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–158
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 117 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 151 | 34 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 152 | 158 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 11–217
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_BallSnap` | 115 | 130 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 148 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 166 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 187 | 20 | inferred_complete_timeline |
| `Action_None` | 188 | 217 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–182
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 117 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 140 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 182 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 117 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 170 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 187 | 12 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 11–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 35 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 72 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 114 | 38 | inferred_complete_timeline |
| `Action_None` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–269
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 134 | 9 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 193 | 9 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 269 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–165
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_None` | 115 | 165 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_None` | 115 | 151 | 37 | inferred_complete_timeline |
| `Action_None` | 156 | 264 | 109 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 11–134 | 124 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 167–184 | 18 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 175–189 | 15 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 175–269 | 92 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 185–269 | 85 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 190–269 | 74 | 4 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 196–267 | 62 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 201–269 | 47 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 202–269 | 62 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 205–269 | 65 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 211–269 | 59 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 223–269 | 46 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 224–269 | 46 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 232–269 | 38 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [115–130], lower_priority='Action_ZoneBlock' annotated_start=118, effective_Action_ZoneBlock_start=131.
- ⚠️ Action 'Action_None' range [115-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '3' starts at frame 160, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [160-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-222] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [152-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 115, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [115-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-217] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-249] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>