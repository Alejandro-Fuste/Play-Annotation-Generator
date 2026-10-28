# Play-Annotation-Generator Annotation Review — Draw_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_38`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `10` | `9` | 56 | START | 56 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `10` | `9` | 59 | START | 77 | 78 |
| ✅ EXACT | `Action_PassBlock` | LT | `11` | `10` | 59 | START | 59 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `2` | `1` | 59 | START | 59 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `3` | `2` | 59 | START | 59 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `8` | 59 | START | 59 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `12` | `11` | 74 | END | 56 | 67 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `12` | `11` | 77 | START | 77 | 90 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 91 | START | 91 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 110 | START | 110 | 114 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 77 | 90 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 91 | 109 | 19 | inferred_complete_timeline |
| `Action_None` | 110 | 230 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 160 | 211 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 91 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 99 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 99 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 135 | 35 | inferred_complete_timeline |
| `Action_None` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_None` | 193 | 299 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 55 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 83 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 116 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 172 | 24 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 120 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 148 | 27 | inferred_complete_timeline |
| `Action_None` | 149 | 181 | 33 | inferred_complete_timeline |
| `Action_None` | 188 | 236 | 49 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 271 | 24 | inferred_complete_timeline |
| `Action_None` | 278 | 292 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 154 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 95 | 40 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 74 | 19 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 116 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 20–299 | 246 | 6 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 69–193 | 78 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 72–177 | 79 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 87–108 | 22 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 94–125 | 32 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 96–290 | 133 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 109–299 | 175 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 154–268 | 108 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 154–299 | 121 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 172–299 | 101 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 174–299 | 126 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 189–299 | 111 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 196–238 | 43 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 213–299 | 87 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 217–252 | 30 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 222–241 | 20 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 227–299 | 56 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 238–287 | 49 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 246–289 | 42 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 250–290 | 41 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 261–299 | 21 | 4 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 280–289 | 10 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [56–74], lower_priority='Action_PassBlock' annotated_start=59, effective_Action_PassBlock_start=75.
- ⚠️ Action 'Action_None' range [56-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [119-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [160-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-181] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-271] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [56-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [63-70] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [56-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-42] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-94] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-108] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-122] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-228] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-265] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-217] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-193] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-238] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-289] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-290] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-285] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>