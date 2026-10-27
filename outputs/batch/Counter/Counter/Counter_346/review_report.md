# Play-Annotation-Generator Annotation Review — Counter_346

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_346`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `13` | `12` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 21 | START | 21 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `11` | `10` | 24 | START | 24 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 24 | START | 35 | 38 |
| ✅ EXACT | `Action_DownBlock` | RG | `4` | `3` | 24 | START | 24 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `7` | `6` | 24 | START | 24 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `13` | `12` | 24 | START | 24 | 78 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `9` | `8` | 33 | START | 33 | 69 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 34 | END | 21 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `3` | `2` | 44 | START | 44 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 70 | START | 70 | 194 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 43 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 44 | 65 | 22 | inferred_complete_timeline |
| `Action_Handoff` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 70 | 159 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 33 | 69 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 194 | 125 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 207 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 24 | 78 | 55 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 81 | 100 | 20 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 102 | 119 | 18 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 38 | 18 | inferred_complete_timeline |
| `Action_None` | 61 | 72 | 12 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 139 | 7 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 24 | 67 | 44 | inferred_complete_timeline |
| `Action_PullBlock` | 69 | 73 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 97 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 107 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 119 | 96 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 50 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 119 | 58 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 61 | 41 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 109 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 39 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 56 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 20–210 | 179 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 62–210 | 149 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 66–210 | 143 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 88–101 | 14 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 89–210 | 109 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 103–143 | 36 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 110–210 | 101 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 114–210 | 97 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 124–210 | 87 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–130 | 5 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 138–210 | 73 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 157–210 | 52 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 192–194 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (RG) duration 96 frames exceeds threshold 90 frames [start=24, end=119].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (RT) duration 96 frames exceeds threshold 90 frames [start=24, end=119].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [21–34], lower_priority='Action_DownBlock' annotated_start=24, effective_Action_DownBlock_start=35.
- ⚠️ Action 'Action_None' range [21-56] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [44-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [24-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [69-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-39] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [33-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [24-50] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [24-78] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [81-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [35-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [40-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [47-51] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [72-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [91-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-210] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-143] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '30' has 1 frames without a visible bounding box.
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