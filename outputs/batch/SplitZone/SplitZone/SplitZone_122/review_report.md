# Play-Annotation-Generator Annotation Review — SplitZone_122

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_122`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 11 | START | 12 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 11 | START | 12 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 11 | START | 12 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 11 | START | 12 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 11 | START | 12 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 11 | START | 12 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 11 | START | 12 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 37 | START | 37 | 54 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `1` | 40 | START | 40 | 156 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `10` | `10` | 40 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 40 | START | 40 | 156 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 40 | START | 40 | 156 |
| ✅ EXACT | `Action_SplitBlock` | TE | `5` | `5` | 42 | START | 42 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `10` | `10` | 49 | START | 55 | 105 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 54 | END | 37 | 54 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 61 | START | 61 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `0` | `0` | 71 | START | 71 | 80 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 156 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 12–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 54 | 18 | inferred_complete_timeline |
| `Action_None` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 61 | 70 | 10 | inferred_complete_timeline |
| `Action_None` | 71 | 249 | 179 | inferred_complete_timeline |
| `Action_None` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–171
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 70 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 112 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 140 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 171 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–121
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_SplitBlock` | 42 | 121 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 39 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 156 | 117 | inferred_complete_timeline |
| `Action_None` | 157 | 269 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–109
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 54 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 55 | 105 | 51 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 108 | 109 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 39 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 156 | 117 | inferred_complete_timeline |
| `Action_None` | 157 | 230 | 74 | inferred_complete_timeline |
| `Action_None` | 232 | 269 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 39 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 156 | 117 | inferred_complete_timeline |
| `Action_None` | 157 | 269 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 269 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 186 | 150 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 55 | 19 | inferred_complete_timeline |
| `Action_None` | 60 | 269 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 113 | 77 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 269 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–214
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 214 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 269 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–155
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 36 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 155 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 12–269 | 237 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 27–29 | 3 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 70–242 | 173 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 85–200 | 107 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 97–262 | 159 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 114–269 | 154 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 117–192 | 75 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 124–188 | 65 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 143–269 | 87 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 155–269 | 115 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 159–265 | 76 | 6 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 168–250 | 61 | 6 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 170–188 | 17 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 190–217 | 28 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 190–269 | 79 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 204–269 | 66 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 246: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 117 frames exceeds threshold 90 frames [start=40, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 117 frames exceeds threshold 90 frames [start=40, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 117 frames exceeds threshold 90 frames [start=40, end=156].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [37–54], lower_priority='Action_ZoneBlock' annotated_start=40, effective_Action_ZoneBlock_start=55.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [37–54], lower_priority='Action_BlockSecondLevel' annotated_start=49, effective_Action_BlockSecondLevel_start=55.
- ⚠️ Action 'Action_BallCarry' range [71-80] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-155] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [42-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-214] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [55-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [108-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-30] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-242] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-186] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-187] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-262] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-265] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '30' has 1 frames without a visible bounding box.
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