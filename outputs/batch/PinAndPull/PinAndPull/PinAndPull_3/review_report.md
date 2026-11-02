# Play-Annotation-Generator Annotation Review — PinAndPull_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_3`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 9 | START | 9 | 25 |
| ✅ EXACT | `Action_DownBlock` | RG | `9` | `8` | 12 | START | 12 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `8` | `7` | 12 | START | 26 | 113 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `4` | `3` | 12 | START | 12 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 25 | END | 9 | 25 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 34 | START | 34 | 41 |
| ✅ EXACT | `Action_BallCarry` | RB | `1` | `0` | 42 | START | 42 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 25 | 17 | inferred_complete_timeline |
| `Action_None` | 26 | 33 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_None` | 42 | 81 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 42 | 180 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 50 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 57 | 49 | inferred_complete_timeline |
| `Action_None` | 64 | 99 | 36 | inferred_complete_timeline |
| `Action_None` | 101 | 129 | 29 | inferred_complete_timeline |
| `Action_None` | 132 | 157 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 164 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 72 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 25 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 26 | 113 | 88 | inferred_complete_timeline |
| `Action_PullBlock` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_None` | 135 | 155 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 12 | 134 | 123 | inferred_complete_timeline |
| `Action_None` | 135 | 153 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 12 | 134 | 123 | inferred_complete_timeline |
| `Action_None` | 135 | 180 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 20 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 147 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 85 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 76 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 54 | 46 | inferred_complete_timeline |
| `Action_None` | 56 | 167 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 91 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 58 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 100 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | Position_Unknown | Team_Unknown | 6–95 | 80 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 19–69 | 51 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 60–64 | 5 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 72–180 | 94 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 77–80 | 4 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 84–109 | 25 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 92–180 | 89 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 116–180 | 65 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 118–171 | 54 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 125–180 | 49 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (C) duration 123 frames exceeds threshold 90 frames [start=12, end=134].
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [9–25], lower_priority='Action_PullBlock' annotated_start=12, effective_Action_PullBlock_start=26.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 123 frames exceeds threshold 90 frames [start=12, end=134].
- ⚠️ Action 'Action_BallCarry' range [42-180] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-57] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-99] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-157] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-72] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [26-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [12-134] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-147] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-164] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-76] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-104] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
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