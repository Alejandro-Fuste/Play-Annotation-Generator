# Play-Annotation-Generator Annotation Review — Counter_391

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `Counter_391`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 125
- **Validation Errors:** 4
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `15` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 8 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `15` | 73 | START | 73 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `15` | 75 | START | 144 | 145 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `14` | `13` | 92 | END | 73 | 81 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 99 | START | 99 | 120 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `11` | `10` | 121 | START | 122 | 123 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 163 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 81 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 99 | 120 | 22 | inferred_complete_timeline |
| `Action_None` | 121 | 169 | 49 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 123 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 238 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 153 | 81 | inferred_complete_timeline |
| `Action_None` | 156 | 171 | 16 | inferred_complete_timeline |
| `Action_None` | 174 | 186 | 13 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 46 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 105 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 8–154
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 72 | 65 | inferred_complete_timeline |
| `Action_BallSnap` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 141 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 93 | 21 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 129 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–24 | 25 | 1 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–8 | 9 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 90–98 | 9 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 98–116 | 17 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 133–135 | 3 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 133–176 | 20 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 137–229 | 6 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 149–239 | 80 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 159–235 | 54 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 163–171 | 7 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 183–237 | 43 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 188–193 | 5 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 190–231 | 22 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 193–215 | 12 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 199–220 | 17 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 223–225 | 3 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 223–233 | 11 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 231–237 | 5 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `11` (RB): Annotated start 121 != Inferred start 122

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_DownBlock' at frame 75 targets track ID 'LG', but it is not found in XML.
- ❌ Event 'Action_DownBlock' at frame 75 targets track ID 'LT', but it is not found in XML.
- ❌ Event 'Action_PullBlock' at frame 75 targets track ID 'RG', but it is not found in XML.
- ❌ Event 'Action_PullLeadBlock' at frame 75 targets track ID 'H', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 784: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [73–92], lower_priority='Action_DownBlock' annotated_start=75, effective_Action_DownBlock_start=93.
- ⚠️ Action 'Action_None' range [73-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-238] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [73-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-46] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [73-78] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-111] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-166] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-235] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-234] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-204] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-239] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>