# Play-Annotation-Generator Annotation Review — Counter_215

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_215`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `9` | `8` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `21` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 61 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 59 | START | 59 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 62 | START | 73 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `19` | `18` | 62 | START | 62 | 95 |
| ✅ EXACT | `Action_DownBlock` | RT | `20` | `19` | 62 | START | 62 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `22` | `21` | 62 | START | 62 | 111 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `9` | `8` | 62 | START | 62 | 121 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `11` | `10` | 65 | START | 65 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 72 | END | 59 | 72 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 89 | START | 89 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `10` | 105 | START | 105 | 125 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 141 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 73 | 88 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_None` | 105 | 112 | 8 | inferred_complete_timeline |
| `Action_None` | 114 | 121 | 8 | inferred_complete_timeline |
| `Action_None` | 124 | 213 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 65 | 104 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 125 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 62 | 121 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 200 | 142 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 138 | 80 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 111 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 141 | 69 | inferred_complete_timeline |
| `Action_None` | 142 | 199 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 95 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 73 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 115 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 112 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 102 | 44 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 136 | 78 | inferred_complete_timeline |
| `Action_None` | 139 | 144 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 106 | 48 | inferred_complete_timeline |
| `Action_None` | 109 | 148 | 40 | inferred_complete_timeline |
| `Action_None` | 159 | 167 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

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
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 152 | 94 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–160 | 161 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 89–239 | 143 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 99–235 | 112 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 141–238 | 98 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 141–178 | 36 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 162–239 | 77 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 165–239 | 73 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 165–239 | 75 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 167–236 | 70 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 183–239 | 57 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 207–239 | 33 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 432: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [59–72], lower_priority='Action_DownBlock' annotated_start=62, effective_Action_DownBlock_start=73.
- ⚠️ Action 'Action_None' range [59-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-115] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [62-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [105-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-148] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [115-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [120-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [124-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [140-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-191] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-230] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-238] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-236] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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