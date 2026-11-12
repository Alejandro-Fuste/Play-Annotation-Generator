# Play-Annotation-Generator Annotation Review — SplitZone_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `10` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 79 | START | 79 | 91 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `13` | 82 | START | 92 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 82 | START | 82 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 82 | START | 82 | 130 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 82 | START | 82 | 130 |
| ✅ EXACT | `Action_SplitBlock` | HB | `10` | `10` | 86 | START | 86 | 112 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 91 | END | 79 | 91 |
| ✅ EXACT | `Action_BallCarry` | QB | `2` | `2` | 112 | START | 112 | 239 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `3` | `3` | 119 | START | 119 | 130 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 130 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 140 | 62 | inferred_complete_timeline |
| `Action_None` | 169 | 239 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SplitBlock` | 86 | 112 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 115 | 37 | inferred_complete_timeline |
| `Action_None` | 125 | 128 | 4 | inferred_complete_timeline |
| `Action_None` | 132 | 162 | 31 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 99 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 119 | 130 | 12 | inferred_complete_timeline |
| `Action_None` | 131 | 212 | 82 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BallSnap` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 130 | 39 | inferred_complete_timeline |
| `Action_None` | 131 | 144 | 14 | inferred_complete_timeline |
| `Action_None` | 161 | 171 | 11 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_None` | 131 | 212 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 239 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 78 | 43 | inferred_complete_timeline |
| `Action_None` | 79 | 195 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 135 | 57 | inferred_complete_timeline |
| `Action_None` | 151 | 161 | 11 | inferred_complete_timeline |
| `Action_None` | 169 | 177 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 139 | 61 | inferred_complete_timeline |
| `Action_None` | 147 | 160 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 228 | 150 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 161 | 83 | inferred_complete_timeline |
| `Action_None` | 167 | 203 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 164 | 86 | inferred_complete_timeline |
| `Action_None` | 170 | 177 | 8 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 239 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 178 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–231 | 230 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 75–96 | 9 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 82–98 | 15 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 117–149 | 33 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 126–132 | 7 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 126–147 | 9 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 141–194 | 46 | 4 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 145–239 | 95 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 147–239 | 92 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 150–162 | 13 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 153–163 | 7 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 177–198 | 22 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 181–212 | 30 | 3 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 182–193 | 12 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 184–205 | 22 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 192–201 | 10 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 202–224 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 82 != Inferred start 92
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 142: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [79–91], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=92.
- ⚠️ Action 'Action_None' range [79-135] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' for track '3' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockSecondLevel' range [119-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-140] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-178] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-231] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-212] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-139] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-160] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [86-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-228] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-161] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-149] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-212] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-205] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-224] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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