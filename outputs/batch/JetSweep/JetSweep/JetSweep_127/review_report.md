# Play-Annotation-Generator Annotation Review — JetSweep_127

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_127`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `1` | `0` | 29 | START | 29 | 76 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 45 | START | 45 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | `17` | `16` | 46 | START | 46 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 46 | START | 57 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 46 | START | 46 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 46 | START | 46 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 46 | START | 46 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 46 | START | 46 | 184 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 56 | END | 45 | 56 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 62 | START | 62 | 76 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `1` | `0` | 77 | START | 77 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 184 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_Toss` | 62 | 76 | 15 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 183 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_JetMotion` | 29 | 76 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 235 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 91 | 47 | inferred_complete_timeline |
| `Action_None` | 97 | 242 | 146 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 262 | 218 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_LeadBlock` | 46 | 69 | 24 | inferred_complete_timeline |
| `Action_LeadBlock` | 71 | 91 | 21 | inferred_complete_timeline |
| `Action_LeadBlock` | 105 | 184 | 80 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 184 | 139 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 78 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 184 | 105 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 158 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 181 | 20 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 90 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 184 | 69 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 140 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 223 | 179 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 86 | 42 | inferred_complete_timeline |
| `Action_None` | 91 | 269 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 175 | 131 | inferred_complete_timeline |
| `Action_None` | 178 | 256 | 79 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 75 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 176 | 132 | inferred_complete_timeline |
| `Action_None` | 178 | 189 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 237 | 193 | inferred_complete_timeline |
| `Action_None` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_None` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_None` | 257 | 264 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 254 | 210 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 146 | 102 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 125 | 81 | inferred_complete_timeline |
| `Action_None` | 141 | 263 | 123 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 104–269 | 166 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 111–115 | 5 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 140–181 | 18 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 158–269 | 112 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 195–269 | 75 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 207–269 | 63 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '16' (TE2) duration 139 frames exceeds threshold 90 frames [start=46, end=184].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 139 frames exceeds threshold 90 frames [start=46, end=184].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [45–56], lower_priority='Action_ZoneBlock' annotated_start=46, effective_Action_ZoneBlock_start=57.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 139 frames exceeds threshold 90 frames [start=46, end=184].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 95 frames exceeds threshold 90 frames [start=46, end=140].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 139 frames exceeds threshold 90 frames [start=46, end=184].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 139 frames exceeds threshold 90 frames [start=46, end=184].
- ⚠️ Action 'Action_BallCarry' range [77-235] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-223] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-256] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-263] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-183] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [46-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [71-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-158] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-90] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '24' has 1 frames without a visible bounding box.
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