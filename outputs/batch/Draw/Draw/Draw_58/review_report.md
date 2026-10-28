# Play-Annotation-Generator Annotation Review — Draw_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_58`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 97
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
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 13 | START | 13 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 13 | START | 13 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 13 | START | 13 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `16` | `Group` | 13 | START | 13 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 13 | START | 13 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 13 | START | 13 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 13 | START | 13 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 13 | START | 13 | 79 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 77 | START | 77 | 88 |
| ✅ EXACT | `Action_PassBlock` | RT | `12` | `11` | 80 | START | 80 | 164 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `15` | `14` | 80 | START | 89 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `3` | `2` | 80 | START | 80 | 164 |
| ✅ EXACT | `Action_PassBlock` | LT | `4` | `3` | 80 | START | 80 | 164 |
| ✅ EXACT | `Action_PassBlock` | RG | `9` | `8` | 80 | START | 80 | 164 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 88 | END | 77 | 88 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `10` | `9` | 92 | START | 92 | 115 |
| ✅ EXACT | `Action_BallCarry` | QB | `10` | `9` | 116 | START | 116 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 164 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–238
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 92 | 115 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 238 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–19
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 19 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–174
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 164 | 85 | inferred_complete_timeline |
| `Action_None` | 165 | 174 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–172
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 164 | 85 | inferred_complete_timeline |
| `Action_None` | 165 | 172 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 13–124
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 124 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–182
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 164 | 85 | inferred_complete_timeline |
| `Action_None` | 165 | 182 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 53 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 79 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 164 | 85 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 269 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–110
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 110 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–170
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 104 | 28 | inferred_complete_timeline |
| `Action_None` | 144 | 170 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–182
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 116 | 40 | inferred_complete_timeline |
| `Action_None` | 122 | 139 | 18 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 182 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–125
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 125 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–229
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 220 | 144 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 164 | 88 | inferred_complete_timeline |
| `Action_None` | 166 | 269 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–124
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 124 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–172
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 42 | 30 | inferred_complete_timeline |
| `Action_None` | 133 | 172 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 22–67 | 30 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 118–269 | 131 | 6 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 127–161 | 35 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 128–269 | 139 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 133–178 | 37 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 149–250 | 95 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 176–208 | 33 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 179–269 | 76 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 198–269 | 25 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 207–257 | 51 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 232–236 | 5 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 254–269 | 13 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 257–269 | 10 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `15` (C): Annotated start 80 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [77–88], lower_priority='Action_PassBlock' annotated_start=80, effective_Action_PassBlock_start=89.
- ⚠️ Action 'Action_None' range [77-164] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-42] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-60] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-116] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-125] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-47] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-256] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-178] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-243] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-254] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '32' has 3 frames without a visible bounding box.
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