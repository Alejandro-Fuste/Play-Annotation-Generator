# Play-Annotation-Generator Annotation Review — Draw_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_4`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 81
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 20 | START | 20 | 40 |
| ✅ EXACT | `Action_PassBlock` | LG | `11` | `10` | 23 | START | 23 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `12` | 23 | START | 41 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `14` | `13` | 23 | START | 30 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `15` | 23 | START | 23 | 60 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `4` | 23 | START | 23 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | RB | `10` | `9` | 40 | END | 20 | 37 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | `10` | `9` | 46 | START | 46 | 52 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `10` | `9` | 64 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 102 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 69 | 50 | inferred_complete_timeline |
| `Action_None` | 73 | 96 | 24 | inferred_complete_timeline |
| `Action_None` | 102 | 207 | 106 | inferred_complete_timeline |
| `Action_None` | 210 | 239 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 37 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 45 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 46 | 52 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 52 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 239 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 33 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 102 | 62 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 134 | 10 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 67 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 60 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 102 | 28 | inferred_complete_timeline |
| `Action_None` | 103 | 167 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 68 | 49 | inferred_complete_timeline |
| `Action_None` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_None` | 93 | 109 | 17 | inferred_complete_timeline |
| `Action_None` | 116 | 160 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 34 | 15 | inferred_complete_timeline |
| `Action_None` | 40 | 102 | 63 | inferred_complete_timeline |
| `Action_None` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 162 | 35 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 31 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 179 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 198 | 179 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 22 | 29 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 35–92 | 58 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 72–239 | 166 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 78–239 | 147 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 120–183 | 63 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 129–168 | 40 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 175–178 | 4 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 180–208 | 29 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 185–189 | 5 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 197–239 | 43 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 210–239 | 30 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 211–239 | 29 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `29` | 178 | 179 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=64, end=52. Clamping end to start.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [20–40], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=41.
- ⚠️ Action 'Action_None' range [20-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-52] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-31] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 20, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [20-20] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-29] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-34] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-102] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [20-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [46-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-134] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '25' has 1 frames without a visible bounding box.
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