# Play-Annotation-Generator Annotation Review — StopAndGo_35

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_35`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 74
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | CB2 | defense | `15` | `15` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | CB2 | defense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 14 | START | 14 | 30 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `19` | `19` | 17 | START | 31 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 17 | START | 17 | 94 |
| ✅ EXACT | `Action_PassBlock` | LT | `6` | `6` | 17 | START | 17 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `7` | `7` | 17 | START | 17 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 17 | START | 17 | 117 |
| ✅ EXACT | `Action_SnapReceive` | CB2 | `15` | `15` | 30 | END | 14 | 30 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `10` | `10` | 77 | START | 77 | 269 |
| ✅ EXACT | `Action_ThrowPass` | CB2 | `15` | `15` | 89 | START | 89 | 98 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 143 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 76 | 23 | inferred_complete_timeline |
| `Action_VerticalStem` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 122 | 109 | inferred_complete_timeline |
| `Action_None` | 127 | 143 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 150 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 153 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 134 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 101 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 128 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 51 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 94 | 78 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 131 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 117 | 101 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 145 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 120 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 145 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 71 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 158 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 158 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 267 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 88 | 58 | inferred_complete_timeline |
| `Action_ThrowPass` | 89 | 98 | 10 | inferred_complete_timeline |
| `Action_None` | 99 | 131 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 164 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 158 | 145 | inferred_complete_timeline |
| `Action_None` | 166 | 269 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 166 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 143 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–252 | 252 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 93–102 | 5 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 95–139 | 18 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 118–142 | 25 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 121–143 | 18 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 144–152 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 144–170 | 27 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 144–159 | 16 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 159–166 | 8 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 169–269 | 101 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 234–264 | 27 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `19` (C): Annotated start 17 != Inferred start 31
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ UNMAPPED_ACTION_COLUMN: play=Play_Pass_StopAndGo video_id=35 column=Vertical Stem value=30,10
- ❌ UNMAPPED_ACTION_COLUMN: play=Play_Pass_StopAndGo video_id=35 column=Sell Stop value=53,10

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 50: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [14–30], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=31.
- ⚠️ Action 'Action_None' range [14-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-248] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-101] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-114] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-158] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-71] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-166] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-142] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-264] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>