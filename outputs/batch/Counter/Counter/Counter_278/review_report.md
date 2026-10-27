# Play-Annotation-Generator Annotation Review — Counter_278

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_278`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 11 | START | 11 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 11 | START | 11 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 11 | START | 11 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 11 | START | 11 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 11 | START | 11 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 11 | START | 11 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 11 | START | 11 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 11 | START | 11 | 48 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `2` | `1` | 49 | START | 49 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `13` | `12` | 52 | START | 52 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `13` | 52 | START | 52 | 119 |
| ✅ EXACT | `Action_PullBlock` | C | `3` | `2` | 52 | START | 52 | 142 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `4` | `3` | 52 | START | 52 | 99 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 63 | END | 49 | 63 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 79 | START | 79 | 98 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `11` | `10` | 99 | START | 105 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 142 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 11–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 63 | 15 | inferred_complete_timeline |
| `Action_None` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 79 | 98 | 20 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 93 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 126 | 239 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 11–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 51 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 89 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 126 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 51 | 41 | inferred_complete_timeline |
| `Action_PullBlock` | 52 | 142 | 91 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 11–216
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 51 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 119 | 68 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_None` | 147 | 216 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–99
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 51 | 41 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 52 | 99 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–134
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 91 | 43 | inferred_complete_timeline |
| `Action_None` | 99 | 127 | 29 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–230
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 90 | 42 | inferred_complete_timeline |
| `Action_None` | 99 | 221 | 123 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 11–224
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 86 | 38 | inferred_complete_timeline |
| `Action_None` | 89 | 138 | 50 | inferred_complete_timeline |
| `Action_None` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 170 | 15 | inferred_complete_timeline |
| `Action_None` | 177 | 224 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 11–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 70 | 22 | inferred_complete_timeline |
| `Action_None` | 73 | 82 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 239 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 108 | 239 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 63 | 15 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 173 | 125 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 239 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 120 | 72 | inferred_complete_timeline |
| `Action_None` | 125 | 217 | 93 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 41–71 | 24 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 100–239 | 139 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 115–239 | 119 | 3 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 124–126 | 3 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 145–200 | 56 | 1 | Undefined position; Undefined team |
| `21` | `37` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `22` | `39` | Position_Unknown | Team_Unknown | 181–238 | 54 | 2 | Undefined position; Undefined team |
| `23` | `40` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `24` | `41` | Position_Unknown | Team_Unknown | 184–239 | 54 | 2 | Undefined position; Undefined team |
| `25` | `43` | Position_Unknown | Team_Unknown | 196–200 | 5 | 1 | Undefined position; Undefined team |
| `26` | `44` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `27` | `45` | Position_Unknown | Team_Unknown | 205–239 | 35 | 1 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `11` (RB): Annotated start 99 != Inferred start 105

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (C) duration 91 frames exceeds threshold 90 frames [start=52, end=142].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (LG) duration 91 frames exceeds threshold 90 frames [start=52, end=142].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (RG) duration 91 frames exceeds threshold 90 frames [start=52, end=142].
- ⚠️ Action 'Action_None' range [49-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [52-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-90] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-221] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-173] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-217] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [91-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-119] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-170] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-239] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-219] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-197] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
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

</details>