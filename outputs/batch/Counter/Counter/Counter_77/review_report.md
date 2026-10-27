# Play-Annotation-Generator Annotation Review — Counter_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_77`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR1 | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 74 | START | 74 | 87 |
| ✅ EXACT | `Action_DownBlock` | LT | `19` | `18` | 77 | START | 77 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 77 | START | 88 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `22` | `21` | 77 | START | 77 | 92 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `19` | 77 | START | 77 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR1 | `5` | `4` | 77 | START | 77 | 130 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 87 | END | 74 | 87 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 97 | START | 97 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 110 | START | 110 | 149 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 164 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 149 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 229 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 257 | 259 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 77 | 130 | 54 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 132 | 133 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 234 | 161 | inferred_complete_timeline |
| `Action_None` | 240 | 251 | 12 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 137 | 64 | inferred_complete_timeline |
| `Action_None` | 142 | 261 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 164 | 88 | inferred_complete_timeline |
| `Action_None` | 165 | 173 | 9 | inferred_complete_timeline |
| `Action_None` | 181 | 221 | 41 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 92 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 164 | 69 | inferred_complete_timeline |
| `Action_None` | 165 | 175 | 11 | inferred_complete_timeline |
| `Action_None` | 177 | 182 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 152 | 65 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 165 | 174 | 10 | inferred_complete_timeline |
| `Action_None` | 177 | 248 | 72 | inferred_complete_timeline |
| `Action_None` | 253 | 260 | 8 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PullBlock` | 77 | 164 | 88 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 184 | 111 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 136 | 63 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_None` | 158 | 176 | 19 | inferred_complete_timeline |
| `Action_None` | 180 | 221 | 42 | inferred_complete_timeline |
| `Action_None` | 224 | 236 | 13 | inferred_complete_timeline |
| `Action_None` | 240 | 269 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 113 | 40 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 135 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 101 | 28 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 258 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 154 | 81 | inferred_complete_timeline |
| `Action_None` | 159 | 236 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 187 | 114 | inferred_complete_timeline |
| `Action_None` | 192 | 221 | 30 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 164 | 91 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 177 | 269 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 237 | 164 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 269 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 135–269 | 135 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 141–269 | 122 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 142–201 | 56 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 181–269 | 89 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 184–216 | 28 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 196–269 | 74 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [74–87], lower_priority='Action_DownBlock' annotated_start=77, effective_Action_DownBlock_start=88.
- ⚠️ Action 'Action_None' range [74-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-113] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-135] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [77-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [132-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-149] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-229] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-238] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [250-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [257-259] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-237] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-136] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-152] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-152] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-248] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-269] for track '27' has 3 frames without a visible bounding box.
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