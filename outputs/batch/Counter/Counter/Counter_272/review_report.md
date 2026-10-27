# Play-Annotation-Generator Annotation Review — Counter_272

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_272`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 9 | START | 9 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 9 | START | 9 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 9 | START | 9 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 9 | START | 9 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 9 | START | 9 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 9 | START | 9 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `2` | `Group` | 9 | START | 9 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 9 | START | 9 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 9 | START | 9 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 37 | START | 37 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `10` | `9` | 40 | START | 40 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 40 | START | 52 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 40 | START | 40 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `11` | `10` | 40 | START | 40 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `2` | `1` | 40 | START | 40 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `17` | `16` | 51 | END | 37 | 45 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 64 | START | 64 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `14` | 84 | START | 84 | 86 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 115 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 9–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 45 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 63 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_None` | 84 | 180 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–146
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 83 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 146 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 39 | 31 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 40 | 67 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 77 | 115 | 39 | inferred_complete_timeline |
| `Action_None` | 116 | 180 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 87 | 51 | inferred_complete_timeline |
| `Action_None` | 90 | 150 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–79
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 39 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 40 | 64 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 9–65
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 39 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 40 | 59 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 65 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 9–87
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 87 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–75
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 39 | 31 | inferred_complete_timeline |
| `Action_PullBlock` | 40 | 67 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 73 | 75 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–180
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 68 | 32 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_None` | 77 | 115 | 39 | inferred_complete_timeline |
| `Action_None` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 180 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 106 | 32 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 103 | 67 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 180 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 9–180
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 53 | 17 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 180 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–104
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 31 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 104 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 61 | 25 | inferred_complete_timeline |
| `Action_None` | 64 | 136 | 73 | inferred_complete_timeline |
| `Action_None` | 139 | 180 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–64
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 64 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 180 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 132 | 96 | inferred_complete_timeline |
| `Action_None` | 137 | 180 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–180
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 36 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 84 | 48 | inferred_complete_timeline |
| `Action_None` | 147 | 180 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 46–180 | 135 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 56–59 | 4 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 59–180 | 122 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 78–92 | 15 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 82–121 | 40 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 107–165 | 53 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 109–180 | 72 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 119–121 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 122–180 | 59 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 143–149 | 4 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 144–156 | 13 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 148–180 | 27 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 156–180 | 25 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 160–180 | 21 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [37–51], lower_priority='Action_DownBlock' annotated_start=40, effective_Action_DownBlock_start=52.
- ⚠️ Action 'Action_None' range [37-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [40-67] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [40-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-115] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-64] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [40-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [40-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [73-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-53] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [37-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-31] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-104] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '34' has 1 frames without a visible bounding box.
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