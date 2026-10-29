# Play-Annotation-Generator Annotation Review — DeepCross_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_67`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | CB3 | defense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `8` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 3 | START | 3 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 6 | START | 6 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 6 | START | 6 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 6 | START | 19 | 122 |
| ✅ EXACT | `Action_PassBlock` | RG | `7` | `7` | 6 | START | 6 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | CB3 | `5` | `5` | 18 | START | 18 | 109 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 18 | END | 3 | 18 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 111 | START | 111 | 119 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_None` | 19 | 110 | 92 | inferred_complete_timeline |
| `Action_ThrowPass` | 111 | 119 | 9 | inferred_complete_timeline |
| `Action_None` | 120 | 186 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 233 | 231 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 218 | 216 | inferred_complete_timeline |
| `Action_None` | 220 | 224 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 93 | 88 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 115 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 146 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 155 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 172 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 78 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 157 | 78 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 175 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 188 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 122 | 104 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 162 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 181 | 187 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 45 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 155 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 122 | 120 | inferred_complete_timeline |
| `Action_None` | 124 | 239 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 227 | 225 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 225 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 109 | 107 | inferred_complete_timeline |
| `Action_None` | 120 | 239 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 232 | 230 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 117 | 198 | 82 | inferred_complete_timeline |
| `Action_None` | 199 | 211 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 72 | 70 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 87 | 85 | inferred_complete_timeline |
| `Action_None` | 94 | 196 | 103 | inferred_complete_timeline |
| `Action_None` | 204 | 224 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 155 | 153 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–164 | 164 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 44–45 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 51–202 | 127 | 6 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 61–62 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 103–105 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 112–199 | 48 | 5 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 167–198 | 19 | 4 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 173–239 | 65 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 198–239 | 42 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 198–200 | 3 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 210–239 | 11 | 5 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 213–225 | 5 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 213–225 | 6 | 2 | Undefined position; Undefined team |
| `36` | `59` | Position_Unknown | Team_Unknown | 226–239 | 11 | 4 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 70: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 70: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 70: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 70: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 70: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=19.
- ⚠️ Action 'Action_None' range [3-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [18-109] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [112-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [117-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-211] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-155] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-225] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-232] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-224] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-109] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-239] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-93] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-115] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-155] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-72] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-186] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-122] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [181-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-155] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>