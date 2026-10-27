# Play-Annotation-Generator Annotation Review — Counter_130

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_130`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 47 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `10` | `9` | 48 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 48 | START | 48 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `9` | `8` | 48 | START | 48 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `7` | `6` | 48 | START | 48 | 81 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `11` | `10` | 48 | START | 48 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 59 | END | 48 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `4` | `3` | 82 | START | 82 | 172 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 135 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–209
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 59 | 12 | inferred_complete_timeline |
| `Action_None` | 60 | 81 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 172 | 91 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 209 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 139 | 92 | inferred_complete_timeline |
| `Action_None` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 48 | 73 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 48 | 81 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 86 | 135 | 50 | inferred_complete_timeline |
| `Action_None` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 61 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 76 | 103 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 135 | 30 | inferred_complete_timeline |
| `Action_None` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 81 | 34 | inferred_complete_timeline |
| `Action_None` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 135 | 88 | inferred_complete_timeline |
| `Action_None` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 92 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 73 | 26 | inferred_complete_timeline |
| `Action_None` | 79 | 86 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |
| `Action_None` | 170 | 197 | 28 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 57–84
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 68 | 84 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 76 | 29 | inferred_complete_timeline |
| `Action_None` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 121 | 25 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |
| `Action_None` | 140 | 210 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 182 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 165 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–89 | 86 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 82–142 | 61 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 99–210 | 112 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 104–210 | 103 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 110–137 | 10 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 114–138 | 25 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 128–210 | 83 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 140–191 | 52 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 140–190 | 46 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 161–210 | 49 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 165–210 | 39 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 171–190 | 18 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 172–210 | 39 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 173–183 | 11 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 174–190 | 12 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 181–210 | 30 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 48 for track '9': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Action 'Action_None' range [48-165] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-76] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-210] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-209] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-182] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [48-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [86-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [76-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [48-73] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-92] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-86] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-197] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-84] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-191] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-190] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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