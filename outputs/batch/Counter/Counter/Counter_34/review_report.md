# Play-Annotation-Generator Annotation Review — Counter_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_34`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 60 | START | 60 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `6` | `5` | 65 | START | 65 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `8` | 65 | START | 74 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `2` | `1` | 65 | START | 65 | 112 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `15` | `14` | 68 | START | 68 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 73 | START | 73 | 105 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `5` | `4` | 73 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 106 | START | 106 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_Handoff` | 73 | 105 | 33 | inferred_complete_timeline |
| `Action_None` | 106 | 237 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 141 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_None` | 100 | 135 | 36 | inferred_complete_timeline |
| `Action_None` | 147 | 155 | 9 | inferred_complete_timeline |
| `Action_None` | 159 | 217 | 59 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 68 | 116 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 128 | 69 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PullBlock` | 65 | 112 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 114 | 155 | 42 | inferred_complete_timeline |
| `Action_None` | 156 | 169 | 14 | inferred_complete_timeline |
| `Action_None` | 173 | 231 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 73 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 84 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 141 | 82 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_DownBlock` | 65 | 99 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 239 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 105 | 46 | inferred_complete_timeline |
| `Action_None` | 110 | 123 | 14 | inferred_complete_timeline |
| `Action_None` | 127 | 150 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–11
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 59 | 33 | inferred_complete_timeline |
| `Action_None` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_None` | 116 | 143 | 28 | inferred_complete_timeline |
| `Action_None` | 146 | 178 | 33 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 119 | 60 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 95 | 36 | inferred_complete_timeline |
| `Action_None` | 100 | 130 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 135 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 20–216 | 126 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 68–239 | 149 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 75–213 | 44 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 85–239 | 145 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 115–239 | 118 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 151–239 | 89 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 152–239 | 87 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 160–239 | 80 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 178–239 | 62 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 199–239 | 36 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 226–239 | 9 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 226–239 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `5` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (LG) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
- ⚠️ Overlapping action conflict at frame 73 for track '4': 'Action_SnapReceive' vs 'Action_Handoff'. Overriding with 'Action_Handoff'.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (RT) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [60–73], lower_priority='Action_DownBlock' annotated_start=65, effective_Action_DownBlock_start=74.
- ⚠️ Action 'Action_None' range [60-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [65-112] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-135] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-143] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [68-116] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-105] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-155] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-145] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-136] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-144] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-239] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '32' has 1 frames without a visible bounding box.
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

</details>