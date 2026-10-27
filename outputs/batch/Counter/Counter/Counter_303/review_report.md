# Play-Annotation-Generator Annotation Review — Counter_303

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_303`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 51
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | DT2 | defense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 59 | START | 59 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `14` | 62 | START | 62 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 62 | START | 73 | 150 |
| ✅ EXACT | `Action_DownBlock` | DT2 | `21` | `20` | 62 | START | 62 | 150 |
| ✅ EXACT | `Action_PullBlock` | RG | `19` | `18` | 62 | START | 62 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 62 | START | 62 | 122 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `6` | `5` | 72 | START | 72 | 106 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 72 | END | 59 | 72 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 81 | START | 81 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 107 | START | 107 | 142 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 81 | 106 | 26 | inferred_complete_timeline |
| `Action_None` | 107 | 173 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 72 | 106 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 142 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 239 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 187 | 129 | inferred_complete_timeline |
| `Action_None` | 190 | 239 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 176 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 165 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 62 | 122 | 61 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 151 | 218 | 68 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 106 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 150 | 39 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 72 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 150 | 78 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 150 | 89 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 93 | 35 | inferred_complete_timeline |
| `Action_None` | 95 | 112 | 18 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 183 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_None` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 222 | 81 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 231 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 219 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 150 | 89 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 113 | 55 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 193 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 135 | 77 | inferred_complete_timeline |
| `Action_None` | 137 | 186 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 167 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 156 | 98 | inferred_complete_timeline |
| `Action_None` | 158 | 239 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 124 | 66 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 223 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 94–124 | 31 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 118–239 | 117 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 144–239 | 96 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 218–239 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [59–72], lower_priority='Action_DownBlock' annotated_start=62, effective_Action_DownBlock_start=73.
- ⚠️ Action 'Action_None' range [59-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-165] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [62-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [130-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-239] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-222] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-112] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>