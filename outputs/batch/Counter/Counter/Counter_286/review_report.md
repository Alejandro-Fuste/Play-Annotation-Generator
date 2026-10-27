# Play-Annotation-Generator Annotation Review — Counter_286

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_286`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 22 | START | 22 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `2` | `1` | 25 | START | 25 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `5` | `4` | 25 | START | 38 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `9` | `8` | 25 | START | 25 | 96 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `7` | `6` | 25 | START | 25 | 120 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 37 | END | 22 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `4` | `3` | 72 | START | 72 | 194 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 37 | 16 | inferred_complete_timeline |
| `Action_None` | 38 | 71 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 72 | 194 | 123 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 232 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 56 | 35 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 109 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 25 | 120 | 96 | inferred_complete_timeline |
| `Action_None` | 121 | 138 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 25 | 96 | 72 | inferred_complete_timeline |
| `Action_PullBlock` | 101 | 120 | 20 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 37 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 38 | 104 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 118 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 25 | 83 | 59 | inferred_complete_timeline |
| `Action_DownBlock` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 120 | 22 | inferred_complete_timeline |
| `Action_None` | 121 | 176 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 125 | 104 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_None` | 220 | 239 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 201 | 180 | inferred_complete_timeline |
| `Action_None` | 207 | 212 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 45 | 24 | inferred_complete_timeline |
| `Action_None` | 52 | 58 | 7 | inferred_complete_timeline |
| `Action_None` | 60 | 121 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 105 | 84 | inferred_complete_timeline |
| `Action_None` | 109 | 143 | 35 | inferred_complete_timeline |
| `Action_None` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 85 | 64 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 119 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 48 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 62–82 | 4 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 63–90 | 16 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 67–106 | 40 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 83–101 | 15 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 98–239 | 141 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 99–115 | 4 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 129–239 | 111 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 140–172 | 33 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 145–235 | 82 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 156–184 | 27 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 160–162 | 3 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 170–173 | 4 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 175–178 | 4 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 181–239 | 59 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 188–239 | 39 | 3 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 197–239 | 41 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 213–238 | 26 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 217–239 | 23 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 219–239 | 21 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 230–239 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (RT) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (C) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [22–37], lower_priority='Action_DownBlock' annotated_start=25, effective_Action_DownBlock_start=38.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (LG) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
- ⚠️ Action 'Action_None' range [22-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [25-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [92-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [72-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-232] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [38-104] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-118] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [25-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-58] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-121] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-174] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-239] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-236] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-238] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '37' has 1 frames without a visible bounding box.
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

</details>