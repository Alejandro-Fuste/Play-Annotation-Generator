# Play-Annotation-Generator Annotation Review — CrackToss_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_26`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 143 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `20` | `18` | 141 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `9` | `8` | 144 | START | 144 | 171 |
| ✅ EXACT | `Action_PullBlock` | LT | `1` | `0` | 144 | START | 144 | 190 |
| ✅ EXACT | `Action_PullBlock` | LG | `7` | `6` | 144 | START | 144 | 160 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 146 | END | 141 | 146 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 162 | START | 162 | 170 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `4` | 182 | START | 182 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 231 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 161 | 15 | inferred_complete_timeline |
| `Action_Toss` | 162 | 170 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_CrackBlock` | 144 | 171 | 28 | inferred_complete_timeline |
| `Action_CrackBlock` | 176 | 192 | 17 | inferred_complete_timeline |
| `Action_CrackBlock` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 221 | 229 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 223 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 190 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 160 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 166 | 26 | inferred_complete_timeline |
| `Action_None` | 168 | 184 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 141 | 1 | inferred_complete_timeline |
| `Action_None` | 145 | 164 | 20 | inferred_complete_timeline |
| `Action_None` | 171 | 184 | 14 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |
| `Action_None` | 212 | 234 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 163 | 23 | inferred_complete_timeline |
| `Action_None` | 169 | 227 | 59 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 176 | 36 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 239 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 140 | 50 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 186 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–191 | 192 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 3–239 | 192 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 19–23 | 5 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 46–61 | 5 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 134–239 | 51 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 152–239 | 88 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 168–215 | 48 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 175–239 | 65 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 179–239 | 61 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 195–239 | 45 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 195–239 | 45 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 195–239 | 45 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 196–229 | 34 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `20` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=141, end=23. Clamping end to start.
- ⚠️ Action 'Action_PullBlock' range [144-190] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-186] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 141, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [141-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-223] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [144-160] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [144-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [176-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [212-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [221-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [162-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-56] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-108] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-239] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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