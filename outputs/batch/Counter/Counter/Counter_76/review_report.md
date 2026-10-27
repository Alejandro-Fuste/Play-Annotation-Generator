# Play-Annotation-Generator Annotation Review — Counter_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_76`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 45 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `10` | `9` | 46 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 46 | START | 46 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `7` | `6` | 46 | START | 46 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `11` | `10` | 46 | START | 46 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `2` | `1` | 46 | START | 46 | 103 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `4` | `3` | 51 | START | 51 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 57 | END | 46 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `3` | `2` | 67 | START | 67 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 92 | START | 92 | 108 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–108
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_None` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_None` | 92 | 108 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 51 | 91 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 108 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 130 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 149 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 46 | 103 | 58 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 113 | 147 | 35 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 69 | 94 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 108 | 141 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 174 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 85 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 121 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_None` | 60 | 66 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 122 | 77 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 147 | 23 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 158 | 113 | inferred_complete_timeline |
| `Action_None` | 160 | 174 | 15 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 36 | 31 | inferred_complete_timeline |
| `Action_None` | 51 | 170 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 139 | 94 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 188 | 143 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 203 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 69 | 24 | inferred_complete_timeline |
| `Action_None` | 74 | 210 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 12–13 | 2 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 15–210 | 159 | 6 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 122–210 | 89 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 144–210 | 64 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 155–210 | 56 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 167–210 | 44 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 171–210 | 40 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 178–210 | 33 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (RT) duration 102 frames exceeds threshold 90 frames [start=46, end=147].
- ⚠️ Overlapping action conflict at frame 46 for track '9': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 102 frames exceeds threshold 90 frames [start=46, end=147].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '10' (LG) duration 102 frames exceeds threshold 90 frames [start=46, end=147].
- ⚠️ Action 'Action_None' range [46-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [46-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [67-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [82-91] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-139] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-129] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [46-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [69-94] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [97-105] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [108-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-36] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-21] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '29' has 1 frames without a visible bounding box.
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

</details>