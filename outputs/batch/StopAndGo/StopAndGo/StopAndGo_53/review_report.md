# Play-Annotation-Generator Annotation Review — StopAndGo_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_53`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 11 | START | 11 | 23 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 14 | START | 14 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 14 | START | 24 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 14 | START | 14 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 14 | START | 14 | 41 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 14 | START | 14 | 50 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 23 | END | 11 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | `6` | `6` | 23 | START | 23 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR3 | `6` | `6` | 93 | START | 93 | 93 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 111 | START | 111 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `6` | `6` | 116 | START | 116 | 187 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_None` | 24 | 110 | 87 | inferred_complete_timeline |
| `Action_ThrowPass` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_None` | 123 | 216 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 70 | 60 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 80 | 131 | 52 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 96 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_VerticalStem` | 23 | 87 | 65 | inferred_complete_timeline |
| `Action_VerticalStem` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_SellStop` | 93 | 93 | 1 | inferred_complete_timeline |
| `Action_SellStop` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_RunGoRoute` | 116 | 187 | 72 | inferred_complete_timeline |
| `Action_RunGoRoute` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_RunGoRoute` | 194 | 222 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 233 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 107 | 94 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 222 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 36 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 231 | 165 | inferred_complete_timeline |
| `Action_PassBlock` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 50 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 41 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 239 | 183 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |
| `Action_None` | 190 | 238 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 58 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 179 | 169 | inferred_complete_timeline |
| `Action_None` | 184 | 239 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 177 | 167 | inferred_complete_timeline |
| `Action_None` | 179 | 204 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 90 | 80 | inferred_complete_timeline |
| `Action_None` | 94 | 239 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 218 | 208 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 136 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 229 | 219 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–239 | 227 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 62–229 | 168 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 70–226 | 153 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 95–239 | 145 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 146–210 | 63 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 169–191 | 13 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 169–185 | 5 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 218–220 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 227–237 | 11 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SellStop` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 68: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 68: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [11–23], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [11-70] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-179] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-96] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [23-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellStop' for track '6' starts at frame 93, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SellStop' range [93-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellStop' range [96-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [116-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [189-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [194-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-170] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-229] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-231] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [234-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-229] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-226] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>