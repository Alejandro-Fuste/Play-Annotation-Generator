# Play-Annotation-Generator Annotation Review — Counter_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_5`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 57 | START | 57 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 63 | START | 85 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 63 | START | 63 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | `8` | `7` | 63 | START | 63 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 63 | START | 63 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `1` | `0` | 63 | START | 63 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 71 | END | 57 | 71 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 83 | START | 83 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `15` | 92 | START | 92 | 142 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 142 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_None` | 72 | 82 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 202 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 142 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 159 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 256 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 142 | 86 | inferred_complete_timeline |
| `Action_None` | 147 | 184 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 150 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 102 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 189 | 46 | inferred_complete_timeline |
| `Action_None` | 194 | 261 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 99 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 142 | 33 | inferred_complete_timeline |
| `Action_None` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 136 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PullBlock` | 63 | 99 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 135 | 142 | 8 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 80 | 24 | inferred_complete_timeline |
| `Action_None` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 189 | 66 | inferred_complete_timeline |
| `Action_None` | 192 | 269 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 102 | 46 | inferred_complete_timeline |
| `Action_None` | 109 | 269 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 99 | 43 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 121 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 92 | 36 | inferred_complete_timeline |
| `Action_None` | 109 | 269 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 103 | 47 | inferred_complete_timeline |
| `Action_None` | 109 | 145 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 249 | 193 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 133 | 77 | inferred_complete_timeline |
| `Action_None` | 136 | 269 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 173 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 152 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 144 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–269 | 263 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 2–118 | 111 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 101–162 | 47 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 107–161 | 24 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 109–161 | 20 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 111–269 | 154 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 116–269 | 151 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 116–269 | 153 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 156–184 | 29 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 176–269 | 78 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 189–238 | 50 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 196–199 | 4 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 198–213 | 12 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 200–233 | 24 | 3 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 206–269 | 64 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 263–267 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 11: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 12: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [57–71], lower_priority='Action_DownBlock' annotated_start=63, effective_Action_DownBlock_start=72.
- ⚠️ Action 'Action_PullLeadBlock' range [63-121] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [123-129] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-102] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-102] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [57-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-91] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-136] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-152] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [63-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [101-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [116-133] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-189] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-103] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-148] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-184] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-269] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-214] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>