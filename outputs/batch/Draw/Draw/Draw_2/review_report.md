# Play-Annotation-Generator Annotation Review — Draw_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_2`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 39
- **Ball Tracks:** 1
- **Action Segments:** 86
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 57 | START | 57 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `10` | 60 | START | 68 | 74 |
| ✅ EXACT | `Action_PassBlock` | LT | `12` | `11` | 60 | START | 60 | 147 |
| ✅ EXACT | `Action_PassBlock` | RT | `2` | `1` | 60 | START | 60 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `4` | `3` | 60 | START | 60 | 147 |
| ✅ EXACT | `Action_PassBlock` | RG | `5` | `4` | 60 | START | 60 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 67 | END | 57 | 67 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `6` | `5` | 71 | START | 71 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `6` | `5` | 102 | START | 102 | 164 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 71 | 101 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 164 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 214 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 75 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 147 | 88 | inferred_complete_timeline |
| `Action_None` | 148 | 259 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 59 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 147 | 88 | inferred_complete_timeline |
| `Action_None` | 148 | 158 | 11 | inferred_complete_timeline |
| `Action_None` | 173 | 220 | 48 | inferred_complete_timeline |
| `Action_None` | 231 | 238 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 122 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 59 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 147 | 88 | inferred_complete_timeline |
| `Action_None` | 148 | 148 | 1 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 147 | 88 | inferred_complete_timeline |
| `Action_None` | 148 | 148 | 1 | inferred_complete_timeline |
| `Action_None` | 198 | 269 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 205 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 132 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 64 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_None` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_None` | 81 | 186 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 114 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 2–90 | 85 | 4 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 83–269 | 184 | 4 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 115–269 | 155 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 156–193 | 38 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 159–215 | 57 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 169–262 | 86 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 175–255 | 81 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 178–224 | 47 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 200–204 | 5 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 206–244 | 39 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 207–269 | 52 | 3 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 210–269 | 57 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 214–269 | 56 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 216–269 | 52 | 3 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 219–223 | 5 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 221–269 | 49 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 226–258 | 33 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 242–269 | 28 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | 93 | 93 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [57–67], lower_priority='Action_PassBlock' annotated_start=60, effective_Action_PassBlock_start=68.
- ⚠️ Action 'Action_None' range [57-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 148, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [148-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-220] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 148, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [148-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-164] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-90] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-162] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-214] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-244] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>