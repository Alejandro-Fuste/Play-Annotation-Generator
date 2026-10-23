# Play-Annotation-Generator Annotation Review — Draw_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_1`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 74
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
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 68 | START | 68 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `15` | 70 | START | 70 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `16` | 70 | START | 81 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 70 | START | 70 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `20` | 70 | START | 70 | 158 |
| ✅ EXACT | `Action_PassBlock` | RG | `22` | `21` | 70 | START | 70 | 128 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 80 | END | 68 | 80 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `15` | `14` | 84 | START | 84 | 117 |
| ✅ EXACT | `Action_BallCarry` | QB | `15` | `14` | 118 | START | 118 | 148 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 84 | 117 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 118 | 148 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 131 | 64 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 184 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 158 | 89 | inferred_complete_timeline |
| `Action_None` | 159 | 221 | 63 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 244 | 11 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 106 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 158 | 41 | inferred_complete_timeline |
| `Action_None` | 159 | 221 | 63 | inferred_complete_timeline |
| `Action_None` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 244 | 11 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 117 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 128 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 158 | 89 | inferred_complete_timeline |
| `Action_None` | 159 | 214 | 56 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 148 | 81 | inferred_complete_timeline |
| `Action_None` | 156 | 208 | 53 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 214 | 147 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 245 | 12 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 172 | 105 | inferred_complete_timeline |
| `Action_None` | 177 | 187 | 11 | inferred_complete_timeline |
| `Action_None` | 192 | 269 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 102 | 35 | inferred_complete_timeline |
| `Action_None` | 109 | 222 | 114 | inferred_complete_timeline |
| `Action_None` | 224 | 269 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>OLB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 154 | 87 | inferred_complete_timeline |
| `Action_None` | 158 | 269 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 160 | 93 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 244 | 177 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 237 | 170 | inferred_complete_timeline |
| `Action_None` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 108–253 | 143 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 130–269 | 132 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 157–269 | 112 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 178–269 | 90 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 212–235 | 4 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 216–269 | 53 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 255–269 | 10 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_PassBlock' annotated_start=70, effective_Action_PassBlock_start=81.
- ⚠️ Action 'Action_None' range [68-172] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-102] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-269] for track '13' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [118-148] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-117] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-221] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-244] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-208] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-244] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-128] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-253] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '29' has 1 frames without a visible bounding box.
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