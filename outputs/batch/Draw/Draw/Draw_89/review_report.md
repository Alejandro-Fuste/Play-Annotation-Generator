# Play-Annotation-Generator Annotation Review — Draw_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_89`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 32 | START | 32 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `12` | 35 | START | 35 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `13` | 35 | START | 48 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `14` | 35 | START | 35 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `6` | `5` | 35 | START | 35 | 68 |
| ✅ EXACT | `Action_PassBlock` | LT | `8` | `7` | 35 | START | 35 | 99 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 47 | END | 32 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | `5` | `4` | 53 | START | 53 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 69 | START | 69 | 88 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 99 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 53 | 58 | 6 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 88 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 94 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 35 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 99 | 65 | inferred_complete_timeline |
| `Action_None` | 100 | 239 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 68 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 88 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 100 | 145 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 45 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 80 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 80 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 94 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 100 | 100 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 50 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 99 | 45 | inferred_complete_timeline |
| `Action_None` | 100 | 131 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 179 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 126 | 95 | inferred_complete_timeline |
| `Action_None` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 102 | 71 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 75 | 44 | inferred_complete_timeline |
| `Action_None` | 80 | 116 | 37 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 126 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 45 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 145 | 114 | inferred_complete_timeline |
| `Action_None` | 155 | 239 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 75 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–119 | 120 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 93–145 | 53 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 98–239 | 142 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 107–110 | 4 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 127–145 | 19 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 127–145 | 19 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 146–182 | 37 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 146–239 | 94 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 146–239 | 89 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 146–239 | 94 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 146–239 | 82 | 5 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 191–239 | 49 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 192–199 | 8 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 200–239 | 40 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 225–237 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_FakePassDroptoHandoff` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [32–47], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=48.
- ⚠️ Action 'Action_None' range [32-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [53-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [63-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-88] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-179] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [32-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-80] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-94] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 100, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [100-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-145] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '30' has 1 frames without a visible bounding box.
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