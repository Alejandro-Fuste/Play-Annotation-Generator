# Play-Annotation-Generator Annotation Review — Counter_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_30`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_BallSnap` | LG | `7` | `6` | 64 | START | 64 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 66 | END | 64 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `18` | 67 | START | 69 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `8` | `7` | 67 | START | 67 | 88 |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | RG | `4` | `3` | 67 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `4` | `3` | 67 | START | 67 | 81 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `5` | `4` | 67 | START | 67 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `16` | `15` | 98 | START | 100 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `10` | 113 | START | 113 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 86 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 147 | 154 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 180 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 184 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 67 | 167 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 98 | 35 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 97 | 31 | inferred_complete_timeline |
| `Action_None` | 100 | 152 | 53 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullBlock` | 67 | 81 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 102 | 118 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 88 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 92 | 112 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 170 | 57 | inferred_complete_timeline |
| `Action_None` | 171 | 202 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 104 | 41 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 199 | 82 | inferred_complete_timeline |
| `Action_None` | 204 | 222 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 118 | 55 | inferred_complete_timeline |
| `Action_None` | 120 | 175 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 69 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 90 | 27 | inferred_complete_timeline |
| `Action_None` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 90 | 27 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 165 | 102 | inferred_complete_timeline |
| `Action_None` | 190 | 211 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 145 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 154 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 159 | 96 | inferred_complete_timeline |
| `Action_None` | 162 | 174 | 13 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–239 | 216 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 10–107 | 81 | 6 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 69–92 | 23 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 94–175 | 69 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 101–239 | 135 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 108–185 | 70 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 140–239 | 87 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 155–239 | 80 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 157–234 | 56 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 163–226 | 64 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 166–239 | 63 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 171–239 | 69 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 174–193 | 16 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 175–239 | 65 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 176–181 | 6 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 187–226 | 40 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 190–213 | 18 | 3 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 193–239 | 47 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 199–216 | 18 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 223–233 | 10 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 224–230 | 7 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (3 segments found)
- ❌ Missing segment for action `Action_PlaySideFakeStep` on target `4` (RG)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (9 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 67 for track '3': 'Action_PlaySideFakeStep' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '3' (RG) duration 101 frames exceeds threshold 90 frames [start=67, end=167].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (RT) duration 104 frames exceeds threshold 90 frames [start=67, end=170].
- ⚠️ Action 'Action_None' range [64-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [67-81] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [88-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [102-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [122-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [135-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [152-155] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [162-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [166-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [67-167] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [67-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [92-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [100-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [107-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [69-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-138] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-227] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-202] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-234] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-216] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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