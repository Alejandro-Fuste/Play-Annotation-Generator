# Play-Annotation-Generator Annotation Review — JetSweep_229

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_229`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | LT | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `2` | `1` | 38 | START | 38 | 82 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 57 | START | 57 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | LT | `12` | `11` | 58 | START | 58 | 90 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `12` | `11` | 58 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 58 | START | 58 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 58 | START | 70 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 58 | START | 58 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 58 | START | 58 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 69 | END | 57 | 69 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 75 | START | 75 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `1` | 83 | START | 83 | 230 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 139 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 69 | 13 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_Toss` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 83 | 269 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 120 | 64 | inferred_complete_timeline |
| `Action_None` | 144 | 153 | 10 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 182 | 23 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_JetMotion` | 38 | 82 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 230 | 148 | inferred_complete_timeline |
| `Action_BallCarry` | 234 | 250 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 158 | 102 | inferred_complete_timeline |
| `Action_None` | 182 | 268 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_LeadBlock` | 58 | 90 | 33 | inferred_complete_timeline |
| `Action_LeadBlock` | 94 | 139 | 46 | inferred_complete_timeline |
| `Action_None` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 137 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 139 | 1 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 69 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 70 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 139 | 68 | inferred_complete_timeline |
| `Action_None` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 84 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 109 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 139 | 29 | inferred_complete_timeline |
| `Action_None` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 139 | 83 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 146 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 77 | 21 | inferred_complete_timeline |
| `Action_None` | 81 | 183 | 103 | inferred_complete_timeline |
| `Action_None` | 185 | 197 | 13 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 171 | 115 | inferred_complete_timeline |
| `Action_None` | 227 | 269 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 181 | 125 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 238 | 182 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 256 | 7 | inferred_complete_timeline |
| `Action_None` | 258 | 265 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 244 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 187 | 131 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 211 | 13 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 233 | 10 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 138 | 82 | inferred_complete_timeline |

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
| `22` | `25` | Position_Unknown | Team_Unknown | 107–113 | 7 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 117–269 | 153 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 150–269 | 119 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 157–269 | 113 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 173–269 | 95 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 196–203 | 8 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 200–269 | 68 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 204–220 | 9 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 236–240 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Overlapping action conflict at frame 58 for track '11': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [57–69], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=70.
- ⚠️ Action 'Action_BallCarry' range [83-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-146] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-153] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-268] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-238] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-269] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [58-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-139] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-137] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-211] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-183] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '19' starts at frame 70, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [70-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '31' has 1 frames without a visible bounding box.
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

</details>