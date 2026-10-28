# Play-Annotation-Generator Annotation Review — Draw_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_90`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 29 | START | 29 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `12` | 32 | START | 32 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 32 | START | 32 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `18` | 32 | START | 44 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 32 | START | 32 | 53 |
| ✅ EXACT | `Action_PassBlock` | RT | `22` | `21` | 32 | START | 32 | 122 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 43 | END | 29 | 43 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 45 | START | 45 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 71 | START | 71 | 99 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 45 | 70 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 99 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 108 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 267 | 158 | inferred_complete_timeline |
| `Action_BallCarry` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 258 | 230 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 51 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 55 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 92 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 122 | 21 | inferred_complete_timeline |
| `Action_None` | 123 | 135 | 13 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 67 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 122 | 50 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 53 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 122 | 66 | inferred_complete_timeline |
| `Action_None` | 123 | 148 | 26 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 122 | 91 | inferred_complete_timeline |
| `Action_None` | 123 | 265 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 92 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 239 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 102 | 74 | inferred_complete_timeline |
| `Action_None` | 110 | 127 | 18 | inferred_complete_timeline |
| `Action_None` | 137 | 230 | 94 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 194 | 166 | inferred_complete_timeline |
| `Action_None` | 200 | 269 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 134 | 106 | inferred_complete_timeline |
| `Action_None` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 157 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 128 | 100 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–269 | 259 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 61–259 | 197 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 98–269 | 171 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 147–269 | 123 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 174–269 | 89 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 176–269 | 87 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 203–205 | 3 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 211–214 | 4 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 236–242 | 7 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [29–43], lower_priority='Action_PassBlock' annotated_start=32, effective_Action_PassBlock_start=44.
- ⚠️ Action 'Action_None' range [29-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-103] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-99] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-267] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-194] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-102] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-92] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-67] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-218] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-244] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>