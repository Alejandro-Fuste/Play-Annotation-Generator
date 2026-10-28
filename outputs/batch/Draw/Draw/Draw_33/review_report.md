# Play-Annotation-Generator Annotation Review — Draw_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_33`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 45 | START | 45 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `12` | 48 | START | 48 | 126 |
| ✅ EXACT | `Action_PassBlock` | LG | `14` | `13` | 48 | START | 48 | 126 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `1` | 48 | START | 48 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `19` | 48 | START | 66 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 48 | START | 48 | 74 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 65 | END | 45 | 65 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `18` | `17` | 72 | START | 72 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `18` | `17` | 95 | START | 95 | 121 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 126 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 65 | 21 | inferred_complete_timeline |
| `Action_None` | 66 | 71 | 6 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 72 | 94 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 121 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 250 | 206 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 126 | 79 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 126 | 79 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 65 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 91 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 126 | 32 | inferred_complete_timeline |
| `Action_None` | 127 | 153 | 27 | inferred_complete_timeline |
| `Action_None` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_None` | 166 | 269 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 74 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 96 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 126 | 79 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 94 | 50 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 106 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 189 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 73–94 | 22 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 89–93 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 106–205 | 22 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 109–269 | 157 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 119–269 | 145 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 120–269 | 150 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 146–269 | 123 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 152–157 | 6 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 176–269 | 35 | 8 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 204–207 | 4 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [45–65], lower_priority='Action_PassBlock' annotated_start=48, effective_Action_PassBlock_start=66.
- ⚠️ Action 'Action_None' range [45-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-96] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-269] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '34' has 1 frames without a visible bounding box.
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