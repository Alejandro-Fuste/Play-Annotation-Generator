# Play-Annotation-Generator Annotation Review — Counter_207

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_207`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | TE1 | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 17 | START | 17 | 29 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `11` | `10` | 21 | START | 30 | 72 |
| ✅ EXACT | `Action_DownBlock` | TE1 | `13` | `12` | 21 | START | 21 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `18` | `17` | 21 | START | 21 | 34 |
| ✅ EXACT | `Action_DownBlock` | RT | `20` | `19` | 21 | START | 21 | 47 |
| ✅ EXACT | `Action_PullBlock` | LG | `21` | `20` | 21 | START | 21 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `22` | `21` | 21 | START | 21 | 102 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 29 | END | 17 | 29 |
| ✅ EXACT | `Action_BallCarry` | QB | `19` | `18` | 58 | START | 58 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 117 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 29 | 13 | inferred_complete_timeline |
| `Action_None` | 30 | 57 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 21 | 117 | 97 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 180 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 111 | 95 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 180 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 21 | 102 | 82 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 180 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 21 | 117 | 97 | inferred_complete_timeline |
| `Action_None` | 118 | 180 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 29 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 30 | 72 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 117 | 81 | inferred_complete_timeline |
| `Action_None` | 118 | 180 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 21 | 47 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 94 | 78 | inferred_complete_timeline |
| `Action_None` | 102 | 180 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 43 | 27 | inferred_complete_timeline |
| `Action_None` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_None` | 58 | 67 | 10 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 76 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 88 | 72 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 135 | 119 | inferred_complete_timeline |
| `Action_None` | 138 | 169 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 153 | 137 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–6 | 7 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 48–82 | 8 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 88–180 | 77 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 92–180 | 86 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 115–161 | 47 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 138–156 | 15 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 155–180 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `11` (C): Annotated start 21 != Inferred start 30
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [17–29], lower_priority='Action_DownBlock' annotated_start=21, effective_Action_DownBlock_start=30.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (TE1) duration 97 frames exceeds threshold 90 frames [start=21, end=117].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (RG) duration 97 frames exceeds threshold 90 frames [start=21, end=117].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '20' (LG) duration 97 frames exceeds threshold 90 frames [start=21, end=117].
- ⚠️ Action 'Action_None' range [17-94] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-180] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-135] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-169] for track '4' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-43] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-55] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [30-72] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [21-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [21-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [21-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '28' has 1 frames without a visible bounding box.
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