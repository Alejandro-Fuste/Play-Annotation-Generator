# Play-Annotation-Generator Annotation Review — Counter_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | DT1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 12 | START | 12 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 12 | START | 12 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 12 | START | 12 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 12 | START | 12 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 12 | START | 12 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 12 | START | 12 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 12 | START | 12 | 44 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `6` | `5` | 45 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `11` | `10` | 45 | START | 45 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `4` | `3` | 45 | START | 45 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `6` | `5` | 45 | START | 45 | 59 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `8` | `7` | 45 | START | 45 | 95 |
| ✅ EXACT | `Action_PullBlock` | DT1 | `15` | `14` | 45 | START | 45 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `10` | `9` | 45 | START | 45 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 54 | END | 45 | 54 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 80 | START | 80 | 97 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `8` | `7` | 98 | START | 102 | 134 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–187
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 54 | 10 | inferred_complete_timeline |
| `Action_None` | 55 | 79 | 25 | inferred_complete_timeline |
| `Action_Handoff` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 187 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–134
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 45 | 95 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 134 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 45 | 79 | 35 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 88 | 123 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_None` | 130 | 232 | 103 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–76
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 45 | 59 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 70 | 76 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–84
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 45 | 64 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 84 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–227
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 45 | 74 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 129 | 41 | inferred_complete_timeline |
| `Action_None` | 130 | 221 | 92 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–192
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 192 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–71
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_PullBlock` | 45 | 71 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–51
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 51 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–97
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 72 | 28 | inferred_complete_timeline |
| `Action_None` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 84 | 97 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–239
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 77 | 33 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 165 | 55 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–67
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 67 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–84
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 84 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 38–239 | 199 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 41–110 | 70 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 51–239 | 165 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 63–126 | 62 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 76–239 | 65 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 81–95 | 15 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 81–98 | 18 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 97–109 | 13 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 107–239 | 133 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 107–239 | 131 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 120–239 | 117 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 124–239 | 114 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 132–155 | 24 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 141–239 | 84 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 167–239 | 69 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 175–239 | 65 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 199–204 | 6 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 203–239 | 37 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `6` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `10` (3 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `8` (RB): Annotated start 98 != Inferred start 102

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 45 for track '5': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Action 'Action_None' range [45-67] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [45-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-72] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [45-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [70-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [45-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-134] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-239] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [45-79] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [88-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [45-64] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-192] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [45-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '32' has 1 frames without a visible bounding box.
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

</details>