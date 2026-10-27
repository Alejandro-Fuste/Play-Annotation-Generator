# Play-Annotation-Generator Annotation Review — Counter_249

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_249`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | offense | `20` | `19` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LG | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 58 | START | 58 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `11` | `10` | 60 | START | 60 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `13` | `12` | 60 | START | 60 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | `20` | `19` | 60 | START | 60 | 128 |
| ✅ EXACT | `Action_PullBlock` | RG | `22` | `21` | 60 | START | 60 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `2` | `1` | 60 | START | 60 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 71 | END | 58 | 71 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 90 | START | 90 | 103 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LG | `13` | `12` | 104 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 72 | 89 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 90 | 103 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 128 | 69 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 134 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 212 | 155 | inferred_complete_timeline |
| `Action_None` | 214 | 224 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 81 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 158 | 74 | inferred_complete_timeline |
| `Action_None` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 87 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 72 | 81 | 10 | inferred_complete_timeline |
| `Action_None` | 85 | 191 | 107 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 158 | 99 | inferred_complete_timeline |
| `Action_None` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 86 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 115 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 79 | 22 | inferred_complete_timeline |
| `Action_None` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 97 | 206 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 90 | 33 | inferred_complete_timeline |
| `Action_None` | 93 | 104 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 129 | 72 | inferred_complete_timeline |
| `Action_None` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 237 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 217 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 185 | 128 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 143 | 86 | inferred_complete_timeline |
| `Action_None` | 145 | 204 | 60 | inferred_complete_timeline |
| `Action_None` | 209 | 228 | 20 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–239 | 232 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 105–239 | 135 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 118–239 | 119 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 134–239 | 83 | 5 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 160–226 | 67 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 171–239 | 60 | 5 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 178–193 | 7 | 2 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 210–239 | 17 | 2 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 230–233 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `13` (LG)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 499: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (LT) duration 99 frames exceeds threshold 90 frames [start=60, end=158].
- ⚠️ Segment 'Action_BallCarry' for track '12' has invalid range: start=104, end=87. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 99 frames exceeds threshold 90 frames [start=60, end=158].
- ⚠️ Action 'Action_PullLeadBlock' range [60-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-224] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-90] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-104] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-87] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-206] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-228] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-128] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-134] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [58-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-191] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-239] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-199] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-226] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-194] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>